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
            ann_cfg=[dict(method='TFA', setting='SPLIT3_10SHOT')],
            num_novel_shots=10,
            num_base_shots=10,
            classes='ALL_CLASSES_SPLIT3',
        )),
    val=dict(classes='ALL_CLASSES_SPLIT3'),
    test=dict(classes='ALL_CLASSES_SPLIT3'))
evaluation = dict(
    interval=40000,
    class_splits=['BASE_CLASSES_SPLIT3', 'NOVEL_CLASSES_SPLIT3'])
checkpoint_config = dict(interval=40000)
optimizer = dict(lr=0.001)
lr_config = dict(
    warmup_iters=10, step=[
        36000,
    ])
runner = dict(max_iters=40000)
# load_from = 'path of base training model'
load_from = \
    'work_dirs/' \
    'tfa_faster_rcnn_r101_fpn_voc_split3_base_training/' \
    'model_reset_surgery.pth'
