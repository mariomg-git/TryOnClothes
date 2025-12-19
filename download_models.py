"""
Download required model checkpoints for OOTDiffusion
"""
import os
from huggingface_hub import snapshot_download

# Create checkpoints directory
os.makedirs("checkpoints", exist_ok=True)

print("Downloading OOTDiffusion models...")
print("This may take 10-20 minutes depending on your internet connection.\n")

# Download OOTD checkpoints
print("1/4 Downloading OOTD models...")
snapshot_download(
    repo_id="levihsu/OOTDiffusion",
    local_dir="checkpoints/ootd",
    allow_patterns=["*.json", "*.safetensors", "*.txt", "*.bin", "*.pth", "*.ckpt", "*.model"],
)

# Download humanparsing checkpoints
print("2/4 Downloading human parsing models...")
snapshot_download(
    repo_id="levihsu/OOTDiffusion",
    local_dir="checkpoints/humanparsing",
    allow_patterns=["humanparsing/*"],
)

# Download openpose checkpoints
print("3/4 Downloading OpenPose models...")
snapshot_download(
    repo_id="levihsu/OOTDiffusion",
    local_dir="checkpoints/openpose",
    allow_patterns=["openpose/*"],
)

# Download CLIP model
print("4/4 Downloading CLIP vision model...")
snapshot_download(
    repo_id="openai/clip-vit-large-patch14",
    local_dir="checkpoints/clip-vit-large-patch14",
)

print("\n✓ All models downloaded successfully!")
print("You can now run the app with: run_app.bat")
