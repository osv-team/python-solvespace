# coding: utf-8

# Some sample code for slvs.dll. We draw some geometric entities, provide
# initial guesses for their positions, and then constrain them. The solver
# calculates their new positions, in order to satisfy the constraints.
#
# Copyright 2008-2013 Jonathan Westhues.
# Copyright 2016-2017 Yuan Chang [pyslvs@gmail.com] Python-Solvespace bundled.

from slvs import System, Point3d, LineSegment3d, Constraint, SLVS_RESULT_OKAY, \
    groupNum, Slvs_MakeQuaternion, Normal3d, Workplane, Point2d, \
    LineSegment2d, ArcOfCircle, Distance, Circle, SLVS_RESULT_INCONSISTENT

sys = System()


def example_3d():
    r"""An example of a constraint in 3d. We create a single group, with some
    entities and constraints."""
    # A point, initially at (x y z) = (10 10 10)
    p0 = sys.add_param(10)
    p1 = sys.add_param(10)
    p2 = sys.add_param(10)
    point101 = Point3d(p0, p1, p2)

    # and a second point at (20 20 20)
    p3 = sys.add_param(20)
    p4 = sys.add_param(20)
    p5 = sys.add_param(20)
    point102 = Point3d(p3, p4, p5)

    # and a line segment connecting them.
    LineSegment3d(point101, point102)

    # The distance between the points should be 30.0 units.
    Constraint.distance(30., point101, point102)

    # Let's tell the solver to keep the second point as close to constant
    # as possible, instead moving the first point.
    Constraint.dragged(point102)

    # Now that we have written our system, we solve.
    result = sys.solve()
    if result == SLVS_RESULT_OKAY:
        print(
            "okay; now at ({:.3f} {:.3f} {:.3f})\n".format(sys.get_param(0).val,
                                                           sys.get_param(1).val,
                                                           sys.get_param(2).val)+
            "             ({:.3f} {:.3f} {:.3f})\n".format(sys.get_param(3).val,
                                                           sys.get_param(4).val,
                                                           sys.get_param(5).val)
        )
        print("{} DOF".format(sys.dof))
    else:
        print("solve failed")


def example_2d():
    r"""An example of a constraint in 2d. In our first group, we create a
    workplane along the reference frame's xy plane.
    In a second group, we create some entities in that group
    and dimension them."""
    g1 = groupNum(1)
    sys.default_group = g1

    # First, we create our workplane. Its origin corresponds to the origin
    # of our base frame (x y z) = (0 0 0)
    p0 = sys.add_param(0)
    p1 = sys.add_param(0)
    p2 = sys.add_param(0)
    point101 = Point3d(p0, p1, p2)

    # and it is parallel to the xy plane, so it has basis vectors (1 0 0)
    # and (0 1 0).
    qw, qx, qy, qz = Slvs_MakeQuaternion(*[1, 0, 0], *[0, 1, 0])
    p3 = sys.add_param(qw)
    p4 = sys.add_param(qx)
    p5 = sys.add_param(qy)
    p6 = sys.add_param(qz)
    normal102 = Normal3d(p3, p4, p5, p6)

    workplane200 = Workplane(point101, normal102)

    # Now create a second group. We'll solve group 2, while leaving group 1
    # constant; so the workplane that we've created will be locked down,
    # and the solver can't move it.
    g2 = groupNum(2)
    sys.default_group = g2

    # These points are represented by their coordinates (u v) within the
    # workplane, so they need only two parameters each.
    p7 = sys.add_param(10)
    p8 = sys.add_param(20)
    point301 = Point2d(workplane200, p7, p8)

    p9 = sys.add_param(20)
    p10 = sys.add_param(10)
    point302 = Point2d(workplane200, p9, p10)

    # And we create a line segment with those endpoints.
    line400 = LineSegment2d(workplane200, point301, point302)

    # Now three more points.
    p11 = sys.add_param(100)
    p12 = sys.add_param(120)
    point303 = Point2d(workplane200, p11, p12)

    p13 = sys.add_param(120)
    p14 = sys.add_param(110)
    point304 = Point2d(workplane200, p13, p14)

    p15 = sys.add_param(115)
    p16 = sys.add_param(115)
    point305 = Point2d(workplane200, p15, p16)

    # And arc, centered at point 303, starting at point 304, ending at
    # point 305.
    arc401 = ArcOfCircle(workplane200, normal102, point303, point304, point305)

    # Now one more point, and a distance
    p17 = sys.add_param(200)
    p18 = sys.add_param(200)
    point306 = Point2d(workplane200, p17, p18)

    p19 = sys.add_param(30)
    distance307 = Distance(workplane200, p19)

    # And a complete circle, centered at point 306 with radius equal to
    # distance 307. The normal is 102, the same as our workplane.
    circle402 = Circle(workplane200, normal102, point306, distance307)

    # The length of our line segment is 30.0 units.
    Constraint.distance(30., workplane200, point301, point302)

    # And the distance from our line segment to the origin is 10.0 units.
    Constraint.distance(10., workplane200, point101, line400)

    # And the line segment is vertical.
    Constraint.vertical(workplane200, line400)

    # And the distance from one endpoint to the origin is 15.0 units.
    Constraint.distance(15., workplane200, point301, point101)

    if 0:
        # And same for the other endpoint; so if you add this constraint then
        # the sketch is overconstrained and will signal an error.
        Constraint.distance(18., workplane200, point301, point101)

    # The arc and the circle have equal radius.
    Constraint.equal_radius(workplane200, arc401, circle402)

    # The arc has radius 17.0 units.
    Constraint.diameter(17.*2, workplane200, arc401)

    # If the solver fails, then ask it to report which constraints caused
    # the problem.
    sys.calculateFaileds = 1

    # And solve.
    result = sys.solve()
    if result == SLVS_RESULT_OKAY:
        print("solved okay")
        # Python-Solvespace can use wrapper of pointer to get the values,
        # or record the entry number first, then using the 'get_param' method.
        print("line from ({:.3f} {:.3f}) to ({:.3f} {:.3f})".format(
            point301.u().value, point301.v().value,  # (sys.get_param(7).val, sys.get_param(8).val) is okay.
            point302.u().value, point302.v().value
        ))
        print("arc center ({:.3f} {:.3f}) start ({:.3f} {:.3f}) finish ({:.3f} {:.3f})".format(
            point303.u().value, point303.v().value,  # (sys.get_param(11).val, sys.get_param(12).val) is okay.
            point304.u().value, point304.v().value,
            point305.u().value, point305.v().value
        ))
        print("circle center ({:.3f} {:.3f}) radius {:.3f}".format(
            point306.u().value, point306.v().value,
            distance307.distance().value
        ))
        print("{} DOF".format(sys.dof))
    else:
        print("solve failed: problematic constraints are:")
        for e in sys.faileds:
            print(e)
        if result == SLVS_RESULT_INCONSISTENT:
            print("system inconsistent")
        else:
            print("system nonconvergent")

if __name__ == '__main__':
    example_3d()
    example_2d()
