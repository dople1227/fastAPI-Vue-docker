import pytest
import pdb;

# 파일을 열고 파일 객체를 반환하는 픽스쳐 함수 정의
@pytest.fixture(scope="module")
def file_fixture():
    pdb.set_trace()
    # 파일을 여는 코드
    file = open("test_file.txt", "w+")
    # 파일 객체를 반환
    
    pdb.set_trace()
    yield file
    
    pdb.set_trace()
    # 정리(clean-up) 코드: 파일을 닫음    
    file.close()
    

# 파일에 데이터를 쓰고, 읽어서 확인하는 테스트 함수 정의
def test_file_operations(file_fixture):
    
    pdb.set_trace()
    file_fixture.write("Hello, pytest!")
    file_fixture.seek(0)
    content = file_fixture.read()
    
    pdb.set_trace()
    assert content == "Hello, pytest!"



def test_file_operations2(file_fixture):
    pdb.set_trace()
    file_fixture.write("Hello, pytest22!")
    file_fixture.seek(0)
    content = file_fixture.read()
    
    pdb.set_trace()
    assert content == "Hello, pytest22!"    