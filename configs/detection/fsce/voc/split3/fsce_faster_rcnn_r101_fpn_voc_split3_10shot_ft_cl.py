_base_ = [
    '../../../_base_/datasets/finetune_based/few_shot_voc.py',
    '../../../_base_/schedules/schedule.py',
    '../../fsce_faster_rcnn_r101_fpn_cl.py',
    '../../../_base_/default_runtime.py'
]
# classes splits are predefined in FewShotVOCDataset
# FewShotVOCDefaultDataset predefine ann_cfg for model reproducibility.
data = dict(
    train=dict(
        dataset=dict(
            type='FewShotVOCDefaultDataset',
            ann_cfg=[dict(method='FSCE', setting='SPLIT3_10SHOT')],
            num_novel_shots=10,
            num_base_shots=10,
            classes='ALL_CLASSES_SPLIT3')),
    val=dict(classes='ALL_CLASSES_SPLIT3'),
    test=dict(classes='ALL_CLASSES_SPLIT3'))
evaluation = dict(
    interval=700, class_splits=['BASE_CLASSES_SPLIT3', 'NOVEL_CLASSES_SPLIT3'])
checkpoint_config = dict(interval=5000)
optimizer = dict(lr=0.001)
lr_config = dict(warmup_iters=200, gamma=0.5, step=[8000, 13000])
runner = dict(max_iters=15000)
custom_hooks = [
    dict(
        type='ContrastiveLossDecayHook',
        decay_steps=(6000, 10000),
        decay_rate=0.5)
]
# load_from = 'path of base training model'
load_from = \
    'work_dirs/' \
    'fsce_faster_rcnn_r101_fpn_voc_split3_base_training/' \
    'model_reset_surgery.pth'
model = dict(
    roi_head=dict(
        bbox_head=dict(
            with_weight_decay=True,
            loss_contrast=dict(iou_threshold=0.8, loss_weight=0.5))))
