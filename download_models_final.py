"""
Download OOTDiffusion models from Hugging Face
"""
import os
from huggingface_hub import snapshot_download

print("=" * 60)
print("Downloading OOTDiffusion Model Checkpoints")
print("=" * 60)
print("\nThis will download approximately 15GB of model files.")
print("Please be patient, this may take 10-30 minutes.\n")

# Download the entire checkpoints directory from the repository
print("Downloading all model files...")
try:
    snapshot_download(
        repo_id="levihsu/OOTDiffusion",
        allow_patterns=["checkpoints/**"],
        local_dir=".",
        local_dir_use_symlinks=False,
        resume_download=True
    )
    print("\n✓ All models downloaded successfully!")
    print("\nCheckpoints are now available in the checkpoints/ directory")
    print("\nYou can now run the app with:")
    print("  python run/gradio_ootd.py")
    print("\nor use the batch file:")
    print("  .\\run_app.bat")
    
except Exception as e:
    print(f"\n✗ Error during download: {e}")
    print("\nPlease check your internet connection and try again.")
