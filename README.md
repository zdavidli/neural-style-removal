Datasets:
*  https://github.com/BathVisArtData/PhotoArt50
*  https://github.com/BathVisArtData/PeopleArt
*  http://www.robots.ox.ac.uk/~vgg/data/paintings/

Reading:
*  YOLOv2 https://pjreddie.com/darknet/yolo/
*  YOLO https://arxiv.org/pdf/1506.02640.pdf
*  Faster R-CNN https://arxiv.org/pdf/1506.01497.pdf
*  RCNN history https://blog.athelas.com/a-brief-history-of-cnns-in-image-segmentation-from-r-cnn-to-mask-r-cnn-34ea83205de4
*  Neural Style Transfer https://medium.com/artists-and-machine-intelligence/neural-artistic-style-transfer-a-comprehensive-look-f54d8649c199
*  Neural Style Transfer Review https://arxiv.org/pdf/1705.04058.pdf


Project Idea:
Detecting objects in artwork with R-CNN, Fast R-CNN, and YOLO/YOLOv2 (in PyTorch?)
1. Start with pre-trained model and report results on PeopleArt, PhotoArt50
2. Try training on PhotoArt/PeopleArt.
3. Try "removing" style with neural style transfer from painting to photograph.
3. Try "removing" style by tuning parameters in neural style transfer.


Presentation Goal:
* Have pre-trained results of some R-CNN variant and YOLO on PeopleArt and PhotoArt50
* (Hopefully) train one of R-CNN variant and YOLO on PeopleArt or PhotoArt50
* Have basic neural style removal

Current progress:
* Have some neural style removal, not good in general, but have one figure and can explain what we've tried and what we can keep trying
* Have DataLoader for PeopleArt, PeopleArt photos
* (David) Working on YOLO pre-trained - Pytorch version is really finicky... maybe I'll try the tensorflow version...
