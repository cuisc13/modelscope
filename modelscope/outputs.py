# Copyright (c) Alibaba, Inc. and its affiliates.

from modelscope.utils.constant import Tasks


class OutputKeys(object):
    LOSS = 'loss'
    LOGITS = 'logits'
    SCORES = 'scores'
    LABEL = 'label'
    LABELS = 'labels'
    LABEL_POS = 'label_pos'
    POSES = 'poses'
    CAPTION = 'caption'
    BOXES = 'boxes'
    KEYPOINTS = 'keypoints'
    MASKS = 'masks'
    TEXT = 'text'
    POLYGONS = 'polygons'
    OUTPUT = 'output'
    OUTPUT_IMG = 'output_img'
    OUTPUT_PCM = 'output_pcm'
    IMG_EMBEDDING = 'img_embedding'
    TEXT_EMBEDDING = 'text_embedding'
    TRANSLATION = 'translation'
    RESPONSE = 'response'
    PREDICTION = 'prediction'
    PREDICTIONS = 'predictions'
    PROBABILITIES = 'probabilities'
    DIALOG_STATES = 'dialog_states'
    VIDEO_EMBEDDING = 'video_embedding'


TASK_OUTPUTS = {

    # ============ vision tasks ===================

    # image classification result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["dog", "horse", "cow", "cat"],
    #   }
    Tasks.image_classification: [OutputKeys.SCORES, OutputKeys.LABELS],
    Tasks.image_tagging: [OutputKeys.SCORES, OutputKeys.LABELS],

    # object detection result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["dog", "horse", "cow", "cat"],
    #       "boxes": [
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #       ],
    #   }
    Tasks.object_detection:
    [OutputKeys.SCORES, OutputKeys.LABELS, OutputKeys.BOXES],

    # face detection result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "boxes": [
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #       ],
    #       "keypoints": [
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #       ],
    #   }
    Tasks.face_detection:
    [OutputKeys.SCORES, OutputKeys.BOXES, OutputKeys.KEYPOINTS],

    # face recognition result for single sample
    #   {
    #       "img_embedding": np.array with shape [1, D],
    #   }
    Tasks.face_recognition: [OutputKeys.IMG_EMBEDDING],

    # instance segmentation result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05],
    #       "labels": ["dog", "horse", "cow", "cat"],
    #       "boxes": [
    #           np.array in bgr channel order
    #       ]
    #   }
    Tasks.image_segmentation:
    [OutputKeys.SCORES, OutputKeys.LABELS, OutputKeys.BOXES],

    # image generation/editing/matting result for single sample
    # {
    #   "output_img": np.array with shape(h, w, 4)
    #                 for matting or (h, w, 3) for general purpose
    # }
    Tasks.image_editing: [OutputKeys.OUTPUT_IMG],
    Tasks.image_matting: [OutputKeys.OUTPUT_IMG],
    Tasks.image_generation: [OutputKeys.OUTPUT_IMG],
    Tasks.image_denoise: [OutputKeys.OUTPUT_IMG],
    Tasks.image_colorization: [OutputKeys.OUTPUT_IMG],
    Tasks.face_image_generation: [OutputKeys.OUTPUT_IMG],
    Tasks.image_super_resolution: [OutputKeys.OUTPUT_IMG],

    # action recognition result for single video
    # {
    #   "output_label": "abseiling"
    # }
    Tasks.action_recognition: [OutputKeys.LABELS],

    # live category recognition result for single video
    # {
    #       "scores": [0.885272, 0.014790631, 0.014558001]
    #       "labels": ['女装/女士精品>>棉衣/棉服', '女装/女士精品>>牛仔裤', '女装/女士精品>>裤子>>休闲裤'],
    # }
    Tasks.live_category: [OutputKeys.SCORES, OutputKeys.LABELS],
    # video category recognition result for single video
    # {
    #       "scores": [0.7716429233551025]
    #       "labels": ['生活>>好物推荐'],
    # }
    Tasks.video_category: [OutputKeys.SCORES, OutputKeys.LABELS],

    # pose estimation result for single sample
    # {
    #   "poses": np.array with shape [num_pose, num_keypoint, 3],
    #       each keypoint is a array [x, y, score]
    #   "boxes": np.array with shape [num_pose, 4], each box is
    #       [x1, y1, x2, y2]
    # }
    Tasks.pose_estimation: [OutputKeys.POSES, OutputKeys.BOXES],

    # ocr detection result for single sample
    # {
    #   "polygons": np.array with shape [num_text, 8], each polygon is
    #       [x1, y1, x2, y2, x3, y3, x4, y4]
    # }
    Tasks.ocr_detection: [OutputKeys.POLYGONS],

    # image embedding result for a single image
    # {
    #   "image_bedding": np.array with shape [D]
    # }
    Tasks.product_retrieval_embedding: [OutputKeys.IMG_EMBEDDING],

    # video embedding result for single video
    # {
    #   "video_embedding": np.array with shape [D],
    # }
    Tasks.video_embedding: [OutputKeys.VIDEO_EMBEDDING],

    # image_color_enhance result for a single sample
    # {
    #    "output_img": np.ndarray with shape [height, width, 3], uint8
    # }
    Tasks.image_color_enhance: [OutputKeys.OUTPUT_IMG],

    # ============ nlp tasks ===================

    # text classification result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["happy", "sad", "calm", "angry"],
    #   }
    Tasks.text_classification: [OutputKeys.SCORES, OutputKeys.LABELS],

    # text generation result for single sample
    # {
    #   "text": "this is the text generated by a model."
    # }
    Tasks.text_generation: [OutputKeys.TEXT],

    # fill mask result for single sample
    # {
    #   "text": "this is the text which masks filled by model."
    # }
    Tasks.fill_mask: [OutputKeys.TEXT],

    # word segmentation result for single sample
    # {
    #   "output": "今天 天气 不错 ， 适合 出去 游玩"
    # }
    Tasks.word_segmentation: [OutputKeys.OUTPUT],

    # named entity recognition result for single sample
    # {
    #   "output": [
    #     {"type": "LOC", "start": 2, "end": 5, "span": "温岭市"},
    #     {"type": "LOC", "start": 5, "end": 8, "span": "新河镇"}
    #   ]
    # }
    Tasks.named_entity_recognition: [OutputKeys.OUTPUT],

    # sentence similarity result for single sample
    #   {
    #       "scores": 0.9
    #       "labels": "1",
    #   }
    Tasks.sentence_similarity: [OutputKeys.SCORES, OutputKeys.LABELS],

    # translation result for a source sentence
    #   {
    #       "translation": “北京是中国的首都”
    #   }
    Tasks.translation: [OutputKeys.TRANSLATION],

    # sentiment classification result for single sample
    #   {
    #       "labels": ["happy", "sad", "calm", "angry"],
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #   }
    Tasks.sentiment_classification: [OutputKeys.SCORES, OutputKeys.LABELS],

    # zero-shot classification result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["happy", "sad", "calm", "angry"],
    #   }
    Tasks.zero_shot_classification: [OutputKeys.SCORES, OutputKeys.LABELS],

    # nli result for single sample
    #   {
    #       "labels": ["happy", "sad", "calm", "angry"],
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #   }
    Tasks.nli: [OutputKeys.SCORES, OutputKeys.LABELS],

    # dialog intent prediction result for single sample
    # {'pred': array([2.62349960e-03, 4.12110658e-03, 4.12748595e-05, 3.77560973e-05,
    #        1.08599677e-04, 1.72710388e-05, 2.95618793e-05, 1.93638436e-04,
    #        6.45841064e-05, 1.15997791e-04, 5.11605394e-05, 9.87020373e-01,
    #        2.66957268e-05, 4.72324500e-05, 9.74208378e-05, 4.18022355e-05,
    #        2.97343540e-05, 5.81317654e-05, 5.44203431e-05, 6.28319322e-05,
    #        7.34537680e-05, 6.61411541e-05, 3.62534920e-05, 8.58885178e-05,
    #        8.24327726e-05, 4.66077945e-05, 5.32869453e-05, 4.16190960e-05,
    #        5.97518992e-05, 3.92273068e-05, 3.44069012e-05, 9.92335918e-05,
    #        9.25978165e-05, 6.26462061e-05, 3.32317031e-05, 1.32061413e-03,
    #        2.01607945e-05, 3.36636294e-05, 3.99156743e-05, 5.84108493e-05,
    #        2.53432900e-05, 4.95731190e-04, 2.64443643e-05, 4.46992999e-05,
    #        2.42672231e-05, 4.75615161e-05, 2.66230145e-05, 4.00083954e-05,
    #        2.90536875e-04, 4.23891543e-05, 8.63691166e-05, 4.98188965e-05,
    #        3.47019341e-05, 4.52718523e-05, 4.20905781e-05, 5.50173208e-05,
    #        4.92360487e-05, 3.56021264e-05, 2.13957210e-05, 6.17428886e-05,
    #        1.43893281e-04, 7.32152112e-05, 2.91354867e-04, 2.46623786e-05,
    #        3.61441926e-05, 3.38475402e-05, 3.44323053e-05, 5.70138109e-05,
    #        4.31488479e-05, 4.94503947e-05, 4.30105974e-05, 1.00963116e-04,
    #        2.82062047e-05, 1.15582036e-04, 4.48261271e-05, 3.99339879e-05,
    #        7.27692823e-05], dtype=float32), 'label_pos': array([11]), 'label': 'lost_or_stolen_card'}
    Tasks.dialog_intent_prediction:
    [OutputKeys.PREDICTION, OutputKeys.LABEL_POS, OutputKeys.LABEL],

    # dialog modeling prediction result for single sample
    # sys : ['you', 'are', 'welcome', '.', 'have', 'a', 'great', 'day', '!']
    Tasks.dialog_modeling: [OutputKeys.RESPONSE],

    # dialog state tracking result for single sample
    # {
    #     "dialog_states": {
    #         "taxi-leaveAt": "none",
    #         "taxi-destination": "none",
    #         "taxi-departure": "none",
    #         "taxi-arriveBy": "none",
    #         "restaurant-book_people": "none",
    #         "restaurant-book_day": "none",
    #         "restaurant-book_time": "none",
    #         "restaurant-food": "none",
    #         "restaurant-pricerange": "none",
    #         "restaurant-name": "none",
    #         "restaurant-area": "none",
    #         "hotel-book_people": "none",
    #         "hotel-book_day": "none",
    #         "hotel-book_stay": "none",
    #         "hotel-name": "none",
    #         "hotel-area": "none",
    #         "hotel-parking": "none",
    #         "hotel-pricerange": "cheap",
    #         "hotel-stars": "none",
    #         "hotel-internet": "none",
    #         "hotel-type": "true",
    #         "attraction-type": "none",
    #         "attraction-name": "none",
    #         "attraction-area": "none",
    #         "train-book_people": "none",
    #         "train-leaveAt": "none",
    #         "train-destination": "none",
    #         "train-day": "none",
    #         "train-arriveBy": "none",
    #         "train-departure": "none"
    #     }
    # }
    Tasks.dialog_state_tracking: [OutputKeys.DIALOG_STATES],

    # ============ audio tasks ===================

    # audio processed for single file in PCM format
    # {
    #   "output_pcm": np.array with shape(samples,) and dtype float32
    # }
    Tasks.speech_signal_process: [OutputKeys.OUTPUT_PCM],
    Tasks.acoustic_echo_cancellation: [OutputKeys.OUTPUT_PCM],
    Tasks.acoustic_noise_suppression: [OutputKeys.OUTPUT_PCM],

    # ============ multi-modal tasks ===================

    # image caption result for single sample
    # {
    #   "caption": "this is an image caption text."
    # }
    Tasks.image_captioning: [OutputKeys.CAPTION],

    # multi-modal embedding result for single sample
    # {
    #   "img_embedding": np.array with shape [1, D],
    #   "text_embedding": np.array with shape [1, D]
    # }
    Tasks.multi_modal_embedding:
    [OutputKeys.IMG_EMBEDDING, OutputKeys.TEXT_EMBEDDING],

    # generative multi-modal embedding result for single sample
    # {
    #   "img_embedding": np.array with shape [1, D],
    #   "text_embedding": np.array with shape [1, D],
    #   "caption": "this is an image caption text."
    # }
    Tasks.generative_multi_modal_embedding:
    [OutputKeys.IMG_EMBEDDING, OutputKeys.TEXT_EMBEDDING, OutputKeys.CAPTION],

    # visual grounding result for single sample
    # {
    #       "boxes": [
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #       ],
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    # }
    Tasks.visual_grounding: [OutputKeys.BOXES, OutputKeys.SCORES],

    # text_to_image result for a single sample
    # {
    #    "output_img": np.ndarray with shape [height, width, 3]
    # }
    Tasks.text_to_image_synthesis: [OutputKeys.OUTPUT_IMG],

    # text_to_speech result for a single sample
    # {
    #    "output_pcm": {"input_label" : np.ndarray with shape [D]}
    # }
    Tasks.text_to_speech: [OutputKeys.OUTPUT_PCM],
    # virtual_try_on result for a single sample
    # {
    #    "output_img": np.ndarray with shape [height, width, 3]
    # }
    Tasks.virtual_try_on: [OutputKeys.OUTPUT_IMG],
    # visual_question_answering result for a single sample
    # {
    #    "text": "this is the text generated by a model."
    # }
    Tasks.visual_question_answering: [OutputKeys.TEXT],
    # auto_speech_recognition result for a single sample
    # {
    #    "text": "每天都要快乐喔"
    # }
    Tasks.auto_speech_recognition: [OutputKeys.TEXT],

    # text_error_correction result for a single sample
    # {
    #    "output": "我想吃苹果"
    # }
    Tasks.text_error_correction: [OutputKeys.OUTPUT]
}
