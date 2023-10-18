---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can download my resume [here](http://tzerbib.github.io/files/resume_ZERBIB_Timothee_2023.pdf).

Education
======
* Master in Parallel and Distributed Systems, Institut Polytechnique de Paris (France), 2023 <!-- studymap: "Institut Polytechnique de Paris" -->
* Bachelor in Computer Sc. & Engineering, University of Strasbourg (France), 2020 <!-- studymap: "Universite de Strasbourg" -->

Research Experience
======
<!-- workmap: "University of California, Berkeley" -->
* **Master's thesis**, 2023: "Taking down the Leader with Bordeaux. A fair & leaderless byzantine ordering service"
  * [University of California, Berkeley](https://sky.cs.berkeley.edu/) (USA)
  * Supervisor: [Natacha Crooks](https://nacrooks.github.io/)

<!-- workmap: "Institut Polytechnique de Paris" -->
* **Master's research project**, 2022-2023: "Implementation of a multikernel"
  * [Institut Polytechnique de Paris](https://www.inf.telecom-sudparis.eu/pds/) (France)
  * Supervisors: [Gaël Thomas](https://www-public.imtbs-tsp.eu/~thomas_g/)
                and [Mathieu Bacou](https://bacou.wp.imtbs-tsp.eu/).
  
<!-- workmap: "Universite de Neuchatel" -->
* **Internship**, 2021: "Configless and Efficient Switchless Calls for SGX"
  * [University of Neuchâtel](https://www.unine.ch/) (Switzerland)
  * Supervisors: [Pascal Felber](http://members.unine.ch/pascal.felber/index.html), [Alain Tchana](https://perso.ens-lyon.fr/alain.tchana/) and [Valerio Schiavoni](http://members.unine.ch/valerio.schiavoni/)



Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<!-- 
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
-->

Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>


Activities and Interests
======
* Pianist in a jazz band after 15 years in music school.
* Singer in the [vocal ensemble of École Polytechnique](https://chorale.binets.fr/#/presentation).
* Graduated artificer, member of [ArtifiX](https://www.youtube.com/channel/UCa3Vf9d4Wkm25n6EASMpDvg),
École Polytechnique’s students fireworks association.
* Judo (twice honored by the City of Schiltigheim as a “deserving athlete” in 2007
and 2009).
* Math tutor for students preparing the high school diploma.

{% if site.cvmap == true %}
Map
======

Here is a map of places I have
<span style="color:#CB2B3E">lived</span>, 
<span style="color:#2AAD27">studied</span>, and
<span style="color:#2A81CB">worked</span>, 
before.

  <iframe src="/talkmap/map.html" height="700" width="850" style="border:none;"></iframe>
{% endif %}