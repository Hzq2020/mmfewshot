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
            ann_cfg=[dict(method='FSCE', setting='SPLIT2_5SHOT')],
            num_novel_shots=5,
            num_base_shots=5,
            classes='ALL_CLASSES_SPLIT2')),
    val=dict(classes='ALL_CLASSES_SPLIT2'),
    test=dict(classes='ALL_CLASSES_SPLIT2'))
evaluation = dict(
    interval=700, class_splits=['BASE_CLASSES_SPLIT2', 'NOVEL_CLASSES_SPLIT2'])
checkpoint_config = dict(interval=5000)
optimizer = dict(lr=0.001)
lr_config = dict(warmup_iters=200, gamma=0.5, step=[5000, 7000])
runner = dict(max_iters=9000)
custom_hooks = [
    dict(
        type='ContrastiveLossDecayHook',
        decay_steps=(4000, 7000),
        decay_rate=0.5)
]
# load_from = 'path of base training model'
load_from = \
    'work_dirs/' \
    'fsce_faster_rcnn_r101_fpn_voc_split2_base_training/' \
    'model_reset_surgery.pth'
model = dict(
    roi_head=dict(
        bbox_head=dict(
            with_weight_decay=True,
            loss_contrast=dict(iou_threshold=0.7, loss_weight=0.5))))
