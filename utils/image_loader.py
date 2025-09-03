# utils/image_loader.py
import os
from pathlib import Path
from django.conf import settings

def load_images_from_static(folder_path, filename_prefix=''):
    """
    static 폴더에서 이미지 파일들을 찾아서 리스트로 반환
    
    Args:
        folder_path (str): static 기준 폴더 경로 (예: 'images/final_page/hypothesis_01')
        filename_prefix (str): 파일명 접두사 (예: 'chart')
    
    Returns:
        list: [{'filename': '파일명', 'path': '웹경로', 'name_without_ext': '확장자없는이름'}, ...]
    """
    images = []
    
    try:
        # static 폴더 경로 찾기
        static_path = Path(settings.BASE_DIR) / 'static' / folder_path
        
        # 폴더가 존재하는지 확인
        if not static_path.exists():
            print(f"폴더가 없습니다: {static_path}")
            return images
        
        # 이미지 확장자
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']
        
        # 폴더 내 파일들 확인
        for file_path in static_path.iterdir():
            if file_path.is_file():
                filename = file_path.name
                extension = file_path.suffix.lower()
                
                # 이미지 파일인지 확인
                if extension not in image_extensions:
                    continue
                
                # 접두사 확인
                if filename_prefix and not filename.startswith(filename_prefix):
                    continue
                
                # 웹에서 접근할 수 있는 경로
                web_path = f'{folder_path}/{filename}'
                
                images.append({
                    'filename': filename,
                    'path': web_path,
                    'name_without_ext': file_path.stem
                })
        
        # 파일명으로 정렬
        images.sort(key=lambda x: x['filename'])
        
    except Exception as e:
        print(f"이미지 로딩 오류: {e}")
    
    return images