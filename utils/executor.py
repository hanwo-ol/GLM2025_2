import sys
import io
import contextlib
import subprocess
import uuid
import os
from pathlib import Path
import traceback

class CodeExecutor:
    def __init__(self, work_dir="workspace"):
        self.work_dir = Path(work_dir)
        self.work_dir.mkdir(exist_ok=True)

    def _get_existing_images(self):
        """Returns a set of existing image filenames in the workspace."""
        images = set()
        for ext in ["*.png", "*.jpg", "*.jpeg"]:
            for f in self.work_dir.glob(ext):
                images.add(f.name)
        return images

    def execute_python(self, code: str) -> dict:
        """Executes Python code and returns the output and any generated image files."""
        
        # We explicitly remove the standard output file 'output_plot.png' if it exists
        # to ensure that if the code regenerates it, we catch it as a 'fresh' file.
        # This solves the static filename overwriting issue.
        standard_plot = self.work_dir / "output_plot.png"
        if standard_plot.exists():
            standard_plot.unlink()

        # Track existing images to only return new ones (or the recreated standard plot)
        existing_images = self._get_existing_images()
        
        # Capture stdout
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        # Prepare context for execution
        exec_globals = {
            "__builtins__": __builtins__,
            "print": print, 
        }
        
        # Safe-ish execution environment
        setup_code = "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\n"
        full_code = setup_code + code

        try:
            with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
                # We execute in the work_dir
                cwd = os.getcwd()
                os.chdir(self.work_dir)
                try:
                    exec(full_code, exec_globals)
                finally:
                    os.chdir(cwd)
            
            output = stdout_capture.getvalue()
            error = stderr_capture.getvalue()
            
            # Find new images
            current_images = self._get_existing_images()
            # New images are those that didn't exist before OR are the standard plot (which we know we deleted)
            new_images = [str(self.work_dir / img) for img in current_images if img not in existing_images or img == "output_plot.png"]
            
            return {
                "success": True,
                "output": output,
                "error": error,
                "images": new_images
            }

        except Exception:
            return {
                "success": False,
                "output": stdout_capture.getvalue(),
                "error": traceback.format_exc(),
                "images": []
            }

    def execute_r(self, code: str) -> dict:
        """Executes R code using Rscript."""
        # Clean standard plot
        standard_plot = self.work_dir / "output_plot.png"
        if standard_plot.exists():
            standard_plot.unlink()

        existing_images = self._get_existing_images()

        # Write code to a temporary file
        script_name = f"script_{uuid.uuid4().hex}.R"
        script_path = self.work_dir / script_name
        
        with open(script_path, "w") as f:
            f.write(code)
            
        try:
            result = subprocess.run(
                ["Rscript", script_name],
                cwd=self.work_dir,
                capture_output=True,
                text=True,
                timeout=30 
            )
            
            # Find new images
            current_images = self._get_existing_images()
            new_images = [str(self.work_dir / img) for img in current_images if img not in existing_images or img == "output_plot.png"]
            
            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr,
                "images": new_images
            }
            
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "images": []
            }
        finally:
            pass
