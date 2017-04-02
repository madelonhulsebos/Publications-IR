#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, sys
import json
from eS import testNaam

elastictest = testNaam()

testjson = json.dumps({
    "_id" : "journals_webology_ErfanmaneshH14",
    "year" : "2014",
    "ee" : "http://www.webology.org/2014/v11n1/bookreview24.pdf",
    "authors" : [ 
        "Mohammadamin Erfanmanesh", 
        "Elaheh Hosseini"
    ],
    "dblpkey" : "journals_webology_ErfanmaneshH14",
    "journal" : "Webology",
    "title" : "Visual indexing and retrieval.",
    "type" : "article",
    "content" : {
        "fulltext" : "Book Review \nVisual Indexing and Retrieval. Edited by Jenny Benois-Pineau, Frédéric Precioso and Matthieu Cord\n, New York : Springer, 2012. VIII, 107p. 17 illus. soft cover. ISBN 978-1-4614 / ISBN 978-1-4614-3588-4 (eBook), DOI: 10.1007/978-1-4614; £32.12. This book includes a preface, a table of contents, six informative chapters and expansive references. In the preface, the editors of the book claim that with the advent of social networks, vast amount of visual information is available for end-users. Therefore, they need innovative and fruitful methods for content understanding, retrieval and classification. \nChapter 1 is written by editors as introduction. They significantly emphasized that \" visual indexing and retrieval \" is a research challenge and has become of foremost importance nowadays. \nThe second chapter provides a deep overview of the basic visual feature extraction and description methods and approaches in the literature for images as well as for spatio-temporal data analysis. The chapter aims to clarify the process of the main recognition steps of detection and description of image. Interest point detection approaches, point-based and region-based detectors, the spatiotemporal feature extraction and some reference feature descriptors are also presented and discussed. On the rest, some well-known feature extraction schemes, like Harris and LoG detectors and feature description approaches like SIFT, SURF and GIST are presented. \nIn a later chapter, the exploitation of these descriptors in a global image processing chain is discussed. Feature Coding and pooling as main steps for deriving image representation from visual local descriptors are also detailed. Moreover, Bag-of-Visual-Words (BVW) including recent extensions as sparse coding and spatial pooling methods are explained. A class of similarity functions, called kernels (Fisher Kernel approach) is deeply presented as a strategy to build similarity measures. Additionally, two major contributions from the Machine learning community as learning algorithm namely Support Vector Machines (SVM) and Boosting are deeply explained. Lastly, new trends (LPBoost, MKL) in machine learning are expressed as well. \n Two trends in incorporation of spatial context in visual content indexing and retrieval and multiresolution/multiscale content description are addressed in chapter 4. Recent works on the border of BoVW and structural pattern recognition approaches called \" Graph Words \" are reviewed. Further, on the basis of scalable, multiresolution/multi-scale visual content representation in modern compression standards is presented. Furthermore, approaches which introduce spatial context during the matching process are explained and Structural pattern are widely represented by graphs. http://www.webology.org/2014/v11n1/bookreview24.html \nChapter 5 focuses on scalability which is a critical requirement for visual information retrieval. A typology of problems both for content-based retrieval and for mining is described in this chapter. Main ideas and recent advances and trends like the use of approximation or of shared-neighbor similarity are presented next. Finally, some prospective solutions such as low distortion embedding, filtering on simplified data representations, optimization of content representations and distributed processing are presented. Chapter 6 tries to give an overview of the evaluation process of visual information indexing and retrieval. Some major evaluation periodical campaigns for related tasks are introduced. Data collection, relevance judgments, performance measures, the metrics and experimentation protocols are discussed in this chapter as well. Finally, The detailed performance in recent campaigns (NIS, TRECVID, Pascal VOC, PetaMedia , ImageNet ILSVRC, ImageCLEF and MediaEval ) and the lessons learned from these campaigns are also presented. This book is a welcome addition to the existing literature that will benefit students, professors and academics in the field of information science and visual indexing. Reading this updated resource will also be enjoyable and inspiring for scholars, researchers, serious practitioners, information professionals, indexers and IT specialist who are interested in information retrieval. The explanations are briefly meaningful and are not overlooked, so, it makes a worth contribution to the debate. It is highly recommended to the editors to develop an index for next edition of the book. \nMohammadamin Erfanmanesh \n",
        "chapters" : [ 
            {}
        ]
    }
}, sort_keys=True, indent=4, separators=(',', ': '))

print json.loads(testjson)

# elastictest.index_docs(testjson)
