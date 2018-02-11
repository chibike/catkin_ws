#ifndef BLINK_PI_OBJECTS_H
#define BLINK_PI_OBJECTS_H

#include <vector>
#include <math.h>
#include "Eigen/Dense"
#include "opencv2/opencv.hpp"

namespace blink
{

using namespace std;
using Eigen::MatrixXd;

double maximum_element(std::vector<double> list)
{
	double max_element = list.at(0);
	for (int i=0; i<list.size(); i++)
	{
		double element = list.at(i);

		if (element > max_element)
		{
			max_element = element;
		}
	}
	return max_element;
}

double minimum_element(std::vector<double> list)
{
	double min_element = list.at(0);
	for (int i=0; i<list.size(); i++)
	{
		double element = list.at(i);

		if (element < min_element)
		{
			min_element = element;
		}
	}
	return min_element;
}

class Point
{
public:
	double          x;
	double          y;
	double          r;
	double          theta;
	vector<double>  point;
	vector<double>  point_polar;

	Point();
	Point(double xx, double yy);

	Point           add(Point other);
	Point           sub(Point other);
	Point           mul(Point other);
	Point           div(Point other);
	bool            equal(Point other);
	vector<double>  get_as_polar();
};

class Line
{
public:
	Point          start;
	Point          end;
	vector<Point>  line;
	double         m;
	Point          ref_point;
	double         length;
	double         angle;

	Line(Point point1, Point point2);

	void   compute();
	Point  _rotate_coord(Point coord, double angle, Point about_point);
	void   rotate(double angle);
	void   rotate(double angle, Point about_point);
	double get_length();
	double get_gradient();
	double get_angle();
	Point  get_midpoint();
	void   plot();
	void   plot(string title);
	bool   is_on_line(Point point);
	Point  get_intersecting_point(Line other);
	void   draw(cv::Mat image, cv::Scalar color);
	void   draw(cv::Mat image, cv::Scalar color, int stroke_width, int line_type, int shift);
};

struct RectInfo
{
	Point bottom_right;
	Point center;
	Point top_left;
	double height;
	double width;
	double radius;
	double area;
};

class Path
{
public:
	std::vector<Point> data_points;
	std::vector<double> xs;
	std::vector<double> ys;
	std::vector<Line> boundary_lines;

	bool closed;
	RectInfo rect_info;

	Path(std::vector<Point> raw_point_data, bool closed);

	Point get_start_point();
	Point get_end_point();
	RectInfo get_rect_info();
	std::vector<Line> get_boundary_lines();
	std::vector<Point> get_intersecting_points(Line test_line);
	std::vector<Line> get_shading_lines(double spacing, double angle, double padding);
	std::vector<Line> get_intersecting_lines(double spacing, double angle);
	void rotate(double angle);
	void rotate(double angle, Point pivot);
	void draw(cv::Mat image, cv::Scalar color);
	void draw(cv::Mat image, cv::Scalar color, int stroke_width, int line_type, int shift);

	void calculate();
	static bool _filter_x_function(Point current, Point next)
	{
		return current.x < next.x;
	}
};

double measure(Point point1, Point point2)
{
	double distance = sqrt(pow(point2.x - point1.x, 2) + pow(point2.y - point1.y, 2));
	return distance;
}

Point::Point()
{
	x = 0;
	y = 0;
	
	r = sqrt(pow(x, 2) + pow(y, 2));
	theta = atan2(y,x);

	point.push_back(x);
	point.push_back(y);
	point_polar.push_back(r);
	point_polar.push_back(theta);
}

Point::Point(double xx, double yy)
{
	x = xx;
	y = yy;

	r = sqrt(pow(x, 2) + pow(y, 2));
	theta = atan2(y,x);

	point.push_back(x);
	point.push_back(y);
	point_polar.push_back(r);
	point_polar.push_back(theta);
}

Point Point::add(Point other)
{
	Point new_point(x + other.x, y + other.y);
	return new_point;
}

Point Point::sub(Point other)
{
	Point new_point(x - other.x, y - other.y);
	return new_point;
}

Point Point::mul(Point other)
{
	Point new_point(x * other.x, y * other.y);
	return new_point;
}

Point Point::div(Point other)
{
	Point new_point(x / other.x, y / other.y);
	return new_point;
}

bool Point::equal(Point other)
{
	return (x == other.x && y == other.y);
}

vector<double> Point::get_as_polar()
{
	return point_polar;
}

Line::Line(Point point1, Point point2)
{
	start = point1;
	end = point2;

	compute();
}

void Line::compute()
{
	line.push_back(start);
	line.push_back(end);

	m = get_gradient();
	ref_point = start;
	length = get_length();
	angle = get_angle();
}

Point Line::_rotate_coord(Point coord, double angle, Point about_point)
{
	double c1 = about_point.x;
	double c2 = about_point.y;

	double xold = coord.x;
	double yold = coord.y;

	MatrixXd x(2,1);
	MatrixXd y(2,2);
	MatrixXd z(2,1);

	x(0,0) = c1; x(1,0) = c2;
	y(0,0) = cos(angle); y(0, 1) = -1.0 * sin(angle);
	y(1,0) = sin(angle); y(1, 1) = cos(angle);
	z(0,0) = xold - c1; z(1,0) = yold - c2;

	MatrixXd a = x + (y*z);

	Point new_point = Point(a(0,0), a(1,0));
	return new_point;
}

void Line::rotate(double angle)
{//rotate start point about midpoint

	Point about_point = get_midpoint();

	start = _rotate_coord(start, angle, about_point);
	end = _rotate_coord(end, angle, about_point);

	compute();
}

void Line::rotate(double angle, Point about_point)
{//rotate start point about midpoint

	start = _rotate_coord(start, angle, about_point);
	end = _rotate_coord(end, angle, about_point);

	compute();
}

double Line::get_length()
{
	return measure(start, end);
}

double Line::get_gradient()
{
	return tan(get_angle());
}

double Line::get_angle()
{
	double dx = end.x - start.x;
	double dy = end.y - start.y;
	double angle = atan2(dy, dx);
	return angle;
}

Point Line::get_midpoint()
{
	double x = (start.x + end.x)/2.0;
	double y = (start.y + end.y)/2.0;
	Point midpoint = Point(x, y);
	return midpoint;
}

void Line::plot(string title)
{
	//pass
}

void Line::plot()
{
	plot("Line-01");
}

bool Line::is_on_line(Point point)
{
	// This works based on the principle
	// A--C-----B; where AC,CB,AB are a lines
	// and AC + CB == AB

	double ac = measure(start, point);
	double cb = measure(point, end);
	double ab = measure(start, end);

	double diff = (ac + cb) - ab;
	return abs(diff) <= 0.001;
}

Point Line::get_intersecting_point(Line other)
{
	// line 1
	double x1 = start.x; double x2 = end.x;
	double y1 = start.y; double y2 = end.y;

	// line 2
	double x3 = other.start.x; double x4 = other.end.x;
	double y3 = other.start.y; double y4 = other.end.y;

	MatrixXd a(2,2);
	MatrixXd b(2,2);
	MatrixXd c(2,2);
	MatrixXd d(2,2);
	MatrixXd e(2,2);
	MatrixXd f(2,2);

	MatrixXd A(2,2);
	MatrixXd B(2,2);
	MatrixXd C(2,2);

	a(0,0) = x1;a(0, 1) = y1; a(1,0) = x2;a(1, 1) = y2;

	b(0,0) = x1;b(0, 1) = 1;  b(1,0) = x2;b(1, 1) = 1;

	c(0,0) = x3;c(0, 1) = y3; c(1,0) = x4;c(1, 1) = y4;

	d(0,0) = x3;d(0, 1) = 1;  d(1,0) = x4;d(1, 1) = 1;

	e(0,0) = y1;e(0, 1) = 1;  e(1,0) = y2;e(1, 1) = 1;

	f(0,0) = y3;f(0, 1) = 1;  f(1,0) = y4;f(1, 1) = 1;

	A(0,0) = a.determinant(); A(0,1) = b.determinant();
	A(1,0) = c.determinant(); A(1,1) = d.determinant();

	B(0,0) = b.determinant(); B(0,1) = e.determinant();
	B(1,0) = d.determinant(); B(1,1) = f.determinant();

	C(0,0) = a.determinant(); C(0,1) = e.determinant();
	C(1,0) = c.determinant(); C(1,1) = f.determinant();

	double x = A.determinant() / B.determinant();
	double y = C.determinant() / B.determinant();

	Point point = Point(x, y);
	if (!(is_on_line(point) && other.is_on_line(point)))
	{
		Point new_point = Point(std::numeric_limits<double>::infinity(), std::numeric_limits<double>::infinity());
		return new_point;
	}

	return point;
}

void Line::draw(cv::Mat image, cv::Scalar color)
{
	draw(image, color, 1, 8, 0);
}

void Line::draw(cv::Mat image, cv::Scalar color, int stroke_width, int line_type, int shift)
{
	cv::Point start_point = cv::Point(start.x, start.y);
	cv::Point end_point   = cv::Point(end.x, end.y);

	cv::line(image, start_point, end_point, color, stroke_width, line_type, shift);
}


Path::Path(std::vector<Point> raw_point_data, bool is_closed)
{
	data_points = raw_point_data;
	closed = is_closed;

	calculate();
}

Point Path::get_start_point()
{
	return data_points.at(0);
}

Point Path::get_end_point()
{
	return data_points.at(data_points.size()-1);
}

RectInfo Path::get_rect_info()
{
	return rect_info;
}

std::vector<Line> Path::get_boundary_lines()
{
	return boundary_lines;
}

std::vector<Point> Path::get_intersecting_points(Line line)
{
	std::vector<Point> intersecting_points;

	for (int i=0; i<boundary_lines.size(); i++)
	{
		Line current_line = boundary_lines.at(i);
		Point intersecting_point = line.get_intersecting_point(current_line);

		if (!(std::isinf(intersecting_point.x) || std::isinf(intersecting_point.y)))
		{
			intersecting_points.push_back(intersecting_point);
		}
	}

	return intersecting_points;
}

std::vector<Line> Path::get_shading_lines(double spacing, double angle, double padding)
{
	std::vector<Line> lines;

	double min_x = rect_info.top_left.x - padding;
	double min_y = rect_info.top_left.y - padding;

	double max_x = rect_info.bottom_right.x + padding;
	double max_y = rect_info.bottom_right.y + padding;

	double cx = (max_x - min_x)/2.0 + min_x;
	double cy = (max_y - min_y)/2.0 + min_y;

	Point about_point = Point(cx, cy);

	// create lines
	for (double y=min_y; y<=max_y; y+=spacing)
	{
		Point start = Point(min_x, y);
		Point end   = Point(max_x, y);
		Line line   = Line(start, end);

		line.rotate(angle, about_point);
		lines.push_back(line);
	}

	return lines;
}

std::vector<Line> Path::get_intersecting_lines(double spacing, double angle)
{
	double padding = std::max(rect_info.width, rect_info.height);
	std::vector<Line> lines = get_shading_lines(spacing, angle, padding);


	std::vector<Line> intersecting_lines;
	for (int i=0; i<lines.size(); i++)
	{
		Line line = lines.at(i);
		std::vector<Point> intersecting_points = get_intersecting_points(line);

		std::sort(intersecting_points.begin(), intersecting_points.end(), _filter_x_function);

		for (int j=0; j<intersecting_points.size(); j+=2)
		{
			Point start = intersecting_points.at(j);
			Point end   = intersecting_points.at(j+1);

			Line line = Line(start, end);
			intersecting_lines.push_back(line);
		}
	}

	return intersecting_lines;
}

void Path::calculate()
{
	if (!closed)
	{
		Point point = data_points.at(0);
		data_points.push_back(point);
	}

	for (int i=0; i<data_points.size(); i++)
	{
		Point point = data_points.at(i);
		xs.push_back(point.x);
		ys.push_back(point.y);
	}

	boundary_lines.clear();
	for (int i=0; i<data_points.size()-1; i++)
	{
		Point start = data_points.at(i);
		Point end   = data_points.at(i+1);

		Line line = Line(start, end);
		boundary_lines.push_back(line);
	}

	rect_info.top_left     = Point(minimum_element(xs), minimum_element(ys));
	rect_info.width        = maximum_element(xs) - rect_info.top_left.x;
	rect_info.height       = maximum_element(ys) - rect_info.top_left.y;
	rect_info.bottom_right = Point(rect_info.top_left.x + rect_info.width, rect_info.top_left.y + rect_info.height);
	rect_info.area         = rect_info.width * rect_info.height;
	rect_info.radius       = std::sqrt(std::pow(rect_info.width, 2) + std::pow(rect_info.height, 2)) / 2.0;
	rect_info.center       = Point(rect_info.top_left.x + (rect_info.width/2.0), rect_info.top_left.y + (rect_info.height/2.0));
}

void Path::rotate(double angle)
{
	Point pivot = rect_info.center;
	rotate(angle, pivot);
}

void Path::rotate(double angle, Point pivot)
{
	data_points.clear();
	closed = false;

	for (int i=0; i<boundary_lines.size(); i++)
	{
		Line line = boundary_lines.at(i);
		line.rotate(angle, pivot);
		data_points.push_back(line.start);
	}

	calculate();
}

void Path::draw(cv::Mat image, cv::Scalar color)
{
	draw(image, color, 1, 8, 0);
}

void Path::draw(cv::Mat image, cv::Scalar color, int stroke_width, int line_type, int shift)
{
	for (int i=0; i<boundary_lines.size(); i++)
	{
		Line line = boundary_lines.at(i);
		line.draw(image, color, stroke_width, line_type, shift);
	}
}

}

#endif /*BLINK_PI_OBJECTS_H*/