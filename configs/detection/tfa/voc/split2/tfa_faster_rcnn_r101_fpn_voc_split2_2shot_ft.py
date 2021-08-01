_base_ = [
    '../../../_base_/datasets/finetune_based/few_shot_voc.py',
    '../../../_base_/schedules/schedule.py',
    '../../tfa_faster_rcnn_r101_fpn.py', '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
# FewShotVOCDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        dataset=dict(
            type='FewShotVOCDefaultDataset',
            ann_cfg=[dict(method='TFA', setting='SPLIT2_2SHOT')],
            num_novel_shots=2,
            num_base_shots=2,
            classes='ALL_CLASSES_SPLIT2',
        )),
    val=dict(classes='ALL_CLASSES_SPLIT2'),
    test=dict(classes='ALL_CLASSES_SPLIT2'))
evaluation = dict(
    interval=8000,
    class_splits=['BASE_CLASSES_SPLIT2', 'NOVEL_CLASSES_SPLIT2'])
checkpoint_config = dict(interval=8000)
optimizer = dict(lr=0.005)
lr_config = dict(
    warmup=None, step=[
        7000,
    ])
runner = dict(max_iters=8000)
# load_from = 'path of base training model'
load_from = \
    'work_dirs/' \
    'tfa_faster_rcnn_r101_fpn_voc_split2_base_training/' \
    'model_reset_surgery.pth'
