import os
from pathlib import Path

BATCH_SIZE = 128
IMG_SIZE = 224
DIM = 768
NUM_CLASSES = 10
NUM_ATTN_HEADS = 12

# resnet 18
model = dict(type='VanillaResNet',
             block_type='ResNetBasicBlock',
             layers=[2, 2, 2, 2],
             num_cls=10)

train_data = dict(dataset=dict(type='CIFAR10Dataset',
                               root=Path(os.environ['DATA']),
                               download=True,
                               transform_pipeline=[
                                   dict(type='Resize',
                                        size=(IMG_SIZE, IMG_SIZE)),
                                   dict(type='ToTensor'),
                                   dict(type='Normalize',
                                        mean=(0.5, 0.5, 0.5),
                                        std=(0.5, 0.5, 0.5))
                               ]),
                  dataloader=dict(batch_size=BATCH_SIZE,
                                  pin_memory=True,
                                  num_workers=4,
                                  drop_last=True))

optimizer = dict(type='Adam', lr=0.001)

loss = dict(type='CrossEntropyLoss')

parallel = dict(
    pipeline=dict(size=4),
    tensor=dict(size=1, mode=None)
)

schedule = dict(
    num_microbatches=4
)
num_pipeling_batches = 2
seed = 1024
lr_scheduler = dict(type='LinearWarmupLR', warmup_steps=5)

num_epochs = 10
