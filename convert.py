def convert_p6_to_p3(input_file, output_file):
    # P6 파일을 바이너리 모드로 열기
    with open(input_file, 'rb') as f:
        # 매직 넘버 읽기
        magic = f.readline().decode('ascii').strip()
        if magic != 'P6':
            raise ValueError(f"입력 파일이 P6 형식이 아닙니다: {magic}")
        
        # 주석 건너뛰기
        line = f.readline()
        while line.startswith(b'#'):
            line = f.readline()
        
        # 너비와 높이 읽기
        dimensions = line.decode('ascii').strip()
        if not dimensions:  # 빈 줄이면 다음 줄 읽기
            dimensions = f.readline().decode('ascii').strip()
        
        width, height = map(int, dimensions.split())
        
        # 최대 색상 값 읽기
        max_val = int(f.readline().decode('ascii').strip())
        
        # 픽셀 데이터 읽기
        pixels = f.read()

    # P3 형식으로 변환하여 텍스트 모드로 파일 작성
    with open(output_file, 'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write(f'{max_val}\n')
        
        # 픽셀 데이터 변환
        pixel_count = 0
        values_per_line = 0
        for i in range(0, len(pixels), 3):
            r = pixels[i]
            g = pixels[i+1]
            b = pixels[i+2]
            
            if values_per_line >= 4:  # 한 줄에 RGB 값 4개씩 (총 12개 숫자)
                f.write('\n')
                values_per_line = 0
                
            f.write(f"{r} {g} {b}")
            pixel_count += 1
            values_per_line += 1
            
            if pixel_count < width * height:
                f.write(' ')

if __name__ == "__main__":
    input_file = "/home/data/colorP6File.ppm"
    output_file = "./colorP3File.ppm"
    convert_p6_to_p3(input_file, output_file)
    print(f"{input_file}를 P3 형식으로 변환하여 {output_file}에 저장했습니다.")
