
import os
import cv2

def read_picture():
    video_path = input('请输入视频保存的路径: ')
    image_path = input('请输入图片素材的路径: ')
    fps = input('请输入视频的帧速率，秒为单位，一秒播放多少张照片：')  # 视频每秒2帧
    img_size = input('请输入目标视频尺寸，如1376x768: ')
    img_size = img_size.split('x')
    weight = img_size[0]
    height = img_size[1]
    size = (int(weight), int(height))  # 需要转为视频的图片的尺寸
    file_list = os.listdir(image_path)
    return [video_path, image_path, fps, size, file_list]


def write_video():
    video_path, image_path, fps, size, file_list = read_picture()
    # AVI格式编码输出 XVID
    four_cc = cv2.VideoWriter_fourcc(*'XVID')
    save_path = video_path + '\\' + 'output.avi'
    video_writer = cv2.VideoWriter(save_path, four_cc, float(fps), size)
    # 视频保存在当前目录下
    for item in file_list:
        if item.endswith('.jpg') or item.endswith('.png'):
            # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
            item = image_path + '\\' + item
            img = cv2.imread(item)
            re_pics = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)  # 定尺寸
            #输出帧率信息
            cv2.putText(re_pics,'FPS:%.2f'%(float(fps)),(10,30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
            video_writer.write(re_pics)

    video_writer.release()
    cv2.destroyAllWindows()
    print("视频输出成功!")


if __name__ == '__main__':
    write_video()
