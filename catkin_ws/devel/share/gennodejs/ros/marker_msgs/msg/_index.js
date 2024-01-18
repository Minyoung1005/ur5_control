
"use strict";

let FiducialDetection = require('./FiducialDetection.js');
let MarkerWithCovariance = require('./MarkerWithCovariance.js');
let MarkerDetection = require('./MarkerDetection.js');
let MarkerWithCovarianceArray = require('./MarkerWithCovarianceArray.js');
let MarkerStamped = require('./MarkerStamped.js');
let MarkerWithCovarianceStamped = require('./MarkerWithCovarianceStamped.js');
let Marker = require('./Marker.js');
let Fiducial = require('./Fiducial.js');

module.exports = {
  FiducialDetection: FiducialDetection,
  MarkerWithCovariance: MarkerWithCovariance,
  MarkerDetection: MarkerDetection,
  MarkerWithCovarianceArray: MarkerWithCovarianceArray,
  MarkerStamped: MarkerStamped,
  MarkerWithCovarianceStamped: MarkerWithCovarianceStamped,
  Marker: Marker,
  Fiducial: Fiducial,
};
