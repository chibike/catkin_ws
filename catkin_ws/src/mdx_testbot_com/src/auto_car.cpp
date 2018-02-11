
#include <string>
#include <vector>
#include <stdio.h>

#include "pi_color.h"
#include "pi_video.h"
#include "pi_objects.h"
#include "opencv2/opencv.hpp"

using namespace blink;
using namespace std;

const string test_image_name = "/home/chibike/catkin_ws/src/mdx_testbot_com/images/auto-car/img_001.jpeg";

void test()
{
	Viewer view; view.start();
	#ifdef USE_CAMERA
		Camera cam(1);
		cam.start();
	#else
		StaticImage still(test_image_name);
		still.start();
	#endif

	std::vector<RGBColor> color_array;
	
	color_array.push_back(BLACK_MAX);
	color_array.push_back(WHITE_MAX);
	color_array.push_back(RED_MAX);
	color_array.push_back(BLUE_MAX);
	color_array.push_back(GREEN_MAX);
	color_array.push_back(YELLOW_MAX);
	color_array.push_back(MAGENTA_MAX);
	color_array.push_back(CYAN_MAX);

	cv::Mat frame;

	while (1)
	{
		#ifdef USE_CAMERA
			cv::Mat frame = cam.get_next_frame();
		#else
			cv::Mat frame = still.get_next_frame();
		#endif

		simplify_image(frame, color_array);
		int key = view.show_frame(frame);
		if ( key == 113 || key < 0 )
		{
			break;
		}
	}

	#ifdef USE_CAMERA
		cam.stop();
	#else
		still.stop();
	#endif
	view.stop();
}

int main()
{
	test();
	return 0;
}