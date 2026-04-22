import torch
import os

# základní cesta ke složce s foldy
base_path = "/home/nohel/DATA/Brain_metastases_segmentation_test/BEAMSTER_nnUNet_models/Dataset505_Brain_metastases_dataset_final/nnUNetTrainer__nnUNetResEncUNetLPlansIso1x1x1_MT__Dataset903_MT_big_withholdout__MultiTalent_trainer_multistems_6000ep__nnUNetResEncUNetLPlansIso1x1x1_bs16__3d_fullres__fold_all__3d_fullres"

# procházení všech foldů
for fold in os.listdir(base_path):
    if fold.startswith('fold_'):
        fold_path = os.path.join(base_path, fold)
        checkpoint_path = os.path.join(fold_path, 'checkpoint_final.pth')
        if os.path.exists(checkpoint_path):
            # načtení checkpointu
            ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
            
            # změna trainer_name na klasický nnUNetTrainer
            ckpt['trainer_name'] = 'nnUNetTrainer'
            
            # uložení zpět
            torch.save(ckpt, checkpoint_path)
            
            print(f"Updated {fold}: trainer_name = {ckpt['trainer_name']}")
        else:
            print(f"Checkpoint not found in {fold}")

print("All folds processed.")