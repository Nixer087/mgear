# MGEAR is under the terms of the MIT License

# Copyright (c) 2016 Jeremie Passerin, Miquel Campos

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author:     Jeremie Passerin      geerem@hotmail.com  www.jeremiepasserin.com
# Author:     Miquel Campos         hello@miquel-campos.com  www.miquel-campos.com
<<<<<<< HEAD
# Date:       2016 / 10 / 10
=======
# Date:       2016 / 11 / 18
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4

# ms 2jnt feature -----------------------
# //done//FK isolation
# //done//FK roll ctl
# //done//Independent IK-FK hand ctl
# //done//IK auto up vector(default off)
# //done//T pose centric FK ctl
<<<<<<< HEAD

# To Do List -------------------------------
# elbow thickness + seperate upper/lower limb roundness ctl
=======
# //done//elbow thickness + seperate upper/lower limb roundness ctl
# To Do List -------------------------------

>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
# elbow scl and hand scl(ik/fk) add to jt scl
# addition limb jt layer ctl(optional)
# upper sleeve lower sleeve ctl(optional)
# custom Upper limb 4 pt bezier node with input for rot interpolation


#############################################
# GLOBAL
#############################################
# Maya
import pymel.core as pm
import pymel.core.datatypes as dt


# mgear
from mgear.maya.shifter.component import MainComponent

import mgear.maya.primitive as pri
import mgear.maya.transform as tra
import mgear.maya.attribute as att
import mgear.maya.node as nod
import mgear.maya.vector as vec
import mgear.maya.applyop as aop
import mgear.maya.fcurve as fcu

#############################################
# COMPONENT
#############################################
class Component(MainComponent):

    def addObjects(self):


        self.normal = self.getNormalFromPos(self.guide.apos)
        self.binormal = self.getBiNormalFromPos(self.guide.apos)

        self.length0 = vec.getDistance(self.guide.apos[0], self.guide.apos[1])
        self.length1 = vec.getDistance(self.guide.apos[1], self.guide.apos[2])
        self.length2 = vec.getDistance(self.guide.apos[2], self.guide.apos[3])

        # FK Controlers -----------------------------------
        # *ms* set npo @ Tpose, to make the fk rotation work best with rot order"yzx"

        self.fk_cns = pri.addTransformFromPos(self.root, self.getName("fk_cns"), self.guide.apos[0])

        tpv = self.guide.apos[0] + ((self.guide.apos[1] - self.guide.apos[0])*[1,0,0])        
        t = tra.getTransformLookingAt(self.guide.apos[0], tpv, self.normal, "xz", self.negate)
        # *ms* add FK isolation
        self.fk0_npo = pri.addTransform(self.fk_cns, self.getName("fk0_npo"), t)
        
        t = tra.getTransformLookingAt(self.guide.apos[0], self.guide.apos[1], self.normal, "xz", self.negate)
<<<<<<< HEAD
        self.fk0_ctl = self.addCtl(self.fk0_npo, "fk0_ctl", t, self.color_fk, "cube", w=self.length0*.55, h=self.size*.1, d=self.size*.1, po=dt.Vector(.35*self.length0*self.n_factor,0,0))
        att.setKeyableAttributes(self.fk0_ctl)
        # *ms* add fk roll control Simage style
        self.fk0_roll_ctl = self.addCtl(self.fk0_ctl, "fk0_roll_ctl", t, self.color_fk, "cube", w=self.length0*.45, h=self.size*.1, d=self.size*.1, po=dt.Vector(.85*self.length0*self.n_factor,0,0))
=======
        self.fk0_ctl = self.addCtl(self.fk0_npo, "fk0_ctl", t, self.color_fk, "cube", w=self.length0*.55, h=self.size*.1, d=self.size*.1, po=dt.Vector(.275*self.length0*self.n_factor,0,0))
        att.setKeyableAttributes(self.fk0_ctl)
        # *ms* add fk roll control Simage style
        self.fk0_roll_ctl = self.addCtl(self.fk0_ctl, "fk0_roll_ctl", t, self.color_fk, "cube", w=self.length0*.45, h=self.size*.1, d=self.size*.1, po=dt.Vector(.775*self.length0*self.n_factor,0,0))
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        att.setKeyableAttributes(self.fk0_roll_ctl)

        t = tra.getTransformLookingAt(self.guide.apos[1], self.guide.apos[2], self.normal, "xz", self.negate)
        self.fk1_npo = pri.addTransform(self.fk0_roll_ctl, self.getName("fk1_npo"), t)
        self.fk1_ctl = self.addCtl(self.fk1_npo, "fk1_ctl", t, self.color_fk, "cube", w=self.length1, h=self.size*.1, d=self.size*.1, po=dt.Vector(.5*self.length1*self.n_factor,0,0))
        att.setKeyableAttributes(self.fk1_ctl)

        t = tra.getTransformLookingAt(self.guide.apos[2], self.guide.apos[3], self.normal, "xz", self.negate)
        # *ms* buffer object to feed into ikfk solver for hand seperation
        self.fk2_mtx = pri.addTransform(self.fk1_ctl, self.getName("fk2_mtx"), t)
       

<<<<<<< HEAD
       # fk2_npo is need to take the effector position
=======
       # fk2_npo is need to take the effector position + bone1 rotation
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        self.fk2_npo = pri.addTransform(self.fk1_ctl, self.getName("fk2_npo"), t) 
        self.fk2_ctl = self.addCtl(self.fk2_npo, "fk2_ctl", t, self.color_fk, "cube", w=self.length2, h=self.size*.1, d=self.size*.1, po=dt.Vector(.5*self.length2*self.n_factor,0,0))
        att.setKeyableAttributes(self.fk2_ctl)

        self.fk_ctl = [self.fk0_roll_ctl, self.fk1_ctl, self.fk2_ctl]

        for  x in self.fk_ctl:
            att.setInvertMirror(x, ["tx", "ty", "tz"])

        


        # IK Controlers -----------------------------------

        self.ik_cns = pri.addTransformFromPos(self.root, self.getName("ik_cns"), self.guide.pos["wrist"])

        self.ikcns_ctl = self.addCtl(self.ik_cns, "ikcns_ctl", tra.getTransformFromPos(self.guide.pos["wrist"]), self.color_ik, "null", w=self.size*.12)
        att.setInvertMirror(self.ikcns_ctl, ["tx", "ty", "tz"])

        if self.negate:
            m = tra.getTransformLookingAt(self.guide.pos["wrist"], self.guide.pos["eff"], self.normal, "x-y", True)
        else:
            m = tra.getTransformLookingAt(self.guide.pos["wrist"], self.guide.pos["eff"], self.normal, "xy", False)
        self.ik_ctl = self.addCtl(self.ikcns_ctl, "ik_ctl", m, self.color_ik, "cube", w=self.size*.12, h=self.size*.12, d=self.size*.12)
        att.setKeyableAttributes(self.ik_ctl)
        att.setInvertMirror(self.ik_ctl, ["tx", "ry", "rz"])

        # upv
        v = self.guide.apos[2] - self.guide.apos[0]
        v = self.normal ^ v
        v.normalize()
        v *= self.size*.5
        v += self.guide.apos[1]
        # *ms* auto up vector ------------------------------
        self.upv_cns = pri.addTransformFromPos(self.root, self.getName("upv_cns"), self.guide.apos[0])
<<<<<<< HEAD
        self.upv_auv = pri.addTransformFromPos(self.upv_cns, self.getName("upv_auv"), self.guide.apos[0])
=======
        self.upv_auv = pri.addTransformFromPos(self.root, self.getName("upv_auv"), self.guide.apos[0])
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        self.upv_mtx = pri.addTransformFromPos(self.upv_cns, self.getName("upv_mtx"), self.guide.apos[0])

        self.upv_npo = pri.addTransformFromPos(self.upv_mtx, self.getName("upv_npo"), v)
        self.upv_ctl = self.addCtl(self.upv_npo, "upv_ctl", tra.getTransform(self.upv_npo), self.color_ik, "diamond", w=self.size*.12)
        att.setKeyableAttributes(self.upv_ctl, self.t_params)
        att.setInvertMirror(self.upv_ctl, ["tx"])

        # References --------------------------------------
        # Calculate  again the transfor for the IK ref. This way align with FK
        trnIK_ref = tra.getTransformLookingAt(self.guide.pos["wrist"], self.guide.pos["eff"], self.normal, "xz", self.negate)
        self.ik_ref = pri.addTransform(self.ik_ctl, self.getName("ik_ref"), trnIK_ref)
        self.fk_ref = pri.addTransform(self.fk_ctl[2], self.getName("fk_ref"), trnIK_ref)

        # Chain --------------------------------------------
<<<<<<< HEAD
        # The outputs of the ikfk2bone solver
=======
        # take outputs of the ikfk2bone solver
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        self.bone0 = pri.addLocator(self.root, self.getName("0_bone"), tra.getTransform(self.fk_ctl[0]))
        self.bone0_shp = self.bone0.getShape()
        self.bone0_shp.setAttr("localPositionX", self.n_factor*.5)
        self.bone0_shp.setAttr("localScale", .5, 0, 0)
        self.bone0.setAttr("sx", self.length0)
        self.bone0.setAttr("visibility", False)

        self.bone1 = pri.addLocator(self.root, self.getName("1_bone"), tra.getTransform(self.fk_ctl[1]))
        self.bone1_shp = self.bone1.getShape()
        self.bone1_shp.setAttr("localPositionX", self.n_factor*.5)
        self.bone1_shp.setAttr("localScale", .5, 0, 0)
        self.bone1.setAttr("sx", self.length1)
        self.bone1.setAttr("visibility", False)

        self.ctrn_loc = pri.addTransformFromPos(self.root, self.getName("ctrn_loc"), self.guide.apos[1])
<<<<<<< HEAD
        self.eff_npo  = pri.addTransformFromPos(self.root, self.getName("eff_npo"), self.guide.apos[2])
=======
        # eff npo --- take the effector output of gear ik solver
        self.eff_npo  = pri.addTransformFromPos(self.root, self.getName("eff_npo"), self.guide.apos[2])
        # eff loc --- take the fk ik blend result
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        self.eff_loc  = pri.addTransformFromPos(self.eff_npo, self.getName("eff_loc"), self.guide.apos[2])

        # Mid Controler ------------------------------------
        self.mid_ctl = self.addCtl(self.ctrn_loc, "mid_ctl", tra.getTransform(self.ctrn_loc), self.color_ik, "sphere", w=self.size*.2)
        att.setInvertMirror(self.mid_ctl, ["tx", "ty", "tz"])
        # *ms* add elbow thickness

<<<<<<< HEAD
        # # Twist references ---------------------------------
        # x = dt.Vector(0,-1,0)
        # x = x * tra.getTransform(self.eff_loc)
        # z = dt.Vector(self.normal.x,self.normal.y,self.normal.z)
        # z = z * tra.getTransform(self.eff_loc)

        # m = tra.getRotationFromAxis(x, z, "xz", self.negate) 
        # m = tra.setMatrixPosition(m, tra.getTranslation(self.ik_ctl))

        #Roll join ref
        #self.rollRef = pri.add2DChain(self.root, self.getName("rollChain"), self.guide.apos[:2], self.normal, self.negate)
        #for x in self.rollRef:
         #   x.setAttr("visibility", False)
=======


        #Roll join ref
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4

        self.tws0_npo = pri.addTransform(self.root, self.getName("tws0_npo"), tra.getTransform(self.fk_ctl[0]))
        self.tws0_loc = pri.addTransform(self.tws0_npo, self.getName("tws0_loc"), tra.getTransform(self.fk_ctl[0]))
        self.tws0_rot = pri.addTransform(self.tws0_loc, self.getName("tws0_rot"), tra.getTransform(self.fk_ctl[0]))

        self.tws1_npo = pri.addTransform(self.ctrn_loc, self.getName("tws1_npo"), tra.getTransform(self.ctrn_loc))
        self.tws1_loc = pri.addTransform(self.tws1_npo, self.getName("tws1_loc"), tra.getTransform(self.ctrn_loc))
        self.tws1_rot = pri.addTransform(self.tws1_loc, self.getName("tws1_rot"), tra.getTransform(self.ctrn_loc))

<<<<<<< HEAD
        self.tws2_npo = pri.addTransform(self.root, self.getName("tws2_npo"), tra.getTransform(self.fk_ctl[2]))
        self.tws2_loc = pri.addTransform(self.tws2_npo, self.getName("tws2_loc"), tra.getTransform(self.fk_ctl[2]))
        self.tws2_rot = pri.addTransform(self.tws2_loc, self.getName("tws2_rot"), tra.getTransform(self.fk_ctl[2]))

        # Divisions ----------------------------------------
        # We have at least one division at the start, the end and one for the elbow. + 2 for elbow angle control
        self.divisions = self.settings["div0"] + self.settings["div1"] + 3 + 2

        self.div_cns = []        
        for i in range(self.divisions):

            div_cns = pri.addTransform(self.root, self.getName("div%s_loc" % i))

            self.div_cns.append(div_cns)
            self.jnt_pos.append([div_cns, i])
=======
        self.tws2_loc = pri.addTransform(self.tws1_npo, self.getName("tws2_loc"), tra.getTransform(self.ctrn_loc))
        self.tws2_rot = pri.addTransform(self.tws2_loc, self.getName("tws2_rot"), tra.getTransform(self.ctrn_loc))

        self.tws3_npo = pri.addTransform(self.root, self.getName("tws3_npo"), tra.getTransform(self.fk_ctl[2]))
        self.tws3_loc = pri.addTransform(self.tws3_npo, self.getName("tws3_loc"), tra.getTransform(self.fk_ctl[2]))
        self.tws3_rot = pri.addTransform(self.tws3_loc, self.getName("tws3_rot"), tra.getTransform(self.fk_ctl[2]))

        # Divisions ----------------------------------------
        # We have at least one division at the start, the end and one for the elbow. + 2 for elbow angle control
        # separate up and dn limb
        self.divisions = self.settings["div0"] + self.settings["div1"] + 3 + 2
        self.divisions0 = self.settings["div0"] +2
        self.divisions1 = self.settings["div1"] +2

        self.div_cns = []
        self.div_cnsUp = []
        self.div_cnsDn = []
        
        self.div_org = pri.addTransform(self.root, self.getName("div_org"), tra.getTransform(self.root))
        
        for i in range(self.divisions0):

            div_cns = pri.addTransform(self.div_org, self.getName("div%s_loc" % i))

            self.div_cns.append(div_cns)
            self.div_cnsUp.append(div_cns)
            self.jnt_pos.append([div_cns,i])

        # mid division
        d = self.divisions0
        self.div_mid = pri.addTransform(self.div_org, self.getName("div%s_loc" % d), tra.getTransform(self.mid_ctl))

        self.div_cns.append(self.div_mid)
        self.jnt_pos.append([self.div_mid,self.divisions0])

        # down division
        for i in range(self.divisions1):

            dd = i +self.divisions1+1
            div_cns = pri.addTransform(self.div_org, self.getName("div%s_loc" % dd))

            self.div_cns.append(div_cns)
            self.div_cnsDn.append(div_cns)
            self.jnt_pos.append([div_cns,i+self.divisions0+1])
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4


        # End reference ------------------------------------
        # To help the deformation on the wrist
        self.jnt_pos.append([self.eff_loc, 'end'])
<<<<<<< HEAD
        # self.end_ref = pri.addTransform(self.eff_loc, self.getName("end_ref"), m)
        # for a in "xyz":
        #         self.end_ref.attr("s%s"%a).set(1.0)
        #         self.end_ref.attr("r%s"%a).set(0.0)
        # self.jnt_pos.append([self.end_ref, 'end'])

        #match IK FK references
        self.match_fk0_off = pri.addTransform(self.root, self.getName("matchFk0_npo"), tra.getTransform(self.fk_ctl[1]))
        # self.match_fk0_off.attr("tx").set(1.0)
        self.match_fk0 = pri.addTransform(self.match_fk0_off, self.getName("fk0_mth"), tra.getTransform(self.fk_ctl[0]))

        self.match_fk1_off = pri.addTransform(self.root, self.getName("matchFk1_npo"), tra.getTransform(self.fk_ctl[2]))
        # self.match_fk1_off.attr("tx").set(1.0)
        self.match_fk1 = pri.addTransform(self.match_fk1_off, self.getName("fk1_mth"), tra.getTransform(self.fk_ctl[1]))
        self.match_fk2 = pri.addTransform(self.ik_ctl, self.getName("fk2_mth"), tra.getTransform(self.fk_ctl[2]))

        self.match_ik = pri.addTransform(self.fk2_ctl, self.getName("ik_mth"), tra.getTransform(self.ik_ctl))
        self.match_ikUpv = pri.addTransform(self.fk0_ctl, self.getName("upv_mth"), tra.getTransform(self.upv_ctl))
=======

        #match IK FK references

        self.match_fk0 = pri.addTransform(self.root, self.getName("fk0_mth"), tra.getTransform(self.fk_ctl[0]))
        self.match_fk1 = pri.addTransform(self.root, self.getName("fk1_mth"), tra.getTransform(self.fk_ctl[1]))
        self.match_fk2 = pri.addTransform(self.ik_ctl, self.getName("fk2_mth"), tra.getTransform(self.fk_ctl[2]))

        self.match_ik = pri.addTransform(self.fk2_ctl, self.getName("ik_mth"), tra.getTransform(self.ik_ctl))
        self.match_ikUpv = pri.addTransform(self.fk0_roll_ctl, self.getName("upv_mth"), tra.getTransform(self.upv_ctl))
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4

    def addAttributes(self):

        # Anim -------------------------------------------
        self.blend_att = self.addAnimParam("blend", "Fk/Ik Arm", "double", self.settings["blend"], 0, 1)
        self.blend2_att = self.addAnimParam("blend_hand", "Fk/Ik Hand", "double", self.settings["blend"], 0, 1)
        self.auv_att = self.addAnimParam("auv", "Auto Upvector", "double", 0, 0, 1)
        self.roll_att = self.addAnimParam("roll", "Roll", "double", 0, -180, 180)
        self.armpit_roll_att = self.addAnimParam("aproll", "Armpit Roll", "double", 0, -360, 360)

        self.scale_att = self.addAnimParam("ikscale", "Scale", "double", 1, .001, 99)
        self.maxstretch_att = self.addAnimParam("maxstretch", "Max Stretch", "double", self.settings["maxstretch"], 1, 99)
        self.slide_att = self.addAnimParam("slide", "Slide", "double", .5, 0, 1)
        self.softness_att = self.addAnimParam("softness", "Softness", "double", 0, 0, 1)
        self.reverse_att = self.addAnimParam("reverse", "Reverse", "double", 0, 0, 1)
<<<<<<< HEAD
        self.roundness_att = self.addAnimParam("roundness", "Roundness", "double", 0, 0, 1)
        self.volume_att = self.addAnimParam("volume", "Volume", "double", 1, 0, 1)

=======
        self.roundness0_att = self.addAnimParam("roundness_up", "Roundness_up", "double", 0, 0, 1)
        self.roundness1_att = self.addAnimParam("roundness_dn", "Roundness_dn", "double", 0, 0, 1)
        self.volume_att = self.addAnimParam("volume", "Volume", "double", 1, 0, 1)
        self.elbow_thickness_att = self.addAnimParam("elbowthickness", "Elbow Thickness", "double", self.settings["elbow"], 0, 5)
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        # Ref
        if self.settings["fkrefarray"]:
            ref_names = self.settings["fkrefarray"].split(",")
            if len(ref_names) > 1:
                self.ref_att = self.addAnimEnumParam("fkref", "Fk Ref", 0, self.settings["fkrefarray"].split(","))

        if self.settings["ikrefarray"]:
            ref_names = self.settings["ikrefarray"].split(",")
            if len(ref_names) > 1:
                self.ikref_att = self.addAnimEnumParam("ikref", "Ik Ref", 0, self.settings["ikrefarray"].split(","))

        if self.settings["upvrefarray"]:
            ref_names = self.settings["upvrefarray"].split(",")
            if len(ref_names) > 1:
                self.upvref_att = self.addAnimEnumParam("upvref", "UpV Ref", 0, self.settings["upvrefarray"].split(","))

        # Setup ------------------------------------------
        # Eval Fcurve
        self.st_value = fcu.getFCurveValues(self.settings["st_profile"], self.divisions)
        self.sq_value = fcu.getFCurveValues(self.settings["sq_profile"], self.divisions)

        self.st_att = [ self.addSetupParam("stretch_%s"%i, "Stretch %s"%i, "double", self.st_value[i], -1, 0) for i in range(self.divisions) ]
        self.sq_att = [ self.addSetupParam("squash_%s"%i, "Squash %s"%i, "double", self.sq_value[i], 0, 1) for i in range(self.divisions) ]

        self.resample_att = self.addSetupParam("resample", "Resample", "bool", True)
        self.absolute_att = self.addSetupParam("absolute", "Absolute", "bool", False)

    def addOperators(self):

        # Visibilities -------------------------------------
        # fk
        fkvis_node = nod.createReverseNode(self.blend_att)

        for shp in self.fk0_ctl.getShapes():
            pm.connectAttr(fkvis_node+".outputX", shp.attr("visibility"))
        for shp in self.fk0_roll_ctl.getShapes():
            pm.connectAttr(fkvis_node+".outputX", shp.attr("visibility"))
        for shp in self.fk1_ctl.getShapes():
            pm.connectAttr(fkvis_node+".outputX", shp.attr("visibility"))
        
        fkvis2_node = nod.createReverseNode(self.blend2_att)
        for shp in self.fk2_ctl.getShapes():
            pm.connectAttr(fkvis2_node+".outputX", shp.attr("visibility"))

        # ik
        for shp in self.upv_ctl.getShapes():
            pm.connectAttr(self.blend_att, shp.attr("visibility"))
        for shp in self.ikcns_ctl.getShapes():
            pm.connectAttr(self.blend_att, shp.attr("visibility"))
        for shp in self.ik_ctl.getShapes():
            pm.connectAttr(self.blend_att, shp.attr("visibility"))

        # Controls ROT order -----------------------------------
        att.setRotOrder(self.fk0_ctl, "YZX")
        att.setRotOrder(self.fk0_roll_ctl, "YZX")
        att.setRotOrder(self.fk1_ctl, "XYZ")
        att.setRotOrder(self.fk2_ctl, "YZX")
        # att.setRotOrder(self.ik_ctl, "ZYX")
        att.setRotOrder(self.ik_ctl, "XYZ")


        # IK Solver -----------------------------------------
        out = [self.bone0, self.bone1, self.ctrn_loc, self.eff_npo]
        
        #self.fk_ctl = [self.fk0_roll_ctl, self.fk1_ctl, self.fk2_mtx]
        node = aop.gear_ikfk2bone_op(out, self.root, self.ik_ref, self.upv_ctl, self.fk_ctl[0], self.fk_ctl[1], self.fk2_mtx, self.length0, self.length1, self.negate)

        pm.connectAttr(self.blend_att, node+".blend")
        pm.connectAttr(self.roll_att, node+".roll")
        pm.connectAttr(self.scale_att, node+".scaleA")
        pm.connectAttr(self.scale_att, node+".scaleB")
        pm.connectAttr(self.maxstretch_att, node+".maxstretch")
        pm.connectAttr(self.slide_att, node+".slide")
        pm.connectAttr(self.softness_att, node+".softness")
        pm.connectAttr(self.reverse_att, node+".reverse")

        # auto upvector -------------------------------------

        
        if self.negate:
            node = aop.aimCns(self.upv_auv, self.ik_ctl, axis="-xy", wupType=4, wupVector=[0,1,0], wupObject=self.upv_auv, maintainOffset=False)
        else:
            node = aop.aimCns(self.upv_auv, self.ik_ctl, axis="xy", wupType=4, wupVector=[0,1,0], wupObject=self.upv_auv, maintainOffset=False)
<<<<<<< HEAD
        pb_node = pm.createNode("pairBlend")
        pb_node.attr("rotInterpolation").set (1)

        pm.connectAttr(self.upv_auv.attr("rotate"), pb_node+".inRotate2")
        pm.connectAttr(pb_node+".outRotate", self.upv_mtx.attr("rotate"))
        pm.connectAttr(self.auv_att, pb_node+".weight")

=======

        node = aop.gear_mulmatrix_op(self.upv_auv.attr("worldMatrix"), self.upv_mtx.attr("parentInverseMatrix")) 
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")  
        pb_node = pm.createNode("pairBlend")
        pb_node.attr("rotInterpolation").set (1)
        pm.connectAttr(dm_node+".outputTranslate", pb_node+".inTranslate2")
        pm.connectAttr(dm_node+".outputRotate", pb_node+".inRotate2")
        # pm.connectAttr(node+".outRotate", pb_node+".inRotate2")
        pm.connectAttr(pb_node+".outRotate", self.upv_mtx.attr("rotate"))
        pm.connectAttr(pb_node+".outTranslate", self.upv_mtx.attr("translate"))
        pm.connectAttr(self.auv_att, pb_node+".weight")
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
      


        # fk2_npo position constraint to effector------------------------
        node = aop.gear_mulmatrix_op(self.eff_npo.attr("worldMatrix"), self.fk2_npo.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputTranslate", self.fk2_npo.attr("translate"))
        # fk2_npo rotation constraint to bone1 (bugfixed) ------------------------
        node = aop.gear_mulmatrix_op(self.bone1.attr("worldMatrix"), self.fk2_npo.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputRotate", self.fk2_npo.attr("rotate"))
       
 
        # hand ikfk blending from fk ref to ik ref (serious bugfix)--------------------------------
        node = aop.gear_mulmatrix_op(self.fk_ref.attr("worldMatrix"), self.eff_loc.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pb_node = pm.createNode("pairBlend")
        pb_node.attr("rotInterpolation").set (1)
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputRotate", pb_node+".inRotate1")
        pm.connectAttr(self.blend2_att, pb_node+".weight")
        pm.connectAttr(pb_node+".outRotate", self.eff_loc.attr("rotate"))
        node = aop.gear_mulmatrix_op(self.ik_ref.attr("worldMatrix"), self.eff_loc.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputRotate", pb_node+".inRotate2")


        # Twist references ---------------------------------
<<<<<<< HEAD
        node = aop.gear_mulmatrix_op(self.mid_ctl.attr("worldMatrix"), self.tws1_npo.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputTranslate", self.tws1_npo.attr("translate"))
        pm.connectAttr(dm_node+".outputRotate", self.tws1_npo.attr("rotate"))
        pm.connectAttr(dm_node+".outputScale", self.tws1_npo.attr("scale"))


        node = aop.gear_mulmatrix_op(self.eff_loc.attr("worldMatrix"), self.tws2_npo.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputTranslate", self.tws2_npo.attr("translate"))
        pm.connectAttr(dm_node+".outputRotate", self.tws2_npo.attr("rotate"))

        # orientConstraint(self.eff_loc, self.tws2_rot, maintainOffset=False)
        node = aop.gear_mulmatrix_op(self.eff_loc.attr("worldMatrix"), self.tws2_rot.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        att.setRotOrder(self.tws2_rot, "XYZ")
        pm.connectAttr(dm_node+".outputRotate", self.tws2_rot+".rotate")

        self.tws0_rot.setAttr("sx", .001)
        self.tws2_rot.setAttr("sx", .001)

        add_node = nod.createAddNode(self.roundness_att, .001)
        pm.connectAttr(add_node+".output", self.tws1_rot.attr("sx"))

        pm.connectAttr(self.armpit_roll_att, self.tws0_rot+".rotateX")

=======
        pm.connectAttr(self.mid_ctl.attr("translate"), self.tws1_npo.attr("translate"))
        pm.connectAttr(self.mid_ctl.attr("rotate"), self.tws1_npo.attr("rotate"))
        pm.connectAttr(self.mid_ctl.attr("scale"), self.tws1_npo.attr("scale"))


        node = aop.gear_mulmatrix_op(self.eff_loc.attr("worldMatrix"), self.tws3_npo.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputTranslate", self.tws3_npo.attr("translate"))
        pm.connectAttr(dm_node+".outputRotate", self.tws3_npo.attr("rotate"))


        att.setRotOrder(self.tws3_rot, "XYZ")

        # elbow thickness connection
        if self.negate:
            node = nod.createMulNode([self.elbow_thickness_att,self.elbow_thickness_att], [0.5,-0.5,0], [self.tws1_loc+".translateX",self.tws2_loc+".translateX"])
        else:
            node = nod.createMulNode([self.elbow_thickness_att,self.elbow_thickness_att], [-0.5,0.5,0], [self.tws1_loc+".translateX",self.tws2_loc+".translateX"])

        # connect both tws1 and tws2  (mid tws)     
        self.tws0_rot.setAttr("sx", .001)
        self.tws3_rot.setAttr("sx", .001)

        add_node = nod.createAddNode(self.roundness0_att, .001)
        pm.connectAttr(add_node+".output", self.tws1_rot.attr("sx"))

        add_node = nod.createAddNode(self.roundness1_att, .001)
        pm.connectAttr(add_node+".output", self.tws2_rot.attr("sx"))


        pm.connectAttr(self.armpit_roll_att, self.tws0_rot+".rotateX")
        
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        #Roll Shoulder--use aimconstraint withour uovwctor to solve the stable twist
        
        if self.negate:
            node = aop.aimCns(self.tws0_loc, self.mid_ctl, axis="-xy", wupType=4, wupVector=[0,1,0], wupObject=self.tws0_npo, maintainOffset=False)
        else:
            node = aop.aimCns(self.tws0_loc, self.mid_ctl, axis="xy", wupType=4, wupVector=[0,1,0], wupObject=self.tws0_npo, maintainOffset=False)
           

        # Volume -------------------------------------------
<<<<<<< HEAD
        distA_node = nod.createDistNode(self.tws0_loc, self.tws1_loc)
        distB_node = nod.createDistNode(self.tws1_loc, self.tws2_loc)
=======
        distA_node = nod.createDistNode(self.tws0_loc, self.tws1_npo)
        distB_node = nod.createDistNode(self.tws1_npo, self.tws3_loc)
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
        add_node = nod.createAddNode(distA_node+".distance", distB_node+".distance")
        div_node = nod.createDivNode(add_node+".output", self.root.attr("sx"))

        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(self.root.attr("worldMatrix"), dm_node+".inputMatrix")

        div_node2 = nod.createDivNode(div_node+".outputX", dm_node+".outputScaleX")
        self.volDriver_att = div_node2+".outputX"

        # Divisions ----------------------------------------
<<<<<<< HEAD
        # at 0 or 1 the division will follow exactly the rotation of the controler.. and we wont have this nice tangent + roll
        for i, div_cns in enumerate(self.div_cns):

            if i < (self.settings["div0"]+1):
                perc = i*.5 / (self.settings["div0"]+1.0)
            elif i < (self.settings["div0"] + 2):
                perc = .49
            elif i < (self.settings["div0"] +  3 ):
                perc = .50
            elif i < (self.settings["div0"] +  4 ):
                perc = .51

            else:
                perc = .5 + (i-self.settings["div0"]-3.0)*.5 / (self.settings["div1"]+1.0)
=======
        # div mid constraint to mid ctl
        node = aop.gear_mulmatrix_op(self.mid_ctl.attr("worldMatrix"), self.div_mid.attr("parentInverseMatrix"))
        dm_node = pm.createNode("decomposeMatrix")
        pm.connectAttr(node+".output", dm_node+".inputMatrix")
        pm.connectAttr(dm_node+".outputTranslate", self.div_mid.attr("translate"))
        pm.connectAttr(dm_node+".outputRotate", self.div_mid.attr("rotate"))

        # at 0 or 1 the division will follow exactly the rotation of the controler.. and we wont have this nice tangent + roll
        for i, div_cnsUp in enumerate(self.div_cnsUp):

            if i < (self.settings["div0"]+1):
                perc = i/ (self.settings["div0"]+1.0)
            elif i < (self.settings["div0"] + 2):
                perc = .95

            perc = max(.001, min(.99, perc))

            # Roll
            if self.negate:
                # node = aop.gear_rollsplinekine_op(div_cns, [self.tws3_rot, self.tws1_rot, self.tws0_rot], 1-perc, 40)
                node = aop.gear_rollsplinekine_op(div_cnsUp, [self.tws1_rot, self.tws0_rot], 1-perc, 20)

            else:
                # node = aop.gear_rollsplinekine_op(div_cns, [self.tws0_rot, self.tws1_rot, self.tws3_rot], perc, 40)
                node = aop.gear_rollsplinekine_op(div_cnsUp, [self.tws0_rot, self.tws1_rot], perc, 20)
            pm.connectAttr(self.resample_att, node+".resample")
            pm.connectAttr(self.absolute_att, node+".absolute")

        for i, div_cnsDn in enumerate(self.div_cnsDn):

            if i == (0):
                 perc = .05
            elif i < (self.settings["div1"]+1):
                perc = i/ (self.settings["div1"]+1.0)
            elif i < (self.settings["div1"] + 2):
                perc = .95
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4

            perc = max(.001, min(.990, perc))

            # Roll
            if self.negate:
<<<<<<< HEAD
                node = aop.gear_rollsplinekine_op(div_cns, [self.tws2_rot, self.tws1_rot, self.tws0_rot], 1-perc, 40)
            else:
                node = aop.gear_rollsplinekine_op(div_cns, [self.tws0_rot, self.tws1_rot, self.tws2_rot], perc, 40)

            pm.connectAttr(self.resample_att, node+".resample")
            pm.connectAttr(self.absolute_att, node+".absolute")

            # Squash n Stretch
=======
                # node = aop.gear_rollsplinekine_op(div_cns, [self.tws3_rot, self.tws1_rot, self.tws0_rot], 1-perc, 40)
                node = aop.gear_rollsplinekine_op(div_cnsDn, [self.tws3_rot, self.tws2_rot], 1-perc, 20)

            else:
                # node = aop.gear_rollsplinekine_op(div_cns, [self.tws0_rot, self.tws1_rot, self.tws3_rot], perc, 40)
                node = aop.gear_rollsplinekine_op(div_cnsDn, [self.tws2_rot, self.tws3_rot], perc, 20)
            pm.connectAttr(self.resample_att, node+".resample")
            pm.connectAttr(self.absolute_att, node+".absolute")
        
        # Squash n Stretch
        for i, div_cns in enumerate(self.div_cns):
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4
            node = aop.gear_squashstretch2_op(div_cns, None, pm.getAttr(self.volDriver_att), "x")
            pm.connectAttr(self.volume_att, node+".blend")
            pm.connectAttr(self.volDriver_att, node+".driver")
            pm.connectAttr(self.st_att[i], node+".stretch")
            pm.connectAttr(self.sq_att[i], node+".squash")

        # match IK/FK ref
<<<<<<< HEAD
        pm.parentConstraint(self.bone0, self.match_fk0_off, mo=True)
        pm.parentConstraint(self.bone1, self.match_fk1_off, mo=True)
=======
        pm.connectAttr(self.bone0.attr("rotate"), self.match_fk0.attr("rotate"))
        pm.connectAttr(self.bone0.attr("translate"), self.match_fk0.attr("translate"))
        pm.connectAttr(self.bone1.attr("rotate"), self.match_fk1.attr("rotate"))
        pm.connectAttr(self.bone1.attr("translate"), self.match_fk1.attr("translate"))
>>>>>>> cb99c615949ab9349af88cdadd3b21e0551fb9e4

        return

    # =====================================================
    # CONNECTOR
    # =====================================================
    ## Set the relation beetween object from guide to rig.\n
    # @param self
    # TODO: replace bone0 and control objects by loc connections
    def setRelation(self):
        self.relatives["root"] = self.div_cns[0]
        self.relatives["elbow"] = self.div_cns[self.settings["div0"] + 2]
        self.relatives["wrist"] = self.div_cns[-1]
        self.relatives["eff"] = self.eff_loc

        self.jointRelatives["root"] = 0
        self.jointRelatives["elbow"] = self.settings["div0"] + 2
        self.jointRelatives["wrist"] = len(self.div_cns)-1
        self.jointRelatives["eff"] = -1
    ## standard connection definition.
    # @param self
    def connect_standard(self):
        self.connect_standardWithIkRef()
        # fk isolation connection
        self.connect_standardWithRotRef(self.settings["fkrefarray"], self.fk_cns)