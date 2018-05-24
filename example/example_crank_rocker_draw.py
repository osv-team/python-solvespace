# # coding: utf-8
#
# # 一三角形呆鍊，由一長一短的連桿固定在水平基線上。
# # 短連桿鎖固在原點上，長連桿鎖固在距原點90mm處。
# # 短連桿長度35mm；長連桿長度70mm。
# # 三角形呆鍊邊長分別為40mm、40mm、70mm
#
# # A chain of triangles, fixed by a long and short connecting rod on
# # the horizontal baseline.
# # The short link is locked at the origin, and the long link is locked
# # at 90mm from the origin.
# # Short link length 35mm; long link length 70mm.
# # The length of the triangle is 40mm, 40mm, and 70mm.
#
# from slvs import *
# from math import *
# import matplotlib.pyplot as plt
#
# # 相關參數
# # Related parameters
# d0 = 90  # Baseline length (mm)
# n1 = 35  # Short link length (mm)
# n2 = 70  # Length of long link (mm)
# t1 = 40  # Triangle first side (mm)
# t2 = 40  # Triangle second side (mm)
# t3 = 70  # Triangle third side (mm)
#
#
# # 開始繪圖
# # Start drawing
#
#
# def crank_rock(degree):
#     sys = System(500)
#     g = 1
#     # 原點Point0
#     # Origin Point0
#     p0 = sys.add_param(0.0)
#     p1 = sys.add_param(0.0)
#     p2 = sys.add_param(0.0)
#     point0 = Point3d(p0, p1, p2)
#
#     # XY法線
#     # XY normal
#     qw, qx, qy, qz = Slvs_MakeQuaternion(1, 0, 0, 0, 1, 0)
#     p3 = sys.add_param(qw)
#     p4 = sys.add_param(qx)
#     p5 = sys.add_param(qy)
#     p6 = sys.add_param(qz)
#     normal1 = Normal3d(p3, p4, p5, p6)
#
#     # 工作平面
#     # Working plane
#     workplane1 = Workplane(point0, normal1)
#
#     # 3D版的Point0=>Point1
#     # 3D version of Point0=>Point1
#     p7 = sys.add_param(0.0)
#     p8 = sys.add_param(0.0)
#     point1 = Point2d(workplane1, p7, p8)
#     Constraint.dragged(workplane1, point1)
#
#     # 長連桿轉軸Point2，還有基線Line0。
#     # Long link shaft Point2, and baseline Line0.
#     p9 = sys.add_param(d0)
#     p10 = sys.add_param(0.0)
#     point2 = Point2d(workplane1, p9, p10)
#     Constraint.dragged(workplane1, point2)
#     line0 = LineSegment2d(workplane1, point1, point2)
#
#     # Angle約束判斷
#     # Angle constraint judgment
#     if degree >= 180:
#         other = -1
#     else:
#         other = 1
#
#     # 三角形Point3 / Point4 / Point5
#     # Triangle Point3 / Point4 / Point5
#     p11 = sys.add_param(20.0)
#     p12 = sys.add_param(20.0)
#     point3 = Point2d(workplane1, p11, p12)
#     p13 = sys.add_param(0.0)
#     p14 = sys.add_param(10.0*other)
#     point4 = Point2d(workplane1, p13, p14)
#     p15 = sys.add_param(30.0)
#     p16 = sys.add_param(20.0)
#     point5 = Point2d(workplane1, p15, p16)
#     Constraint.distance(t1, workplane1, point4, point3)
#     Constraint.distance(t2, workplane1, point3, point5)
#     Constraint.distance(t3, workplane1, point4, point5)
#
#     # 連桿約束
#     # Link constraints
#     Constraint.distance(n1, workplane1, point1, point4)
#     Constraint.distance(n2, workplane1, point2, point5)
#     line1 = LineSegment2d(workplane1, point1, point4)
#
#     # 短連桿與水平軸的角度
#     # The angle between the short link and the horizontal axis
#     Constraint.angle(workplane1, degree, line1, line0)
#
#     # 以下解題
#     # The following problem solving
#
#     sys.solve()
#
#     if sys.result == SLVS_RESULT_OKAY:
#         x = sys.get_param(11).val
#         y = sys.get_param(12).val
#         return x, y
#     elif sys.result == SLVS_RESULT_INCONSISTENT:
#         print("solve failed")
#         print("SLVS_RESULT_INCONSISTENT")
#         print("%d DOF" % sys.dof)
#     elif sys.result == SLVS_RESULT_DIDNT_CONVERGE:
#         print("solve failed")
#         print("SLVS_RESULT_DIDNT_CONVERGE")
#         print("%d DOF" % sys.dof)
#     elif sys.result == SLVS_RESULT_TOO_MANY_UNKNOWNS:
#         print("solve failed")
#         print("SLVS_RESULT_TOO_MANY_UNKNOWNS")
#         print("%d DOF" % sys.dof)
#
# # 主程式
# # Main program
# Xval = []
# Yval = []
#
# for i in range(0, 360, 10):
#     x, y = crank_rock(i)
#     Xval += [x]
#     Yval += [y]
# print("Solve Completed")
#
# plt.plot(Xval, Yval)
# plt.ylabel('some numbers')
# plt.show()


# coding: utf-8

# 一三角形呆鍊，由一長一短的連桿固定在水平基線上。
# 短連桿鎖固在原點上，長連桿鎖固在距原點90mm處。
# 短連桿長度35mm；長連桿長度70mm。
# 三角形呆鍊邊長分別為40mm、40mm、70mm

# A chain of triangles, fixed by a long and short connecting rod on
# the horizontal baseline.
# The short link is locked at the origin, and the long link is locked
# at 90mm from the origin.
# Short link length 35mm; long link length 70mm.
# The length of the triangle is 40mm, 40mm, and 70mm.

from slvs import System, Point3d, Slvs_MakeQuaternion, Normal3d, Workplane, \
    Point2d, Constraint, LineSegment2d, SLVS_RESULT_OKAY, \
    SLVS_RESULT_INCONSISTENT, SLVS_RESULT_DIDNT_CONVERGE, \
    SLVS_RESULT_TOO_MANY_UNKNOWNS

import matplotlib.pyplot as plt

# 相關參數
# Related parameters
d0 = 90  # Baseline length (mm)
n1 = 35  # Short link length (mm)
n2 = 70  # Length of long link (mm)
t1 = 40  # Triangle first side (mm)
t2 = 40  # Triangle second side (mm)
t3 = 70  # Triangle third side (mm)

# 開始繪圖
# Start drawing


def crank_rock(degree):
    sys = System(500)
    g = 1
    # 原點Point0
    # Origin Point0
    p0 = sys.add_param(0.0)
    p1 = sys.add_param(0.0)
    p2 = sys.add_param(0.0)
    point0 = Point3d(p0, p1, p2)

    # XY法線
    # XY normal
    qw, qx, qy, qz = Slvs_MakeQuaternion(1, 0, 0, 0, 1, 0)
    p3 = sys.add_param(qw)
    p4 = sys.add_param(qx)
    p5 = sys.add_param(qy)
    p6 = sys.add_param(qz)
    normal1 = Normal3d(p3, p4, p5, p6)

    # 工作平面
    # Working plane
    workplane1 = Workplane(point0, normal1)

    # 3D版的Point0=>Point1
    # 3D version of Point0=>Point1
    p7 = sys.add_param(0.0)
    p8 = sys.add_param(0.0)
    point1 = Point2d(workplane1, p7, p8)
    Constraint.dragged(workplane1, point1)

    # 長連桿轉軸Point2，還有基線Line0。
    # Long link shaft Point2, and baseline Line0.
    p9 = sys.add_param(d0)
    p10 = sys.add_param(0.0)
    point2 = Point2d(workplane1, p9, p10)
    Constraint.dragged(workplane1, point2)
    line0 = LineSegment2d(workplane1, point1, point2)

    # Angle約束判斷
    # Angle constraint judgment
    if degree >= 180:
        other = -1
    else:
        other = 1

    # 三角形Point3 / Point4 / Point5
    # Triangle Point3 / Point4 / Point5
    p11 = sys.add_param(20.0)
    p12 = sys.add_param(20.0)
    point3 = Point2d(workplane1, p11, p12)
    p13 = sys.add_param(0.0)
    p14 = sys.add_param(10.0*other)
    point4 = Point2d(workplane1, p13, p14)
    p15 = sys.add_param(30.0)
    p16 = sys.add_param(20.0)
    point5 = Point2d(workplane1, p15, p16)
    Constraint.distance(t1, workplane1, point4, point3)
    Constraint.distance(t2, workplane1, point3, point5)
    Constraint.distance(t3, workplane1, point4, point5)

    # 連桿約束
    # Link constraints
    Constraint.distance(n1, workplane1, point1, point4)
    Constraint.distance(n2, workplane1, point2, point5)
    line1 = LineSegment2d(workplane1, point1, point4)

    # 短連桿與水平軸的角度
    # The angle between the short link and the horizontal axis
    Constraint.angle(workplane1, degree, line1, line0)

    # 以下解題
    # The following problem solving

    result = sys.solve()

    if result == SLVS_RESULT_OKAY:
        print("Point coordinates：")
        print("P3(%.3f %.3f %.3f)" % (sys.get_param(11).val,
                                      sys.get_param(12).val,
                                      sys.get_param(2).val))
        print("P4(%.3f %.3f %.3f)" % (sys.get_param(13).val,
                                      sys.get_param(14).val,
                                      sys.get_param(2).val))
        print("%d DOF" % sys.dof)
        x = sys.get_param(11).val
        y = sys.get_param(12).val
        return x, y
    elif result == SLVS_RESULT_INCONSISTENT:
        print("solve failed")
        print("SLVS_RESULT_INCONSISTENT")
        print("%d DOF" % sys.dof)
    elif result == SLVS_RESULT_DIDNT_CONVERGE:
        print("solve failed")
        print("SLVS_RESULT_DIDNT_CONVERGE")
        print("%d DOF" % sys.dof)
    elif result == SLVS_RESULT_TOO_MANY_UNKNOWNS:
        print("solve failed")
        print("SLVS_RESULT_TOO_MANY_UNKNOWNS")
        print("%d DOF" % sys.dof)

# 主程式
# Main program
Xval = []
Yval = []

for i in range(0, 361, 5):
    print("Degree: {:03} deg".format(i))
    # x, y = crank_rock(i)
    t = crank_rock(i)
    if t is not None:
        x, y = t
        Xval += [x]
        Yval += [y]
    else:
        # TODO : Happens at 0,180 and 360 deg - why?
        msg = "crank_rock(%i) returned None" % i
        print(msg)
        # raise AssertionError("crank_rock(%i) returned None" % i)
print("Solve Completed")

plt.plot(Xval, Yval)
plt.ylabel('some numbers')
plt.show()
print("Solve Completed")
