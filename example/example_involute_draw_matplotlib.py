# coding: utf-8

# 漸開線解題
# 由端點Point3畫出圖形

# Involute problem solving
# Draw a graph from endpoint Point3

from slvs import System, Point3d, Slvs_MakeQuaternion, Normal3d, Workplane, \
    Point2d, Constraint, LineSegment2d, SLVS_RESULT_OKAY, \
    SLVS_RESULT_INCONSISTENT, SLVS_RESULT_DIDNT_CONVERGE, \
    SLVS_RESULT_TOO_MANY_UNKNOWNS
import matplotlib.pyplot as plt
from math import pi

# 參數
# parameter
r = 10.0  # Base circle radius


def involute(degree):
    # 角度換算：degree去除重複圈數
    # Angle conversion: degree to remove the number of repeats
    d = r*(degree*pi/180)
    n = degree//360
    degree -= 360*n

    # 開始繪圖
    # Start drawing
    sys = System(500)
    g = 1

    # 3D原點Point0
    # 3D origin Point0
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

    # 2D原點Point1
    # 2D Origin Point1
    p7 = sys.add_param(0.0)
    p8 = sys.add_param(0.0)
    point1 = Point2d(workplane1, p7, p8)
    Constraint.dragged(workplane1, point1)

    # Angle約束判斷
    # Angle constraint judgment
    if degree >= 180:
        other = -1
    else:
        other = 1

    # Point2繞行圓周，距離r
    # Point2 circle around, distance r
    p9 = sys.add_param(0.0)
    p10 = sys.add_param(10.0*other)
    point2 = Point2d(workplane1, p9, p10)
    Constraint.distance(r, workplane1, point1, point2)
    line1 = LineSegment2d(workplane1, point1, point2)

    # Point3距離Point2為目前圓周長
    # Point3 is the current circumference distance from Point2
    # 並且連線d會垂直半徑連線r
    # And the connection d will have a vertical radius connection r
    p11 = sys.add_param(10.0*other)
    p12 = sys.add_param(10.0*other)
    point3 = Point2d(workplane1, p11, p12)
    if d == 0:
        Constraint.on(workplane1, point2, point3)
    else:
        line2 = LineSegment2d(workplane1, point2, point3)
        Constraint.distance(d, workplane1, point2, point3)
        Constraint.perpendicular(workplane1, line1, line2, False)

    # 輔助基線Line0
    # Auxiliary baseline Line0
    p13 = sys.add_param(10.0)
    p14 = sys.add_param(0.0)
    point4 = Point2d(workplane1, p13, p14)
    Constraint.dragged(workplane1, point4)
    line0 = LineSegment2d(workplane1, point1, point4)

    # 約束角度
    # Constraint angle
    Constraint.angle(workplane1, degree, line1, line0, False)

    # 以下解題
    # The following problem solving
    sys.solve()

    if sys.result == SLVS_RESULT_OKAY:
        # 回傳Point7
        # Return to Point7
        x = sys.get_param(11).val
        y = sys.get_param(12).val
        return x, y
    elif sys.result == SLVS_RESULT_INCONSISTENT:
        print("solve failed")
        print("SLVS_RESULT_INCONSISTENT")
        print("%d DOF" % sys.dof)
    elif sys.result == SLVS_RESULT_DIDNT_CONVERGE:
        print("solve failed")
        print("SLVS_RESULT_DIDNT_CONVERGE")
        print("%d DOF" % sys.dof)
    elif sys.result == SLVS_RESULT_TOO_MANY_UNKNOWNS:
        print("solve failed")
        print("SLVS_RESULT_TOO_MANY_UNKNOWNS")
        print("%d DOF" % sys.dof)

# 主程式
# Main program
Xval = []
Yval = []
degree = 720
for i in range(0, degree+1, 1):
    t = involute(i)
    if t is not None:
        x, y = t
        Xval += [x]
        Yval += [y]
    else:
        # TODO : Happens at 0, 180, 360, 540 and 720 deg - why?
        msg = "involute(%i) returned None" % i
        print(msg)
        # raise AssertionError("involute(%i) returned None" % i)
print("Solve Completed")

plt.plot(Xval, Yval)
plt.xlabel('x coordinate')
plt.ylabel('y coordinate')
plt.title("Involute - "+str(degree)+" deg")
plt.show()
