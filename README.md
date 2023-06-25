# detecting-moon-craters-YOLOv5
Detecting craters using machine learning techniques and plotting their distribution by diameter

Using YOLOv5, I was able to train model "yolov5x.yaml" on a dataset and I obtained the weights file "best.pt". Using this file, you can then detect craters in a high-res photo of the moon and plot their distribution by diameter. I obtained the diameters by counting the pixels of the smallest side of the rectangular bounding box - this could, roughly, represent the diameter - and multiplied it by 400, since the image I used had a resolution of about 400 m/pixel. I implemented this small change in the source of the "detect.py" file (file "detect_areas2.py") - more precisely the part:

                with open("detected_areas", "a") as out1, open("detected_diameters", "a") as out2:
                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        x1, y1, x2, y2 = xyxy
                        if (x2 - x1) < (y2 - y1):
                            diameter = (x2 - x1) * 400
                            out2.write(str(diameter) + "\n")
                            area = m.pi * ((diameter/2) ** 2)
                            print("crater_diameter=" + str(x2 - x1) + "px")
                            out1.write(str(area) + "\n")
                        else:
                            diameter = (y2 - y1) * 400
                            out2.write(str(diameter) + "\n")
                            area = m.pi * ((diameter/2) ** 2)
                            print("crater_diameter=" + str(y2 - y1) + "px")
                            out1.write(str(area) + "\n")


The dataset I used - 2500 training, 711 validation and 356 testing images - comes from:

@misc{ crater-vrqmn_dataset,
    title = { crater Dataset },
    type = { Open Source Dataset },
    author = { crater },
    howpublished = { \url{ https://universe.roboflow.com/crater-zqpjg/crater-vrqmn } },
    url = { https://universe.roboflow.com/crater-zqpjg/crater-vrqmn },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { jun },
    note = { visited on 2023-06-25 },
}

YOLOv5:

@software{yolov5,
  title = {YOLOv5 by Ultralytics},
  author = {Glenn Jocher},
  year = {2020},
  version = {7.0},
  license = {AGPL-3.0},
  url = {https://github.com/ultralytics/yolov5},
  doi = {10.5281/zenodo.3908559},
  orcid = {0000-0001-5950-6979}
}
