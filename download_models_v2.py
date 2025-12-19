"""
Download OOTDiffusion models with resume capability
"""
import os
from huggingface_hub import hf_hub_download

def download_file(repo_id, filename, local_dir, subfolder=None):
    """Download a single file with error handling"""
    try:
        print(f"\nDownloading: {filename}")
        cache_dir = os.path.join(local_dir, ".cache")
        
        hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=local_dir,
            cache_dir=cache_dir,
            resume_download=True,
            subfolder=subfolder
        )
        print(f"✓ Completed: {filename}")
        return True
    except Exception as e:
        print(f"✗ Error downloading {filename}: {e}")
        return False

# Create directories
os.makedirs("checkpoints/ootd", exist_ok=True)
os.makedirs("checkpoints/humanparsing", exist_ok=True)
os.makedirs("checkpoints/openpose", exist_ok=True)
os.makedirs("checkpoints/clip-vit-large-patch14", exist_ok=True)

print("=" * 60)
print("OOTDiffusion Model Downloader")
print("=" * 60)

# Define all files to download
downloads = [
    # OOTD HD models
    ("levihsu/OOTDiffusion", "ootd_hd/checkpoint-36000/config.json", "checkpoints/ootd", None),
    ("levihsu/OOTDiffusion", "ootd_hd/checkpoint-36000/diffusion_pytorch_model.safetensors", "checkpoints/ootd", None),
    
    # OOTD DC models
    ("levihsu/OOTDiffusion", "ootd_dc/checkpoint-36000/config.json", "checkpoints/ootd", None),
    ("levihsu/OOTDiffusion", "ootd_dc/checkpoint-36000/diffusion_pytorch_model.safetensors", "checkpoints/ootd", None),
    
    # Human parsing models
    ("levihsu/OOTDiffusion", "humanparsing/parsing_atr.onnx", "checkpoints/humanparsing", None),
    ("levihsu/OOTDiffusion", "humanparsing/parsing_lip.onnx", "checkpoints/humanparsing", None),
    
    # OpenPose (already downloaded via annotator)
    # Skip since it's handled by the annotator __init__.py
    
    # CLIP vision model
    ("openai/clip-vit-large-patch14", "config.json", "checkpoints/clip-vit-large-patch14", None),
    ("openai/clip-vit-large-patch14", "preprocessor_config.json", "checkpoints/clip-vit-large-patch14", None),
    ("openai/clip-vit-large-patch14", "pytorch_model.bin", "checkpoints/clip-vit-large-patch14", None),
]

# Download each file
total = len(downloads)
success = 0

for i, (repo, filename, local_dir, subfolder) in enumerate(downloads, 1):
    print(f"\n[{i}/{total}] Processing {filename}")
    if download_file(repo, filename, local_dir, subfolder):
        success += 1

print("\n" + "=" * 60)
print(f"Download complete: {success}/{total} files downloaded")
print("=" * 60)

if success == total:
    print("✓ All models downloaded successfully!")
    print("\nYou can now run the app with:")
    print("  python run/gradio_ootd.py")
else:
    print(f"⚠ {total - success} files failed to download")
    print("You can re-run this script to retry failed downloads.")
