"""
Simple test to verify OOTDiffusion models are loading correctly
"""
import sys
import os

print("=" * 60)
print("OOTDiffusion Model Test")
print("=" * 60)

# Test 1: Check critical files exist
print("\n1. Checking if model files exist...")
files_to_check = [
    'checkpoints/humanparsing/parsing_atr.onnx',
    'checkpoints/humanparsing/parsing_lip.onnx',
    'checkpoints/ootd/model_index.json',
    'checkpoints/ootd/ootd_hd/checkpoint-36000/unet_garm/config.json',
    'checkpoints/ootd/ootd_hd/checkpoint-36000/unet_vton/config.json',
    'checkpoints/clip-vit-large-patch14/pytorch_model.bin',
]

all_exist = True
for file in files_to_check:
    exists = os.path.exists(file)
    status = "✓" if exists else "✗"
    print(f"  {status} {file}")
    if not exists:
        all_exist = False

if not all_exist:
    print("\n✗ Some model files are missing!")
    sys.exit(1)

print("\n✓ All critical model files exist!")

# Test 2: Try importing the modules
print("\n2. Testing module imports...")
try:
    from preprocess.humanparsing.run_parsing import Parsing
    print("  ✓ Parsing module imported")
except Exception as e:
    print(f"  ✗ Error importing Parsing: {e}")
    sys.exit(1)

try:
    from preprocess.openpose.run_openpose import OpenPose
    print("  ✓ OpenPose module imported")
except Exception as e:
    print(f"  ✗ Error importing OpenPose: {e}")
    sys.exit(1)

try:
    from ootd.inference_ootd_hd import OOTDiffusionHD
    print("  ✓ OOTDiffusionHD module imported")
except Exception as e:
    print(f"  ✗ Error importing OOTDiffusionHD: {e}")
    sys.exit(1)

print("\n✓ All modules imported successfully!")

# Test 3: Try initializing Parsing model (fastest to load)
print("\n3. Testing Parsing model initialization...")
print("  This may take a minute on CPU...")
try:
    parsing_model = Parsing(-1)  # -1 = CPU mode
    print("  ✓ Parsing model initialized successfully!")
except Exception as e:
    print(f"  ✗ Error initializing Parsing model: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ All tests passed!")
print("=" * 60)
print("\nThe models are ready to use.")
print("You can now run the Gradio app with:")
print("  python run/gradio_ootd.py")
print("\nNote: On CPU, the first run will take several minutes to load all models.")
