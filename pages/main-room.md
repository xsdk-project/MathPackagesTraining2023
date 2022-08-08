---
layout: page
show_meta: false
title: "Main Room"
header:
   image_fullwidth: "q_center_main.jpg"
permalink: "/main-room/"
---
{% assign vroom = nil %}
{% for vr in site.data.vrooms %}
  {% if vr.name == page.title %}
    {% assign vroom = vr %}
    {% break %}
  {% endif %}
{% endfor %}

This is the main meeting room at the [Q-Center](https://qcenter.com/home-guest/)
in [St. Charles, IL.](https://en.wikipedia.org/wiki/St._Charles,_Illinois)
where [ATPESC](https://extremecomputingtraining.anl.gov) is ordinarily hosted.

### Events occuring in this space

{% include agenda room_filter="Main-room" %}

{% include link-shortcuts %}
