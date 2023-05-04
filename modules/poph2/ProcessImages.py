from src.utils.utils.s3_utils import S3Utils

from modules.api.models import TextToImageResponseV2


def tag_and_upload_image(request_id, local_file_path):
    file_name = local_file_path.split('\\')[-1]
    s3_file_path = f's3://h2-generated-images/{request_id}/{file_name}'
    S3Utils.upload_file_to_s3(local_file_path, s3_file_path)


def tag_and_upload_images(response: TextToImageResponseV2):
    file_paths = response.images_paths

    # Upload to s3
    for local_file_path in file_paths:
        tag_and_upload_image(request_id=response.request_id, local_file_path=local_file_path)

    # Notify Redis

    # Notify MySQL
