import subprocess

def clone_yolov5_repo():
    repo_url = "https://github.com/ultralytics/yolov5.git"
    subprocess.run(["git", "clone", repo_url])
    print("Repositório YOLOv5 clonado com sucesso.")

clone_yolov5_repo()
