//#line 2 "/opt/ros/kinetic/share/dynamic_reconfigure/cmake/../templates/ConfigType.h.template"
// *********************************************************
//
// File autogenerated for the tuw_aruco package
// by the dynamic_reconfigure package.
// Please do not edit.
//
// ********************************************************/

#ifndef __tuw_aruco__ARUCOCONFIG_H__
#define __tuw_aruco__ARUCOCONFIG_H__

#if __cplusplus >= 201103L
#define DYNAMIC_RECONFIGURE_FINAL final
#else
#define DYNAMIC_RECONFIGURE_FINAL
#endif

#include <dynamic_reconfigure/config_tools.h>
#include <limits>
#include <ros/node_handle.h>
#include <dynamic_reconfigure/ConfigDescription.h>
#include <dynamic_reconfigure/ParamDescription.h>
#include <dynamic_reconfigure/Group.h>
#include <dynamic_reconfigure/config_init_mutex.h>
#include <boost/any.hpp>

namespace tuw_aruco
{
  class ArUcoConfigStatics;

  class ArUcoConfig
  {
  public:
    class AbstractParamDescription : public dynamic_reconfigure::ParamDescription
    {
    public:
      AbstractParamDescription(std::string n, std::string t, uint32_t l,
          std::string d, std::string e)
      {
        name = n;
        type = t;
        level = l;
        description = d;
        edit_method = e;
      }

      virtual void clamp(ArUcoConfig &config, const ArUcoConfig &max, const ArUcoConfig &min) const = 0;
      virtual void calcLevel(uint32_t &level, const ArUcoConfig &config1, const ArUcoConfig &config2) const = 0;
      virtual void fromServer(const ros::NodeHandle &nh, ArUcoConfig &config) const = 0;
      virtual void toServer(const ros::NodeHandle &nh, const ArUcoConfig &config) const = 0;
      virtual bool fromMessage(const dynamic_reconfigure::Config &msg, ArUcoConfig &config) const = 0;
      virtual void toMessage(dynamic_reconfigure::Config &msg, const ArUcoConfig &config) const = 0;
      virtual void getValue(const ArUcoConfig &config, boost::any &val) const = 0;
    };

    typedef boost::shared_ptr<AbstractParamDescription> AbstractParamDescriptionPtr;
    typedef boost::shared_ptr<const AbstractParamDescription> AbstractParamDescriptionConstPtr;

    // Final keyword added to class because it has virtual methods and inherits
    // from a class with a non-virtual destructor.
    template <class T>
    class ParamDescription DYNAMIC_RECONFIGURE_FINAL : public AbstractParamDescription
    {
    public:
      ParamDescription(std::string a_name, std::string a_type, uint32_t a_level,
          std::string a_description, std::string a_edit_method, T ArUcoConfig::* a_f) :
        AbstractParamDescription(a_name, a_type, a_level, a_description, a_edit_method),
        field(a_f)
      {}

      T (ArUcoConfig::* field);

      virtual void clamp(ArUcoConfig &config, const ArUcoConfig &max, const ArUcoConfig &min) const
      {
        if (config.*field > max.*field)
          config.*field = max.*field;

        if (config.*field < min.*field)
          config.*field = min.*field;
      }

      virtual void calcLevel(uint32_t &comb_level, const ArUcoConfig &config1, const ArUcoConfig &config2) const
      {
        if (config1.*field != config2.*field)
          comb_level |= level;
      }

      virtual void fromServer(const ros::NodeHandle &nh, ArUcoConfig &config) const
      {
        nh.getParam(name, config.*field);
      }

      virtual void toServer(const ros::NodeHandle &nh, const ArUcoConfig &config) const
      {
        nh.setParam(name, config.*field);
      }

      virtual bool fromMessage(const dynamic_reconfigure::Config &msg, ArUcoConfig &config) const
      {
        return dynamic_reconfigure::ConfigTools::getParameter(msg, name, config.*field);
      }

      virtual void toMessage(dynamic_reconfigure::Config &msg, const ArUcoConfig &config) const
      {
        dynamic_reconfigure::ConfigTools::appendParameter(msg, name, config.*field);
      }

      virtual void getValue(const ArUcoConfig &config, boost::any &val) const
      {
        val = config.*field;
      }
    };

    class AbstractGroupDescription : public dynamic_reconfigure::Group
    {
      public:
      AbstractGroupDescription(std::string n, std::string t, int p, int i, bool s)
      {
        name = n;
        type = t;
        parent = p;
        state = s;
        id = i;
      }

      std::vector<AbstractParamDescriptionConstPtr> abstract_parameters;
      bool state;

      virtual void toMessage(dynamic_reconfigure::Config &msg, const boost::any &config) const = 0;
      virtual bool fromMessage(const dynamic_reconfigure::Config &msg, boost::any &config) const =0;
      virtual void updateParams(boost::any &cfg, ArUcoConfig &top) const= 0;
      virtual void setInitialState(boost::any &cfg) const = 0;


      void convertParams()
      {
        for(std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = abstract_parameters.begin(); i != abstract_parameters.end(); ++i)
        {
          parameters.push_back(dynamic_reconfigure::ParamDescription(**i));
        }
      }
    };

    typedef boost::shared_ptr<AbstractGroupDescription> AbstractGroupDescriptionPtr;
    typedef boost::shared_ptr<const AbstractGroupDescription> AbstractGroupDescriptionConstPtr;

    // Final keyword added to class because it has virtual methods and inherits
    // from a class with a non-virtual destructor.
    template<class T, class PT>
    class GroupDescription DYNAMIC_RECONFIGURE_FINAL : public AbstractGroupDescription
    {
    public:
      GroupDescription(std::string a_name, std::string a_type, int a_parent, int a_id, bool a_s, T PT::* a_f) : AbstractGroupDescription(a_name, a_type, a_parent, a_id, a_s), field(a_f)
      {
      }

      GroupDescription(const GroupDescription<T, PT>& g): AbstractGroupDescription(g.name, g.type, g.parent, g.id, g.state), field(g.field), groups(g.groups)
      {
        parameters = g.parameters;
        abstract_parameters = g.abstract_parameters;
      }

      virtual bool fromMessage(const dynamic_reconfigure::Config &msg, boost::any &cfg) const
      {
        PT* config = boost::any_cast<PT*>(cfg);
        if(!dynamic_reconfigure::ConfigTools::getGroupState(msg, name, (*config).*field))
          return false;

        for(std::vector<AbstractGroupDescriptionConstPtr>::const_iterator i = groups.begin(); i != groups.end(); ++i)
        {
          boost::any n = &((*config).*field);
          if(!(*i)->fromMessage(msg, n))
            return false;
        }

        return true;
      }

      virtual void setInitialState(boost::any &cfg) const
      {
        PT* config = boost::any_cast<PT*>(cfg);
        T* group = &((*config).*field);
        group->state = state;

        for(std::vector<AbstractGroupDescriptionConstPtr>::const_iterator i = groups.begin(); i != groups.end(); ++i)
        {
          boost::any n = boost::any(&((*config).*field));
          (*i)->setInitialState(n);
        }

      }

      virtual void updateParams(boost::any &cfg, ArUcoConfig &top) const
      {
        PT* config = boost::any_cast<PT*>(cfg);

        T* f = &((*config).*field);
        f->setParams(top, abstract_parameters);

        for(std::vector<AbstractGroupDescriptionConstPtr>::const_iterator i = groups.begin(); i != groups.end(); ++i)
        {
          boost::any n = &((*config).*field);
          (*i)->updateParams(n, top);
        }
      }

      virtual void toMessage(dynamic_reconfigure::Config &msg, const boost::any &cfg) const
      {
        const PT config = boost::any_cast<PT>(cfg);
        dynamic_reconfigure::ConfigTools::appendGroup<T>(msg, name, id, parent, config.*field);

        for(std::vector<AbstractGroupDescriptionConstPtr>::const_iterator i = groups.begin(); i != groups.end(); ++i)
        {
          (*i)->toMessage(msg, config.*field);
        }
      }

      T (PT::* field);
      std::vector<ArUcoConfig::AbstractGroupDescriptionConstPtr> groups;
    };

class DEFAULT
{
  public:
    DEFAULT()
    {
      state = true;
      name = "Default";
    }

    void setParams(ArUcoConfig &config, const std::vector<AbstractParamDescriptionConstPtr> params)
    {
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator _i = params.begin(); _i != params.end(); ++_i)
      {
        boost::any val;
        (*_i)->getValue(config, val);

        if("show_debug_image"==(*_i)->name){show_debug_image = boost::any_cast<bool>(val);}
        if("marker_dictonary"==(*_i)->name){marker_dictonary = boost::any_cast<std::string>(val);}
        if("marker_size"==(*_i)->name){marker_size = boost::any_cast<double>(val);}
        if("publish_tf"==(*_i)->name){publish_tf = boost::any_cast<bool>(val);}
        if("publish_markers"==(*_i)->name){publish_markers = boost::any_cast<bool>(val);}
        if("publish_fiducials"==(*_i)->name){publish_fiducials = boost::any_cast<bool>(val);}
        if("pose_estimation_enabled"==(*_i)->name){pose_estimation_enabled = boost::any_cast<bool>(val);}
      }
    }

    bool show_debug_image;
std::string marker_dictonary;
double marker_size;
bool publish_tf;
bool publish_markers;
bool publish_fiducials;
bool pose_estimation_enabled;

    bool state;
    std::string name;

    
}groups;



//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      bool show_debug_image;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      std::string marker_dictonary;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      double marker_size;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      bool publish_tf;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      bool publish_markers;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      bool publish_fiducials;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      bool pose_estimation_enabled;
//#line 228 "/opt/ros/kinetic/share/dynamic_reconfigure/cmake/../templates/ConfigType.h.template"

    bool __fromMessage__(dynamic_reconfigure::Config &msg)
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      const std::vector<AbstractGroupDescriptionConstPtr> &__group_descriptions__ = __getGroupDescriptions__();

      int count = 0;
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); ++i)
        if ((*i)->fromMessage(msg, *this))
          count++;

      for (std::vector<AbstractGroupDescriptionConstPtr>::const_iterator i = __group_descriptions__.begin(); i != __group_descriptions__.end(); i ++)
      {
        if ((*i)->id == 0)
        {
          boost::any n = boost::any(this);
          (*i)->updateParams(n, *this);
          (*i)->fromMessage(msg, n);
        }
      }

      if (count != dynamic_reconfigure::ConfigTools::size(msg))
      {
        ROS_ERROR("ArUcoConfig::__fromMessage__ called with an unexpected parameter.");
        ROS_ERROR("Booleans:");
        for (unsigned int i = 0; i < msg.bools.size(); i++)
          ROS_ERROR("  %s", msg.bools[i].name.c_str());
        ROS_ERROR("Integers:");
        for (unsigned int i = 0; i < msg.ints.size(); i++)
          ROS_ERROR("  %s", msg.ints[i].name.c_str());
        ROS_ERROR("Doubles:");
        for (unsigned int i = 0; i < msg.doubles.size(); i++)
          ROS_ERROR("  %s", msg.doubles[i].name.c_str());
        ROS_ERROR("Strings:");
        for (unsigned int i = 0; i < msg.strs.size(); i++)
          ROS_ERROR("  %s", msg.strs[i].name.c_str());
        // @todo Check that there are no duplicates. Make this error more
        // explicit.
        return false;
      }
      return true;
    }

    // This version of __toMessage__ is used during initialization of
    // statics when __getParamDescriptions__ can't be called yet.
    void __toMessage__(dynamic_reconfigure::Config &msg, const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__, const std::vector<AbstractGroupDescriptionConstPtr> &__group_descriptions__) const
    {
      dynamic_reconfigure::ConfigTools::clear(msg);
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); ++i)
        (*i)->toMessage(msg, *this);

      for (std::vector<AbstractGroupDescriptionConstPtr>::const_iterator i = __group_descriptions__.begin(); i != __group_descriptions__.end(); ++i)
      {
        if((*i)->id == 0)
        {
          (*i)->toMessage(msg, *this);
        }
      }
    }

    void __toMessage__(dynamic_reconfigure::Config &msg) const
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      const std::vector<AbstractGroupDescriptionConstPtr> &__group_descriptions__ = __getGroupDescriptions__();
      __toMessage__(msg, __param_descriptions__, __group_descriptions__);
    }

    void __toServer__(const ros::NodeHandle &nh) const
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); ++i)
        (*i)->toServer(nh, *this);
    }

    void __fromServer__(const ros::NodeHandle &nh)
    {
      static bool setup=false;

      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); ++i)
        (*i)->fromServer(nh, *this);

      const std::vector<AbstractGroupDescriptionConstPtr> &__group_descriptions__ = __getGroupDescriptions__();
      for (std::vector<AbstractGroupDescriptionConstPtr>::const_iterator i = __group_descriptions__.begin(); i != __group_descriptions__.end(); i++){
        if (!setup && (*i)->id == 0) {
          setup = true;
          boost::any n = boost::any(this);
          (*i)->setInitialState(n);
        }
      }
    }

    void __clamp__()
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      const ArUcoConfig &__max__ = __getMax__();
      const ArUcoConfig &__min__ = __getMin__();
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); ++i)
        (*i)->clamp(*this, __max__, __min__);
    }

    uint32_t __level__(const ArUcoConfig &config) const
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      uint32_t level = 0;
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); ++i)
        (*i)->calcLevel(level, config, *this);
      return level;
    }

    static const dynamic_reconfigure::ConfigDescription &__getDescriptionMessage__();
    static const ArUcoConfig &__getDefault__();
    static const ArUcoConfig &__getMax__();
    static const ArUcoConfig &__getMin__();
    static const std::vector<AbstractParamDescriptionConstPtr> &__getParamDescriptions__();
    static const std::vector<AbstractGroupDescriptionConstPtr> &__getGroupDescriptions__();

  private:
    static const ArUcoConfigStatics *__get_statics__();
  };

  template <> // Max and min are ignored for strings.
  inline void ArUcoConfig::ParamDescription<std::string>::clamp(ArUcoConfig &config, const ArUcoConfig &max, const ArUcoConfig &min) const
  {
    (void) config;
    (void) min;
    (void) max;
    return;
  }

  class ArUcoConfigStatics
  {
    friend class ArUcoConfig;

    ArUcoConfigStatics()
    {
ArUcoConfig::GroupDescription<ArUcoConfig::DEFAULT, ArUcoConfig> Default("Default", "", 0, 0, true, &ArUcoConfig::groups);
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __min__.show_debug_image = 0;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __max__.show_debug_image = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __default__.show_debug_image = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.abstract_parameters.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("show_debug_image", "bool", 0, "Show camera debug image", "", &ArUcoConfig::show_debug_image)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __param_descriptions__.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("show_debug_image", "bool", 0, "Show camera debug image", "", &ArUcoConfig::show_debug_image)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __min__.marker_dictonary = "";
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __max__.marker_dictonary = "";
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __default__.marker_dictonary = "ARTOOLKITPLUSBCH";
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.abstract_parameters.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<std::string>("marker_dictonary", "str", 0, "Marker dictonary type", "{'enum_description': 'Marker dictonary type', 'enum': [{'srcline': 11, 'description': 'ArUco orginal', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO'}, {'srcline': 12, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_25h7', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_25h7'}, {'srcline': 13, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_16h3', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_16h3'}, {'srcline': 14, 'description': 'recommended', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_36h12', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_36h12'}, {'srcline': 15, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTAG', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTAG'}, {'srcline': 16, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTOOLKITPLUS', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTOOLKITPLUS'}, {'srcline': 17, 'description': 'default', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTOOLKITPLUSBCH', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTOOLKITPLUSBCH'}, {'srcline': 19, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG16h5', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG16h5'}, {'srcline': 20, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG25h7', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG25h7'}, {'srcline': 21, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG25h9', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG25h9'}, {'srcline': 22, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG36h11', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG36h11'}, {'srcline': 23, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG36h10', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG36h10'}]}", &ArUcoConfig::marker_dictonary)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __param_descriptions__.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<std::string>("marker_dictonary", "str", 0, "Marker dictonary type", "{'enum_description': 'Marker dictonary type', 'enum': [{'srcline': 11, 'description': 'ArUco orginal', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO'}, {'srcline': 12, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_25h7', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_25h7'}, {'srcline': 13, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_16h3', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_16h3'}, {'srcline': 14, 'description': 'recommended', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARUCO_MIP_36h12', 'ctype': 'std::string', 'type': 'str', 'name': 'ARUCO_MIP_36h12'}, {'srcline': 15, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTAG', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTAG'}, {'srcline': 16, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTOOLKITPLUS', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTOOLKITPLUS'}, {'srcline': 17, 'description': 'default', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'ARTOOLKITPLUSBCH', 'ctype': 'std::string', 'type': 'str', 'name': 'ARTOOLKITPLUSBCH'}, {'srcline': 19, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG16h5', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG16h5'}, {'srcline': 20, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG25h7', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG25h7'}, {'srcline': 21, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG25h9', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG25h9'}, {'srcline': 22, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG36h11', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG36h11'}, {'srcline': 23, 'description': '', 'srcfile': '/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg', 'cconsttype': 'const char * const', 'value': 'TAG36h10', 'ctype': 'std::string', 'type': 'str', 'name': 'TAG36h10'}]}", &ArUcoConfig::marker_dictonary)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __min__.marker_size = -std::numeric_limits<double>::infinity();
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __max__.marker_size = std::numeric_limits<double>::infinity();
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __default__.marker_size = 0.06;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.abstract_parameters.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<double>("marker_size", "double", 0, "Marker size in meters", "", &ArUcoConfig::marker_size)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __param_descriptions__.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<double>("marker_size", "double", 0, "Marker size in meters", "", &ArUcoConfig::marker_size)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __min__.publish_tf = 0;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __max__.publish_tf = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __default__.publish_tf = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.abstract_parameters.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("publish_tf", "bool", 0, "", "", &ArUcoConfig::publish_tf)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __param_descriptions__.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("publish_tf", "bool", 0, "", "", &ArUcoConfig::publish_tf)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __min__.publish_markers = 0;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __max__.publish_markers = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __default__.publish_markers = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.abstract_parameters.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("publish_markers", "bool", 0, "", "", &ArUcoConfig::publish_markers)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __param_descriptions__.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("publish_markers", "bool", 0, "", "", &ArUcoConfig::publish_markers)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __min__.publish_fiducials = 0;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __max__.publish_fiducials = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __default__.publish_fiducials = 0;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.abstract_parameters.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("publish_fiducials", "bool", 0, "Publish fiducials to allow 3th party pose estimation.", "", &ArUcoConfig::publish_fiducials)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __param_descriptions__.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("publish_fiducials", "bool", 0, "Publish fiducials to allow 3th party pose estimation.", "", &ArUcoConfig::publish_fiducials)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __min__.pose_estimation_enabled = 0;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __max__.pose_estimation_enabled = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __default__.pose_estimation_enabled = 1;
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.abstract_parameters.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("pose_estimation_enabled", "bool", 0, "ArUco pose estimation is enabled.", "", &ArUcoConfig::pose_estimation_enabled)));
//#line 290 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __param_descriptions__.push_back(ArUcoConfig::AbstractParamDescriptionConstPtr(new ArUcoConfig::ParamDescription<bool>("pose_estimation_enabled", "bool", 0, "ArUco pose estimation is enabled.", "", &ArUcoConfig::pose_estimation_enabled)));
//#line 245 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      Default.convertParams();
//#line 245 "/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py"
      __group_descriptions__.push_back(ArUcoConfig::AbstractGroupDescriptionConstPtr(new ArUcoConfig::GroupDescription<ArUcoConfig::DEFAULT, ArUcoConfig>(Default)));
//#line 366 "/opt/ros/kinetic/share/dynamic_reconfigure/cmake/../templates/ConfigType.h.template"

      for (std::vector<ArUcoConfig::AbstractGroupDescriptionConstPtr>::const_iterator i = __group_descriptions__.begin(); i != __group_descriptions__.end(); ++i)
      {
        __description_message__.groups.push_back(**i);
      }
      __max__.__toMessage__(__description_message__.max, __param_descriptions__, __group_descriptions__);
      __min__.__toMessage__(__description_message__.min, __param_descriptions__, __group_descriptions__);
      __default__.__toMessage__(__description_message__.dflt, __param_descriptions__, __group_descriptions__);
    }
    std::vector<ArUcoConfig::AbstractParamDescriptionConstPtr> __param_descriptions__;
    std::vector<ArUcoConfig::AbstractGroupDescriptionConstPtr> __group_descriptions__;
    ArUcoConfig __max__;
    ArUcoConfig __min__;
    ArUcoConfig __default__;
    dynamic_reconfigure::ConfigDescription __description_message__;

    static const ArUcoConfigStatics *get_instance()
    {
      // Split this off in a separate function because I know that
      // instance will get initialized the first time get_instance is
      // called, and I am guaranteeing that get_instance gets called at
      // most once.
      static ArUcoConfigStatics instance;
      return &instance;
    }
  };

  inline const dynamic_reconfigure::ConfigDescription &ArUcoConfig::__getDescriptionMessage__()
  {
    return __get_statics__()->__description_message__;
  }

  inline const ArUcoConfig &ArUcoConfig::__getDefault__()
  {
    return __get_statics__()->__default__;
  }

  inline const ArUcoConfig &ArUcoConfig::__getMax__()
  {
    return __get_statics__()->__max__;
  }

  inline const ArUcoConfig &ArUcoConfig::__getMin__()
  {
    return __get_statics__()->__min__;
  }

  inline const std::vector<ArUcoConfig::AbstractParamDescriptionConstPtr> &ArUcoConfig::__getParamDescriptions__()
  {
    return __get_statics__()->__param_descriptions__;
  }

  inline const std::vector<ArUcoConfig::AbstractGroupDescriptionConstPtr> &ArUcoConfig::__getGroupDescriptions__()
  {
    return __get_statics__()->__group_descriptions__;
  }

  inline const ArUcoConfigStatics *ArUcoConfig::__get_statics__()
  {
    const static ArUcoConfigStatics *statics;

    if (statics) // Common case
      return statics;

    boost::mutex::scoped_lock lock(dynamic_reconfigure::__init_mutex__);

    if (statics) // In case we lost a race.
      return statics;

    statics = ArUcoConfigStatics::get_instance();

    return statics;
  }

//#line 11 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_ARUCO = "ARUCO";
//#line 12 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_ARUCO_MIP_25h7 = "ARUCO_MIP_25h7";
//#line 13 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_ARUCO_MIP_16h3 = "ARUCO_MIP_16h3";
//#line 14 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_ARUCO_MIP_36h12 = "ARUCO_MIP_36h12";
//#line 15 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_ARTAG = "ARTAG";
//#line 16 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_ARTOOLKITPLUS = "ARTOOLKITPLUS";
//#line 17 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_ARTOOLKITPLUSBCH = "ARTOOLKITPLUSBCH";
//#line 19 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_TAG16h5 = "TAG16h5";
//#line 20 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_TAG25h7 = "TAG25h7";
//#line 21 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_TAG25h9 = "TAG25h9";
//#line 22 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_TAG36h11 = "TAG36h11";
//#line 23 "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/cfg/ArUco.cfg"
      const char * const ArUco_TAG36h10 = "TAG36h10";
}

#undef DYNAMIC_RECONFIGURE_FINAL

#endif // __ARUCORECONFIGURATOR_H__
