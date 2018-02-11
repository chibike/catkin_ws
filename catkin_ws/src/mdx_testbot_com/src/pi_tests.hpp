#ifndef BLINK_PI_TESTS_HPP
#define BLINK_PI_TESTS_HPP

#include "pi_color.h"
#include "pi_video.h"
#include "pi_objects.h"
#include "opencv2/opencv.hpp"

#define USE_CAMERA

namespace blink
{
	const string test_image_name = "/home/chibike/catkin_ws/src/mdx_testbot_com/images/img_001.jpeg";

	void test_video()
	{
		Viewer view; view.start();
		#ifdef USE_CAMERA
			Camera cam(1);
			cam.start();
		#else
			StaticImage still(test_image_name);
			still.start();
		#endif

		while (1)
		{
			#ifdef USE_CAMERA
				cv::Mat frame = cam.get_next_frame();
			#else
				cv::Mat frame = still.get_next_frame();
			#endif

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

	void test_simplify_image()
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

	void test_objects()
	{
		cv::Mat frame;
		cv::Scalar path_color(255,0,0);
		cv::Scalar shade_color(0,255,0);

		std::vector<Point> points;
		std::vector<Line> lines;

		points.push_back(Point(240, 80));
		points.push_back(Point(400, 400));
		points.push_back(Point(80,  400));

		Path my_path = Path(points, false);

		// visualise
		Viewer view(4, "objects"); view.start();
		while (1)
		{
			frame = cv::Mat(480, 480, CV_8UC3, cv::Scalar(0,0,0));

			my_path.rotate(0.1);
			my_path.draw(frame, path_color);

			lines = my_path.get_intersecting_lines(10, 0.0);
			for (int i=0; i<lines.size(); i++)
			{
				Line line = lines.at(i);
				line.draw(frame, shade_color);
			}

			lines = my_path.get_intersecting_lines(10, M_PI_2);
			for (int i=0; i<lines.size(); i++)
			{
				Line line = lines.at(i);
				line.draw(frame, shade_color);
			}

			int key = view.show_frame(frame);
			if ( key == 113 || key < 0 )
			{
				break;
			}
		}
		view.stop();
	}
}

#endif /*BLINK_PI_TESTS_HPP*/