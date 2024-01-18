
"use strict";

let SetPayload = require('./SetPayload.js')
let EndPose = require('./EndPose.js')
let SetSpeedSliderFraction = require('./SetSpeedSliderFraction.js')
let JointTrajectory = require('./JointTrajectory.js')
let JointStates = require('./JointStates.js')
let SetIO = require('./SetIO.js')

module.exports = {
  SetPayload: SetPayload,
  EndPose: EndPose,
  SetSpeedSliderFraction: SetSpeedSliderFraction,
  JointTrajectory: JointTrajectory,
  JointStates: JointStates,
  SetIO: SetIO,
};
