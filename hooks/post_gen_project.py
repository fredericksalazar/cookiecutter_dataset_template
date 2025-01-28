import os
import subprocess

def main():
    # Inicializar un repositorio Git
    subprocess.run(["git", "init"], check=True)
    print("Repositorio Git inicializado.")

    # Agregar los archivos al stage
    subprocess.run(["git", "add", "."], check=True)
    print("Archivos añadidos al stage.")

    # Hacer el primer commit
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    print("Commit inicial creado.")

    # Configurar la rama principal como 'main'
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    print("Rama principal configurada como 'main'.")

    # Solicitar la URL del repositorio remoto al usuario
    repo_url = input("Introduce la URL del repositorio remoto (deja vacío si no quieres agregar un remoto ahora): ").strip()
    if repo_url:
        # Configurar el repositorio remoto
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        print(f"Repositorio remoto configurado: {repo_url}")

        # Subir el proyecto al repositorio remoto
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Código subido al repositorio remoto.")

if __name__ == "__main__":
    main()
