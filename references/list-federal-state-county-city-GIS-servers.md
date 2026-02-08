# List of Federal ArcGIS Servers and State ArcGIS Servers and County ArcGIS Servers and City ArcGIS Servers

Source PDF: fd4edc51-1fa4-4414-b712-586bf87b7640.pdf

Extracted on: 2026-02-07

## Page 1

List of Federal ArcGIS Servers
and State ArcGIS Servers
and County ArcGIS Servers
and City ArcGIS Servers
Any Dead Links Are Fixed or Flagged Each Week
By Joseph Elfelt, https://mappingsupport.com
Mastodon social media: https://m.ai6yr.org/@mappingsupport
February 4, 2026
See a mistake?  Have relevant information to share?  Please send me an email via
this contact page: https://mappingsupport.com/p2/gissurfer-about-contact.html
Table of contents
1.
Copyright and terms of service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.
About the report and tips. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
3.
Special notes for some servers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.
Business user? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.
View ArcGIS data offline on Android and iOS for free. . . . . . . . . . . . . . . . . . . . 10
6.
Federal GIS Servers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
7.
State, Regional, County and City GIS Servers . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
8.
Washington D.C. Servers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464
9.
Native American Tribes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464
10.
U.S. Territories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 465
11.
Multi-state planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 466
12.
Miscellaneous Regional Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467
13.
USA Miscellaneous Servers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
14.
World Miscellaneous Servers With Some USA Data. . . . . . . . . . . . . . . . . . . . . 472
15.
Environmental groups. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 473
16.
Canada GIS servers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 476
This report has 7,500+ ArcGIS server addresses for the USA.  Those servers all include
“rest/services” somewhere in the address.  The original list only had federal ArcGIS server
addresses.  Over time, state, county and city ArcGIS server addresses were included.  For those
learning or teaching GIS this list will help you learn about and explore geospatial data for your
own backyard.  Hopefully this work will help promote public access to government data which,
after all, is paid for with tax dollars.  As explained below, many of these server addresses were
found with simple Google searches.
This report is online at:
pdf file
https://mappingsupport.com/p/surf_gis/list-federal-state-county-
city-GIS-servers.pdf

## Page 2

1.
Copyright and terms of service
This list of GIS server addresses and their status as currently working or a “dead link” is
copyrighted by Joseph Elfelt.  Contact information is on the first page under the title.  This
copyright covers all file formats that are produced by Joseph Elfelt.
Scrapping data from the PDF file is prohibited.
Commercial products based on this list are prohibited unless specific written permission is
obtained from Joseph Elfelt authorizing that commercial use.
Permission is given for anyone to make a derivative work based on this list as long as the
derivative work is available to everyone for free.  Your derivative work must clearly refer to this
original copyright and state that commercial products based on your derivative work are
prohibited unless specific written permission is obtained from Joseph Elfelt authorizing that
commercial use.
2.
About the report and tips
Update frequency
An updated list is usually posted each Wednesday.  Often this gets done in the morning.
Automated weekly scan
Once a week my code automatically tests each link in this report.  Each link is tested at least 3
times spread over a several hours.  Bad links will promptly be fixed or flagged.  If the address is
not working at all then it will be rendered unclickable and marked “dead link 1”.   In many cases
that government entity still has an ArcGIS server but has simply changed the address and/or
configured their server for internal use only.  Every few months I will check the jurisdictions that
are flagged “dead link 1”.  In many cases I will be able to find a new ArcGIS server address to
add to this list.  If I cannot find a new server address then that entry will be marked “dead link
2”.  From time to time those entries will be deleted from the list.
Tip: Sometimes a link that is flagged as ‘dead’ is only down temporarily.  If you think
such a link might have data you would like to see, you can always replace the leading
underline character with the letter “h” and give the link a try.
As part of the weekly scan each GIS server link will also be tested to detect (1) if directory
services (i.e. table of contents) has been disabled and (2) whether login credentials are required.
This automated weekly code will also test each http link to see if there is now a https version.
This report will be updated with any such new information.
If any kind of login, token or permission is required then that server entry will be marked “Not
open to public”.

## Page 3

If you would like to give GISsurfer a try there are both video and PDF tutorials
to show you how it works.  For links to the tutorials open https://gissurfer.com,
click the big green 'Menu' button and go to the Help page.
One of the videos shows how to find useful information in an ArcGIS
server’s table of contents.
Caution!  Some of the GIS data on these servers will be draft and/or temporary.  Also the server
administrators sometimes renumber the data layers with little to no warning.  This will break any
maps that are based on the former layer numbers.  Another common problem is the use of
gibberish names to identify data folders/layers/attributes combined with the lack of metadata to
translate that gibberish into something useful.  And when you want to ask a question about the
data usually the GIS server metadata lacks any contact information.
See any mistakes?
Some of the servers in this list have multiple jurisdictions and from one entry to the next they
jump between states/counties/cities.  No doubt I became mesmerized a time or two by the
repetition involved and entered some server addresses under the wrong state.  Or I may have
entered a city server’s address in the section for county servers or vice versa.  I cannot fix it
unless someone tells me I goofed.
Why am I doing this?
I am a software developer in the field of online/offline web maps.  One of my projects is
GISsurfer (https://gissurfer.com) which is a general purpose web map based on the free open-
source Leaflet map API (Application Program Interface).  One of the features of GISsurfer is the
ability to display any public-facing (i.e. no login required) ArcGIS MapServer, ImageServer and
FeatureServer data.  GISsurfer can also display WMS data and XYZ tiles.
This list was first published in early 2018 and back then the list only had addresses for some
federal ArcGIS servers.  Over time the list has expanded to include state, county and local
ArcGIS servers.
Personally, I am most interested in GIS data related to disasters (especially wildland fire) and
recreation (especially trails).  A good place to see examples of GISsurfer disaster and recreation
maps is to open GISsurfer and then click “Menu”.  The choices include “Recreation maps” and
“Fire and weather maps”.
If you would like to jump right in and start ‘surfing’ data on ArcGIS servers, then here is the
recipe.
1.
Open GISsurfer: https://mappingsupport.com/p2/gissurfer.php
2.
Zoom in on a state, county or city where you would like to see some GIS data.
3.
Click the basemap button and change the basemap to “USA basemap”.

## Page 4

4.
Click the basemap button again and look under the “Overlay” heading (mobile
users might need to scroll down).  Select “Add GIS overlays”.
5.
Use this ArcGIS server list to copy the address for an ArcGIS server for that state,
county or city and then paste that address into the GISsurfer dialog box.
6.
Click “Send request to GIS server”.  After a few seconds, the sidebar will open
and display the top of the table of contents for that GIS server.
7.
Click an entry in the table of contents to go down to the next level.
8.
An entry with a checkbox can be displayed on the map as an overlay.  Click that
entry to add that GIS data to the map as an overlay.
9.
Click “Menu” ==> “Link to this map”.  The link that is displayed will replicate
the map on your screen.
10.
Click “Menu” ==> “Screenshot mode” to take a series of georeferenced
screenshots that exactly adjoin.
Table of contents disabled
This comment by a server address means that the server administrator has turned off the table of
contents.  If you click that link then the server will display an error message that says “Services
Directory has been disabled.”  Even if a server does in fact have a few data layers that truly are
sensitive and should not be available to the public, that is not a good reason for turning off the
entire table of contents.  There is nothing sensitive about the location of parks, fire stations, roads
and the vast majority of other data that is hosted on GIS servers.
Tip:  To find out the folder and layer names when the table of contents are disabled
simply add ?f=pjson to the end of the address.  Here are generic examples:
https://_____/rest/services?f=pjson
https://_____/rest/services/foldername?f=pjson
https://_____/rest/services/foldername/servicename/MapServer?f=pjson
“ArcGIS server address is not public”
When you see “ArcGIS server address is not public” this means that there is an ArcGIS server
but the server address is hidden from the public by 3rd party (i.e. non-ESRI) software.  An
identifier for the 3rd party software is included.  This is NOT the same as simply disabling the
ArcGIS server’s table of contents.
Some of the jurisdictions that you see in this list with the above label might actually have (in
addition to the 3rd party software) a different ArcGIS server address that is public.  If you know
of any such address please email it to me and I will add it to this list.
Other ways to access this data
For you Python users, Joshua Bailey has built restgdf_api which is a proxy for ArcGIS servers.
The features include access to the ArcGIS servers listed here.  For more information start at
https://github.com/joshuasundance-swca/restgdf_api#readme
http v. https
If you find a GIS server that is not on this list and that starts with http://  then change the link to
https:// and see if that works.  If so then you should use the https version of the server link.

## Page 5

@ServerAdmins - Way to many SSL problems
Thank you to those server administrators who have converted from http to https.  However, too
many of you have not yet made this conversion.  Do you know that SSL certificates from
https://letsencrypt.org/ cost nothing?  And there is a second group of you that has attempted to
convert to https but either have not done so correctly or are using SSL certificates that the
browsers do not trust or that have expired.  Those servers are flagged in this report as having an
SSL problem.  If you would please get new SSL certificates from LetsEncrypt, then this problem
will go away.  To test your https implementation, try browsing to your “rest/services” address
and see if an error message appears.  Both Chrome and Firefox browsers require TLS 1.2
protocol.
Multiple entries for some counties/cities
The focus of this list is to present links that go directly to data for a state agency or county or
city/town/village.  Some of the servers on this list have data for multiple jurisdictions.  It would
have been nice if the server administrator had made a folder for each jurisdiction and then put
all the data for that jurisdiction into that folder.  Unfortunately, sometimes that did not happen.
Data ‘Portals’
Yes, this report does include some addresses for federal and state data portals.  No, publishing
portal addresses is not the primary purpose of this report.  If you are looking for government GIS
portals instead of GIS servers, then here is a list of portal addresses from a volunteer that wishes
to remain anonymous.  The links in this list will take you to maps produced by the governmental
unit.
https://transparentgov.net/cleargov1/777/arcgis-online-10820-entrance-2
Tiled data
This type of data has been pre-rendered into sets of map tiles that display at different zoom
levels.  Tiled data typically display faster than data that has not been tiled.  Basemaps and aerials
are examples of data that is often tiled.  When you see “XYZ” that is usually a reference to tiled
data.
Here is an example GISsurfer map link that displays tiled aerial photos for NewJersey.  Open the
map and zoom in for lots of detail.
https://mappingsupport.com/p2/gissurfer.php?center=40.159660,-75.042114&zoom=8&basemap
=USA_basemap&overlay=New_Jersey_2020_aerial&data=overlay^name=New_Jersey_2020_ae
rial^url=https://mapstest.nj.gov/arcgis/rest/services/Basemap/Orthos_Natural_2020_NJ_WM/Ma
pServer/tile/{z}/{y}/{x}
Mosy of the federal and state ArcGIS servers have been checked to see if they are hosting tiled
data.  The list indicates whether one or more layers of tiled data were found on the server.
When you see a server address that has tiled data then you can get a list of the layers that are tiled
by doing a Google search like so:
site:server-address  "wmts"      include the quotes and there is no space after the colon
Example
site:https://mapstest.nj.gov/arcgis/rest/services    "wmts"

## Page 6

There are also some tile servers in this list that only have tiled data.  If you search this list on
tiles.arcgis.com then you will find the tile servers.  Some of these servers have many layers of
tiled data.  The word “tile” is highlighted in the server address.
To check any county or city ArcGIS server for tiled data first find the server address in this list
and then do a Google search as described above.  You never know what you might find unless
you look.
GIS data for tax parcels
Many people are interested in GIS data showing tax parcels.  Just over half of the states have a
GIS layer that shows parcel lines for the entire state.  Here is a GISsurfer map link that you can
use to view the parcel line data for those states.  For help using the map click “Map tips” in the
upper left corner.
https://mappingsupport.com/p2/gissurfer.php?center=47.398569,-120.317459&zoom=11
&basemap=USA_basemap&overlay=PAD-US_all,PAD-US_all_outline&data=https://ma
ppingsupport.com/p2/parcels/USA_public_private_parcels.txt
Caution!  GIS parcel line data is not a survey and is not authoritative.  You cannot rely on GIS
parcel line data to determine if your neighbor’s driveway or anything else is on your land.  You
may have heard about apps such as onX, LandGlide, Regrid, etc that display parcel lines.
Those apps simply display a copy of the GIS parcel line data maintained by the counties.  If the
GIS parcel line data is bad then the parcel lines displayed by these apps is also bad.
A few additional states have parcel line data for each county in a separate GIS layer.  To find that
data, search this list on a state name and then scroll through the state servers looking for “Parcel
lines”.  Many county and some city GIS servers also have parcel line data although those layers
are usually not identified in this report.  To look for parcel line data on a specific server use  a
google ‘advanced’ search.  Here is an example:
site:https://gismaps.kingcounty.gov/arcgis/rest/services   parcel
Tip:  This type of search works for any data.  For example to see if a server has trail data
you could search on:
site:server_address   trail
Often the ‘description’ on the GIS server for parcel data does not tell you how often it is updated
or even if it is updated at all!  If parcel line data is available on a county GIS server then it is
usually a good idea to use that data instead of parcel line data on a state server.  The data on the
county server might be more current and might have better attribute data.
Custom property line map
Instead of relying on GIS parcel line data, here is an option.  I offer a consulting service that
produces the most accurate property line maps you can get without buying a survey.  You
will be pleasantly surprised by the affordable price.  If that sounds interesting then for more
information please see https://findpropertylines.com.

## Page 7

Login required v. public-facing
A small number a ArcGIS servers on this list require a login in order to access any data.  That
type of  restriction is noted in the list.  Fortunately the great majority of government GIS servers
are public-facing - i.e. no login is required.
Ways to help
If you know of a federal, state, regional, county or city ArcGIS server that is not already listed
below and that includes at least some data where no login credentials are required, please send
me an email via the contact link posted above.  Note that I am only looking for the ‘top’
endpoint for ArcGIS servers.  Those links all end in “rest/services”.  I would particularly like
to get addresses for more ArcGIS servers operated by regional planning bodies.
Anyone can easily search for ArcGIS servers.  Assume you want to know if St. Louis County
Minnesota (County seat is Duluth) has a public-facing ArcGIS server.  First, find the county
website.  Note that the website address includes “stlouiscountymn”.  Second, do a Google search
on: stlouiscountymn “rest/services”.  Include the quotes in your search.  If this county has a GIS
server then you will likely see search hits to various places within the table of contents.  Open
any table of contents page and then in the upper left corner click on “Home”.  You now will see
the ‘top’ of the table of contents for this ArcGIS server and the browser address bar will display
an address that ends in “/rest/services”.
Of course at the county and city level you could simply call or email the GIS staff and ask.  Here
is one way to phrase the question:  “Do you have a public-facing ArcGIS server and, if so, what
is the rest service endpoint?”
Sometimes you might see two server addresses that appear identical except one of them says
“arcgis” and the other says “ArcGIS”.  Technically these are different internet addresses and
these two servers may or may not contain the same information.
Each state has a section for links to county ArcGIS servers and then a section for links to city
ArcGIS servers.  Find your state and see if it looks like I listed any city servers in the county
section or vice versa.
Some counties and cities have agreed to cooperate and have data layers for both jurisdictions on a
single server.  When that happens I want to show both the city name and county name in this list
along with a pointer to whichever one is hosting the combined data.  If you know of any such
ArcGIS servers, please send me an email via my contact page.  Go to
https://mappingsupport.com, click the big green “Menu” button and select “About and contact”.
See the section “USA Miscellaneous Servers” near the start of the list.  If you can identify any of
those links as primarily having data for one state or one county or one city, please let me know
and I will move that server link to the appropriate location.
Searching tips
If you are looking for a certain type of data, try a Google advanced search.  For example, if you
are looking for trail data then search on:

## Page 8

site:server-address   trail
There is no space in between “site:” and the server address.
If you are interested in a topic instead of a state/county/city then try a Google search like this
example:
"climate change" "rest/services".
Include keywords for your topic and always include rest/services in quotes.  Many of the hits that
are returned will point you to ArcGIS layers.
Related web pages
Data.gov and GeoPlatform:  These two websites can also help you find federal GIS servers.
Enter your search criteria and then in the left sidebar find the “Format” section and select “ESRI
Rest”.  The hits will be for ArcGIS layers.  In other words, these two sites index the ‘bottom’ of
a GIS server table of contents.  By contrast, this PDF report shows you the ‘top’ of the table of
contents for GIS servers.  One advantage of these two sites is that you may find metadata that is
not present when you look at the GIS server page for the same data.  Caution:  Many (most?) of
the GIS layers on the various federal servers have not been submitted by the server
administrators for inclusion on data.gov or geoplatform.
Geodatadownloader:  Do you want to download ArcGIS data?  Here is a tool to help you.  The
link points to the GitHub ‘Read me’ file.  Here is a related thread on Reddit.
GeoSeer is a search engine for finding data served through WMS, WFS, WCS, and WMTS
services. It allows users to easily find publicly available datasets which they can then use in their
own projects using normal GIS tools. At the time of writing GeoSeer has over 1.2 million distinct
spatial layers in its index from over 160,000 services.  This is a worldwide search tool.  Note:
GeoSeer does not index ArcGIS ESRI Rest data (the ArcGIS Server default).  It only indexes
data that are available via any of the four standards listed above - all of which ArcGIS Server is
capable of serving - but none of which are the default.
Are you looking for maps instead of just data?
I expect that most government entities that have a GIS server also have produced some maps
anyone can look at.  Just go to the website for that city, county or other government entity and
search their site for maps.  If that does not work then you might look for a link to the GIS or
planning department.  Maps that are produced by GIS staff often include explanations about the
data along with supporting information such as a contact link for questions.
Are you a GIS server administrator?
First, hopefully you are in favor of public access to data and will not take any action to make it
hard/impossible for people to view the data your server is hosting.  And if you have disabled the
‘services directory’ (i.e. table of contents) please consider turning that back on.  Yes, if you allow
the public to browse the services directory there is at least a theoretical security risk in the form
of cross site scripting attacks (XSS).  But if this was actually a significant threat then it would be
a common practice for server administrators to disable the services directory and that is simply
not happening.

## Page 9

Second, if your server is still using http then notice that the great majority of servers in this
report are using https.  This is in keeping with the philosophy promoted by Google and others to
‘encrypt everything’.  You can get free SSL certificates from https://letsencrypt.org/.  I use this
service for the domains that I own.
Third, if you make a significant change to your server that affects (for better or worse) the
public’s ability to view the data on your server, please send me an email and I will update this
list.
Fourth, are you using gibberish for the names of the folders, services, layers and attribute data
on your server?  Are you using names like PG instead of Playgrounds?  What good public
purpose is served by obfuscating the data your server is hosting by using gibberish names
instead of plain-speak?  ESRI does not charge by the letter!
Fifth, is there data on your server that might endanger public safety if that data was publicly
available?  If so, then consider placing that data in a folder that requires login credentials.  By
doing that, most of the data on the server could continue to be publically available while the truly
sensitive data would be protected behind a login requirement.
Credits
Thanks to Jonathan at GeoSeer (https://www.geoseer.net/) for sharing over 200(!) ArcGIS server
addresses.  The GeoSeer site is a great complement to this list of server addresses.  GeoSeer
indexes individual GIS data layers and provides a way for anyone to freely search their
database for GIS data.  GeoSeer builds its database with code that scans GIS servers that are
based on WMS, WMTS, WFS, WCS and ArcGIS.
Thanks also to everyone else that has sent me addresses for ArcGIS REST services.  All things
considered, I decided that the best course of action is to not credit anyone by name unless you
give me permission to do so.  So if you contributed and would like to be credited, please drop me
an email via my contact page: https://mappingsupport.com/p2/gissurfer-about-contact.html
3.
Special notes for some servers
The names of some counties/cities are followed only by a line.  That means this curated list used
to have an address for ArcGIS layers for that jurisdiction but the server hosting that data is gone.
As time allows I will look for a new server address for each of those counties/cities.
Example:
Anderson
__________
The servers listed below each support many different jurisdictions.  Each server will either
display the table of contents for all of the jurisdictions it is hosting or the server will not display
any of those table of contents.  Alas, some of these servers have changed this setting back and
forth more than once.  I am no longer going to take the time to update this list with those
changes.  If you are looking for data on any of the following servers simply try one of the links to
see whether or not the table of contents is displayed.

## Page 10

If you are using this list for business purposes then you are taking advantage of my
hard work to help you make money.  Please consider making a donation.
https://gis2.gisworkshop.com/arcgis/rest/services
https://gis3.gisworkshop.com/arcgis/rest/services
https://gis2.gworks.com/arcgis/rest/services
https://gis3.gworks.com/arcgis/rest/services
For servers that do not host many different jurisdictions, this list will continue to be updated to
show whether or not those servers display the table of contents.
4.
Business user?
The report you are looking at has taken days and days of effort to compile.  Time is spent each
week to maintain and update the list.  And there certainly are additional government ArcGIS
servers waiting to be discovered and added to this list.  If you find this list of server addresses to
be useful please consider making a donation to help fund this work.
If you know of any grant programs that might be interested in funding this work, please use the
‘contact’ link at the top of this report and send me that information.
Here is a link for the GISsurfer donate page.  You can always include a short note indicating that
you are donating to help fund the ArcGIS server list.
https://mappingsupport.com/p2/gissurfer-donate.html
5.
View ArcGIS data offline on Android and iOS for free
ATAK is a free Android app that is funded by the federal government.  There are no ads.  Its
primary focus is helping first responders (or anyone else) maintain situational awareness.
However it can certainly be used for recreation or any other purpose.
Download ATAK Civilian from https://tak.gov.  After installing you can find the User Guide at
atak > support > docs.
Tip:  If all you want to do is use ATAK to view ArcGIS data then you can ignore all the ATAK
documentation about servers, radios, team communication and plug-ins.
ArcGIS data that is tiled can be displayed as either a basemap or as an overlay.
ArcGIS MapServer point/line/polygon data that is not tiled can be streamed directly from the
ArcGIS server into ATAK.

## Page 11

ArcGIS FeatureServer point/line/polygon data can be converted to KMZ (see below) and then
displayed.
Here are some good sources for information on ATAK.
https://www.takps.org
https://www.thetaksyndicate.org
https://www.youtube.com/@thetaksyndicate6234/videos
https://www.civtak.org
Discord: https://discord.com/invite/zj24N89yZ7
For detailed information on displaying ArcGIS data with ATAK I have produced several PDF
files.  Displaying ArcGIS MapServer and FeatureServer data is covered by the following three
PDFs.

Introduction.
https://mappingsupport.com/p2/atak/pdf/atak_arcgis_tips.pdf
Download ArcGIS MapServer data as KMZ.  Learn how to stream data directly from an
ArcGIS server into ATAK.
https://mappingsupport.com/p2/atak/pdf/atak_arcgis_query.pdf
Download ArcGIS FeatureServer data as KMZ.
https://mappingsupport.com/p2/atak/pdf/atak_arcgis_convert.pdf
Tip:  Google Earth Pro is free software for PCs and laptops.  It can display KMZ data and let you
fly over the data in simulated 3D.  Very cool.
If you want to use ATAK to display ArcGIS tiled data then the following web page has links to
several PDFs I produced with step-by-step instructions.  This information also shows how to
display non-ESRI GIS data with ATAK.
https://mappingsupport.com/p2/atak/display_gis_data_with_atak.html
You can ignore any information you see about an ESRI plug-in for ATAK.  I tested it and it does
not work very well at all.  Also you can only get that plug-in if you have a ‘gov’ or ‘mil’ email
address.
TAK Aware and iTAK are free iOS apps.   There are no ads.
TAK Aware is a newer app that is steadily being improved as features are added.  One focus of
this app is to try and have the same ‘look and feel’ as ATAK.
https://apps.apple.com/in/app/tak-aware/id6738631659
The TAK Aware website includes links to the user manual and GitHub page.
https://www.flighttactics.com/takaware

## Page 12

The iTAK app does not try to mimic the ‘look and feel’ of ATAK.  Many features of ATAK
have not been implemented.  The pace of improvements is slow.
https://apps.apple.com/us/app/itak/id1561656396
6.
Federal GIS Servers
House of Representatives
GIS: https://services1.arcgis.com/o90r8yeUBWgKSezU/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/o90r8yeUBWgKSezU/arcgis/rest/services
Library of Congress
GIS: https://services5.arcgis.com/ohAFyIFvXFRGcC67/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/ohAFyIFvXFRGcC67/arcgis/rest/services
Department of Agriculture (USDA)
* Various agriculture related layers - unknown ownership
GIS: https://services1.arcgis.com/SyUSN23vOoYdfLC8/arcgis/rest/services
layers that start PHZM contain current plant hardiness zone data
GIS: https://tiles.arcgis.com/tiles/SyUSN23vOoYdfLC8/arcgis/rest/services
* USDA - Enterprise Geospatial Management
Website:
https://www.usda.gov/about-usda/general-information/staff-offices/office-
chief-information-officer/enterprise-geospatial-management-office
GIS: https://services8.arcgis.com/5vMtpwj1mnc06Rmi/arcgis/rest/services
* USDA - Agricultural Research Service
Website: https://www.ars.usda.gov
GIS: _ttps://www.nrrig.mwa.ars.usda.gov/server40/rest/services
dead link 3
* USDA - Bio Gas
Website: _ttps://www.wctsservices.usda.gov/Energy/maps/Biogas
dead link 3
GIS: See “USDA - Rural Development” below
* USDA - Foreign Agricultural Service
Website: https://www.fas.usda.gov
GIS: https://geo.fas.usda.gov/arcgis1/rest/services
8-13-2023 no tiled data
GIS: https://geo.fas.usda.gov/arcgis2/rest/services
8-13-2023 no tiled data
GIS: https://services.arcgis.com/Z58T9dmhcpCmous1/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Z58T9dmhcpCmous1/arcgis/rest/services

## Page 13

* USDA - Economic Research Service
Website: https://www.ers.usda.gov/
GIS: https://gisportal.ers.usda.gov/server/rest/services
* USDA -  Farm Production and Conservation Business Center
Website: https://www.fpacbc.usda.gov
GIS: _ttps://gis.apfo.usda.gov/arcgis/rest/services
dead link 1
Includes NAIP as ImageServer
2-21-2023 no tiled data
* USDA -  Marketing and Regulatory Programs
Website: https://www.ams.usda.gov
GIS: https://services7.arcgis.com/2C1NQ7u6M6SXoa8p/ArcGIS/rest/services
* USDA - Forest Service - Geospatial Data Discovery
Website: https://data-usfs.hub.arcgis.com
GIS: https://apps.fs.usda.gov/arcx/rest/services
2-22-2025 interesting wildfire data at RDW_Wildfire
* USDA - Forest Service - Enterprise Data Warehouse (EDW)
Website: https://data.fs.usda.gov/geodata/edw/mapServices.php
GIS: https://apps.fs.usda.gov/arcx/rest/services/EDW
2-21-2023 no tiled data
/RDW_Climate/plant hardiness, etc
Here are some key recreation layers
Land USFS owns
    EDW/EDW_BasicOwnership_01/MapServer/0  (green areas)
USFS Trails
    EDW/EDW_TrailNFSPublish_01/MapServer/0
USFS Recreation sites
    EDW/EDW_RecreationAreaActivities_01/MapServer/0
MVUM - Motor  Vehicle Use Map
    EDW/EDW_MVUM_01/MapServer/1,2
* USDA - Forest Service - Forest Atlas
PDF: https://www.fs.usda.gov/research/treesearch/64468
GIS: https://apps.fs.usda.gov/arcx/rest/services/RDW_FIA_ForestAtlas
8-13-2023 No tiled data
* USDA - Forest Service - Forest health
Website: https://www.fs.usda.gov/foresthealth
GIS:  https://apps.fs.usda.gov/fsgisx02/rest/services/foresthealth
8-13-2023 No tiled data
* USDA - Forest Service - Various links
GIS: https://apps.fs.usda.gov/fsgisx01/rest/services

## Page 14

RDW_Wildfire  has wildfire risk assessment
2-21-2023 no tiled data
GIS: https://apps.fs.usda.gov/fsgisx02/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://apps.fs.usda.gov/fsgisx03/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://apps.fs.usda.gov/fsgisx04/rest/services
GIS: https://apps.fs.usda.gov/fsgisx05/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://fsapps.nwcg.gov/psp/arcgis/rest/services
wildfire related data
2-21-2023 no tiled data
GIS: https://services1.arcgis.com/gGHDlz6USftL5Pau/arcgis/rest/services
Region 6 (WA OR) closures.  R06_FireClosureOrders_PublicView/FeatureServer
GIS: https://tiles.arcgis.com/tiles/gGHDlz6USftL5Pau/arcgis/rest/services
Region 6.  Includes basemaps for many national forests.  I tried one but got 404 on
the tile call.
GIS: https://apps.fs.usda.gov/dmsm/rest/services
8-13-2023 No tiled data
GIS: https://services1.arcgis.com/gGHDlz6USftL5Pau/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/gGHDlz6USftL5Pau/arcgis/rest/services
All data is tiled
* USDA - Natural Resources Conservation Service
Soil Survey Geographic (SSURGO)
Website:
https://www.nrcs.usda.gov/conservation-basics/natural-resource-concerns/
soils/soil-geography
GIS: https://nrcsgeoservices.sc.egov.usda.gov/arcgis/rest/services
2-21-2023 no tiled data
GIS: https://services.arcgis.com/SXbDpmb7xQkk44JV/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/SXbDpmb7xQkk44JV/arcgis/rest/services
* USDA - CarbonScapes
Website: _ttps://www.carbonscapes.org
dead link 3
GIS: _ttps://opendata.wvgis.wvu.edu/arcgis/rest/services/CarbonScapes      dead link 3
2-21-2023 no tiled data
* USDA - Rural Development
Website: https://www.rd.usda.gov/
GIS: https://rdgdwe.sc.egov.usda.gov/arcgis/rest/services
8-13-2023 No tiled data
Includes BioGas data
GIS: https://services.arcgis.com/UbyviKPk0x1UemzF/arcgis/rest/services
* USDA - Scientific Computing

## Page 15

Website: https://scinet.usda.gov
GIS: https://pdi.scinet.usda.gov/image/rest/services
Department of Commerce (DOC)

*DOC - Census Bureau
Website: https://www.census.gov/
GIS: https://tigerweb.geo.census.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Tiled transportation.  Use as an overlay.  TIGERweb/Transportation/MapServer
GIS: https://mtgis-server.geo.census.gov/arcgis/rest/services     Table of contents disabled
2-21-2023 no tiled data
GIS: https://services8.arcgis.com/DlJzJLOZpPXmMpWi/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/DlJzJLOZpPXmMpWi/arcgis/rest/services
* DOC - National Oceanic and Atmospheric Administration (NOAA)
GIS: https://maps.water.noaa.gov/server/rest/services
Added 9-25-2024   Flood related
GIS: https://imagery.coast.noaa.gov/arcgis/rest/services
GIS: https://services9.arcgis.com/RHVPKKiFTONKtxq3/ArcGIS/rest/services
Added 9-15-2024
Lots of  weather data.  Also fire perimeter
GIS: https://www.coast.noaa.gov/arcgis/rest/services
GIS: https://coast.noaa.gov/arcgismc/rest/services
Added 3-12-2024 tons of data.  NOAA says new services each month to the
“Hosted” folder.
GIS: Tiled server for hurricane damage aerials   https://storms.ngs.noaa.gov/
://stormscdn.ngs.noaa.gov/20220929a-rgb/{z}/{x}/{y}^layers=20220929a_RGB
GIS: https://maps.fisheries.noaa.gov/server/rest/services
GIS: https://seamlessrnc.nauticalcharts.noaa.gov/arcgis/rest/services
SSL problem
2-21-2023 no tiled data
GIS: https://coast.noaa.gov/arcgis/rest/services/
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://maps.coast.noaa.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://maps1.coast.noaa.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://maps2.coast.noaa.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://maritimeboundaries.noaa.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Tiled: MarineChart_Services/NOAACharts/MapServer
GIS: https://gis.charttools.noaa.gov/arcgis/rest/services
2-21-2023 no tiled data
NGS folder has benchmarks.

## Page 16

Here is a GISsurfer map that displays the nautical charts.  Zoom in for more
detail.  There are also some additional GIS overlays you can turn on/off and
restack.  For the map legend and more information please click "Map tips" in the
upper left corner.
https://mappingsupport.com/p2/gissurfer.php?center=26.211214,-80.870361&zoo
m=7&basemap=NOAA_marine_chart&overlay=AWOIS_obstructions,ENC_wrec
ks,AWOIS_wrecks&data=https://mappingsupport.com/p2/recreation/USA_NOA
A_nautical.txt
GIS: https://satellitemaps.nesdis.noaa.gov/arcgis/rest/services
See: https://www.nesdis.noaa.gov
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.dat.noaa.gov/arcgis/rest/services
nws_damageassessmenttoolkit:  preliminary storm damage
https://services.dat.noaa.gov/arcgis/rest/services/nws_damageassessmenttoolkit/D
amageViewer/MapServer      tornado data
8-13-2023 No tiled data
GIS: https://services1.arcgis.com/2iUE8l8JKrP2tygQ/ArcGIS/rest/services
A lot of Georgia layers but also some USA weather layers
GIS: https://services2.arcgis.com/C8EMgrsFcRFL6LrL/arcgis/rest/services
slow server
Lots of weather/storm data.  Damage pics after EF3 or higher tornado
NGS_Datasheets_Feature_Service (FeatureServer)
NGS_Published_Benchmarks (FeatureServer)
change_8110_7100 new plant hardiness zone
hot_springs
Tsunami data
GIS: https://tiles.arcgis.com/tiles/C8EMgrsFcRFL6LrL/arcgis/rest/services
GIS: https://gis.nnvl.noaa.gov/arcgis/rest/services
NOAA’s interactive map viewer uses these datasets.
https://www.nnvl.noaa.gov/view/globaldata.html
There is a layer that displays heat in the water for hurricanes.
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
* DOC - National Center for Environmental Prediction
Website: https://www.weather.gov/ncep
New addresses for ArcGIS hosted on Amazon’s cloud
See: https://www.weather.gov/gis/cloudgiswebservices
GIS: https://mapservices.weather.noaa.gov/static/rest/services
8-13-2023 No tiled data
GIS: https://mapservices.weather.noaa.gov/experimental/rest/services
 Flood Hazard Outlook
8-13-2023 No tiled data
GIS: https://mapservices.weather.noaa.gov/eventdriven/rest/services
Serves this map: https://viewer.geospatial.weather.gov
SSL problem
8-13-2023 No tiled data

## Page 17

GIS: https://mapservices.weather.noaa.gov/tropical/rest/services
Pre-hurricane
8-13-2023 No tiled data
GIS: https://mapservices.weather.noaa.gov/vector/rest/services
8-13-2023 No tiled data
Weather Hazard Outlooks for 3-14 days
/hazards/cpc_weather_hazards/MapServer
GIS: https://mapservices.weather.noaa.gov/raster/rest/services
8-13-2023 No tiled data
Includes winter weather outlook and snow data
* DOC - nowCOAST
NOAA’s nowcoast ArcGIS server  was shutdown in April, 2023.  About 1/4 of the
data layers moved to Amazon’s cloud and use geoserver and other open source (i.e. not
ArcGIS) software.  Primary data access will be by WMS.  Additional data layers will
hopefully be added over next 1-2 years.
For a conversion table from the old ArcGIS addresses to the new geoserver cloud
addresses and links to multiple GetCapabilities files, see:
https://mappingsupport.com/p2/noaa/2023-nowCOAST-ServicesMappingTable-V4.pdf
* DOC - National Center for Environmental Information (NCEI - formerly NGDC)
Website: https://www.ngdc.noaa.gov/
GIS: https://gis.ngdc.noaa.gov/arcgis/rest/services
2-21-2023 no tiled data
cdo directory has good weather data.  Also countries outline, but no names.
/web_mercator/hazards/MapServer   Includes tsunami data
GIS: https://gis.ncdc.noaa.gov/arcgis/rest/services
Might include the same ‘cdo’ data as above server.
Includes reference layers
Need to find out what data all these weather layers display
8-13-2023 No tiled data
* DOC - Electronic Nautical Charts (ENC)
Website: https://www.nauticalcharts.noaa.gov/index.html
GIS: https://encdirect.noaa.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”

GIS: https://wrecks.nauticalcharts.noaa.gov/arcgis/rest/services
SSL problem
8-13-2023 No tiled data
* DOC - Gulf of Mexico Fishery Management Council
Website: https://gulfcouncil.org
GIS: https://portal.gulfcouncil.org/arcgis/rest/services
8-13-2023 No tiled data
Department of Defense (DOD)

## Page 18

* DOD - Air Force Recruiting Service
Website: https://www.afaccessionscenter.af.mil
* DOD - Army Corps of Engineers - Readiness Support Center
Website: _ttps://rsc.usace.army.mil
dead link 3
GIS: https://ienccloud.us/arcgis/rest/services
Inland water, major rivers
8-13-2023 No tiled data
GIS: https://services7.arcgis.com/n1YM8pTrFmm7L4hs/ArcGIS/rest/services
/usace_river_mile_markers
Same address also exists as:  ___.ArcGIS.___
GIS: https://tiles.arcgis.com/tiles/n1YM8pTrFmm7L4hs/arcgis/rest/services
GIS: https://geospatial.sec.usace.army.mil/server/rest/services
119th congress, dynamic layers    name and party
Census/Congressional_Districts/MapServer/0
GIS: https://geospatial.sec.usace.army.mil/dls/rest/services
NID/National_Inventory_of_Dams_Public_Service/MapServer
GIS: https://spatial.usace.army.mil/opjarcgis/rest

GIS: _ttps://geoportal-dmzu.usace.army.mil/s1arcgis/rest/services
dead link 2
/ERDC has river data
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: _ttps://arcservices-ucop.usace.army.mil/arcgis/rest/services
dead link 2
GIS: _ttps://gis.sam.usace.army.mil/server/rest/services
dead link 2
GIS: _ttps://ags01.sec.usace.army.mil/server/rest/services
dead link 2
Lots of flood data
GIS: _ttps://ags02.sec.usace.army.mil/server/rest/services
dead link 2
GIS: _ttps://ags03.sec.usace.army.mil/server/rest/services
dead link 2
GIS: https://services7.arcgis.com/wooIevDLYznutGEM/ArcGIS/rest/services
Charleston District
GIS: https://tiles.arcgis.com/tiles/wooIevDLYznutGEM/arcgis/rest/services
Charleston District
GIS: https://services5.arcgis.com/W7M7ugHEl8tg1wcM/ArcGIS/rest/services
Kansas City District
GIS: https://tiles.arcgis.com/tiles/W7M7ugHEl8tg1wcM/arcgis/rest/services
Kansas City District
GIS: https://services6.arcgis.com/wyJygLsBd4XEYUkl/ArcGIS/rest/services
Los Angeles District
GIS:https://tiles.arcgis.com/tiles/wyJygLsBd4XEYUkl/arcgis/rest/services
Los Angeles District
GIS: https://services5.arcgis.com/NCw7W7TLyX1lQly1/ArcGIS/rest/services
Norfolk District
GIS: https://tiles.arcgis.com/tiles/NCw7W7TLyX1lQly1/arcgis/rest/services
Norfolk District
GIS: https://services7.arcgis.com/zv5PbHd04c1UNAiH/ArcGIS/rest/services
Rock Island District
GIS: https://tiles.arcgis.com/tiles/zv5PbHd04c1UNAiH/arcgis/rest/services

## Page 19

Rock Island District
GIS: https://maps.fodis.net/server/rest/services
Sacramento District?

GIS: https://services5.arcgis.com/fIxWxKCksQz2Hltv/ArcGIS/rest/services
Sacramento District?
* DOD - National Geospatial-Intelligence Agency
Geonames Website: https://geonames.nga.mil/geonames/GNSHome/welcome.html
GIS: https://geonames.nga.mil/geon-ags/rest/services
8-13-2023 No tiled data
GIS: https://services1.arcgis.com/cc7nIINtrZ67dyVJ/arcgis/rest/services
Includes tornado points (with photo links) and paths
GIS: https://tiles.arcgis.com/tiles/cc7nIINtrZ67dyVJ/arcgis/rest/services
GIS: https://geonames.nga.mil/geon-ags/rest/services
* DOD - Arlington National Cemetery
Website: https://www.arlingtoncemetery.mil
GIS: https://ancexplorer.army.mil/arcgis/rest/services
Table of contents disabled
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Department of Education
* DOEd - Data and Statistics
Website: https://www.ed.gov/data
GIS: https://nces.ed.gov/arcgis/rest/services
GIS: https://nces.ed.gov/opengis/rest/services
8-13-2023 No tiled data
Department of Energy (DOE)
* DOE - Bonneville Power Administration
Website: https://www.bpa.gov
GIS: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Iz3chmSt4P7oOoZy/arcgis/rest/services
* DOE -  National Energy Technology Laboratory
Website: https://www.netl.doe.gov
GIS: https://prod.arcgis.netl.doe.gov/server/rest/services

* DOE - Legacy Management
Website: https://www.energy.gov/lm/office-legacy-management
GIS: https://gems.lm.doe.gov/arcgis/rest/services
8-13-2023 No tiled data

## Page 20

* DOE - National Renewable Energy Laboratory
Website: https://www.nrel.gov
GIS: _ttp://gisatnrel.nrel.gov/ArcGIS/rest/services
dead link 3
* DOE - Argonne National Laboratory
Website: https://www.anl.gov
GIS: https://disgeoportal.egs.anl.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: _ttps://evsgeoportal.evs.anl.gov/arcgis/rest/services
dead link 2
* DOE - Pacific Northwest National Laboratory
Website: https://www.pnnl.gov
GIS: _ttps://apps.pnnl.gov/mapserver/rest/services
dead link 2
* DOE - Energy Information Administration (EIA)
Website: https://www.eia.gov
GIS: https://services.arcgis.com/jDGuO8tYggdCCnUJ/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/jDGuO8tYggdCCnUJ/arcgis/rest/services
Lots of energy related layers
GIS: https://services7.arcgis.com/FGr1D95XCGALKXqM/ArcGIS/rest/services
Table of contents hidden by javascript
GIS: https://tiles.arcgis.com/tiles/FGr1D95XCGALKXqM/arcgis/rest/services

2-2-2026: Used to have info on gas and oil wells.  Vector tiles.  Now there is no
data at this address.
Department of Health and Human Services (HHS)
* HHS - Office of the Inspector General
Website: https://oig.hhs.gov
GIS: https://services6.arcgis.com/lDz78yO9NI8SoTkW/arcgis/rest/services
GIS: https://services.arcgis.com/iW55qaI4k5NTm9RB/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/iW55qaI4k5NTm9RB/arcgis/rest/services
* HHS - Administration for Strategic Preparedness and Response (ASPR)
Website: https://aspr.hhs.gov/Pages/Home.aspx
GIS: https://services2.arcgis.com/ZQ4jTQn6k7VPXEwO/arcgis/rest/services
* HHS - Centers for Disease Control and Prevention (CDC)
Website: https://www.cdc.gov
GIS: https://onemap.cdc.gov/onemapservices/rest/services
* HHS - Health Resources and Services Administration (HRSA)
Website: https://www.hrsa.gov/
GIS: https://gisportal.hrsa.gov/server/rest/services
2-21-2023 no tiled data

## Page 21

* HHS -  Indian Health Service
Website: https://www.ihs.gov/
GIS: https://maps.ihs.gov/server/rest/services
2-21-2023 no tiled data
* HHS -  Various
GIS: https://services5.arcgis.com/qWZ7BaZXaP5isnfT/arcgis/rest/services
Department of Homeland Security (DHS)
* DHS - Federal Emergency Management Agency (FEMA)
GIS: https://hazards.fema.gov/arcgis/rest/services
Includes ID for FIRM panels (related to flood risk)
Flood related:  /public/NFHL/MapServer
2-21-2023 no tiled data
River mile markers
Levees
GIS: https://disasters.geoplatform.gov/image/rest/services
GIS: _ttps://hazards.geoplatform.gov/server/rest/services
dead link 2
Dead link detected 6-3-2025
GIS: https://gis.fema.gov/arcgis/rest/services/
2-21-2023 no tiled data
Lots of interesting weather data
/Partner/Fire_List_Current/MapServer
Wildland fires
GIS: https://services.arcgis.com/XG15cJAlne2vxtgt/ArcGIS/rest/services
Server might be slow.  Scans ‘timed out’
Civil air patrol photos: Image_Points_view/FeatureServer/1
GIS: https://tiles.arcgis.com/tiles/XG15cJAlne2vxtgt/arcgis/rest/services
* DHS - Various layers
GIS: https://gii.dhs.gov/host/rest/services
2-21-2023 no tiled data
Department of Housing and Urban Development (HUD)
* HUD - Geospatial Data Storefront
GIS:  https://egis.hud.gov/arcgis/rest/services
2-21-2023 no tiled data

* HUD -  Location Affordability Portal
Website: https://www.locationaffordability.info
GIS: https://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services
Department of the Interior (DOI)

## Page 22

Land BLM owns
lands/BLM_Natl_SMA_Cached_BLM_Only/MapServer/2
Roads and trails
transportation/BLM_Natl_GTLF_Public_Display
* DOI - Bureau of Land Management
Website: https://www.blm.gov/
GIS: https://gis.blm.gov/arcgis/rest/services
For key recreation layers see box below
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.blm.gov/akarcgis/rest/services
Alaska
GIS: https://gis.blm.gov/azarcgis/rest/services
Arizona
GIS: https://gis.blm.gov/caarcgis/rest/services
California
GIS: https://gis.blm.gov/coarcgis/rest/services
Colorado
GIS: https://gis.blm.gov/idarcgis/rest/services
Idaho
GIS: https://gis.blm.gov/orarcgis/rest/services
Oregon
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.blm.gov/mtarcgis/rest/services
Montana
GIS: https://gis.blm.gov/nvarcgis/rest/services
Nevada
GIS: https://gis.blm.gov/nmarcgis/rest/services
New Mexico
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.blm.gov/utarcgis/rest/services
Utah
GIS: https://gis.blm.gov/wyarcgis/rest/services
Wyoming
GIS: _ttps://eplanspatial.blm.gov/arcgis/rest/services
dead link 2
GIS: https://fire.ak.blm.gov/arcgis/rest/services
Includes Alaska wildland fires
Lightning strikes, etc
2-21-2023 no tiled data
GIS: _ttps://landscape.blm.gov/nwparcgis/rest/services
dead link 2
GIS: _ttps://landscape.blm.gov/cyrarcgis/rest/services
dead link 2
GIS: _ttps://landscape.blm.gov/nosarcgis/rest/services
dead link 2
GIS: https://services1.arcgis.com/KbxwQRRfWyEYLgp4/arcgis/rest/services
Lots of interesting data
GIS: https://tiles.arcgis.com/tiles/KbxwQRRfWyEYLgp4/arcgis/rest/services
Here is a GISsurfer map that covers all BLM land and has many recreation overlays
that you can turn on/off and restack.  To get the most benefit from the map please read the
“Map tips”.  See link in upper left corner of the map.
https://mappingsupport.com/p2/gissurfer.php?center=42.682309,-118.706245&zoom=12
&basemap=USA_basemap&overlay=BLM_land_shaded,BLM_land_outline,State_bound
ary,BLM_recreation_facility,BLM-G_trail_not_assessed,BLM_trail_not_assessed&data=
https://mappingsupport.com/p2/recreation/BLM_recreation.txt

## Page 23

* DOI - Bureau of Ocean Energy Management
Website: https://www.boem.gov/

GIS: https://gis.boem.gov/arcgis/rest/services
Above server produces an unusual message.
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://geoseas.geoplatform.gov/hosting/rest/services
GIS: https://geoseas.geoplatform.gov/image/rest/services
GIS: https://services5.arcgis.com/g7OtfotLzNoMMSUp/ArcGIS/rest/services
Lots of oil/gas data
GIS: https://tiles.arcgis.com/tiles/g7OtfotLzNoMMSUp/arcgis/rest/services
GIS: https://services7.arcgis.com/G5Ma95RzqJRPKsWL/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/G5Ma95RzqJRPKsWL/arcgis/rest/services
* DOI - Bureau of Reclamation
Website: https://www.usbr.gov
GIS: https://geo.usbr.gov/server/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
* DOI - Fish and Wildlife Service
Website: https://www.fws.gov
Website: https://fws.maps.arcgis.com/home/index.html
Website: https://gis-fws.opendata.arcgis.com
GIS: _ttps://www.fws.gov/wetlandsmapservice/rest/services
dead link 2
Dead link detected 9-30-2025
2-22-2023 no tiled data
GIS: _ttps://ecos.fws.gov/arcgis/rest/services
dead link 2
Dead link detected 3-4-2025
Environmental Conservation Online System (ECOS)
The Environmental Conservation Online System (ECOS) is a gateway web site
that provides access to data systems in the U.S. Fish and Wildlife Service
(Service) and other government data sources. This central point of access assists
Service personnel in managing data and information, and it provides public access
to information from numerous Service databases.
GIS: _ttps://ecos.fws.gov/rest/services
dead link 2
Dead link detected 10-28-2025
GIS: _ttps://criticalhabitat.fws.gov/arcgis/rest/services
dead link 2
Dead link detected 3-4-2025
GIS: _ttps://criticalhabitat.fws.gov/rest/services
dead link 2
Dead link detected 3-4-2025
GIS: https://fwsprimary.wim.usgs.gov/server/rest/services
GIS: https://gis1.wim.usgs.gov/server/rest/services
GIS: https://fwspublicservices.wim.usgs.gov/wetlandsmapservice/rest/services
GIS: https://cbrsgis.wim.usgs.gov/arcgis/rest/services  Coastal Barrier Resources System
8-13-2023 no tiled data
GIS: https://services.arcgis.com/QVENGdaPbd4LUkLV/ArcGIS/rest/services
Includes FWS critial habitat:  USFWS_Critical_Habitat

## Page 24

GIS: https://tiles.arcgis.com/tiles/QVENGdaPbd4LUkLV/arcgis/rest/services
* DOI - Bureau of Indian Affairs
Website: https://www.bia.gov
Data portal: https://opendata-1-bia-geospatial.hub.arcgis.com
GIS: https://biamaps.geoplatform.gov/server/rest/services
8-13-2023 no tiled data
GIS: https://services1.arcgis.com/UxqqIfhng71wUT9x/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/UxqqIfhng71wUT9x/arcgis/rest/services
* DOI - National Park Service (NPS)
Website: https://www.nps.gov/index.htm
Website related to GIS: https://www.nps.gov/orgs/1581/index.htm
GIS: https://mapservices.nps.gov/arcgis/rest/services

2-22-2023 no tiled data.
For the main recreation layers look under NationalDatasets
GIS: _ttps://mobilegis.nps.gov/arcgis/rest/services
dead link 2
2-22-2023 no tiled data.
GIS: https://services1.arcgis.com/fBc8EJBxQRMcHlei/ArcGIS/rest/services
Many layers for specific parks using the 4 character park ID
GIS: https://tiles.arcgis.com/tiles/fBc8EJBxQRMcHlei/arcgis/rest/services
GIS: https://services.arcgis.com/EeCmkqXss9GYEKIZ/ArcGIS/rest/services
Includes Ice Age National Scenic Trail
GIS: https://services2.arcgis.com/UfGVyqUm4GHa2zrj/ArcGIS/rest/services
Includes North Country National Scenic Trail
Here is a webpage that contains a GISsurfer map link for each national park.  Each
map has a  “Map tips” link in the upper left corner with the map legend and more
information.
https://mappingsupport.com/p2/gissurfer-national-park-gis-trail-maps.html
* DOI - Integrated Resource Management Applications
Website: https://irmaservices.nps.gov/
GIS: https://irmaservices.nps.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
* DOI - Office of Surface Mining Reclamation and Enforcement (OSMRE)
Website: https://www.osmre.gov/
GIS: https://geoservices.osmre.gov/arcgis/rest/services
2-22-2023 no tiled data
DOI - US Geological Survey (USGS)
*
USGS - The national map
Website:
https://www.usgs.gov/core-science-systems/national-geospatial-program/n
ational-map
National map themes: https://apps.nationalmap.gov/services/

## Page 25

The USGS National Digital Trails program is collecting authoritative trail
data and hosting it in a single GIS layer on the above server at
USGSTrails/MapServer.  This includes  federal, state and local trail data.
Since dynamic layers are supported GISsurfer can restyle the data. No, they do
not have data on every trail, but they sure have a lot.
GIS: https://basemap.nationalmap.gov/arcgis/rest/services
Includes USTopo basemap
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://index.nationalmap.gov/arcgis/rest/services
2-22-2023 no tiled data
/USTopoAvailability/MapServer        Layer 3 includes attribute data that lets you
download the 7.5 minute vector topo map including data outside neatline.
GIS: https://partnerships.nationalmap.gov/arcgis/rest/services
2-22-2023 no tiled data
GIS: https://hydro.nationalmap.gov/arcgis/rest/services
2-25-2023 no tiled data
GIS: https://hydro-wfs.nationalmap.gov/arcgis/rest/services
GIS: https://hydrowfs.nationalmap.gov/arcgis/rest/services
GIS: https://3dhp.nationalmap.gov/arcgis/rest/services
3D National Hydrography Program (3DHP)
GIS: https://carto.nationalmap.gov/arcgis/rest/services
2-25-2023 no tiled data

GIS: https://cartowfs.nationalmap.gov/arcgis/rest/services
2-25-2023 no tiled data
Same data as prior address??

GIS: https://carto-wfs.nationalmap.gov/arcgis/rest/services
GIS: _ttps://certmapper.cr.usgs.gov/arcgis/rest/services
dead link 2
Dead link detected 6-4-2025
GIS: _ttps://certmapper.cr.usgs.gov/server/rest/services
dead link 2
Dead link detected 6-4-2025
GIS: https://elevation.nationalmap.gov/arcgis/rest/services
2-25-2023 no tiled data
GIS: https://imagery.nationalmap.gov/arcgis/rest/services
Includes NAIP and NAIPPlus
2-25-2023 no tiled data
GIS: https://eerscmap.usgs.gov/arcgis/rest/services
wind turbines: /uswtdb/uswtdbDyn/MapServer
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: _ttps://co2public.er.usgs.gov/arcgis/rest/services
dead link 2
Dead link detected 4-29-2025
Includes data about CO2 Storage
GIS: https://nimbus.cr.usgs.gov/arcgis/rest/services

## Page 26

Latitude longitude lines with dynamic layers   Reference/LatLon/MapServer
2-25-2023 no tiled data
Here are two non-government data sources that are also used on the national map
GIS: https://services.arcgisonline.com/arcgis/rest/services/USA_Topo_Maps/MapServer
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS:
_ttps://maps1.arcgisonline.com/arcgis/rest/services/NGA_US_National_Grid/Map
Server
dead link 2
U.S. National Grid (USNG).
2-25-2023 no tiled data
*
USGS - Coastal and Marine Geology Program
GIS: _ttps://coastalmap.marine.usgs.gov/cmgp/rest/services
dead link 2
*
USGS - Land Treatments Digital Library
Website:
https://www.usgs.gov/centers/forest-and-rangeland-ecosystem-science-cen
ter/science/land-treatment-digital-library
GIS: _ttps://srfs.wr.usgs.gov/arcgis/rest/services/LTDL_Tool
dead link 2
*
USGS - Snake River Field Station
Website:
https://www.usgs.gov/centers/forest-and-rangeland-ecosystem-science-cen
ter/fresc-snake-river-field-station
GIS: _ttps://srfs.wr.usgs.gov/arcgis/rest/services
dead link 2
*
USGS - Earthquake and landslide
Website: https://earthquake.usgs.gov/
Website: https://landslides.usgs.gov/
GIS: https://earthquake.usgs.gov/arcgis/rest/services
The ls folder has data showing the risk of  debris flow following wildland fire
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
*
USGS - Wildland fire
GIS: _ttps://wildfire.cr.usgs.gov/arcgis/rest/services
dead link 2
2-25-2023 no tiled data
GIS: _ttps://rmgsc.cr.usgs.gov/arcgis/rest/services
dead link 2
dead link detected 3-4-2025
GIS: https://lfps.usgs.gov/arcgis/rest/services
Includes ‘landfire’ data
*
Upper Midwest Environmental Sciences Center
Website: https://www.usgs.gov/centers/upper-midwest-environmental-sciences-center
GIS: https://services.arcgis.com/v01gqwM5QqNysAAi/ArcGIS/rest/services
Includes landslide data and debris flow after wildfire
PADUS data
GIS: https://tiles.arcgis.com/tiles/v01gqwM5QqNysAAi/arcgis/rest/services

## Page 27

*
USGS - Eastern Energy Resources Science Center
GIS: https://eerscmap.usgs.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
*
USGS - LandsatLook
Website: https://landsatlook.usgs.gov/
GIS: _ttps://landlook.usgs.gov/arcgis/rest/services
dead link 2
*
USGS - ScienceBase
Website: https://www.sciencebase.gov/catalog     might be real slow
GIS: _ttps://www.sciencebase.gov/arcgis/rest/services
dead link 2
Dead link detected 10-8-2025
2-22-2023 no tiled data
GIS: _ttps://gis.usgs.gov/sciencebase1/rest/services
dead link 2
Dead link detected 10-8-2025
2-25-2023 no tiled data
GIS: _ttps://gis.usgs.gov/sciencebase2/rest/services
dead link 2
Dead link detected 10-22-2025
2-25-2023 no tiled data
GIS: _ttps://gis.usgs.gov/sciencebase3/rest/services
dead link 2
Dead link detected 10-8-2025
*
USGS - Web Informatics and Mapping (WiM)
Website: https://wim.usgs.gov/#/
GIS: _ttps://gis.wim.usgs.gov/arcgis/rest/services
dead link 2
GIS: https://cbrsgis.wim.usgs.gov/arcgis/rest/services
*
USGS - myUSGS
Website: https://my.usgs.gov/welcome
GIS: _ttps://my.usgs.gov/arcgis/rest/services
dead link 2
2-25-2023 no tiled data
*
USGS - National Geologic Map Database
Website: https://ngmdb.usgs.gov/ngmdb/ngmdb_home.html
GIS: https://ngmdb.usgs.gov/arcgis/rest/services
*
USGS - Astrogeology
Website: https://www.usgs.gov/centers/astrogeology-science-center
GIS: _ttps://webgis2.wr.usgs.gov/ArcGIS/rest/services
dead link 2
GIS: _ttps://webgis3.wr.usgs.gov/ArcGIS/rest/services
dead link 2
*
USGS - Other ArcGIS servers
GIS: https://edcintl.cr.usgs.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis1.usgs.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”

## Page 28

GIS: https://grandcanyon.usgs.gov/server/rest/services
Grand Canyon
2-25-2023 no tiled data
GIS: https://energy.usgs.gov/arcgis/rest/services
GIS: _ttps://stratus.cr.usgs.gov/arcgis/rest/services
dead link 2
GIS: https://umesc-gisdb03.er.usgs.gov/arcgis/rest/services
Department of Justice (DOJ)
GIS: https://esp.usdoj.gov/arcweb/rest/services
GIS: https://services9.arcgis.com/LJKafwRzLHEkKeOL/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/LJKafwRzLHEkKeOL/arcgis/rest/services
* DOJ -  Drug Enforcement Administration
Website: https://www.dea.gov
GIS: https://services9.arcgis.com/lrIcotXs0HKkk8yY/arcgis/rest/services
Department of Labor (DOL)
No GIS servers found
Department of State (DOS)
Website: https://www.state.gov
GIS: https://services6.arcgis.com/R6wlO6UHmSzqm9Vs/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/R6wlO6UHmSzqm9Vs/arcgis/rest/services
Department of Transportation (DOT)
* DOT - Bureau of Transportation Statistics (BTS)
Website:  https://geodata.bts.gov
GIS: https://geo.dot.gov/mapping/rest/services
Table of contents opens but the data requires login credentials.
GIS: https://services.arcgis.com/xOi1kZaI0eWDREZv/ArcGIS/rest/services
Includes all the National Transportation Atlas Database (NTAD) including dams.
NTAD_Congressional_Districts
/NTAD_National_Bridge_Inventory/FeatureServer/0
GIS: https://tiles.arcgis.com/tiles/xOi1kZaI0eWDREZv/arcgis/rest/services
* DOT - Federal Highway Administration - Highway Safety Improvement Program (HSIP)
Website: https://safety.fhwa.dot.gov/hsip
GIS: https://geo.dot.gov/server/rest/services

## Page 29

8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Pipelines
* DOT - Federal Aviation Administration (FAA)
GIS: https://services6.arcgis.com/ssFJjBXIUyZDrSYZ/arcgis/rest/services
UAS_Part_107  has the drone ceiling data
GIS: https://tiles.arcgis.com/tiles/ssFJjBXIUyZDrSYZ/arcgis/rest/services
* DOT - Federal Railroad Administration
Website: https://railroads.dot.gov
GIS: https://fragis.fra.dot.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
* DOT - Various layers
GIS: _ttps://fhfl15gisweb.flhd.fhwa.dot.gov/arcgis/rest/services
dead link 2
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Department of the Treasury

* DOTr - Community Development Financial Institutions Fund
Website: https://www.cdfifund.gov
GIS: https://cimsprodprep.cdfifund.gov/arcgis/rest/services
2-25-2023 no tiled data
Department of Veterans Affairs
Website: https://www.va.gov
GIS: https://services1.arcgis.com/smmmD7AGkh7eJR2a/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/smmmD7AGkh7eJR2a/arcgis/rest/services
Independent Agencies
Environmental Protection Agency (EPA)
* EPA - Environmental Data Gateway (EDG)
Website: https://www.epa.gov/data/environmental-dataset-gateway
GIS: https://edg.epa.gov/arcgis/rest/services
* EPA - EnviroAtlas
Website: https://www.epa.gov/enviroatlas
GIS: https://enviroatlas.epa.gov/arcgis/rest/services
2-26-2023 no tiled data

## Page 30

GIS: https://enviroatlas2.epa.gov/arcgis/rest/services
* EPA - Environmental Justice Screening and Mapping
Website: _ttps://www.epa.gov/ejscreen
dead link 2
Dead link detected 2-5-2025
GIS: _ttps://ejscreen.epa.gov/arcgis/rest/services
dead link 2
Dead link detected 2-5-2025
* EPA - WATERS (Watershed Assessment, Tracking and Environmental Results System)
Website:
https://www.epa.gov/waterdata/waters-watershed-assessment-tracking-env
ironmental-results-system
GIS:
https://watersgeo.epa.gov/ArcGIS/rest/services
2-26-2023 no tiled data
GIS:
https://watersgeo.epa.gov/arcgis/rest/services
2-26-2023 no tiled data
* EPA - Enforcement and Compliance History Online
Website: https://echo.epa.gov
GIS: https://echogeo.epa.gov/arcgis/rest/services
* EPA -  Various layers
GIS: https://geopub.epa.gov/arcgis/rest/services
8-14-2023 No tiled data
GIS: https://gispub.epa.gov/arcgis/rest/services
8-14-2023 No tiled data

GIS: _ttps://gispub4.epa.gov/arcgis/rest/services
dead link 2
GIS: _ttps://gispub6.epa.gov/arcgis/rest/services
dead link 2
GIS: _ttps://gispub10.epa.gov/arcgis/rest/services
dead link 2
GIS: https://geodata.epa.gov/arcgis/rest/services
8-14-2023 No tiled data
GIS: https://map22.epa.gov/arcgis/rest/services
8-14-2023 No tiled data
GIS: https://map23.epa.gov/ArcGIS/rest/services
8-14-2023 No tiled data
GIS: https://map24.epa.gov/ArcGIS/rest/services
8-14-2023 No tiled data
GIS: https://services.arcgis.com/cJ9YHowT8TU7DUyn/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/cJ9YHowT8TU7DUyn/arcgis/rest/services
National Aeronautics and Space Administration (NASA)
* NASA - SERVIR
Website: https://www.servirglobal.net/
GIS: https://gis1.servirglobal.net/arcgis/rest/services
8-14-2023 No tiled data

## Page 31

* NASA - MODIS and VIIRS imagery as ImageServer data:
GIS: https://modis.arcgis.com/arcgis/rest/services
8-14-2023 No tiled data
* NASA - Global Imagery Browse Services (GIBS)
Website:
https://www.earthdata.nasa.gov/engage/open-data-services-software/earthd
ata-developer-portal/gibs-api
GIS:
The GIBS tile data is not hosted on an ArcGIS server.  Instead, these tiles
can be accessed via WMTS plus other tile specifications.
GIS:
https://gis.earthdata.nasa.gov/maphost/rest/services
* NASA - Disaster related
GIS: _ttps://maps.disasters.nasa.gov/ags01/rest/services
dead link 1
8-14-2023 No tiled data
GIS: _ttps://maps.disasters.nasa.gov/ags02/rest/services
dead link 1
8-14-2023 No tiled data
GIS: _ttps://maps.disasters.nasa.gov/ags03/rest/services
dead link 1
8-14-2023 No tiled data
GIS: _ttps://maps.disasters.nasa.gov/ags04/rest/services
dead link 1
8-14-2023 No tiled data
* NASA - Langley Research Center
Website: https://www.nasa.gov/langley
GIS: https://gis.earthdata.nasa.gov/image/rest/services
8-14-2023 No tiled data
Lots of climate related data
* NASA - Center for Climate Simulation
Website: https://www.nccs.nasa.gov
GIS: _ttps://maps.nccs.nasa.gov/server/rest/services
dead link 1
8-14-2023 No tiled data
GIS: _ttps://maps.nccs.nasa.gov/mapping/rest/services
dead link 1
Countries.  Includes layer for country boundaries with dynamic layer support
8-14-2023 No tiled data
GIS: _ttps://maps.nccs.nasa.gov/image01/rest/services
dead link 1
8-14-2023 No tiled data
GIS: _ttps://maps.nccs.nasa.gov/image02/rest/services
dead link 1
8-14-2023 No tiled data
* NASA - Global Precipitation Measurement Mission
Website: https://gpm.nasa.gov/data/sources/ges-disc
GIS: _ttps://arcgis.gesdisc.eosdis.nasa.gov/authoritative/rest/services
dead link 2
* NASA various layers
GIS: _ttps://trek.nasa.gov/arcgis/rest/services
dead link 2
GIS: https://landsat2.arcgis.com/arcgis/rest/services

## Page 32

8-14-2023 No tiled data
GIS: https://landsat3.arcgis.com/arcgis/rest/services
8-14-2023 No tiled data
GIS: https://services7.arcgis.com/WSiUmUhlFx4CtMBB/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/WSiUmUhlFx4CtMBB/arcgis/rest/services
* Federal Communications Commission (FCC)
GIS: https://services.arcgis.com/YnOQrIGdN9JGtBh4/arcgis/rest/services

GIS: https://tiles.arcgis.com/tiles/YnOQrIGdN9JGtBh4/arcgis/rest/services
GIS: https://services8.arcgis.com/peDZJliSvYims39Q/ArcGIS/rest/services
* Social Security Administration
GIS: https://services6.arcgis.com/zFiipv75rloRP5N4/ArcGIS/rest/services
* Tennessee Valley Authority (TVA)
Website: https://www.tva.gov/
GIS: https://services.arcgis.com/w8auYAijfGK1Mydj/arcgis/rest/services

GIS: https://tiles.arcgis.com/tiles/w8auYAijfGK1Mydj/arcgis/rest/services
* U.S. Post Office
GIS: https://gis.usps.com/arcgis/rest/services
Table of contents disabled
EDDM/EDDM_ZIP5/MapServer
The following layers display at different zoom levels
    USPS_ZIP5 (1)
    USPS_ZIP5_15 (2)
    USPS_ZIP5_30 (3)
    USPS_ZIP5_60 (4)
Miscellaneous Federal Related
*
Civil Air Patrol
Website: https://www.gocivilairpatrol.com/
GIS: _ttps://imageryuploader.geoplatform.gov/arcgis/rest/services
dead link 2
8-11-2023 for possible new links see
https://disasters-geoplatform.hub.arcgis.com/pages/civil-air-patrol-cap-browser
*
Federal Geographic Data Committee (FGDC)
GIS: https://geoseas.geoplatform.gov/hosting/rest/services
GIS: https://geoseas.geoplatform.gov/image/rest/services

## Page 33

GIS: _https://inlandwaters.geoplatform.gov/arcgis/rest/services
dead link 1
GIS: _ttps://disasters.geoplatform.gov/arcgis/rest/services
dead link 2
dead link detected 2-5-2025
*
Various layers of federal data
_ttps://maps1.arcgisonline.com/arcgis/rest/services
dead link 2
8-14-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
_ttps://maps2.arcgisonline.com/arcgis/rest/services
dead link 2
8-14-2023 No tiled data
_ttps://maps3.arcgisonline.com/arcgis/rest/services
dead link 2
8-14-2023 No tiled data
_ttps://maps4.arcgisonline.com/arcgis/rest/services
dead link 2
8-14-2023 No tiled data
_ttps://maps5.arcgisonline.com/arcgis/rest/services
dead link 2
Zip codes.  Current?
8-14-2023 No tiled data
_ttps://maps6.arcgisonline.com/arcgis/rest/services
dead link 2
8-14-2023 No tiled data
_ttps://maps7.arcgisonline.com/arcgis/rest/services
dead link 2
8-14-2023 No tiled data
7.
State, Regional, County and City GIS Servers
Alabama State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Alabama Open Data
Website: https://data-algeohub.opendata.arcgis.com
Alabama Department of Conservation and Natural Resources
Website: https://www.outdooralabama.com

GIS: https://conservationgis.alabama.gov/adcnrweb/rest/services
7-30-2023 No tiled data
Alabama Department of Economic and Community Affairs
Website: https://adeca.alabama.gov

GIS: https://services7.arcgis.com/ecupH7bxameyeamw/ArcGIS/rest/services
Alabama Department of Environmental Management
Website: https://adem.alabama.gov
GIS: https://gis.adem.alabama.gov/arcgis/rest/services

7-30-2023 No tiled data
Alabama Department of Transportation

## Page 34

Website: https://www.dot.state.al.us/
GIS: https://aldotgis.dot.state.al.us/pubgis1/rest/services
7-30-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://aldotgis.dot.state.al.us/pubgis2/rest/services
7-30-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://aldotgis.dot.state.al.us/imggis/rest/services
Alabama Emergency Management Agency
Website: https://ema.alabama.gov
GIS: https://services5.arcgis.com/Z9xwByitYQVMAR7n/ArcGIS/rest/services
Alabama Forestry Commission
Website: https://www.forestry.alabama.gov
GIS: https://gis.forestry.alabama.gov/arcgis/rest/services
7-30-2023 No tiled data
Alabama Geological Survey and Oil Gas Board
Website: https://www.gsa.state.al.us/
GIS: https://map.gsa.state.al.us/arcgis/rest/services
7-30-2023 No tiled data
GIS: https://services.arcgis.com/EXOiO4lfloWtTo0V/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/EXOiO4lfloWtTo0V/arcgis/rest/services
Alabama 811
Website: https://al811.com
GIS: https://services9.arcgis.com/jPLsb1VY5p6LJoDX/ArcGIS/rest/services
Alabama various layers
GIS: https://maps.alabama.gov/algogis/rest/services
7-30-2023 No tiled data
GIS: https://services7.arcgis.com/iH8unQljYvyFM6F1/arcgis/rest/services
Flood data
GIS: https://tiles.arcgis.com/tiles/iH8unQljYvyFM6F1/arcgis/rest/services
Flood data
GIS: https://services7.arcgis.com/jF2q3LPxL7PETdYk/arcgis/rest/services
Parcel layers for (all?) counties
GIS: https://tiles.arcgis.com/tiles/jF2q3LPxL7PETdYk/arcgis/rest/services
Alabama Regional
Regional Planning Commission of Greater Birmingham
GIS: https://services1.arcgis.com/WUxqOZ70v5sx9tgs/ArcGIS/rest/services
Alabama County GIS Servers
All counties are listed.  Any showing _______ need to be checked for a GIS server.

## Page 35

Autauga
https://maps.capturecama.com/arcgis/rest/services/Autauga
Baldwin
https://web5.kcsgis.com/kcsgis/rest/services/Baldwin
Baldwin
https://services6.arcgis.com/aROFfSNHbmHPb6wX/ArcGIS/rest/s
ervices
Baldwin
https://tiles.arcgis.com/tiles/aROFfSNHbmHPb6wX/arcgis/rest/ser
vices
Barbour
https://maps.capturecama.com/arcgis/rest/services/Barbour
Bibb
GIS is not ArcGIS
Blount
https://web5.kcsgis.com/kcsgis/rest/services/Blount_Imagery
Bullock
https://web5.kcsgis.com/kcsgis/rest/services/Bullock/Public/MapS
erver
Bullock
https://maps.capturecama.com/arcgis/rest/services/Bullock
Butler
GIS is not ArcGIS
Calhoun
https://gis.calhouncounty.org/arcgis5/rest/services/
Calhoun
https://gis.calhouncounty.org/arcgis6/rest/services/
Chambers
GIS is not ArcGIS
Cherokee
https://web3.kcsgis.com/kcsgis/rest/services/Cherokee
Chilton
GIS is not ArcGIS
Choctaw
GIS is not ArcGIS
Clarke
GIS is not ArcGIS
Clay
__________
Cleburne
https://maps.capturecama.com/arcgis/rest/services/Cleburne
Coffee
They have a GIS but it is not ArcGIS
Colbert
https://al20portal.kcsgis.com/al20server/rest/services/Internal
Conecuh
__________
Coosa
https://maps.capturecama.com/arcgis/rest/services/Coosa
Covington
__________

## Page 36

Crenshaw
__________
Cullman
https://al25portal.kcsgis.com/al25server/rest/services
Dale
__________
Dallas
https://maps.capturecama.com/arcgis/rest/services/Dallas
Dallas
They also have another GIS but it is not ArcGIS
DeKalb
__________
Elmore
https://maps.capturecama.com/arcgis/rest/services/Elmore
Elmore
https://services9.arcgis.com/F8Xig6Pjld0x0gpn/ArcGIS/rest/servic
es
Elmore
https://tiles.arcgis.com/tiles/F8Xig6Pjld0x0gpn/arcgis/rest/services
Escambia
__________
Etowah
https://web3.kcsgis.com/kcsgis/rest/services/Etowah
Fayette
__________
Franklin
https://web5.kcsgis.com/kcsgis/rest/services/Franklin
Geneva
__________
Greene
https://services8.arcgis.com/XI1FxP9uZwSBSNV8/arcgis/rest/serv
ices
Hale
https://maps.capturecama.com/arcgis/rest/services/Hale
Henry
https://maps.capturecama.com/arcgis/rest/services/Henry
Houston
__________
Jackson
https://web3.kcsgis.com/kcsgis/rest/services/Jackson
Jefferson
https://jccgis.jccal.org/server/rest/services
Jefferson
https://services2.arcgis.com/2FZPLYt8NeStZfN0/ArcGIS/rest/serv
ices
Lamar
__________
Lauderdale
https://web5.kcsgis.com/kcsgis/rest/services/Lauderdale
Lawrence
https://web6.kcsgis.com/kcsgis/rest/services/Lawrence

## Page 37

Lee
https://services5.arcgis.com/swomwLs3iGyK80EW/ArcGIS/rest/se
rvices
Limestone
https://gis.limestonecounty-al.gov/kwlsmkfxks/rest/services
Lowndes
__________
Macon
https://maps.capturecama.com/arcgis/rest/services/Macon
Madison
https://maps.madisonal.gov/server/rest/services
Marengo
__________
Marion
__________
Marshall
https://web5.kcsgis.com/kcsgis/rest/services/Marshall
Mobile
https://gis.mobilecountyal.gov/server/rest/services
Mobile
https://maps.capturecama.com/arcgis/rest/services/Mobile
Mobile
https://services2.arcgis.com/dJHAcAx6kccDBtM6/arcgis/rest/servi
ces
Mobile
https://services3.arcgis.com/AcvBA1fcgucsFQvO/ArcGIS/rest/ser
vices
Mobile
https://tiles.arcgis.com/tiles/AcvBA1fcgucsFQvO/arcgis/rest/servic
es
Mobile
https://services5.arcgis.com/iTkvnIp1V0G8Aliu/ArcGIS/rest/servi
ces
Monroe
https://maps.capturecama.com/arcgis/rest/services/Monroe
Montgomery
https://gis.montgomeryal.gov/server/rest/services
Morgan
https://web5.kcsgis.com/kcsgis/rest/services/Morgan/Public/MapS
erver
Perry
__________
Pickens
__________
Pike
They have a GIS but it is not ArcGIS
Randolph
__________
Russell
https://maps.capturecama.com/arcgis/rest/services/Russell

## Page 38

St. Clair
https://map.stclairco.com/arcgis/rest/services
Shelby
https://maps.shelbyal.com/gisserver/rest/services
Sumter
https://maps.capturecama.com/arcgis/rest/services/Sumter
Talladega
https://web5.kcsgis.com/kcsgis/rest/services/Talladega
Talladega
https://web5.kcsgis.com/kcsgis/rest/services/Talladega911
Tallapoosa
__________
Tuscaloosa
https://arcgis.tuscco.com/arcgis5/rest/services
Walker
__________
Washington
__________
Wilcox
https://maps.capturecama.com/arcgis/rest/services/Wilcox
Winston
__________
Alabama City GIS Servers
Alexander City
https://cityworks.alexandercityal.gov/arcgis/rest/services
Alexander City
https://services2.arcgis.com/x0l8bDA5Yc8mkT8g/ArcGIS/rest/ser
vices
Auburn
https://gis.auburnalabama.org/public/rest/services
Auburn
https://services1.arcgis.com/0RjRAvWbkNc5KOKe/arcgis/rest/ser
vices
Auburn
https://tiles.arcgis.com/tiles/0RjRAvWbkNc5KOKe/arcgis/rest/ser
vices
Birmingham
https://gisweb.birminghamal.gov/arcgis/rest/services
Boaz
https://web4.kcsgis.com/kcsgis/rest/services/Boaz_City
Daphne
https://services2.arcgis.com/qPvhx4U7hE1WSehr/arcgis/rest/servi
ces
Water utility
Dothan
https://services.arcgis.com/UXN4FGWBfn79LLPC/arcgis/rest/serv
ices
Escambia
https://arcgis4.roktech.net/arcgis/rest/services/escambia
Eutaw
https://services5.arcgis.com/NiqtQ6s8YDKQVXpM/arcgis/rest/ser
vices

## Page 39

Foley
https://arcgis.cityoffoley.org/server/rest/services
Foley
https://services6.arcgis.com/qnrjUkxpg5QOS71d/ArcGIS/rest/servi
ces
Gadsden
https://coggis.cityofgadsden.com/arcgis/rest/services
Gardendale
See Jefferson County
Huntsville
https://maps.huntsvilleal.gov/server/rest/services
Loxley
Madison
https://madmaps1.madisonal.gov/server/rest/services
Mobile
https://maps.cityofmobile.org/arcgis/rest/services
Montgomery
https://gis.montgomeryal.gov/server/rest/services
Montgomery
https://services7.arcgis.com/xNUwUjOJqYE54USz/ArcGIS/rest/se
rvices
Montgomery
https://tiles.arcgis.com/tiles/xNUwUjOJqYE54USz/arcgis/rest/serv
ices
Mountain Brook
https://services6.arcgis.com/8d73jg7hu4OPnp1F/ArcGIS/rest/servi
ces
Mountain Brook        https://tiles.arcgis.com/tiles/8d73jg7hu4OPnp1F/arcgis/rest/services
Oxford
https://services3.arcgis.com/TNkH2k8w3FQZcXL3/arcgis/rest/ser
vices
Water Works & Sewer Board
Pelham
ArcGIS table of contents not available
Prattville
https://services1.arcgis.com/fWUhmUATXl9W5CJW/ArcGIS/rest
/services
Prattville
https://tiles.arcgis.com/tiles/fWUhmUATXl9W5CJW/arcgis/rest/s
ervices
Robertsdale
_________
Tuscaloosa
https://services1.arcgis.com/DADyRNMb7tdzKmmq/arcgis/rest/se
rvices
Tuscaloosa
https://tiles.arcgis.com/tiles/DADyRNMb7tdzKmmq/arcgis/rest/se
rvices
Alaska State GIS Servers
Parcel lines:  See below

## Page 40

- - -
Alaska State GIS Links
Website: https://dec.alaska.gov/das/gis/links
GIS: https://geoportal.alaska.gov/arcgis/rest/services
GIS: https://geoportal.dggs.dnr.alaska.gov/arcgis/rest/services
Alaska Department of Commerce, Community, and Economic Development
Website: https://www.commerce.alaska.gov/web
GIS: https://maps.commerce.alaska.gov/server/rest/services
7-30-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services2.arcgis.com/0DjevcWawQ1dy3il/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/0DjevcWawQ1dy3il/arcgis/rest/services
Alaska Department of Environmental Conservation
Website: https://dec.alaska.gov/
GIS: https://dec.alaska.gov/arcgis/rest/services
7-30-2023 No tiled data
GIS: https://services.arcgis.com/8MMg7skvEbOESlSM/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/8MMg7skvEbOESlSM/arcgis/rest/services
Alaska Department of Fish and Game
Website: https://www.adfg.alaska.gov
GIS: https://gis.adfg.alaska.gov/mapping/rest/services
7-30-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.adfg.alaska.gov/ags/rest/services
GIS: https://services.arcgis.com/VdkVOAHovLuozJG4/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/VdkVOAHovLuozJG4/arcgis/rest/services
Alaska Department of Health and Social Services
Website: https://dhss.alaska.gov/Pages/default.aspx
GIS: https://services1.arcgis.com/WzFsmainVTuD5KML/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/WzFsmainVTuD5KML/arcgis/rest/services
Alaska Department of Natural Resources
Website: https://dnr.alaska.gov
GIS: https://arcgis.dnr.alaska.gov/arcgis/rest/services
7-30-2023 No tiled data
Alaska Department of Transportation and Public Facilities
Website: https://dot.alaska.gov
GIS: https://services.arcgis.com/r4A0V7UzH9fcLVvv/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/r4A0V7UzH9fcLVvv/arcgis/rest/services
GIS: https://services8.arcgis.com/QkuEKmOLMuHLCt8W/arcgis/rest/services
ARROW program
Alaska Division of Forestry

## Page 41

Website: https://forestry.alaska.gov
GIS: See “Other data” below
Alaska Division of Geological and Geophysical Surveys
Website:  https://dggs.alaska.gov
GIS:  https://maps.dggs.alaska.gov/arcgis/rest/services
NOAA - Alaska
Website: https://www.fisheries.noaa.gov/region/alaska
GIS: https://alaskafisheries.noaa.gov/arcgis/rest/services
7-30-2023 No tiled data
GIS: https://alaskafisheries.noaa.gov/mapping/arcgis/rest/services
Other data
GIS:  https://elevation.alaska.gov/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://services1.arcgis.com/7HDiw78fcUiM2BWn/arcgis/rest/services
AK_Parcels   claims to be statewide parcels
GIS: https://tiles.arcgis.com/tiles/7HDiw78fcUiM2BWn/arcgis/rest/services
Alaska Regional
Coastal Villages Region Fund
Website: https://coastalvillages.org
GIS: https://services8.arcgis.com/HXv92wfqHcYIh2KB/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/HXv92wfqHcYIh2KB/arcgis/rest/services
Alaska Borough GIS Servers
Anchorage
https://services2.arcgis.com/Ce3DhLRthdwbHlfF/ArcGIS/rest/services
Anchorage
https://tiles.arcgis.com/tiles/Ce3DhLRthdwbHlfF/arcgis/rest/services
Fairbanks North Star Borough
https://gisportal.fnsb.gov/image/rest/services
https://gisportal.fnsb.gov/referenced/rest/services
Fairbanks North Star Borough
https://services.arcgis.com/f4rR7WnIfGBdVYFd/ar
cgis/rest/services
Kenai Peninsula Borough
https://services.arcgis.com/ba4DH9pIcqkXJVfl/arcg
is/rest/services
Kenai Peninsula Borough
https://tiles.arcgis.com/tiles/ba4DH9pIcqkXJVfl/arc
gis/rest/services
Kodiak Island Borough
https://services1.arcgis.com/R5BNizttyFKxRSMm/
arcgis/rest/services
Kodiak Island Borough
https://tiles.arcgis.com/tiles/R5BNizttyFKxRSMm/a
rcgis/rest/services

## Page 42

Matanuska-Susitna Borough
https://maps.matsugov.us/map/rest/services
Matanuska-Susitna Borough
https://maps.matsugov.us/imagery/rest/services
Table of contents disabled
Matanuska-Susitna Borough
https://services.arcgis.com/fX5IGselyy1TirdY/arcgi
s/rest/services
Matanuska-Susitna Borough
https://tiles.arcgis.com/tiles/fX5IGselyy1TirdY/arcg
is/rest/services
Alaska City, Town, Village, etc GIS Servers
Anchorage
https://www.ancgis.com/arcgis/rest/services
Juneau
https://epv.ci.juneau.ak.us/arcgis/rest/services
Ketchikan
https://services2.arcgis.com/65jtiGuzdaRB5FxF/ArcGIS/rest/servic
es
Ketchikan
           https://tiles.arcgis.com/tiles/65jtiGuzdaRB5FxF/arcgis/rest/services
Sitka
WMS server
Unalaska
https://services7.arcgis.com/XYRnCwZ037YZHYH0/ArcGIS/rest/
services
Unalaska
https://tiles.arcgis.com/tiles/XYRnCwZ037YZHYH0/arcgis/rest/se
rvices
Arizona State GIS Servers
Arizona - AZGEO - Open Data
Website: https://azgeo-open-data-agic.hub.arcgis.com
GIS: https://azgeo.az.gov/arcgis/rest/services
7-30-2023 Tiled data.  Several.  Go to top of this PDF file and search for ‘wmts’.
GIS: https://services6.arcgis.com/clPWQMwZfdWn4MQZ/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/clPWQMwZfdWn4MQZ/arcgis/rest/services
Arizona Department of Environmental Quality
Website: https://azdeq.gov
GIS: https://services.arcgis.com/SzoH1oFM2apCSkx3/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/SzoH1oFM2apCSkx3/arcgis/rest/services
GIS: https://services8.arcgis.com/GiSDmZEW1CS233C3/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/GiSDmZEW1CS233C3/arcgis/rest/services
Arizona Game and Fish Department
Website: https://ert.azgfd.gov
GIS: https://maps.azgfd.com/server/rest/services
Table of contents disabled
GIS: https://services2.arcgis.com/os1CphwIyxBDDUGn/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/os1CphwIyxBDDUGn/arcgis/rest/services

## Page 43

Arizona Department of Health Services
Website: https://www.azdhs.gov
GIS: https://services1.arcgis.com/mpVYz37anSdrK4d8/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/mpVYz37anSdrK4d8/arcgis/rest/services
Arizona Land Department
Website: https://land.az.gov
GIS: _ttp://gis.azland.gov/arcgis/rest/services
dead link 1
7-30-2023 No tiled data
GIS: https://services1.arcgis.com/UpxtrwRYNaXVpkGe/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/UpxtrwRYNaXVpkGe/arcgis/rest/services
Arizona Department of Transportation
Website: https://www.azdot.gov/home
GIS: https://gis.azdot.gov/gis/rest/services
Table of contents disabled
7-30-2023 No tiled data
GIS: https://services1.arcgis.com/XAiBIVuto7zeZj1B/ArcGIS/rest/services
Arizona Department of Water Resources
Website: https://new.azwater.gov/
GIS: https://azwatermaps.azwater.gov/arcgis/rest/services
Parcels by county
/General/Parcels/MapServer
GIS: https://services.arcgis.com/C34zQ7veRS0V1t04/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/C34zQ7veRS0V1t04/arcgis/rest/services
Arizona Geological Survey
Website: https://azgs.arizona.edu
GIS:
https://services1.arcgis.com/Ezk9fcjSUkeadg6u/ArcGIS/rest/services/AZGS_Min
ing_Districts_WFL1/FeatureServer
GIS: https://tiles.arcgis.com/tiles/Ezk9fcjSUkeadg6u/arcgis/rest/services
 Museum of Northern Arizona - Springs Stewardship Institute
Website: https://springsdata.org
GIS: ArcGIS server no longer public
Arizona Independent Redistricting Commission
Website: https://irc.az.gov
GIS: https://services8.arcgis.com/x0l81el0LN7X67MM/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/x0l81el0LN7X67MM/arcgis/rest/services
Various layers
GIS: https://services6.arcgis.com/l7uujk4hHifqabRB/ArcGIS/rest/services
GIS: https://services6.arcgis.com/MrgGZS7oC7drh1E8/ArcGIS/rest/services
Arizona Regional
Central Arizona Project

## Page 44

Website: https://www.cap-az.com
GIS: https://services1.arcgis.com/osPHyJW29upTLmlM/ArcGIS/rest/services
Maricopa Association of Governments
GIS: https://geo.azmag.gov/arcgis/rest/services
7-30-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/MdyCMZnX1raZ7TS3/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/MdyCMZnX1raZ7TS3/arcgis/rest/services
Valley Metro
Website: https://www.valleymetro.org
GIS: https://services2.arcgis.com/2t1927381mhTgWNC/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/2t1927381mhTgWNC/arcgis/rest/services
Arizona County GIS Servers
Cochise
https://services6.arcgis.com/Yxem0VOcqSy8T6TE/arcgis/rest/serv
ices
Cochise
https://tiles.arcgis.com/tiles/Yxem0VOcqSy8T6TE/arcgis/rest/serv
ices
Coconino
https://services1.arcgis.com/Rlvx5g8pKeK13apH/arcgis/rest/servic
es
Coconino
https://tiles.arcgis.com/tiles/Rlvx5g8pKeK13apH/arcgis/rest/servic
es
Gila
https://gis.gilacountyaz.gov/arcgis/rest/services
Greenlee
https://gis.newedgeservices.com/arcgis/rest/services/Greenlee
La Paz
https://gis.lapazcountyaz.org/server/rest/services
Maricopa
https://gis.mcassessor.maricopa.gov/arcgis/rest/services
Maricopa
https://gispreview.maricopa.gov/arcgis/rest/services
Table of contents disabled
Maricopa
https://gis.maricopa.gov/arcgis/rest/services
Table of contents disabled
Maricopa
https://gis.maricopa.gov/imagery/rest/service
Table of contents disabled
Maricopa
https://gis.maricopa.gov/dot/rest/services
Table of contents disabled
Maricopa
https://gis.maricopa.gov/flood/rest/service
Table of contents disabled
Maricopa
https://services.arcgis.com/ykpntM6e3tHvzKRJ/ArcGIS/rest/servic
es
Maricopa
https://tiles.arcgis.com/tiles/ykpntM6e3tHvzKRJ/arcgis/rest/servic
es

## Page 45

Mohave
https://mcgis.mohave.gov/arcgis/rest/services
Mohave
https://services7.arcgis.com/lmLFfg1NId9XINIK/arcgis/rest/servic
es
Navajo
           https://services.arcgis.com/cghC2lEIpJ2TRrs5/ArcGIS/rest/services
Pima
https://gisdata.pima.gov/arcgis1/rest/services
Pima
https://pimamaps.pima.gov/arcgis/rest/services
Pima
https://services2.arcgis.com/UTBp78iglGpbqp1B/ArcGIS/rest/serv
ices
Pima
https://tiles.arcgis.com/tiles/UTBp78iglGpbqp1B/arcgis/rest/servic
es
Pinal
https://gis.pinal.gov/mapping/rest/services
Table of contents disabled
Pinal
https://services6.arcgis.com/0Fva1mQQBFB0bwvx/ArcGIS/rest/se
rvices
Pinal
https://tiles.arcgis.com/tiles/0Fva1mQQBFB0bwvx/arcgis/rest/serv
ices
Santa Cruz
https://mapservices.santacruzcountyaz.gov/wagis01/rest/services
Santa Cruz
https://sccgis.santacruzcountyca.gov/server/rest/services
Santa Cruz
https://services1.arcgis.com/ZrefO5k0ipEAOFhn/ArcGIS/rest/servi
ces
Santa Cruz
https://tiles.arcgis.com/tiles/ZrefO5k0ipEAOFhn/arcgis/rest/servic
es
Yavapai
https://gis.yavapaiaz.gov/arcgis/rest/services
Yavapai
https://services1.arcgis.com/BajuNXbtZNiBKFkx/arcgis/rest/servi
ces
Yavapai
https://tiles.arcgis.com/tiles/BajuNXbtZNiBKFkx/arcgis/rest/servic
es
Yuma
https://arcgis.yumacountyaz.gov/webgis/rest/services
Table of contents disabled
Arizona City, Town, Village, etc GIS Servers
Buckeye
https://maps.buckeyeaz.gov/server/rest/services
Buckeye
https://services1.arcgis.com/sixrqw8b8BHDvWq2/ArcGIS/rest/ser
vices
Buckeye
https://tiles.arcgis.com/tiles/sixrqw8b8BHDvWq2/arcgis/rest/servi
ces
Casa Grande
https://services2.arcgis.com/CXsamt7kqbfZOQwU/ArcGIS/rest/ser
vices

## Page 46

Chandler
https://gis.chandleraz.gov/images/rest/services
Chandler
https://services1.arcgis.com/HIBNcuytta1apnkB/ArcGIS/rest/servi
ces
Chandler
           https://tiles.arcgis.com/tiles/HIBNcuytta1apnkB/arcgis/rest/services
East Peoria
https://services1.arcgis.com/tInG7fYjoF1Sayng/ArcGIS/rest/servic
es
East Peoria
https://tiles.arcgis.com/tiles/tInG7fYjoF1Sayng/arcgis/rest/services
Eloy
https://services7.arcgis.com/VfOwt1fngp5cVBlk/arcgis/rest/servic
es
Flagstaff
https://gis.flagstaffaz.gov/arcgisserver/rest/services
Flagstaff
_ttps://gis.flagstaffaz.gov/imageserver/rest/services      dead link 3
Flagstaff
https://services6.arcgis.com/CNNo1rxoi1NqCYkY/ArcGIS/rest/ser
vices
Flagstaff
https://tiles.arcgis.com/tiles/CNNo1rxoi1NqCYkY/arcgis/rest/servi
ces
Florence
https://arcgis.florenceaz.gov/arcgis/rest/services
Gilbert
https://maps.gilbertaz.gov/arcgis/rest/services
Glendale
https://gismaps.glendaleaz.com/gisserver/rest/services
Glendale
https://services1.arcgis.com/9fVTQQSiODPjLUTa/ArcGIS/rest/ser
vices
Glendale
https://tiles.arcgis.com/tiles/9fVTQQSiODPjLUTa/arcgis/rest/servi
ces
Goodyear
https://maps.goodyearaz.gov/server/rest/services
Maricopa
https://services7.arcgis.com/MlfUGd2UJYefAS7v/ArcGIS/rest/ser
vices
Maricopa
https://tiles.arcgis.com/tiles/MlfUGd2UJYefAS7v/arcgis/rest/servi
ces
Mesa
https://gis.mesaaz.gov/mesaaz/rest/services
Mesa
https://services2.arcgis.com/1gVyYKfYgW5Nxb1V/arcgis/rest/ser
vices
Mesa
https://tiles.arcgis.com/tiles/1gVyYKfYgW5Nxb1V/arcgis/rest/ser
vices
Peoria
https://gis.peoriaaz.gov/arcgis/rest/services
Peoria
https://gis.peoriaaz.gov/hosting/rest/services
Peoria
https://services.arcgis.com/OR7AzQGyqIyUNS4h/arcgis/rest/servi
ces

## Page 47

Peoria
https://tiles.arcgis.com/tiles/OR7AzQGyqIyUNS4h/arcgis/rest/serv
ices

Phoenix
https://maps.phoenix.gov/pub/rest/services

Phoenix
https://maps.phoenix.gov/app/rest/services

Phoenix
https://maps.phoenix.gov/gisfed/rest/services

Phoenix
https://services.arcgis.com/cfKakmeHE95cgeEK/arcgis/rest/servic
es
Scottsdale
https://maps.scottsdaleaz.gov/arcgis/rest/services
Table of contents disabled
Scottsdale
https://services6.arcgis.com/hvDuIN6e7bxkHpdO/ArcGIS/rest/ser
vices
Sierra Vista
https://services6.arcgis.com/qsfT0E2It2u5vqBg/arcgis/rest/services
Sierra Vista
https://tiles.arcgis.com/tiles/qsfT0E2It2u5vqBg/arcgis/rest/services
Surprise
https://services.arcgis.com/rAkRDX3xCHZjZTGW/arcgis/rest/serv
ices
Tempe
https://gis.tempe.gov/arcgis/rest/services
Tempe
https://services.arcgis.com/lQySeXwbBg53XWDi/arcgis/rest/servi
ces
Tempe
https://tiles.arcgis.com/tiles/lQySeXwbBg53XWDi/arcgis/rest/serv
ices
Tucson
https://mapdata.tucsonaz.gov/arcgis/rest/services
Tucson
https://images.tucsonaz.gov/images/rest/services
Tucson
https://cotgisengv.tucsonaz.gov/arcgis/rest/services
Tucson
https://services3.arcgis.com/9coHY2fvuFjG9HQX/arcgis/rest/servi
ces
Tucson
https://tiles.arcgis.com/tiles/9coHY2fvuFjG9HQX/arcgis/rest/servi
ces
Yuma
https://gisimg.ci.yuma.az.us/imagery/rest/services
Arkansas State GIS Servers
Arkansas GIS Office
Website: https://gis.arkansas.gov
GIS: https://gis.arkansas.gov/arcgis/rest/services
Parcel lines:  FEATURESERVICES/Planning_Cadastre/FeatureServer/6
7-30-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://geostor.arkansas.gov/ArcGIS/rest/services
7-30-2023 No tiled data
GIS: http://www.geostor.arkansas.gov/ArcGIS/rest/services
not https

## Page 48

7-30-2023 No tiled data
GIS: http://www.geostor.arkansas.gov/arcgis/rest/services
not https
7-30-2023 No tiled data
GIS: https://services.arcgis.com/PwY9ZuZRDiI5nXUB/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/PwY9ZuZRDiI5nXUB/arcgis/rest/services
Arkansas Division of Emergency Management
Website: https://dps.arkansas.gov/emergency-management/adem
GIS: https://services3.arcgis.com/aHoBXMRQeEIJbBUA/ArcGIS/rest/services
Arkansas Department of Environmental Quality
Website: https://www.adeq.state.ar.us
GIS: https://gis.adeq.state.ar.us/arcgis/rest/services
7-30-2023 No tiled data
Arkansas Department of Transportation
Website: https://www.arkansashighways.com
GIS: https://gis.ardot.gov/hosting/rest/services
7-30-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/7cbqsWqMe170dJ3k/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/7cbqsWqMe170dJ3k/arcgis/rest/services
Arkansas Economic Development Institute
Website: https://youraedi.com/services/geographic-information-services
GIS: https://services2.arcgis.com/wu7u046EJ59dJv3h/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/wu7u046EJ59dJv3h/arcgis/rest/services
Arkansas Game and Fish Commission
Website: https://www.agfc.com/en/
GIS: https://gisec2.agfc.com/arcgis/rest/services
7-30-2023 No tiled data
Arkansas Regional
Northwest Arkansas Regional Planning Commission
Website: https://www.nwarpc.org
slow server
GIS: https://services1.arcgis.com/G4bYaaas92zuKaUR/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/G4bYaaas92zuKaUR/arcgis/rest/services
Western Arkansas Planning and Development District
Website: https://www.wagis.org/default.html
GIS: _ttps://www.wagis.org/arcgis/rest/services
dead link 3
Arkansas County GIS Servers
Ashley
https://www.efsedge.com/arcgis/rest/services/Ashley_County

## Page 49

Benton
https://gis.bentoncountyar.gov/arcgis/rest/services
Table of contents disabled
Benton
https://gis.bentoncountyar.gov/arcgis/rest/services
Table of contents disabled
Bradley
https://www.efsedge.com/arcgis/rest/services/Bradley_County
Calhoun
https://www.efsedge.com/arcgis/rest/services/Calhoun_County
Chicot
https://www.efsedge.com/arcgis/rest/services/Chicot_County
Columbia
https://www.efsedge.com/arcgis/rest/services/Columbia_County
Crawford
Schneider Geospatial - ArcGIS server address is not public
Craighead
https://www.efsedge.com/arcgis/rest/services/Craighead
Crittenden
https://www.efsedge.com/arcgis/rest/services/Crittenden_County
Dallas
https://www.efsedge.com/arcgis/rest/services/Dallas_County
Desha
https://www.efsedge.com/arcgis/rest/services/Desha_County
Drew
https://www.efsedge.com/arcgis/rest/services/Drew_County
Faulkner
https://www.efsedge.com/arcgis/rest/services/Faulkner_County
Franklin
https://gis.aumentumtech.com/arcgis/rest/services
Table of contents disabled
Grant
https://www.efsedge.com/arcgis/rest/services/Grant
Howard
https://www.efsedge.com/arcgis/rest/services/Howard_County
Johnson
https://www.efsedge.com/arcgis/rest/services/Johnson_County
Lee
https://www.efsedge.com/arcgis/rest/services/Lee_County
Logan
https://www.efsedge.com/arcgis/rest/services/Logan_County
Ouachita
https://www.efsedge.com/arcgis/rest/services/Ouachita_County
Phillips
https://services5.arcgis.com/UWXeShqi0BLIyN15/arcgis/rest/servi
ces

## Page 50

Pike
https://www.efsedge.com/arcgis/rest/services/Pike_County
Poinsett
https://www.efsedge.com/arcgis/rest/services/Poinsett_County
Pope
https://www.efsedge.com/arcgis/rest/services/Pope_County
Pulaski
https://www.pagis.org/arcgis/rest/services
Pulaski
https://services1.arcgis.com/wyoDVuo3QgawYe6R/ArcGIS/rest/se
rvices
Pulaski
https://tiles.arcgis.com/tiles/wyoDVuo3QgawYe6R/arcgis/rest/serv
ices
Saline
https://www.efsedge.com/arcgis/rest/services/Saline_County
St. Francis
https://www.efsedge.com/arcgis/rest/services/StFrancis_County
Stone
https://www.efsedge.com/arcgis/rest/services/Stone_County
Union
https://www.efsedge.com/arcgis/rest/services/Union_County

Washington
https://arcserv.co.washington.ar.us/server/rest/services
Yell
https://www.efsedge.com/arcgis/rest/services/Yell_County
Arkansas City, Town, Village, etc GIS Servers
Altus
_ttps://maps.meshekgis.com/arcgis/rest/services/City_of_Altus
dead link 3
Bella Vista
See Benton County
Benton
https://www.efsedge.com/arcgis/rest/services/City_of_Benton
Bentonville
https://gis.bentonvillear.com/arcgis/rest/services
Bentonville
https://services1.arcgis.com/KVEBkgY6kMufuFG2/ArcGIS/rest/se
rvices
Bryant
https://www.efsedge.com/arcgis/rest/services/BryantCity

Cave Springs
__________
Conway
https://data.conwayarkansas.gov/arcgis/rest/services
Conway
https://services2.arcgis.com/CkKrqG1zrwsqR2GK/arcgis/rest/servi
ces
Conway
https://tiles.arcgis.com/tiles/CkKrqG1zrwsqR2GK/arcgis/rest/servi
ces

## Page 51

Decatur
__________
Dillingham
https://services3.arcgis.com/gdLTz4xpy5IxwbSz/ArcGIS/rest/servi
ces
Farmington
__________
Fayetteville
https://maps.fayetteville-ar.gov/server/rest/services
Fayetteville
https://services.arcgis.com/jybuAt4W2nM6OoyQ/arcgis/rest/servic
es
Fayetteville
https://tiles.arcgis.com/tiles/jybuAt4W2nM6OoyQ/arcgis/rest/servi
ces
Fort Smith
https://gis.fortsmithar.gov/arcgis/rest/services
Fort Smith
https://services6.arcgis.com/L7G7UyFFygxBTZ4E/ArcGIS/rest/ser
vices
Garfield
_________
Gentry
_________
Goshen
_________
Gravette
_________
Greenland
_________
Haskell
https://www.efsedge.com/arcgis/rest/services/City_of_Haskell
Highfill
_________
Hot Springs
          https://services1.arcgis.com/lCwVhIwyitVebu0v/arcgis/rest/services
Hot Springs
          https://tiles.arcgis.com/tiles/lCwVhIwyitVebu0v/arcgis/rest/services
Hot Springs Village
https://www.efsedge.com/arcgis/rest/services/HSV
Jonesboro
See Craighead County
Lawrence
https://gis2.lawrenceks.org/arcgis/rest/services
Lincoln
_________

Little Rock
https://maps.littlerock.gov/server/rest/services
Lonoke
https://www.efsedge.com/arcgis/rest/services/Lonoke

## Page 52

Lowell
_________
Pea Ridge
_________
Rogers
https://gis.rogersar.gov/gis/rest/services
Springdale
https://gis2.springdalear.gov/arcgis/rest/services
SSL problem
Stuttgart
___________
Sulphur Springs
________
Texarkana
https://services1.arcgis.com/1qdvoNGNoopZM1s5/ArcGIS/rest/ser
vices
Texarkana
https://tiles.arcgis.com/tiles/1qdvoNGNoopZM1s5/arcgis/rest/servi
ces
Tontitown
________
West Fork
________
California State GIS Servers
California Open Data Portal
Website: https://data.ca.gov/
CDEC sensor ID numbers: https://cdec.water.ca.gov/misc/senslist.html
California - Governor's Office of Emergency Services
Website: https://www.caloes.ca.gov
GIS: https://services.arcgis.com/BLN4oKB0N1YSgvY8/arcgis/rest/services
Lots of good layers.  Wildland fire layers.
Power_Outages_(View)
GIS: https://tiles.arcgis.com/tiles/BLN4oKB0N1YSgvY8/arcgis/rest/services
California - Governor's Office of Planning & Research
Website: https://www.ca.gov/departments/255
GIS: https://services8.arcgis.com/Xr1lDrwMv89PhjD9/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Xr1lDrwMv89PhjD9/arcgis/rest/services
California Department of Conservation
Website: https://www.conservation.ca.gov
GIS: https://gis.conservation.ca.gov/server/rest/services
Includes data on earthquake hazard areas.
7-31-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services2.arcgis.com/zr3KAIbsRSUyARHG/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/zr3KAIbsRSUyARHG/arcgis/rest/services

## Page 53

California Department of Education
Website: https://www.cde.ca.gov
GIS: https://services3.arcgis.com/fdvHcZVgB2QSRNkL/ArcGIS/rest/services
California Department of Finance
Website: https://dof.ca.gov
GIS: https://services8.arcgis.com/d9Au2j3KckAl7VOw/ArcGIS/rest/services
Demographic Research Unit
California Department of Fish and Wildlife
Website: https://www.wildlife.ca.gov/
GIS: https://map.dfg.ca.gov/arcgis/rest/services
7-31-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services2.arcgis.com/Uq9r85Potqm3MfRV/arcgis/rest/services
California Department of Forestry and Fire Protection (Cal Fire)
Website: https://www.fire.ca.gov
GIS: https://egis.fire.ca.gov/arcgis/rest/services
7-30-2023 No tiled data
California Department of Health Care Access and Information
Website: https://hcai.ca.gov
GIS: https://services5.arcgis.com/fMBfBrOnc6OOzh7V/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/fMBfBrOnc6OOzh7V/arcgis/rest/services
California Department of Health Care Services
Website: https://www.dhcs.ca.gov
GIS: https://services7.arcgis.com/7MUwsS9z05YumJRZ/ArcGIS/rest/services
California Department of Housing & Community Development
Website: https://www.hcd.ca.gov
GIS: https://services6.arcgis.com/r537NjmK7zG2SbB9/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/r537NjmK7zG2SbB9/arcgis/rest/services
California Department of Parks and Recreation
Website: https://www.parks.ca.gov
GIS: https://parksportal.parks.ca.gov/server/rest/services
GIS: https://services2.arcgis.com/AhxrK3F6WM8ECvDi/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/AhxrK3F6WM8ECvDi/arcgis/rest/services
California Department of Public Health
Website: https://www.cdph.ca.gov
GIS: https://services2.arcgis.com/wi1yEacfYjH5viqb/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/wi1yEacfYjH5viqb/arcgis/rest/services
California Department of Social Services

## Page 54

Website: https://www.cdss.ca.gov
GIS:  https://services.arcgis.com/XLPEppdz2H9dOiqp/arcgis/rest/services
California Department of Tax and Fee Administration
Website: https://www.cdtfa.ca.gov
GIS: https://services6.arcgis.com/snwvZ3EmaoXJiugR/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/snwvZ3EmaoXJiugR/arcgis/rest/services
California Department of Technology
Website: https://cdt.ca.gov
GIS: https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services
Evacuations: .../CA_EVACUATIONS_PROD/FeatureServer/0
Info:
____s://calema.maps.arcgis.com/home/item.html?id=c0dd2a8779764c26910b83a
7e974ee66#overview
GIS: https://tiles.arcgis.com/tiles/uknczv4rpevve42E/arcgis/rest/services
California Department of Toxic Substances Control
Website: https://www.ca.gov/departments/227
GIS: https://services3.arcgis.com/Oy2JTCD10wkoelxS/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Oy2JTCD10wkoelxS/arcgis/rest/services
California Department of Transportation
Website: https://www.dot.ca.gov/
GIS: https://gisdata.dot.ca.gov/arcgis/rest/services
7-31-2023 No tiled data
GIS: _ttps://odpsvcs.dot.ca.gov/arcgis/rest/services
dead link 1
7-31-2023 No tiled data
GIS: https://caltrans-gis.dot.ca.gov/arcgis/rest/services
GIS: _ttps://svctenvims.dot.ca.gov/dea_dmz/rest/services
dead link 1
California Department of Water Resources
Website: https://water.ca.gov
GIS: https://gis.water.ca.gov/arcgis/rest/services
dams:   Structure/i17_California_Jurisdictional_Dams
For dam info search on: Dams Within Jurisdiction of the State of California
GIS: https://gis.water.ca.gov/arcgisimg/rest/services
Levee flood protection zones: Boundaries/lfpzbam2019/MapServer
7-31-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
California Energy Commission
Website: https://www.energy.ca.gov
Website Open Data: https://cecgis-caenergy.opendata.arcgis.com/
GIS: https://services3.arcgis.com/bWPjFyq029ChCGur/ArcGIS/rest/services
TransmissionLine_CEC (2)
GIS: https://tiles.arcgis.com/tiles/bWPjFyq029ChCGur/arcgis/rest/services

## Page 55

California Air Resources Board
Website: https://ww2.arb.ca.gov
GIS: https://services6.arcgis.com/x7ftScCDR8g2kVFB/ArcGIS/rest/services
California Flood Emergency Response Information Exchange (FERIX)
Website: https://ferix.water.ca.gov/webapp/home.jsp
GIS: https://gispublic.waterboards.ca.gov/portalserver/rest/services
GIS: https://ferix.water.ca.gov/arcgis/rest/services
sensors:  ferix/CDEC_Sensors_Active_2021/MapServer
levees:  ferix/leveevulnerability
7-31-2023 No tiled data
California Natural Resources Agency
Website: https://resources.ca.gov
GIS: https://gis.cnra.ca.gov/arcgis/rest/services
7-31-2023 No tiled data
GIS: https://devegis.fire.ca.gov/arcgis/rest/services
7-31-2023 No tiled data
GIS: https://services8.arcgis.com/JFYbogndXme7ddg8/ArcGIS/rest/services
30x30 project
GIS: https://tiles.arcgis.com/tiles/JFYbogndXme7ddg8/arcgis/rest/services
California Statewide Groundwater Elevation Monitoring (CASGEM)
Website: https://water.ca.gov/Programs/Groundwater-Management
GIS: https://casgemgis.water.ca.gov/arcgis/rest/services
7-31-2023 No tiled data
California Water Resources Control Board
Web site: https://www.waterboards.ca.gov/
GIS: https://gispublic.waterboards.ca.gov/arcgis/rest/services
7-31-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/EDxZDh4HqQ1a9KvA/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/EDxZDh4HqQ1a9KvA/arcgis/rest/services
UC Davis Center for Regional Change
Website: https://interact.regionalchange.ucdavis.edu
GIS: _ttps://interact.regionalchange.ucdavis.edu/arcgis/rest/services
dead link 3
7-31-2023 No tiled data
UC Davis Arboretum & Public Garden
Website: https://arboretum.ucdavis.edu
GIS: https://services2.arcgis.com/1RSE3iajknwvOyGq/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/1RSE3iajknwvOyGq/arcgis/rest/services
UC Agriculture and Natural Resources
Website: https://ucanr.edu

## Page 56

GIS: https://services.arcgis.com/0xnwbwUttaTjns4i/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/0xnwbwUttaTjns4i/arcgis/rest/services
University of California - Santa  Cruz
GIS: https://services3.arcgis.com/21H3muniXm83m5hZ/ArcGIS/rest/services
University of California - Davis
GIS: https://services9.arcgis.com/mt4kvYhNXSa5AqLG/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/mt4kvYhNXSa5AqLG/arcgis/rest/services
University of California - San Francisco
GIS: https://services2.arcgis.com/7QFoBxBgcWaqCg0N/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/7QFoBxBgcWaqCg0N/arcgis/rest/services
California various layers
GIS: https://services.gis.ca.gov/arcgis/rest/services
Transportation/Bottleneck
Parcel lines: Boundaries/UCD_Parcels
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://maps.calagpermits.org/arcgis/rest/services
Parcel lines by county for most counties.
7-31-2023 No tiled data
GIS: https://services1.arcgis.com/jUJYIo9tSA7EHvfZ/ArcGIS/rest/services
CA_Perimeters_NIFC_FIRIS_public_view/FeatureServer
Palisades fire damage assessment  DINS_2025_Palisades_Public_View
GIS: https://tiles.arcgis.com/tiles/jUJYIo9tSA7EHvfZ/arcgis/rest/services
GIS: https://services1.arcgis.com/PCHfdHz4GlDNAhBb/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/PCHfdHz4GlDNAhBb/arcgis/rest/services
GIS: https://services1.arcgis.com/sTaVXkn06Nqew9yU/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/sTaVXkn06Nqew9yU/arcgis/rest/services
GIS: https://services3.arcgis.com/5aaQCuq3e4GRvkFG/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/5aaQCuq3e4GRvkFG/arcgis/rest/services
GIS: https://services6.arcgis.com/bxsVBCAOuftUsVxD/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/bxsVBCAOuftUsVxD/arcgis/rest/services
GIS: _ttps://services7.arcgis.com/1hXKyJAQgsvzDCOs/arcgis/rest/services    dead link 1
GIS: https://services8.arcgis.com/s7n9cRiugyMCsR0U/ArcGIS/rest/services
Pacific Gas and Electric
Website: https://www.pge.com
GIS: https://services2.arcgis.com/mJaJSax0KPHoCNB6/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/mJaJSax0KPHoCNB6/arcgis/rest/services
Southern California Edison
GIS: https://services5.arcgis.com/z6hI6KRjKHvhNO0r/arcgis/rest/services
California Regional

## Page 57

California Coastal Commission
Website: https://www.coastal.ca.gov/
GIS: https://services9.arcgis.com/wwVnNW92ZHUIr0V0/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/wwVnNW92ZHUIr0V0/arcgis/rest/services
Coachella Valley Association of Governments
Website: https://cvag.org
GIS: https://services9.arcgis.com/CBx4dpJSQTY7NvOy/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/CBx4dpJSQTY7NvOy/arcgis/rest/services
East Bay Regional Park District
Website: https://www.ebparks.org
GIS: https://services2.arcgis.com/jeEP9c9zZoQQwtck/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/jeEP9c9zZoQQwtck/arcgis/rest/services
Fresno Council of Governments
Website: https://www.fresnocog.org
GIS: https://services.arcgis.com/v2YXtBuIb8gr4ywi/arcgis/rest/services
Metropolitan Transportation Commission (Bay area)
Website: https://mtc.ca.gov
GIS: https://services3.arcgis.com/i2dkYWmb4wHvYPda/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/i2dkYWmb4wHvYPda/arcgis/rest/services
Middle Mile Broadband for California
Website: https://broadbandforall.cdt.ca.gov/middle-mile-broadband-initiative
GIS: https://services6.arcgis.com/sAv98EYUZbLCVPW0/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/sAv98EYUZbLCVPW0/arcgis/rest/services
Midpeninsula Regional Open Space District
Website: https://www.openspace.org
GIS: https://services2.arcgis.com/qmhndvC947rDNl6t/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/qmhndvC947rDNl6t/arcgis/rest/services
Sacramento Area Council of Governments
Website: https://www.sacog.org
GIS: https://services6.arcgis.com/YBp5dUuxCMd8W1EI/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/YBp5dUuxCMd8W1EI/arcgis/rest/services
San Diego Association of Governments
Website: https://www.sandag.org
GIS: https://gis.sandag.org/sdgis/rest/services
7-31-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/HG80xaIVT1z1OdO5/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/HG80xaIVT1z1OdO5/arcgis/rest/services

## Page 58

San Francisco Bay Conservation & Development Commission
Website: https://www.bcdc.ca.gov
GIS: https://services2.arcgis.com/4Z9x989NrBVrvFwm/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/4Z9x989NrBVrvFwm/arcgis/rest/services
Santa Clara Valley Open Space Authority
Website: https://www.openspaceauthority.org
GIS: https://services3.arcgis.com/kdBUV7ozB9Xo7h9c/ArcGIS/rest/services
Santa Clara Valley Transportation Authority
Website: https://www.vta.org
GIS: https://services2.arcgis.com/cEcV2eKpmBtlBVpA/arcgis/rest/services
South Coast Air Quality Management District
Website: https://www.aqmd.gov
GIS: https://services2.arcgis.com/I4NVzmfP3kyPvlVg/arcgis/rest/services
Southern California Association of Governments
Website: https://scag.ca.gov
GIS: https://maps.scag.ca.gov/scaggis/rest/services
7-31-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services5.arcgis.com/RrYXaSQEz1h5iDHP/ArcGIS/rest/services
GIS: https://services5.arcgis.com/YzWImMY4GtDcMxOx/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/YzWImMY4GtDcMxOx/arcgis/rest/services
Southern California Coastal Water Research Project
Website: https://www.sccwrp.org
GIS: https://gis.sccwrp.org/arcgis/rest/services
Tahoe Regional Planning Agency
Website: https://www.trpa.gov
GIS: https://services5.arcgis.com/fXXSUzHD5JjcOt1v/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/fXXSUzHD5JjcOt1v/arcgis/rest/services
Yosemite Sequoia Resource Conservation and Development Council
Website: https://www.ysrcandd.org
GIS: https://services.arcgis.com/V1HNkfTHhuLxh68E/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/V1HNkfTHhuLxh68E/arcgis/rest/services
California Water Districts
State Water Resources Control Board
Website: https://www.waterboards.ca.gov
GIS: https://gispublic.waterboards.ca.gov/portalserver/rest/services
GIS: https://services.arcgis.com/Wvy1i2QPQwOxNumH/arcgis/rest/services
Jurupa Community Services District

## Page 59

Website: https://www.jcsd.us
GIS: https://services2.arcgis.com/9Ae9gDD0ADyyTpkP/ArcGIS/rest/services
Lake Hemet Municipal Water District
Website: https://www.lhmwd.org
GIS: https://services6.arcgis.com/2IVGUx0w84YRGgW6/arcgis/rest/services
Northstar Community Services District
Website: https://www.northstarcsd.org
GIS: https://services.arcgis.com/ku0YuX4TBkysFFVy/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/ku0YuX4TBkysFFVy/arcgis/rest/services
St. Marys Metropolitan Commission
Website: https://www.metcom.org
GIS: https://services3.arcgis.com/oMyOi7kozGXYXHPr/arcgis/rest/services
Santa Clara Valley Water District
Website: https://www.valleywater.org/
GIS: https://gis.valleywater.org/arcgis/rest/services
Table of contents disabled
GIS: https://services2.arcgis.com/9KdAx8qBsHiGXOEw/ArcGIS/rest/services
Sierra Water Workgroup
Website: https://swwg.maps.arcgis.com/home/index.html
GIS: https://services6.arcgis.com/MtSzpOZ2FMytnchL/arcgis/rest/services
Vallecitos Water District
Website: https://www.vwd.org
GIS: https://services6.arcgis.com/PplY6LYxgLzp5J0L/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/PplY6LYxgLzp5J0L/arcgis/rest/services
West Basin Municipal Water District
Website: https://www.westbasin.org
GIS: https://newgis.westbasin.org/arcgis/rest/services
GIS: https://services3.arcgis.com/mAmgbZIF7tJbqGmL/arcgis/rest/services
West Valley Water District
Website: https://wvwd.org
GIS: _ttps://www.gis.wvwd.org/arcgis/rest/services
dead link 3
Western Municipal Water District
Website: https://westernwaterca.gov
GIS: https://services1.arcgis.com/M0t6YWjmKfNetUqN/ArcGIS/rest/services
California Utility District
Truckee Donner Public Utility District (PUD)
_ttps://web.tdpud.org/tdpudmaps/rest/services
dead link 3

## Page 60

California County GIS Servers
All counties are listed and have been checked for GIS
Alameda
https://services5.arcgis.com/ROBnTHSNjoZ2Wm1P/ArcGIS/rest/s
ervices
Alameda
https://tiles.arcgis.com/tiles/ROBnTHSNjoZ2Wm1P/arcgis/rest/ser
vices
Alpine
https://services1.arcgis.com/9z9tEfqo0TExR9C8/arcgis/rest/servic
es
Alpine
          https://tiles.arcgis.com/tiles/9z9tEfqo0TExR9C8/arcgis/rest/services
Amador
https://services8.arcgis.com/uzb563eo87NppqyM/ArcGIS/rest/serv
ices
Amador Fire Safe Council
Amador
https://services9.arcgis.com/Z65sx307Hunxj6eq/ArcGIS/rest/servi
ces
Amador
           https://tiles.arcgis.com/tiles/Z65sx307Hunxj6eq/arcgis/rest/services
Butte
http://gis.buttecounty.net/arcgis/rest/services
not https
Butte
https://gisportal.buttecounty.net/arcgis/rest/services
Butte
          https://services.arcgis.com/3t3QfTXFRFX44zo8/arcgis/rest/services
Butte

https://tiles.arcgis.com/tiles/3t3QfTXFRFX44zo8/arcgis/rest/servic
es
Calaveras
https://gisportal.co.calaveras.ca.us/server/rest/services
SSL problem
Calaveras
https://services6.arcgis.com/rNuo8nvF17v2dPFX/ArcGIS/rest/serv
ices
Calaveras
https://tiles.arcgis.com/tiles/rNuo8nvF17v2dPFX/arcgis/rest/servic
es
Colusa
https://services5.arcgis.com/RHVBVx0fVmUtvfJV/arcgis/rest/serv
ices
Contra Costa
https://ccmap.cccounty.us/arcgis/rest/services
Contra Costa
https://gis.cccounty.us/arcgis/rest/services
Del Norte
https://services3.arcgis.com/IkUDY1vRIUWiVvcz/arcgis/rest/servi
ces
El Dorado
https://see-eldorado.edcgov.us/arcgis/rest/services
El Dorado
https://services.arcgis.com/UHg8l1wC48WQyDSO/arcgis/rest/serv
ices
Foster City
https://bart.fostercity.org/arcgis/rest/services

## Page 61

Foster City
https://services7.arcgis.com/CYn8XGt0yVlPlS5X/ArcGIS/rest/ser
vices
Foster City
https://tiles.arcgis.com/tiles/CYn8XGt0yVlPlS5X/arcgis/rest/servi
ces
Fresno
https://gisprod10.co.fresno.ca.us/server/rest/services
Fresno
https://services3.arcgis.com/ibgDyuD2DLBge82s/arcgis/rest/servic
es
Fresno
https://tiles.arcgis.com/tiles/ibgDyuD2DLBge82s/arcgis/rest/servic
es
Glenn
https://services3.arcgis.com/GUHJKBhKMcD5JjTe/arcgis/rest/ser
vices
Glenn
https://tiles.arcgis.com/tiles/GUHJKBhKMcD5JjTe/arcgis/rest/ser
vices
Humboldt
https://webgis.co.humboldt.ca.us/arcgis/rest/services
Table of contents disabled
Humboldt
           https://services7.arcgis.com/xcDZAIhbyblBfhsu/arcgis/rest/services
Imperial
https://services1.arcgis.com/fwUrSNrE506Uxp7v/arcgis/rest/servic
es
Imperial
https://services7.arcgis.com/RomaVqqozKczDNgd/ArcGIS/rest/ser
vices
Inyo
https://gis.inyo.gov/server/rest/services
Inyo
           https://services.arcgis.com/0jRlQ17Qmni5zEMr/arcgis/rest/services
Inyo
https://tiles.arcgis.com/tiles/0jRlQ17Qmni5zEMr/arcgis/rest/servic
es
Kern
https://maps.co.kern.ca.us/arcgis/rest/services
Kern
https://phweb.co.kern.ca.us/arcgis/rest/services
Kings
https://services3.arcgis.com/24gLq1DBBzDfd0cZ/arcgis/rest/servi
ces
Lake
https://gispublic.co.lake.ca.us/server/rest/services
Lassen
3-29-2024 no GIS found
Lathrop
https://gis2.ci.lathrop.ca.us/arcgis/rest/services
Los Angeles
https://arcgis.gis.lacounty.gov/arcgis/rest/services
Los Angeles
https://public.gis.lacounty.gov/public/rest/services
Los Angeles
https://assessor.gis.lacounty.gov/assessor/rest/services
Los Angeles
https://assessor.gis.lacounty.gov/oota/rest/services

## Page 62

Los Angeles
https://dpw.gis.lacounty.gov/dpw/rest/services
includes runoff channel data  sdn/MapServer
Los Angeles
https://rpgis.isd.lacounty.gov/arcgis/rest/services
Dynamic parcels: SmallApps/County_Displacement_Map_2020/MapServer/25
Los Angeles
https://cache.gis.lacounty.gov/cache/rest/services
includes parcels
Los Angeles
https://services.arcgis.com/RmCCgQtiZLDCtblq/arcgis/rest/servic
es      scans ‘timed out’
Los Angeles
https://tiles.arcgis.com/tiles/RmCCgQtiZLDCtblq/arcgis/rest/servi
ces
Los Angeles
https://services1.arcgis.com/tp9wqSVX1AitKgjd/arcgis/rest/servic
es
Los Angeles
https://tiles.arcgis.com/tiles/tp9wqSVX1AitKgjd/arcgis/rest/servic
es
Los Angeles
https://services5.arcgis.com/7nsPwEMP38bSkCjy/ArcGIS/rest/ser
vices
Los Angeles
https://tiles.arcgis.com/tiles/7nsPwEMP38bSkCjy/arcgis/rest/servi
ces
Los Angeles
https://services8.arcgis.com/TNoJFjk1LsD45Juj/ArcGIS/rest/servi
ces
Metro
Los Angeles
           https://tiles.arcgis.com/tiles/TNoJFjk1LsD45Juj/arcgis/rest/services
Metro
Madera
https://gis.maderacounty.com/server/rest/services
Table of contents disabled
Marin
https://gis.marinpublic.com/arcgis/rest/services
Marin
https://gis.marinpublic.com/ArcGIS/rest/services
Marin
https://services6.arcgis.com/T8eS7sop5hLmgRRH/ArcGIS/rest/ser
vices
Marin
https://tiles.arcgis.com/tiles/T8eS7sop5hLmgRRH/arcgis/rest/servi
ces
Mariposa
https://services2.arcgis.com/wEula7SYiezXcdRv/ArcGIS/rest/servi
ces
Mariposa
https://tiles.arcgis.com/tiles/wEula7SYiezXcdRv/arcgis/rest/servic
es
Mendocino
_ttps://gis.mendocinocounty.org/server/rest/services    dead link 1
Merced
https://map.co.merced.ca.us/arcgis/rest/services
SSL problem
Merced
https://maps.countyofmerced.com/server/rest/services
Merced
https://gis.countyofmerced.com/server/rest/services
Merced
          https://services3.arcgis.com/jUftDOfQo1g8oFan/arcgis/rest/services
Merced
https://services6.arcgis.com/LYh3hRvKq5ASgAVM/arcgis/rest/ser
vices

## Page 63

Merced
https://tiles.arcgis.com/tiles/LYh3hRvKq5ASgAVM/arcgis/rest/ser
vices
Modoc
3-29-2024 no GIS found
Mono
https://gis.mono.ca.gov/webgis/rest/services
Mono
https://services.arcgis.com/rQj5FcfuWPllzwY8/arcgis/rest/services
Mono
           https://tiles.arcgis.com/tiles/rQj5FcfuWPllzwY8/arcgis/rest/services
Monterey
https://maps.co.monterey.ca.us/server/rest/services
Monterey
https://services2.arcgis.com/nOGTdfb4kF4dZljH/ArcGIS/rest/servi
ces
Monterey
https://tiles.arcgis.com/tiles/nOGTdfb4kF4dZljH/arcgis/rest/servic
es
Monterey
https://services8.arcgis.com/NEGiWOO2EgrOZAJB/arcgis/rest/ser
vices
Napa
https://gis.napa.ca.gov/arcgis/rest/services
Napa
https://services1.arcgis.com/Ko5rxt00spOfjMqj/ArcGIS/rest/servic
es
Napa
https://tiles.arcgis.com/tiles/Ko5rxt00spOfjMqj/arcgis/rest/services
Nevada
https://maps.nevadacountyca.gov/arcgis/rest/services
Nevada
https://services1.arcgis.com/UvqJJ6GFv4u5BZQj/ArcGIS/rest/serv
ices
Nevada
https://tiles.arcgis.com/tiles/UvqJJ6GFv4u5BZQj/arcgis/rest/servic
es
Orange
https://maps.ocgov.net/arcgis/rest/services
Orange
https://www.ocgis.com/arcpub/rest/services
Orange
https://ocgis.com/arcpub/rest/services
Orange
https://services6.arcgis.com/8gsLpEklUFBwJM9s/arcgis/rest/servi
ces
Orange
https://services.arcgis.com/UXmFoWC7yDHcDN5Q/arcgis/rest/se
rvices
Orange
https://tiles.arcgis.com/tiles/UXmFoWC7yDHcDN5Q/arcgis/rest/s
ervices
Orange
https://services8.arcgis.com/3DyTcAm7GjHPm0D0/ArcGIS/rest/s
ervices
Orange
https://tiles.arcgis.com/tiles/3DyTcAm7GjHPm0D0/arcgis/rest/ser
vices
Palo Alto
https://services6.arcgis.com/evmyRZRrsopdeog7/ArcGIS/rest/servi
ces

## Page 64

Placentia
https://services1.arcgis.com/3CyDafKD7aN8Dr8M/arcgis/rest/serv
ices
Placentia
https://tiles.arcgis.com/tiles/3CyDafKD7aN8Dr8M/arcgis/rest/serv
ices
Placer
https://maps.placer.ca.gov/arcgis/rest/services        SSL problem
Plumas
WMS server
Riverside
https://gis.countyofriverside.us/arcgis_public/rest/services
Riverside
https://content.rcflood.org/arcgis/rest/services
Riverside
https://services1.arcgis.com/pWmBUdSlVpXStHU6/ArcGIS/rest/s
ervices
Riverside
https://tiles.arcgis.com/tiles/pWmBUdSlVpXStHU6/arcgis/rest/ser
vices
Riverside
https://services7.arcgis.com/rzgv2nM13HRIVPf3/ArcGIS/rest/serv
ices
Feeding America Riverside and San Bernardino Counties
Riverside
https://services5.arcgis.com/pJeu9ySWa2KVyGt6/arcgis/rest/servi
ces
Western Riverside County Regional Conservation
Authority
Sacramento
https://mapservices.gis.saccounty.net/arcgis/rest/services
Sacramento
https://services1.arcgis.com/5NARefyPVtAeuJPU/arcgis/rest/servi
ces
Sacramento
https://tiles.arcgis.com/tiles/5NARefyPVtAeuJPU/arcgis/rest/servi
ces
San Benito
https://gisweb.cosb.us/arcgis/rest/services
San Benito
https://services2.arcgis.com/NjMFCzThTMQy3AJa/arcgis/rest/ser
vices
San Benito
https://tiles.arcgis.com/tiles/NjMFCzThTMQy3AJa/arcgis/rest/ser
vices
San Bernardino
https://maps.sbcounty.gov/arcgis/rest/services
San Bernardino
https://maps.sbcounty.gov/img/rest/services
San Bernardino
_ttps://permitrack2.sbcounty.gov/webadaptor/rest/services
dead link 1
San Bernardino         https://services.arcgis.com/aA3snZwJfFkVyDuP/arcgis/rest/services
San Bernardino
https://tiles.arcgis.com/tiles/aA3snZwJfFkVyDuP/arcgis/rest/servic
es
San Bernardino
https://services2.arcgis.com/pXSDhBcg9ZHrVBu8/ArcGIS/rest/se
rvices
County Transportation Authority
San Bernardino
https://tiles.arcgis.com/tiles/pXSDhBcg9ZHrVBu8/arcgis/rest/servi
ces
San Bernardino
https://services7.arcgis.com/40Uis8WPYCPELipr/ArcGIS/rest/ser
vices
Public schools

## Page 65

San Diego
https://gis.sandag.org/sdgis/rest/services
San Diego
https://gis-public.sandiegocounty.gov/arcgis/rest/services
San Diego (Port)
https://gisportal.portofsandiego.org/posdservices/rest/services
San Diego
https://services.arcgis.com/ZAA95z0SYTDJP9yw/ArcGIS/rest/ser
vices
San Diego
https://tiles.arcgis.com/tiles/ZAA95z0SYTDJP9yw/arcgis/rest/serv
ices
San Diego (Port)
https://services2.arcgis.com/kvy1JT30Izby5wgm/ArcGIS/rest/servi
ces
San Francisco
https://services.sfmta.com/arcgis/rest/services
San Francisco
https://sfplanninggis.org/arcgiswa/rest/services
San Francisco
https://maps.sfdpw.org/arcgis/rest/services
San Francisco
https://atlas.sfbg.org/sfbgis/rest/services
San Francisco
https://services.arcgis.com/Zs2aNLFN00jrS4gG/ArcGIS/rest/servic
es
San Francisco
https://tiles.arcgis.com/tiles/Zs2aNLFN00jrS4gG/arcgis/rest/servic
es
San Joaquin
https://sjmap.org/ArcGIS/rest/services
San Joaquin
https://services2.arcgis.com/GQhSReJEO6f7tsvy/ArcGIS/rest/servi
ces
San Joaquin
https://tiles.arcgis.com/tiles/GQhSReJEO6f7tsvy/arcgis/rest/servic
es
San Luis Obispo
https://gis.slocounty.ca.gov/arcgis/rest/services
Table of contents disabled
/Parks/ParksandTrails_APP/MapServer   trail data. Dynamic layers
San Luis Obispo
https://services.arcgis.com/yygmGNIVQrHqSELP/arcgis/rest/servi
ces
San Luis Obispo
https://tiles.arcgis.com/tiles/yygmGNIVQrHqSELP/arcgis/rest/serv
ices
San Luis Obispo
https://services6.arcgis.com/M6e56DqzbdJf20YO/ArcGIS/rest/ser
vices
San Mateo
https://gis.smcgov.org/image/rest/services
San Mateo
https://services.arcgis.com/yq3FgOI44hYHAFVZ/arcgis/rest/servic
es
San Mateo
https://tiles.arcgis.com/tiles/yq3FgOI44hYHAFVZ/arcgis/rest/servi
ces
Santa Ana
https://services1.arcgis.com/u3G8zpmDyNtG4F4e/arcgis/rest/servi
ces
Santa Barbara
https://services8.arcgis.com/s7n9cRiugyMCsR0U/ArcGIS/rest/serv
ices

## Page 66

Santa Barbara
https://services9.arcgis.com/ztLwtMXzJMy86yJE/arcgis/rest/servi
ces
Santa Clara
          https://services.arcgis.com/NkcnS0qk4w2wasOJ/arcgis/rest/services
Santa Clara
https://services1.arcgis.com/4QPaqCJqF1UIaPbN/arcgis/rest/servic
es
Parks and Recreation
Santa Clara
https://tiles.arcgis.com/tiles/4QPaqCJqF1UIaPbN/arcgis/rest/servic
es
Santa Clara
https://services2.arcgis.com/tcv2cMrq63AgvbHF/arcgis/rest/servic
es
Santa Clara
https://tiles.arcgis.com/tiles/tcv2cMrq63AgvbHF/arcgis/rest/servic
es

Santa Clara
https://services2.arcgis.com/RiZWfy7B1r76pKTz/ArcGIS/rest/serv
ices
County Public Health
Santa Clara
https://tiles.arcgis.com/tiles/RiZWfy7B1r76pKTz/arcgis/rest/servic
es
Santa Clara
https://services7.arcgis.com/NRiGh7naXuXQFn3K/arcgis/rest/serv
ices
Santa Clara
https://tiles.arcgis.com/tiles/NRiGh7naXuXQFn3K/arcgis/rest/serv
ices
Santa Clara
https://tiles.arcgis.com/tiles/NkcnS0qk4w2wasOJ/arcgis/rest/servic
es
Santa Cruz
https://gis.santacruzcounty.us/arcserver/rest/services
Santa Cruz
https://sccgis.santacruzcountyca.gov/server/rest/services
Shasta
https://gis.shastacounty.gov/arcgis/rest/services
Shasta
https://services2.arcgis.com/22p1CUjMjjRWlw6O/arcgis/rest/servi
ces
Shasta
https://services7.arcgis.com/6w3Ige9sQWLxrvet/ArcGIS/rest/servi
ces
Western Shasta Resource Conservation District
Sierra
GIS based on Google maps
Siskiyou
https://services3.arcgis.com/JmPiYilyU1x5zuxM/arcgis/rest/servic
es
Solano
https://solanocountygis.com/server/rest/services
Sonoma
https://socogis.sonomacounty.ca.gov/map/rest/services
Sonoma
https://socogis.sonomacounty.ca.gov/image/rest/services
Sonoma
https://maps.sonomawater.org/server/rest/services
Sonoma Water
Sonoma
https://services1.arcgis.com/P5Mv5GY5S66M8Z1Q/ArcGIS/rest/s
ervices

## Page 67

Sonoma
https://tiles.arcgis.com/tiles/P5Mv5GY5S66M8Z1Q/arcgis/rest/ser
vices
Sonoma
           https://services3.arcgis.com/3zBiIfyTuFEqW7Ig/arcgis/rest/services
Sonoma Water
Stanislaus
           https://services.arcgis.com/EeYBJFxLdUojipYa/arcgis/rest/services
Stanislaus
https://tiles.arcgis.com/tiles/EeYBJFxLdUojipYa/arcgis/rest/servic
es
Sutter
https://services6.arcgis.com/rHMUPKWdiOvdGXkw/ArcGIS/rest/
services
Sutter
https://tiles.arcgis.com/tiles/rHMUPKWdiOvdGXkw/arcgis/rest/se
rvices
Tehama
https://nspdcwebsrv.csuchico.edu/nspdcarcsrv01/rest/services/Teha
ma_County
Tehama
          https://services2.arcgis.com/3iNbxbY9zhyxPvde/arcgis/rest/services
Tehama
          https://tiles.arcgis.com/tiles/3iNbxbY9zhyxPvde/arcgis/rest/services
Trinity
          https://services2.arcgis.com/32siQkg0O6da8zFF/arcgis/rest/services
Tulare
https://ihost.tularecounty.ca.gov/ihost/rest/services
Table of contents disabled
Tulare
https://ehost.tularecounty.ca.gov/ehost/rest/services
Table of contents disabled
Tulare
https://services2.arcgis.com/bYBANhmQGwSSLC0l/ArcGIS/rest/
services
Tulare
https://tiles.arcgis.com/tiles/bYBANhmQGwSSLC0l/arcgis/rest/se
rvices
Tuolumne
https://services3.arcgis.com/afQpMaliVrwHS7Ud/ArcGIS/rest/ser
vices
Ventura
https://maps.ventura.org/arcgis/rest/services
Ventura
https://maps.cityofventura.ca.gov/image/rest/services
Ventura
https://services5.arcgis.com/Mn9RcWO3YYOeWUyC/arcgis/rest/s
ervices
Yolo
https://gis.yolocounty.gov/ext/rest/services
Yuba
https://services5.arcgis.com/THtdW72WxYCCmIVL/arcgis/rest/se
rvices
Yucaipa
https://services5.arcgis.com/86gdKBxZf7GIt2Or/arcgis/rest/servic
es

## Page 68

California City, Town, Village, etc GIS Servers
Alameda
https://mobile.alamedaca.gov/arcgis/rest/services
Anaheim
https://gis.anaheim.net/server/rest/services
Anaheim
https://services3.arcgis.com/hPs600I3X0RTaaaq/ArcGIS/rest/servi
ces
Apple Valley
https://services1.arcgis.com/FGe4g7ObpdDb0DvO/ArcGIS/rest/ser
vices
Bakersfield
https://gis.bakersfieldcity.us/webmaps/rest/services
Bakersfield
https://services3.arcgis.com/OKildAHLkXjQX8Ca/ArcGIS/rest/ser
vices
Belmont
https://maps.belmont.gov/arcgis/rest/services
Belmont
https://services2.arcgis.com/yj9NEYUuOce5iBjA/ArcGIS/rest/serv
ices
Belmont
https://tiles.arcgis.com/tiles/yj9NEYUuOce5iBjA/arcgis/rest/servic
es
Benicia
https://services5.arcgis.com/eclQh1J6mUFYeV4m/ArcGIS/rest/ser
vices
Berkeley
https://gis.cityofberkeley.info/arcgis3/rest/services
Berkeley
https://services1.arcgis.com/IYiCpZoSIq9lAxi8/ArcGIS/rest/servic
es
Berkeley
https://tiles.arcgis.com/tiles/IYiCpZoSIq9lAxi8/arcgis/rest/services
Biggs
https://nspdcwebsrv.csuchico.edu/nspdcarcsrv01/rest/services/City
_of_Biggs
Brentwood
https://gis.brentwoodca.gov/arcgis/rest/services
Brentwood
https://services5.arcgis.com/RhahVThhd37dUKIl/ArcGIS/rest/serv
ices
Buena Park
https://services8.arcgis.com/eVbtY4q6KGlXIxQE/arcgis/rest/servi
ces
Buena Park
https://tiles.arcgis.com/tiles/eVbtY4q6KGlXIxQE/arcgis/rest/servi
ces
Burbank
https://mobilegis.burbankca.gov/burgis/rest/services/Planning
Carlsbad
https://gisglobals.carlsbadca.gov/dmzsags/rest/services
Carlsbad
https://gisportals.carlsbadca.gov/arcgis/rest/services

## Page 69

Carlsbad
https://services.arcgis.com/ay9ePoQ2UfAX3U38/arcgis/rest/servic
es
Carlsbad
https://tiles.arcgis.com/tiles/ay9ePoQ2UfAX3U38/arcgis/rest/servi
ces
Cathedral City
https://gissrv.cathedralcity.gov/arcgis/rest/services
Table of contents disabled
Cathedral City
https://services8.arcgis.com/kG6WbW2TR4SvOdBc/arcgis/rest/ser
vices
Chico
https://nspdcwebsrv.csuchico.edu/nspdcarcsrv01/rest/services/City
_of_Chico
Chico
https://services1.arcgis.com/afGgcgqM3caiSYv7/ArcGIS/rest/servi
ces
Chico
          https://tiles.arcgis.com/tiles/afGgcgqM3caiSYv7/arcgis/rest/services
Chula Vista
https://gisweb.chulavistaca.gov/arcgis/rest/services
Table of contents disabled
Chula Vista
https://services2.arcgis.com/2nV1ORz8qFa0iiF2/ArcGIS/rest/servi
ces

Clovis
https://gis.ci.clovis.ca.us/cloviswebgis/rest/services
Concord
https://concordgis.ci.concord.ca.us/public/rest/services
Corning
https://nspdcwebsrv.csuchico.edu/nspdcarcsrv01/rest/services/City
_of_Corning
Corona
https://services3.arcgis.com/4pohxs3ZXJsQTQod/ArcGIS/rest/serv
ices
Corona
https://tiles.arcgis.com/tiles/4pohxs3ZXJsQTQod/arcgis/rest/servic
es
Costa Mesa
https://apps.costamesaca.gov/arcgis/rest/services
Covina
http://maps.covinaca.gov:6080/arcgis/rest/services      not https
Cupertino
https://gis.cupertino.org/cupgis/rest/services
Cupertino
https://services2.arcgis.com/WsCmJmL1F5wsSOiu/ArcGIS/rest/se
rvices
Cupertino
https://tiles.arcgis.com/tiles/WsCmJmL1F5wsSOiu/arcgis/rest/serv
ices
Dublin
https://gis.dublin.ca.gov/arcgis/rest/services
El Cajon
https://docs.cityofelcajon.us/arcgis/rest/services

## Page 70

El Cajon
https://docs.cityofelcajon.us:8552/arcgis/rest/services
El Cajon
https://services2.arcgis.com/sNwJsChyrhgtFVFc/ArcGIS/rest/servi
ces
El Cajon
          https://tiles.arcgis.com/tiles/sNwJsChyrhgtFVFc/arcgis/rest/services
Elk Grove
https://services1.arcgis.com/r6QlyAADl0kfhp1m/arcgis/rest/servic
es
Elk Grove
https://tiles.arcgis.com/tiles/r6QlyAADl0kfhp1m/arcgis/rest/servic
es
Emeryville
https://services3.arcgis.com/ljOdqLVbHpS7dOJQ/arcgis/rest/servi
ces
Emeryville
https://tiles.arcgis.com/tiles/ljOdqLVbHpS7dOJQ/arcgis/rest/servi
ces
Encinitas
https://coemapservices.encinitasca.gov/hypegis/rest/services
Escondido
           https://services2.arcgis.com/eJcVbjTyyZIzZ5Ye/arcgis/rest/services
Escondido
           https://tiles.arcgis.com/tiles/eJcVbjTyyZIzZ5Ye/arcgis/rest/services
Escondido
https://services6.arcgis.com/K8WIEKZd6VPay1c3/ArcGIS/rest/ser
vices
Fairfield
https://gis.fairfield.ca.gov/server/rest/services
Fairfield
https://services1.arcgis.com/A14KNJpxNyBTu19J/ArcGIS/rest/ser
vices
Fairfield
https://tiles.arcgis.com/tiles/A14KNJpxNyBTu19J/arcgis/rest/servi
ces
Fortana
https://services1.arcgis.com/XhE4Nx2bBPScQrhF/ArcGIS/rest/ser
vices
Fortana
https://tiles.arcgis.com/tiles/XhE4Nx2bBPScQrhF/arcgis/rest/servi
ces
Fresno
https://gis4u.fresno.gov/arcgis/rest/services
Fresno
https://services2.arcgis.com/WkBUojyNPhsWOk1W/ArcGIS/rest/s
ervices
Fresno
https://tiles.arcgis.com/tiles/WkBUojyNPhsWOk1W/arcgis/rest/ser
vices
Fullerton
https://gis.cityoffullerton.com/arcgis/rest/services
Fullerton
https://services6.arcgis.com/yMM0eCpNU0fzBaIm/ArcGIS/rest/se
rvices
Gilroy
https://services8.arcgis.com/n7NW5ijV4dJUmrID/ArcGIS/rest/ser
vices

## Page 71

Gilroy
https://tiles.arcgis.com/tiles/n7NW5ijV4dJUmrID/arcgis/rest/servi
ces
Glendale
https://gismap.glendaleca.gov/arcgis/rest/services
Glendora
https://services2.arcgis.com/NQC8oBejgXkIxQpu/ArcGIS/rest/ser
vices
Glendora
https://tiles.arcgis.com/tiles/NQC8oBejgXkIxQpu/arcgis/rest/servi
ces
Goleta
https://services7.arcgis.com/1sU4ryVt4fUb3UBC/ArcGIS/rest/serv
ices
Goleta
https://tiles.arcgis.com/tiles/1sU4ryVt4fUb3UBC/arcgis/rest/servic
es
Hayward
https://maps.hayward-ca.gov/arcgis/rest/services
Hayward
https://services3.arcgis.com/VRO5V8PH7DzSE6AU/arcgis/rest/se
rvices
Hayward
https://tiles.arcgis.com/tiles/VRO5V8PH7DzSE6AU/arcgis/rest/ser
vices
Indian Wells
_________
Inglewood
https://gisweb.cityofinglewood.org/arcgis/rest/services
Irvine
https://gis.cityofirvine.org/arcgis/rest/services
La Habra
https://services9.arcgis.com/wGK8Rz3RqYkFF2a3/ArcGIS/rest/se
rvices
La Mesa
https://platinum.ci.la-mesa.ca.us/arcgis/rest/services
Laguna Niguel
https://services5.arcgis.com/abcxmzumsTdyRGep/ArcGIS/rest/ser
vices
Livermore
https://gisweb.cityoflivermore.net/arcgis/rest/services
Long Beach
https://services6.arcgis.com/yCArG7wGXGyWLqav/arcgis/rest/ser
vices
Los Altos
https://map.losaltosca.gov/arcgis/rest/services
Los Angeles
https://maps.lacity.org/arcgis/rest/services
Los Angeles
https://maps.lacity.org/lahub/rest/services
Los Angeles
http://myladot.lacity.org/arcgis/rest/services
not https
Los Angeles
https://zimas.lacity.org/arcgis/rest/services

## Page 72

Los Angeles
https://services5.arcgis.com/7nsPwEMP38bSkCjy/arcgis/rest/servi
ces
Los Angeles
https://tiles.arcgis.com/tiles/7nsPwEMP38bSkCjy/arcgis/rest/servi
ces
Los Angeles
https://services5.arcgis.com/VAb1qw880ksyBtIL/arcgis/rest/servic
es
Los Angeles
https://tiles.arcgis.com/tiles/VAb1qw880ksyBtIL/arcgis/rest/servic
es
Los Angeles Homeless Services Authority
https://services2.arcgis.com/LMBdfutQCnDGYUyc/ArcGIS/rest/se
rvices
Los Angeles Homeless Services Authority
https://tiles.arcgis.com/tiles/LMBdfutQCnDGYUyc/arcgis/rest/ser
vices
Loyalton
__________
Manteca
https://services5.arcgis.com/apvcu8kifKuj4Ua8/arcgis/rest/services
Manteca
https://tiles.arcgis.com/tiles/apvcu8kifKuj4Ua8/arcgis/rest/services
Manhattan Beach
https://services2.arcgis.com/mP6Ul6JKT9roxmWT/ArcGIS/rest/se
rvices
Menlo Park
https://cmpweb2.menlopark.org/arcgis/rest/services   SSL problem
Menlo Park
https://services7.arcgis.com/uRrQ0O3z2aaiIWYU/arcgis/rest/servi
ces
Menlo Park
https://tiles.arcgis.com/tiles/uRrQ0O3z2aaiIWYU/arcgis/rest/servi
ces
Modesto
https://gis.modestogov.com/hosting/rest/services
Modesto
https://services1.arcgis.com/KN76x1eyfvozZO4M/ArcGIS/rest/ser
vices
Monterey
https://maps.co.monterey.ca.us/server/rest/services
Mountain View
https://maps.mountainview.gov/arcgis/rest/services
Napa
https://services1.arcgis.com/Ko5rxt00spOfjMqj/arcgis/rest/services
Napa
https://tiles.arcgis.com/tiles/Ko5rxt00spOfjMqj/arcgis/rest/services
Newport Beach
https://nbgis.newportbeachca.gov/arcgis/rest/services
Table of contents disabled
Oakland
https://gisapps1.mapoakland.com/oakgis/rest/services
Oakland
https://gismaps.oaklandca.gov/oaklandgis/rest/services

## Page 73

Oakland
          https://services.arcgis.com/9tC74aDHuml0x5Yz/arcgis/rest/services
Oakland
https://tiles.arcgis.com/tiles/9tC74aDHuml0x5Yz/arcgis/rest/servic
es
Oceanside
https://gis.oceansideca.org/gis/rest/services
Table of contents disabled
Oceanside
https://services5.arcgis.com/6UYc3MjsfrxiazMH/ArcGIS/rest/serv
ices
Ontario
https://services3.arcgis.com/hw9dvDTLn0ngkGb1/ArcGIS/rest/ser
vices
Ontario
https://tiles.arcgis.com/tiles/hw9dvDTLn0ngkGb1/arcgis/rest/servi
ces
Orland
https://nspdcwebsrv.csuchico.edu/nspdcarcsrv01/rest/services/City
_of_Orland
Oroville
https://nspdcwebsrv.csuchico.edu/nspdcarcsrv01/rest/services/City
_of_Oroville
Oxnard
https://maps.oxnard.org/arcgis/rest/services
Oxnard
https://services3.arcgis.com/PWexKTkN39Lf339y/ArcGIS/rest/ser
vices
Pacific Grove
https://services6.arcgis.com/fFoVriq6AL2dS2oW/ArcGIS/rest/serv
ices
Palm Desert
https://services2.arcgis.com/i4mrGZu1Isvl0rWt/ArcGIS/rest/servic
es
Palm Desert
https://tiles.arcgis.com/tiles/i4mrGZu1Isvl0rWt/arcgis/rest/services
Palm Springs
https://services.arcgis.com/f48yV21HSEYeCYMI/arcgis/rest/servi
ces
Palm Springs
https://tiles.arcgis.com/tiles/f48yV21HSEYeCYMI/arcgis/rest/serv
ices
Paradise
__________
Pasadena
https://services2.arcgis.com/zNjnZafDYCAJAbN0/arcgis/rest/servi
ces
Pasadena
https://tiles.arcgis.com/tiles/zNjnZafDYCAJAbN0/arcgis/rest/servi
ces
Paso Robles
https://maps.prcity.com/server/rest/services

## Page 74

Perris
https://services7.arcgis.com/LNp9QekVQ7pNnS4Q/arcgis/rest/ser
vices
Pico Rivera
https://services2.arcgis.com/OCysFFatYM3MITwS/ArcGIS/rest/se
rvices
Pittsburg
https://services6.arcgis.com/X3LnFc9yy269fH43/ArcGIS/rest/servi
ces
Pittsburg
https://tiles.arcgis.com/tiles/X3LnFc9yy269fH43/arcgis/rest/servic
es
Pomona
https://gismaps.ci.pomona.ca.us/arcgis/rest/services
Table of contents disabled
Pomona
https://services.arcgis.com/uhcc7qx0gSnzEgBx/arcgis/rest/services
Poway
https://services5.arcgis.com/CjWCkQzgTTO1K3C3/ArcGIS/rest/s
ervices
Poway
https://tiles.arcgis.com/tiles/CjWCkQzgTTO1K3C3/arcgis/rest/ser
vices
Rancho Cordova
https://maps.cityofranchocordova.org/externalarcgis/rest/services
Rancho Cucamonga
https://services1.arcgis.com/bF44QtfoYZDGo7TK/arcgis/rest/servi
ces
Rancho Cucamonga
https://tiles.arcgis.com/tiles/bF44QtfoYZDGo7TK/arcgis/rest/servi
ces
Rancho Palos Verdes  https://gis.rpvca.gov/server/rest/services
Red Bluff
https://nspdcwebsrv.csuchico.edu/nspdcarcsrv01/rest/services/City
_of_RedBluff
Redding
https://services2.arcgis.com/3cLBYFivUvlzVu0H/arcgis/rest/servi
ces
Redlands
https://gis.cityofredlands.org/arcgis/rest/services
Redlands
https://services.arcgis.com/FLM8UAw9y5MmuVTV/arcgis/rest/se
rvices
Redlands
https://tiles.arcgis.com/tiles/FLM8UAw9y5MmuVTV/arcgis/rest/s
ervices
Redondo Beach
https://services6.arcgis.com/4Y3DUWGj4Rq1ajvv/ArcGIS/rest/ser
vices
Redondo Beach
https://tiles.arcgis.com/tiles/4Y3DUWGj4Rq1ajvv/arcgis/rest/servi
ces

## Page 75

Richmond
http://geoweb02.ci.richmond.ca.us/arcgis/rest/services    not https
Riverside
https://services.arcgis.com/Fu2oOWg1Aw7azh41/arcgis/rest/servic
es
Riverside
https://tiles.arcgis.com/tiles/Fu2oOWg1Aw7azh41/arcgis/rest/servi
ces
Rocklin
https://gis.rocklin.ca.us/server/rest/services
Roseville
https://ags.roseville.ca.us/arcgis/rest/services

Sacramento
https://services5.arcgis.com/54falWtcpty3V47Z/ArcGIS/rest/servic
es
Sacramento
https://tiles.arcgis.com/tiles/54falWtcpty3V47Z/arcgis/rest/services
Salinas
https://giswebservices.ci.salinas.ca.us/arcgis/rest/services
San Bruno
https://etrakit.sanbrunocable.com/arcgis/rest/services
SSL problem
San Clemente
https://services3.arcgis.com/x68DaqVkReQwi0Vd/ArcGIS/rest/ser
vices
San Clemente
https://tiles.arcgis.com/tiles/x68DaqVkReQwi0Vd/arcgis/rest/servi
ces
San Diego
https://services.arcgis.com/oxInpRhVIBxlo4pO/arcgis/rest/services
San Diego
https://webmaps.sandiego.gov/arcgis/rest/services
San Francisco
See San Francisco county
San Jose
https://geo.sanjoseca.gov/server/rest/services
San Jose
https://services.arcgis.com/6kSayNlqm3HvsYZ8/arcgis/rest/servic
es
San Leandro
           https://services.arcgis.com/nFaSPZoTjS78xXjw/arcgis/rest/services
San Leandro
https://tiles.arcgis.com/tiles/nFaSPZoTjS78xXjw/arcgis/rest/servic
es
San Rafael
https://services5.arcgis.com/sruoiBDPu8SihcGN/ArcGIS/rest/servi
ces
San Rafael
          https://tiles.arcgis.com/tiles/sruoiBDPu8SihcGN/arcgis/rest/services
San Ramon
https://gis.sanramon.ca.gov/server/rest/services
Santa Clara
https://map.santaclaraca.gov/maps/rest/services

## Page 76

Santa Clara
https://services2.arcgis.com/evwJC31SSJVvbZfF/ArcGIS/rest/serv
ices
Santa Clara
https://tiles.arcgis.com/tiles/evwJC31SSJVvbZfF/arcgis/rest/servic
es
Santa Clarita
https://services6.arcgis.com/VIT2lop0SYQZYGmw/ArcGIS/rest/s
ervices
Santa Clarita
https://maps.santa-clarita.com/arcgis/rest/services
Table of contents disabled
Santa Cruz
https://services5.arcgis.com/RjgxPpXv8MHiv19f/ArcGIS/rest/serv
ices
Santa Maria
https://services2.arcgis.com/aJWfVFc3hKf5GLo2/ArcGIS/rest/ser
vices
Santa Maria
https://tiles.arcgis.com/tiles/aJWfVFc3hKf5GLo2/arcgis/rest/servic
es
Santa Monica
https://gis.santamonica.gov/server/rest/services
Santa Monica
https://services1.arcgis.com/ntb1ZybmOdA9GyKm/arcgis/rest/serv
ices
Santa Monica
https://tiles.arcgis.com/tiles/ntb1ZybmOdA9GyKm/arcgis/rest/serv
ices
Santa Rosa
https://ags2maps.srcity.org/arcgis/rest/services
Santa Rosa
https://services2.arcgis.com/BhTdzxiJkq4oXsPh/ArcGIS/rest/servi
ces
Santa Rosa
           https://tiles.arcgis.com/tiles/BhTdzxiJkq4oXsPh/arcgis/rest/services
San Diego
https://gis.sangis.org/maps/rest/services
San Diego
https://geo.sandag.org/server/rest/services
San Jacinto
https://gis01.city.sanjacintoca.gov/server/rest/services
San Jacinto
https://services6.arcgis.com/GWV58jOyFyDtOPG2/ArcGIS/rest/se
rvices
San Jose
https://geo.sanjoseca.gov/server/rest/services
San Luis Obispo
See San Luis Obispo County
San Marcos
https://services1.arcgis.com/e7Mp0AHrN8K5Kx6X/ArcGIS/rest/s
ervices
Santa Barbara
https://gisportal.santabarbaraca.gov/server1/rest/services
Santa Cruz
https://vwgisportal2.santacruzca.gov/arcgis/rest/services

## Page 77

Santa Monica
https://gis.santamonica.gov/server/rest/services
Sedona
https://services.arcgis.com/pFzi7bOdCZMDuqYB/arcgis/rest/servi
ces
Shasta Lake
https://services9.arcgis.com/jlS3bBZGj44UAM9Z/ArcGIS/rest/ser
vices
Shasta Lake
https://tiles.arcgis.com/tiles/jlS3bBZGj44UAM9Z/arcgis/rest/servi
ces
South Lake Tahoe
https://services2.arcgis.com/gWRYLIS16mKUskSO/arcgis/rest/ser
vices
South Lake Tahoe
https://tiles.arcgis.com/tiles/gWRYLIS16mKUskSO/arcgis/rest/ser
vices
South San Francisco https://services5.arcgis.com/inY93B27l4TSbT7h/ArcGIS/rest/servi
ces
Stockton
_ttps://gisportal.stocktonca.gov/arcgis/rest/services    dead link 1
Temecula
https://gis.temeculaca.gov/arcgis/rest/services
Table of contents disabled
Temecula
https://services3.arcgis.com/IgR6ay8jzuIj7VSF/arcgis/rest/services
Temecula
https://tiles.arcgis.com/tiles/IgR6ay8jzuIj7VSF/arcgis/rest/services
Thousand Oaks
https://gis.toaks.gov/server/rest/services
Tracy
https://maps.cityoftracy.org/server/rest/services
Tracy
https://services1.arcgis.com/jhomrVPNnIcrbVuz/ArcGIS/rest/servi
ces
Truckee
https://services5.arcgis.com/i75zh9vlhYUpqwjr/ArcGIS/rest/servic
es
Truckee
https://tiles.arcgis.com/tiles/i75zh9vlhYUpqwjr/arcgis/rest/services
Tulare
https://maps.tulare.ca.gov/server/rest/services
Vacaville
https://covgis.cityofvacaville.com/externalgis/rest/services
Vacaville
https://services3.arcgis.com/ceLnGXX8aWBjc5h0/ArcGIS/rest/ser
vices
Vallejo
https://services7.arcgis.com/MyTOuXKXZoizwPz9/ArcGIS/rest/se
rvices
Ventura
https://map.cityofventura.net/arcgis/rest/services

## Page 78

Victorville
https://services3.arcgis.com/8Fll56KQwYKXAi7m/ArcGIS/rest/se
rvices
Victorville
https://tiles.arcgis.com/tiles/8Fll56KQwYKXAi7m/arcgis/rest/serv
ices
Visalia
https://services7.arcgis.com/q3SI94vj8qWDxwBr/arcgis/rest/servic
es
Visalia
https://tiles.arcgis.com/tiles/q3SI94vj8qWDxwBr/arcgis/rest/servic
es
Vista
https://services3.arcgis.com/z9GvP47f4vbAXFVB/arcgis/rest/servi
ces
West Sacramento
https://gis.cityofwestsacramento.org/server/rest/services
West Sacramento
https://services5.arcgis.com/rAPK9OWCvAUbTKLM/ArcGIS/rest
/services
Wildomar
https://services6.arcgis.com/kIJQVjhDSsSdR0Xt/ArcGIS/rest/servi
ces
Whittier
https://services6.arcgis.com/ep2P4aOWGVVBct0i/arcgis/rest/servi
ces
Whittier
https://tiles.arcgis.com/tiles/ep2P4aOWGVVBct0i/arcgis/rest/servi
ces
Woodland
https://gis.cityofwoodland.org/cowgis/rest/services
Woodland
https://services5.arcgis.com/QfFJJU2FARaLlY26/ArcGIS/rest/serv
ices
Woodland
https://tiles.arcgis.com/tiles/QfFJJU2FARaLlY26/arcgis/rest/servic
es
Yolo
https://services2.arcgis.com/RETsakmE0SJfZXCd/arcgis/rest/servi
ces
Yolo
https://tiles.arcgis.com/tiles/RETsakmE0SJfZXCd/arcgis/rest/servi
ces
Yorba Linda
https://services9.arcgis.com/2inIk9VHQaVn3Vkf/ArcGIS/rest/serv
ices
Colorado State GIS Servers
Colorado Open Data Catalog
Website: https://data.colorado.gov
Colorado - Office of Information Technology
Website: https://oit.colorado.gov

## Page 79

GIS: https://gis.colorado.gov/oit/rest/services
8-2-2023 No tiled data
  GIS: https://services3.arcgis.com/DgjqnJA1rgO92Soi/arcgis/rest/services
Colorado Department of Public Health and Environment
Website: https://www.colorado.gov/cdphe
GIS: https://www.cohealthmaps.dphe.state.co.us/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://services3.arcgis.com/66aUo8zsujfVXRIT/ArcGIS/rest/services
Colorado Department of Transportation
Website: https://www.codot.gov/
GIS: https://dtdapps.coloradodot.info/arcgis/rest/services
7-31-2023 Has tiled data.  Do a Google search.  site:server_address   "wmts"
GIS: https://services.arcgis.com/yzB9WM8W0BO3Ql7d/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/yzB9WM8W0BO3Ql7d/arcgis/rest/services
Colorado Natural Heritage Program
Website: https://cnhp.colostate.edu
GIS: _ttp://maps.natureserve.org/landscope3/rest/services/CO
dead link 3
7-31-2023 No tiled data
Colorado State University - Colorado Atlas: Parks - Hunting and Fishing
Website: https://ndismaps.nrel.colostate.edu/index.html

GIS: https://ndismaps.nrel.colostate.edu/arcgis/rest/services
7-31-2023 No tiled data
Colorado various layers
GIS: https://gis.colorado.gov/public/rest/services
Parcel lines:  Parcels/All_Public_Parcel_Map_Service/MapServer
Parcel lines:  Entire state?  Parcels/Public_Parcel_Map_Services/MapServer
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services5.arcgis.com/ttNGmDvKQA7oeDQ3/arcgis/rest/services
Trail data: CPWAdminData/FeatureServer/15
GIS: https://tiles.arcgis.com/tiles/ttNGmDvKQA7oeDQ3/arcgis/rest/services
GIS: https://services7.arcgis.com/WvgOaBfZeRNlBq3y/ArcGIS/rest/services
Trail data
See section on BLM servers, there is one with just Colorado data
Colorado Regional
Denver Regional Council of Governments
Website: https://drcog.org
GIS: https://gis.drcog.org/server/rest/services
7-31-2023 No tiled data

## Page 80

Left Hand Water District
Website: https://lefthandwater.gov
GIS: https://services9.arcgis.com/k7w2kqUeGa3WO1tq/ArcGIS/rest/services
Mile High Flood District
Website: https://www.mhfd.org
GIS: https://services3.arcgis.com/TCnvslgqrzhT2ZXG/ArcGIS/rest/services
Table of contents hidden by javascript
GIS: https://tiles.arcgis.com/tiles/TCnvslgqrzhT2ZXG/arcgis/rest/services
North Front Range Water Quality Planning Association
Website: https://www.nfrwqpa.org
GIS: https://services6.arcgis.com/BbqfP96K8rEv72Qz/ArcGIS/rest/services
Northern Water
Website: https://www.northernwater.org
GIS: https://services.arcgis.com/T9hw6UCKSZpziTpg/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/T9hw6UCKSZpziTpg/arcgis/rest/services
Pikes Peak Area Council of Governments
Website: https://www.ppacg.org
GIS: https://services1.arcgis.com/0plDVQODvYjBRQXP/arcgis/rest/services
Pueblo Area Council of Governments
Website: https://www.pacog.net
GIS: https://gisdata.pueblo.us/server/rest/services
South Suburban Parks & Recreation
Website: https://www.ssprd.org
GIS: https://services3.arcgis.com/ZFmKUKfLNHslSqEG/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/ZFmKUKfLNHslSqEG/arcgis/rest/services
Southeast Metro Stormwater Authority
Website: https://www.semswa.org
GIS: https://services7.arcgis.com/Fdq7oIUy06DMmtrT/ArcGIS/rest/services
Colorado County GIS Servers
Adams
https://gisapp.adcogov.org/arcgis/rest/services
Adams
https://gisimg.adcogov.org/arcgis/rest/services
Adams
https://services3.arcgis.com/4PNQOtAivErR7nbT/ArcGIS/rest/ser
vices
Adams
https://services8.arcgis.com/8G2jD4VY84pgX1Z5/ArcGIS/rest/ser
vices
Adams
https://tiles.arcgis.com/tiles/8G2jD4VY84pgX1Z5/arcgis/rest/servi
ces

## Page 81

Arapahoe
https://gis.arapahoegov.com/arcgis/rest/services
Arapahoe
https://services2.arcgis.com/OSbOBWdLkmvu5I9F/ArcGIS/rest/se
rvices
Arapahoe
https://tiles.arcgis.com/tiles/OSbOBWdLkmvu5I9F/arcgis/rest/serv
ices
Archuleta
https://services5.arcgis.com/b1fZk1fY2MHCTEXz/ArcGIS/rest/se
rvices
Archuleta
https://tiles.arcgis.com/tiles/b1fZk1fY2MHCTEXz/arcgis/rest/serv
ices
Boulder
https://maps.bouldercounty.org/arcgis/rest/services
Table of contents hidden by javascript
Trailhead: /Recreation/BOCO_POS_Trails/MapServer/0
Trail: /Recreation/BOCO_POS_Trails/MapServer/1
Boulder
https://services3.arcgis.com/0jWpHMuhmHsukKE3/arcgis/rest/ser
vices
Boulder
https://tiles.arcgis.com/tiles/0jWpHMuhmHsukKE3/arcgis/rest/ser
vices
Centennial
https://maps.centennialco.gov/arcgis/rest/services
Centennial
https://services2.arcgis.com/qzGaVFGfQxn25AYB/ArcGIS/rest/se
rvices
Centennial
https://tiles.arcgis.com/tiles/qzGaVFGfQxn25AYB/arcgis/rest/serv
ices
Chaffee
Schneider Geospatial - ArcGIS server address is not public
Clear Creek
https://map.co.clear-creek.co.us/arcgis2/rest/services
SSL problem
Conejos
Schneider Geospatial - ArcGIS server address is not public
Costilla
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/CostillaCOFeatures/FeatureServer
Go to the top and search for ‘CostillaCO’
Costilla
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/CostillaCOCadastral/MapServer
Go to the top and search for ‘CostillaCO’
Crowley
Schneider Geospatial - ArcGIS server address is not public
Custer
Schneider Geospatial - ArcGIS server address is not public
Delta
https://maps.deltacountyco.gov/arcgis/rest/services

## Page 82

Denver
See the city of Denver
Douglas
https://apps.douglas.co.us/gisis/rest/services
Douglas
https://apps.douglas.co.us/gishost/rest/services
Douglas
https://apps.douglas.co.us/gisod/rest/services
Douglas
           https://services.arcgis.com/seTexOicoRXDvRsJ/arcgis/rest/services
Douglas
https://tiles.arcgis.com/tiles/seTexOicoRXDvRsJ/arcgis/rest/servic
es
Eagle
https://map.eaglecounty.us/arcgiswa/rest/services
El Paso
https://gisservices.elpasoco.com/arcgis2/rest/services
El Paso
https://services3.arcgis.com/6Y56Ohy0RCFlntCT/ArcGIS/rest/ser
vices
El Paso
https://tiles.arcgis.com/tiles/6Y56Ohy0RCFlntCT/arcgis/rest/servic
es
Elbert
https://maps.elbertcounty-co.gov/data/rest/services
Fremont
https://fremontgis.com/server/rest/services
Garfield
https://maps.garfield-county.com/arcgis/rest/services
Garfield
https://services1.arcgis.com/nfpqZdY6vs2HwXa1/ArcGIS/rest/ser
vices
Garfield
https://tiles.arcgis.com/tiles/nfpqZdY6vs2HwXa1/arcgis/rest/servic
es

Gilpin
https://data.digitaldataservices.com/arcgis/rest/services/GilpinCoun
ty
Gilpin
https://services9.arcgis.com/O7afVM5z7n9SwfvW/ArcGIS/rest/ser
vices
Grand
https://gis.co.grand.co.us:6443/arcgis/rest/services
Grand
https://services1.arcgis.com/neOH9wP2I5x0qGmG/ArcGIS/rest/se
rvices/gcRoads/FeatureServer
Grand
https://tiles.arcgis.com/tiles/neOH9wP2I5x0qGmG/arcgis/rest/serv
ices
Huerfano
https://maps.huerfano.us/server/rest/services
Jefferson
https://gisportal.jeffco.us/server/rest/services
Jefferson
https://mapservices1.jeffco.us/arcgis/rest/services
Jefferson
https://mapservices2.jeffco.us/arcgis/rest/services
Jefferson
https://services3.arcgis.com/9ntQlfNHEhmpX4cl/ArcGIS/rest/serv
ices

## Page 83

La Plata
https://gis.laplata.co.us/arcgis/rest/services
La Plata
https://services2.arcgis.com/ilLrLpXfElYxSy9y/arcgis/rest/services
La Plata
https://tiles.arcgis.com/tiles/ilLrLpXfElYxSy9y/arcgis/rest/services
Lake
https://services1.arcgis.com/38PTfoP8IjlBsxZN/ArcGIS/rest/servic
es
Lake
https://tiles.arcgis.com/tiles/38PTfoP8IjlBsxZN/arcgis/rest/services
Larimer
https://maps1.larimer.org/arcgis/rest/services
Las Animas
https://services7.arcgis.com/NWWOCaXnjdetEWUz/arcgis/rest/se
rvices
Logan
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/LoganCOFeatures/FeatureServer
Go to the top and search for ‘LoganCO’
Logan
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/LoganCOAerial2015/MapServer
Mesa
https://mcgis.mesacounty.us/arcgis/rest/services
Mesa
https://mcgis.mesacounty.us/imagery/rest/services
Mineral
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MineralCOFeatures/FeatureServer
Go to the top and search for ‘MineralCO’
Mineral
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MineralCOCadastral/MapServer
Moffat
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MoffatCOFeatures/FeatureServer
Go to the top and search for ‘MoffatCO’
Moffat
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MoffatCOAerial2013/MapServer
Go to the top and search for ‘MoffatCO’
Montezuma
https://gis-server.co.montezuma.co.us/arcgis/rest/services
Montezuma
https://services6.arcgis.com/2WpvlGLSkwz1I8NR/arcgis/rest/servi
ces
Montrose
https://mcmap.montrosecounty.net/server/rest/services
Montrose
https://services2.arcgis.com/zJ3Q5ooyo5GODjaM/arcgis/rest/servi
ces
Montrose
https://services3.arcgis.com/arjIZiPnUOHQnhsl/ArcGIS/rest/servic
es
Otero
Schneider Geospatial - ArcGIS server address is not public

## Page 84

Park
_ttps://maps.parkco.us/arcgis/rest/services
dead link 1
Park
https://services3.arcgis.com/atP7uTVHA2caR3p6/arcgis/rest/servic
es
Park
https://tiles.arcgis.com/tiles/atP7uTVHA2caR3p6/arcgis/rest/servic
es
Pitkin
https://maps.pitkincounty.com/arcgis/rest/services
Pitkin
https://services1.arcgis.com/v0IZLkgglG1DPU2C/ArcGIS/rest/ser
vices
Pitkin
https://tiles.arcgis.com/tiles/v0IZLkgglG1DPU2C/arcgis/rest/servic
es
Prowers
Schneider Geospatial - ArcGIS server address is not public
Pueblo
https://maps.co.pueblo.co.us/outside/rest/services
Rio Blanco
https://services1.arcgis.com/pfZ4YwxhgKucWn2S/ArcGIS/rest/ser
vices
Rio Blanco
https://tiles.arcgis.com/tiles/pfZ4YwxhgKucWn2S/arcgis/rest/servi
ces
Rio Grande
https://services8.arcgis.com/S4XaDWnt7zDg1erG/ArcGIS/rest/ser
vices
Rio Grande
https://tiles.arcgis.com/tiles/S4XaDWnt7zDg1erG/arcgis/rest/servi
ces
Routt
https://services6.arcgis.com/VxFGFP4XeHMTNgVs/ArcGIS/rest/s
ervices
Routt
https://tiles.arcgis.com/tiles/VxFGFP4XeHMTNgVs/arcgis/rest/ser
vices
San Miguel
https://mapping.sanmiguelcountyco.gov/server/rest/services
San Miguel
https://services.arcgis.com/aXqye4IXyXsdIpPb/arcgis/rest/services
Summit
https://gis.summitcountyco.gov/arcgis/rest/services
Summit
https://services6.arcgis.com/dmNYNuTJZDtkcRJq/ArcGIS/rest/ser
vices
Summit
https://tiles.arcgis.com/tiles/dmNYNuTJZDtkcRJq/arcgis/rest/servi
ces
Teller
https://services5.arcgis.com/haXoJFLDtvxGvyC1/arcgis/rest/servic
es
Teller
https://tiles.arcgis.com/tiles/haXoJFLDtvxGvyC1/arcgis/rest/servic
es
Washington
Schneider Geospatial - ArcGIS server address is not public

## Page 85

Weld
https://www.co.weld.co.us/maps/gis/rest/services
Weld
https://services.arcgis.com/ewjSqmSyHJnkfBLL/ArcGIS/rest/servi
ces
Yuma
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/YumaCOFeatures/FeatureServer
Go to the top and search for ‘YumaCO’
Yuma
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/YumaCOCadastral/MapServer
Colorado City, Town, Village, etc GIS Servers
Alamosa
https://services2.arcgis.com/kQ9CrbL3URg6t3jo/arcgis/rest/servic
es
Alamosa
          https://tiles.arcgis.com/tiles/kQ9CrbL3URg6t3jo/arcgis/rest/services
Arvada
https://maps.arvada.org/arcgis/rest/services
Table of contents disabled
Aspen
https://services3.arcgis.com/5FkYBrhNzpVtlA6F/arcgis/rest/servic
es
Aspen
https://tiles.arcgis.com/tiles/5FkYBrhNzpVtlA6F/arcgis/rest/servic
es
Aurora
           https://ags.auroragov.org/aurora/rest/services/OpenData/MapServer
Aurora
https://services3.arcgis.com/0Va1ID99NSrNyyPX/arcgis/rest/servi
ces
Aurora
https://tiles.arcgis.com/tiles/0Va1ID99NSrNyyPX/arcgis/rest/servi
ces
Avon
https://hostingdata2.tighebond.com/arcgis/rest/services/AvonCT
Bethel
https://hostingdata2.tighebond.com/arcgis/rest/services/BethelCT
Boulder
https://maps.bouldercolorado.gov/arcgis/rest/services
Boulder
https://gis.bouldercolorado.gov/ags_svr2/rest/services
Boulder
https://maps.bouldercolorado.gov/arcgis2/rest/services
Breckenridge
https://maps.townofbreckenridge.com/arcgis/rest/services
Brighton
https://maps.brightonco.gov/public/rest/services
Brighton
https://services6.arcgis.com/FoIoSLUvgp6HznSK/ArcGIS/rest/ser
vices
Brookfield
https://hostingdata2.tighebond.com/arcgis/rest/services/Brookfield
CT

## Page 86

Broomfield
https://services1.arcgis.com/vXSRPZbyyOmH9pek/arcgis/rest/services
Broomfield
https://tiles.arcgis.com/tiles/vXSRPZbyyOmH9pek/arcgis/rest/services
Canon City
https://gis.canoncity.org/arcgis/rest/services
Table of contents disabled
Castle Pines
          https://services8.arcgis.com/UbfrjwJF0ZkVzVrn/arcgis/rest/services
Castle Pines
          https://tiles.arcgis.com/tiles/UbfrjwJF0ZkVzVrn/arcgis/rest/services
Castle Rock
https://maps.crgov.com/web/rest/services
Centennial
See centennial county
Central City
https://data.digitaldataservices.com/arcgis/rest/services/CentralCity
Clinton
https://hostingdata2.tighebond.com/arcgis/rest/services/ClintonCT
Colorado Springs
https://gis.coloradosprings.gov/arcgis/rest/services
Table of contents disabled
Colorado Springs
https://data.digitaldataservices.com/arcgis/rest/services/ColoradoS
prings
Commerce City
https://services.arcgis.com/iyZLRarIZZa0GHya/arcgis/rest/services
Commerce City         https://tiles.arcgis.com/tiles/iyZLRarIZZa0GHya/arcgis/rest/services

Denver
https://denvergov.org/arcgis/rest/services
SSL problem
Denver
https://services1.arcgis.com/zdB7qR0BtYrg0Xpl/ArcGIS/rest/servi
ces
Denver
https://tiles.arcgis.com/tiles/zdB7qR0BtYrg0Xpl/arcgis/rest/servic
es
Denver
https://services7.arcgis.com/chFtbDhOWTyv6vVj/ArcGIS/rest/ser
vices
Denver International Airport
Denver
https://tiles.arcgis.com/tiles/chFtbDhOWTyv6vVj/arcgis/rest/servi
ces
Durango
https://services.arcgis.com/iqrNQm6g4Pj36MWn/arcgis/rest/servic
es
Durango
https://tiles.arcgis.com/tiles/iqrNQm6g4Pj36MWn/arcgis/rest/servi
ces
Englewood
https://agiso.englewoodco.gov/public/rest/services
Englewood
https://services6.arcgis.com/2gwTlp6STLlfLYIT/ArcGIS/rest/servi
ces
Englewood
          https://tiles.arcgis.com/tiles/2gwTlp6STLlfLYIT/arcgis/rest/services
Erie
https://eags.erieco.gov/arcgis/rest/services

## Page 87

Estes Park
https://services2.arcgis.com/O6o5Uj7kGWn9nWXG/ArcGIS/rest/s
ervices
Fort Collins
https://gisweb.fcgov.com/arcgis/rest/services
Table of contents disabled
Fort Collins
https://services1.arcgis.com/dLpFH5mwVvxSN4OE/ArcGIS/rest/s
ervices
Fort Collins
https://tiles.arcgis.com/tiles/dLpFH5mwVvxSN4OE/arcgis/rest/ser
vices
Fort Collins
See Larimer County
Frederick
https://gis.frederickco.gov/arcgis/rest/services
Frederick
https://services2.arcgis.com/kUg4C2jBpieHWTtl/arcgis/rest/servic
es
Glenwood Springs
https://maps.cogs.us/server/rest/services
Greeley
https://services.arcgis.com/pfd9xSB0fCRnWvDl/arcgis/rest/servic
es
Greeley
https://tiles.arcgis.com/tiles/pfd9xSB0fCRnWvDl/arcgis/rest/servic
es
Greenwood Village
https://online.greenwoodvillage.com/server/rest/services
Lakewood
https://egis.lakewood.org/server/rest/services
Littleton
https://services6.arcgis.com/lJUBf9F1fZJRB4zT/ArcGIS/rest/servi
ces
Littleton
          https://tiles.arcgis.com/tiles/lJUBf9F1fZJRB4zT/arcgis/rest/services
Lone Tree
https://services7.arcgis.com/M6RDkiPo9JtEo7N6/ArcGIS/rest/ser
vices
Longmont
https://maps.ci.longmont.co.us/arcgis_public/rest/services
Longmont
https://pwnrmaps.ci.longmont.co.us/arcgis_public/rest/services
Longmont
https://lpcmaps.ci.longmont.co.us/arcgis_public/rest/services
Longmont
https://services1.arcgis.com/Sb0rgSd67ecLKIvl/ArcGIS/rest/servic
es/LongmontBusinesses/FeatureServer
Louisville
https://gis.louisvilleco.gov/arcgis/rest/services
Loveland
https://mapserv.cityofloveland.org/arcgis/rest/services
Loveland
https://services1.arcgis.com/d4MV7N9xmuHYbLrF/ArcGIS/rest/s
ervices

## Page 88

Manitou Springs
https://services6.arcgis.com/JvLU4FaQtqrjGWfU/arcgis/rest/servic
es
Manitou Springs
https://tiles.arcgis.com/tiles/JvLU4FaQtqrjGWfU/arcgis/rest/servic
es
Mofatt
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MoffatCOFeatures/FeatureServer
Go to the top and search for ‘MoffatCO’
Mountain Village
https://services3.arcgis.com/Nefdxa42x2DnAd5Z/ArcGIS/rest/serv
ices
Mountain Village
https://tiles.arcgis.com/tiles/Nefdxa42x2DnAd5Z/arcgis/rest/servic
es
Pueblo
https://services1.arcgis.com/IL17xsvNU5Bmw3RY/arcgis/rest/serv
ices
Pueblo
https://tiles.arcgis.com/tiles/IL17xsvNU5Bmw3RY/arcgis/rest/serv
ices
South Fort Collins
https://services7.arcgis.com/hfYPVtCcZzduCT4x/arcgis/rest/servic
es
Sanitation District
Steamboat Springs
https://services1.arcgis.com/sUA1cRqDokwhkDcl/arcgis/rest/servi
ces
Superior
https://services2.arcgis.com/RQsC4DSkpr4c1bMs/ArcGIS/rest/ser
vices
Thornton
https://gis.thorntonco.gov/arcgis/rest/services
Thornton
https://maps.thorntonco.gov/citydevweb/rest/services
Thornton
https://webmaps.thorntonco.gov/arcgis/rest/services
Thornton
https://maps.thorntonco.gov/infraweb/rest/services
Thornton
https://services3.arcgis.com/0xk0XPYhuLWo5oda/ArcGIS/rest/ser
vices
Vail
https://services2.arcgis.com/z8wv5ZDe2QJhWrKN/arcgis/rest/serv
ices
Vail
https://tiles.arcgis.com/tiles/z8wv5ZDe2QJhWrKN/arcgis/rest/serv
ices
Westminster
https://maps.cityofwestminster.us/server/rest/services
Westminster
https://services1.arcgis.com/1qGtTVx4f5UwkUd6/arcgis/rest/servi
ces
Westminster
https://tiles.arcgis.com/tiles/1qGtTVx4f5UwkUd6/arcgis/rest/servi
ces

## Page 89

Wheatridge
https://services1.arcgis.com/aZEZgA7GEh819dvL/arcgis/rest/servi
ces
Wheatridge
https://tiles.arcgis.com/tiles/aZEZgA7GEh819dvL/arcgis/rest/servi
ces
Yuma
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/YumaCOFeatures/FeatureServer
Go to the top and search for ‘YumaCO’
Connecticut State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Connecticut Open Data
Website: https://data.ct.gov/
GIS: https://maps.ct.gov/arcgis/rest/services
Connecticut Department of Energy and Environmental Protection (DEEP)
Website: https://www.ct.gov/deep/site/default.asp
GIS: https://services1.arcgis.com/FjPcSmEFuDYlIdKC/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/FjPcSmEFuDYlIdKC/arcgis/rest/services
Connecticut Department of  Transportation
Website: https://portal.ct.gov/dot
GIS: https://gisportal.dot.ct.gov/server/rest/services
GIS: https://services1.arcgis.com/FCaUeJ5SOVtImake/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/FCaUeJ5SOVtImake/arcgis/rest/services
University of Connecticut - Environmental Conditions Online
Website: https://maps.cteco.uconn.edu
GIS: https://cteco.uconn.edu/ctmaps/rest/services/
includes parcel layers
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://cteco.uconn.edu/ctraster/rest/services/
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
University of Connecticut - Center for Land Use Education and Research (CLEAR)
Website: https://clear.uconn.edu
GIS: https://clear3.uconn.edu/arcgis/rest/services
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Connecticut layers from FEMA
GIS: https://sgsdgf.mapxpress.net/arcgis/rest/services/FEMA_Statewide
8-1-2023 No tiled data
Connecticut - Various layers
https://services1.arcgis.com/FjPcSmEFuDYlIdKC/arcgis/rest/services

## Page 90

https://tiles.arcgis.com/tiles/FjPcSmEFuDYlIdKC/arcgis/rest/services
https://services2.arcgis.com/GJ0FAStzsVuLqJVA/ArcGIS/rest/services
https://services3.arcgis.com/3FL1kr7L4LvwA2Kb/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/3FL1kr7L4LvwA2Kb/arcgis/rest/services
Connecticut Regional
Capitol Region Council of Governments
Website: https://crcog.org
GIS: https://gis.crcog.org/arcgis/rest/services
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Connecticut Water Company
Website: https://www.ctwater.com
GIS: https://services5.arcgis.com/HepPyrQhgnnNghkp/arcgis/rest/services
Metropolitan Council of Governments
GIS: https://maps.ctmetro.org/server/rest/services
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://maps.ctmetro.org/server/rest/services/GBRC
8-1-2023 No tiled data
GIS: https://maps.ctmetro.org/server/rest/services/MetroCOG
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/IzCLn1q8U511eQsa/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/IzCLn1q8U511eQsa/arcgis/rest/services
Lower Connecticut River Valley Council of Governments
Website: https://rivercog.org
GIS: https://services7.arcgis.com/uH7GnAlGDzMooG4B/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/uH7GnAlGDzMooG4B/arcgis/rest/services
Naugatuck Valley Council of Governments
Website: https://nvcogct.gov
GIS: https://services2.arcgis.com/LD8LGc05Tkd3FQoz/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/LD8LGc05Tkd3FQoz/arcgis/rest/services
Northeastern Connecticut Council of Governments
Website: https://neccog.org
GIS: https://gis.neccog.org/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://services.arcgis.com/oT3yVWpbYAcq647w/arcgis/rest/services
Northwest Hills Council of Governments
Website: https://northwesthillscog.org
server *very* slow
GIS: https://services3.arcgis.com/liKpeCR7exNEqmTR/arcgis/rest/services
South Central Regional Council of Governments

## Page 91

Website: https://scrcog.org
GIS: https://dfgdfg.mapxpress.net/arcgis/rest/services/SCRCOG
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://sgsdgf.mapxpress.net/arcgis/rest/services/SCRCOG
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://server1.mapxpress.net/arcgis/rest/services/SCRCOG
Southeastern Connecticut Council of Governments
Website: https://seccog.org
GIS: https://services6.arcgis.com/c8bwOPjaFB6olbad/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/c8bwOPjaFB6olbad/arcgis/rest/services
Western Connecticut Council of Governments
Website: https://westcog.org
GIS: https://services6.arcgis.com/UwEXjTguDDovBVaQ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/UwEXjTguDDovBVaQ/arcgis/rest/services
Madison Land Conservation Trust
Website: https://www.madisonlandtrust.org
GIS:  https://dfgdfg.mapxpress.net/arcgis/rest/services/MLCT
8-1-2023 No tiled data
Connecticut Environmental Conditions Online
Website: https://maps.cteco.uconn.edu/map-services
GIS: https://cteco.uconn.edu/ctraster/rest/services
includes aerials
Connecticut County GIS Servers
Does not have county governments
Connecticut City, Town, Village, etc GIS Servers
Ansonia
https://dfgdfg.mapxpress.net/arcgis/rest/services/Ansonia
Ansonia
https://sgsdgf.mapxpress.net/arcgis/rest/services/Ansonia
Ansonia
https://server1.mapxpress.net/arcgis/rest/services/Ansonia
Ashford
See also above: Northeastern Connecticut Council of Governments
Ashford
_ttps://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Ashford_REVAL_Viewer/FeatureServer      dead link 1
Go to the top and search for ‘Ashford’
Ashford
_ttps://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Ashford_CAMA_Viewer_Basemap/MapServer
Go to the top and search for ‘Ashford’
dead link 1
Avon
https://hostingdata2.tighebond.com/arcgis/rest/services/AvonCT
Beacon Falls
https://dfgdfg.mapxpress.net/arcgis/rest/services/Beacon_Falls

## Page 92

Beacon Falls
https://sgsdgf.mapxpress.net/arcgis/rest/services/Beacon_Falls
Beacon Falls
https://server1.mapxpress.net/arcgis/rest/services/Beacon_Falls
Berlin
https://dfgdfg.mapxpress.net/arcgis/rest/services/Berlin
Berlin
https://sgsdgf.mapxpress.net/arcgis/rest/services/Berlin
Berlin
https://server1.mapxpress.net/arcgis/rest/services/Berlin
Bethel
https://hostingdata3.tighebond.com/arcgis/rest/services/BethelCT
Bethany
https://dfgdfg.mapxpress.net/arcgis/rest/services/Bethany
Bethany
https://sgsdgf.mapxpress.net/arcgis/rest/services/Bethany
Bethany
https://server1.mapxpress.net/arcgis/rest/services/Bethany
Bethlehem
https://server1.mapxpress.net/arcgis/rest/services/Bethlehem
Bloomfield
https://dfgdfg.mapxpress.net/arcgis/rest/services/Bloomfield
Bloomfield
https://sgsdgf.mapxpress.net/arcgis/rest/services/Bloomfield
Bloomfield
https://server1.mapxpress.net/arcgis/rest/services/Bloomfield
Branford
https://dfgdfg.mapxpress.net/arcgis/rest/services/Branford
Branford
https://sgsdgf.mapxpress.net/arcgis/rest/services/Branford
Branford
https://server1.mapxpress.net/arcgis/rest/services/Branford
Bridgeport
https://maps.ctmetro.org/server/rest/services/Bridgeport
Bristol
https://dfgdfg.mapxpress.net/arcgis/rest/services/Bristol
Bristol
https://sgsdgf.mapxpress.net/arcgis/rest/services/Bristol
Bristol
https://arcgis.vgsi.com/server/rest/services/Bristol_CT
Bristol
https://server1.mapxpress.net/arcgis/rest/services/Bristol
Brookfield
https://dfgdfg.mapxpress.net/arcgis/rest/services/Brookfield
Brookfield
https://sgsdgf.mapxpress.net/arcgis/rest/services/Brookfield
Brookfield
https://server1.mapxpress.net/arcgis/rest/services/Brookfield
Burlington
https://dfgdfg.mapxpress.net/arcgis/rest/services/Burlington
Burlington
https://sgsdgf.mapxpress.net/arcgis/rest/services/Burlington
Burlington
https://server1.mapxpress.net/arcgis/rest/services/Burlington
Canaan
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_North_Canaan_Adv_Viewer_Parcels_View/FeatureServ
er
Go to the top and search for ‘Canaan’
Canaan
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Canaan_Adv_Viewer_Basemap_08252025/MapServer
Go to the top and search for ‘Canaan’

## Page 93

Canterbury
https://hostingdata3.tighebond.com/arcgis/rest/services/Canterbury
CT
Canton
https://dfgdfg.mapxpress.net/arcgis/rest/services/Canton
Canton
https://sgsdgf.mapxpress.net/arcgis/rest/services/Canton
Canton
https://server1.mapxpress.net/arcgis/rest/services/Canton
Chaplin
https://gisserver2.axisgis.com/arcgis/rest/services/ChaplinCT
Not open to public
Cheshire
https://dfgdfg.mapxpress.net/arcgis/rest/services/Cheshire
Cheshire
https://sgsdgf.mapxpress.net/arcgis/rest/services/Cheshire
Cheshire
https://server1.mapxpress.net/arcgis/rest/services/Cheshire
Chester
https://gisserver2.axisgis.com/arcgis/rest/services/ChesterCT
Not open to public
Clinton
https://hostingdata3.tighebond.com/arcgis/rest/services/ClintonCT
Colchester
https://dfgdfg.mapxpress.net/arcgis/rest/services/Colchester
Colchester
https://sgsdgf.mapxpress.net/arcgis/rest/services/Colchester
Colchester
https://server1.mapxpress.net/arcgis/rest/services/Colchester
Colebrook
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Colebrook_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Colebrook’
Colebrook
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Colebrook_Adv_Viewer_Basemap_1001025/MapServer
Go to the top and search for ‘Colebrook’
Columbia
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Columbia_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Columbia’
Columbia
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Columbia_Adv_Viewer_Basemap_09172025/MapServer
Go to the top and search for ‘Columbia’
Cornwall
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Cornwall_Adv_Viewer_Parcels/FeatureServer
Go to the top and search for ‘Cormwall’
Cornwall
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Cornwall_Adv_Viewer_Basemap_08142025/MapServer
Go to the top and search for ‘Cormwall’
Coventry
https://dfgdfg.mapxpress.net/arcgis/rest/services/Coventry
Coventry
https://sgsdgf.mapxpress.net/arcgis/rest/services/Coventry

## Page 94

Coventry
https://server1.mapxpress.net/arcgis/rest/services/Coventry
Cromwell
They have a GIS that uses Google maps.
Danbury
https://services1.arcgis.com/TWuNUq6ILU5haptM/arcgis/rest/serv
ices
Table of contents hidden by javascript
Danbury
https://tiles.arcgis.com/tiles/TWuNUq6ILU5haptM/arcgis/rest/serv
ices
Darien
https://map.appgeo.com/arcgis/rest/services/DarienCT
Not open to public
Darien
https://hostingdata3.tighebond.com/arcgis/rest/services/ClintonCT
Derby
https://sgsdgf.mapxpress.net/arcgis/rest/services/Derby
Derby
https://server1.mapxpress.net/arcgis/rest/services/Derby
Durham
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Durham_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Durham’
Durham
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Durham_Adv_Viewer_Basemap_01122026/MapServer
Go to the top and search for ‘Durham’
East Granby
https://server1.mapxpress.net/arcgis/rest/services/East_Granby
East Haddam
https://gisserver2.axisgis.com/arcgis/rest/services/East_HaddamCT
Not open to public
East Hampton
https://hostingdata3.tighebond.com/arcgis/rest/services/EastHampt
onCT
East Hampton
_ttps://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_East_Hampton_REVAL_Viewer/FeatureServer
dead link 1
East Hampton
_ttps://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_East_Hampton_Adv_Viewer_Basemap_04102025/MapSe
rver
dead link 1
East Haven
https://dfgdfg.mapxpress.net/arcgis/rest/services/East_Haven
East Haven
https://sgsdgf.mapxpress.net/arcgis/rest/services/East_Haven
East Haven
https://server1.mapxpress.net/arcgis/rest/services/East_Haven
East Lyme
         https://hostingdata3.tighebond.com/arcgis/rest/services/EastLymeCT
East Windsor
They have a GIS that uses Google maps.

## Page 95

Ellington
https://map.appgeo.com/arcgis/rest/services/EllingtonCT
Not open to public
Enfield
https://gis.enfield.org/enfieldgis/rest/services
Enfield
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/Enfield
CT_Basemap/MapServer
Enfield
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/Enfield
CT_OpLayers/MapServer
Essex
https://arcgis.vgsi.com/server/rest/services/Essex_CT
Fairfield
https://maps.ctmetro.org/server/rest/services/Fairfield
Franklin
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Franklin_Adv_Viewer_Parcels/FeatureServer
Go to the top and search for ‘Franklin’
Franklin
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Franklin_Adv_Viewer_Basemap_08272025/MapServer
Go to the top and search for ‘Franklin’
Farmington
https://dfgdfg.mapxpress.net/arcgis/rest/services/Farmington
Farmington
https://sgsdgf.mapxpress.net/arcgis/rest/services/Farmington
Farmington
https://server1.mapxpress.net/arcgis/rest/services/Farmington
Glastonbury
https://gisarc2022.glastonbury-ct.gov/server/rest/services
Goshen
https://dfgdfg.mapxpress.net/arcgis/rest/services/Goshen
Goshen
https://sgsdgf.mapxpress.net/arcgis/rest/services/Goshen
Goshen
https://server1.mapxpress.net/arcgis/rest/services/Goshen
Granby
Schneider Geospatial - ArcGIS server address is not public
Groton
https://maps.groton-ct.gov/arcgis/rest/services
Guilford
https://dfgdfg.mapxpress.net/arcgis/rest/services/Guilford
Guilford
https://sgsdgf.mapxpress.net/arcgis/rest/services/Guilford
Guilford
https://server1.mapxpress.net/arcgis/rest/services/Guilford
Haddam
https://hostingdata3.tighebond.com/arcgis/rest/services/HaddamCT
Haddam
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Haddam_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Haddam’
Haddam
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Haddam_Adv_Viewer_2ft_Contours/MapServer
Go to the top and search for ‘Haddam’

## Page 96

Hamden
https://dfgdfg.mapxpress.net/arcgis/rest/services/Hamden
Hamden
https://sgsdgf.mapxpress.net/arcgis/rest/services/Hamden
Hamden
https://server1.mapxpress.net/arcgis/rest/services/Hamden

Hartford
https://gis.hartford.gov/arcgis/rest/services

Hartford
https://services2.arcgis.com/WM6ZNcwewSWH8Mo9/ArcGIS/res
t/services
Harwinton
https://services1.arcgis.com/DjfAyvUwdiY6gnFC/arcgis/rest/servi
ces/Parcels_view/FeatureServer
Harwinton
https://tiles.arcgis.com/tiles/DjfAyvUwdiY6gnFC/arcgis/rest/servic
es
Harwinton
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Harwinton_LHA/FeatureServer   Not open to public
Go to the top and search for ‘Harwinton’
Hebron
https://gisserver2.axisgis.com/arcgis/rest/services/HebronCT
Not open to public
Kent
Schneider Geospatial - ArcGIS server address is not public
Killingworth
https://hostingdata3.tighebond.com/arcgis/rest/services/Killingwort
hCT
Lisbon
https://dfgdfg.mapxpress.net/arcgis/rest/services/Lisbon
Lisbon
https://sgsdgf.mapxpress.net/arcgis/rest/services/Lisbon
Lisbon
https://server1.mapxpress.net/arcgis/rest/services/Lisbon
Litchfield
https://dfgdfg.mapxpress.net/arcgis/rest/services/Litchfield
Litchfield
https://sgsdgf.mapxpress.net/arcgis/rest/services/Litchfield
Litchfield
https://server1.mapxpress.net/arcgis/rest/services/Litchfield
Madison
https://dfgdfg.mapxpress.net/arcgis/rest/services/Madison
Madison
https://sgsdgf.mapxpress.net/arcgis/rest/services/Madison
Madison
https://server1.mapxpress.net/arcgis/rest/services/Madison
Madison
https://server1.mapxpress.net/arcgis/rest/services/MLCT
Trails - Madison Land Conservation Trust
Manchester
https://gis1.townofmanchester.org/arcgis/rest/services
Manchester
https://services.arcgis.com/kGolg8iONc8RVei5/arcgis/rest/services
Mansfield
https://gisserver2.axisgis.com/arcgis/rest/services/MansfieldCT
Not open to public
Marlborough
_ttps://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Marlborough_REVAL_Viewer_FS/FeatureServer

## Page 97

dead link 1
Marlborough
_ttps://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Marlborough_Viewer_REVAL_Basemap/MapServer
dead link 1
Meriden
https://gis.meridenct.gov/server/rest/services
Middlebury
https://dfgdfg.mapxpress.net/arcgis/rest/services/Middlebury
Middlebury
https://sgsdgf.mapxpress.net/arcgis/rest/services/Middlebury
Middlebury
https://server1.mapxpress.net/arcgis/rest/services/Middlebury
Middlefield
https://hostingdata3.tighebond.com/arcgis/rest/services/Middlefield
CT
Middletown
http://gis.cityofmiddletown.com:6080/arcgis/rest/services  not https
Milford
https://dfgdfg.mapxpress.net/arcgis/rest/services/Milford
Milford
https://sgsdgf.mapxpress.net/arcgis/rest/services/Milford
Milford
https://server1.mapxpress.net/arcgis/rest/services/Milford
Monroe
https://maps.ctmetro.org/server/rest/services/Monroe
Morris
Schneider Geospatial - ArcGIS server address is not public
Naugatuck
https://dfgdfg.mapxpress.net/arcgis/rest/services/Naugatuck
Naugatuck
https://sgsdgf.mapxpress.net/arcgis/rest/services/Naugatuck
Naugatuck
https://server1.mapxpress.net/arcgis/rest/services/Naugatuck
New Britain
https://dfgdfg.mapxpress.net/arcgis/rest/services/New_Britain
New Britain
https://sgsdgf.mapxpress.net/arcgis/rest/services/New_Britain
New Britain
https://server1.mapxpress.net/arcgis/rest/services/New_Britain
New Canaan
https://hostingdata2.tighebond.com/arcgis/rest/services/NewCanaa
nCT
New Canaan
https://hostingdata3.tighebond.com/arcgis/rest/services/NewCanaa
nCT
New Fairfield
https://hostingdata3.tighebond.com/arcgis/rest/services/NewFairfie
ldCT
New Hartford
https://dfgdfg.mapxpress.net/arcgis/rest/services/New_Hartford
New Hartford
https://sgsdgf.mapxpress.net/arcgis/rest/services/New_Hartford
New Hartford
https://server1.mapxpress.net/arcgis/rest/services/New_Hartford
New Haven
_ttps://nhgis.newhavenct.gov/server/rest/services
     dead link 3
New Haven
https://arcgis.vgsi.com/server/rest/services/New_Haven_CT

## Page 98

New Haven
https://services6.arcgis.com/AWSPcxcHO7OnZlnu/ArcGIS/rest/se
rvices
New Haven
https://tiles.arcgis.com/tiles/AWSPcxcHO7OnZlnu/arcgis/rest/serv
ices
New London
https://arcgis.vgsi.com/server/rest/services/New_London_CT
New Milford
https://hostingdata2.tighebond.com/arcgis/rest/services/NewMilfor
dCT
New Milford
https://map.appgeo.com/arcgis/rest/services/NewMilfordCT
Not open to public
Newington
https://server1.mapxpress.net/arcgis/rest/services/Newington
Newington
_ttps://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Newington_REVAL_Viewer_Full/FeatureServer
Go to the top and search for ‘Newington’
dead link 1
Newington
_ttps://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Newington_REVAL_Viewer_Basemap/MapServer
Go to the top and search for ‘Newington’
dead link 1
Newtown
https://dfgdfg.mapxpress.net/arcgis/rest/services/Newtown
Newtown
https://sgsdgf.mapxpress.net/arcgis/rest/services/Newtown
Newtown
https://server1.mapxpress.net/arcgis/rest/services/Newtown
Newtown
https://services1.arcgis.com/6v6OusjE9RaBLf3L/arcgis/rest/servic
es
Newtown
https://tiles.arcgis.com/tiles/6v6OusjE9RaBLf3L/arcgis/rest/servic
es
Norfolk
Schneider Geospatial - ArcGIS server address is not public
North Branford
https://hostingdata3.tighebond.com/arcgis/rest/services/NorthBranf
ordCT
North Canaan
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_North_Canaan_Adv_Viewer_Parcels_View/FeatureServ
er
Go to the top and search for ‘North_Canaan’
North Canaan
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_North_Canaan_Adv_Viewer_Basemap_10242025/MapSer
ver
Go to the top and search for ‘North_Canaan’
North Haven
https://map.appgeo.com/arcgis/rest/services/NorthHavenCT
Not open to public
North Stonington
https://dfgdfg.mapxpress.net/arcgis/rest/services/North_Stonington
North Stonington
https://sgsdgf.mapxpress.net/arcgis/rest/services/North_Stonington
North Stonington      https://server1.mapxpress.net/arcgis/rest/services/North_Stonington

## Page 99

North Stonington
_ttps://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_North_Stonington_REVAL_Viewer/FeatureServer
dead link 1
North Stonington
_ttps://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_North_Stonington_Adv_Viewer_Basemap_04072025/Map
Server
dead link 1
Norwalk
https://services2.arcgis.com/HfsHDBmkGwb1UtID/ArcGIS/rest/se
rvices
Norwalk
https://tiles.arcgis.com/tiles/HfsHDBmkGwb1UtID/arcgis/rest/serv
ices
Orange
https://hostingdata2.tighebond.com/arcgis/rest/services/OrangeCT
Orange
https://hostingdata3.tighebond.com/arcgis/rest/services/OrangeCT
Oxford
https://dfgdfg.mapxpress.net/arcgis/rest/services/Oxford
Oxford
https://sgsdgf.mapxpress.net/arcgis/rest/services/Oxford
Oxford
https://server1.mapxpress.net/arcgis/rest/services/Oxford
Plainfield
          https://hostingdata3.tighebond.com/arcgis/rest/services/PlainfieldCT
Plainville
https://dfgdfg.mapxpress.net/arcgis/rest/services/Plainville
Plainville
https://sgsdgf.mapxpress.net/arcgis/rest/services/Plainville
Plainville
https://server1.mapxpress.net/arcgis/rest/services/Plainville
Plainville
https://server1.mapxpress.net/arcgis/rest/services/PlainvilleV2
Plymouth
https://dfgdfg.mapxpress.net/arcgis/rest/services/Plymouth
Plymouth
https://sgsdgf.mapxpress.net/arcgis/rest/services/Plymouth
Plymouth
https://server1.mapxpress.net/arcgis/rest/services/Plymouth
Plymouth
_ttps://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Plymouth_REVAL_Viewer/FeatureServer
Go to the top and search for ‘Plymouth’
dead link 1
Plymouth
_ttps://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Plymouth_REVAL_Viewer_Basemap/MapServer
Go to the top and search for ‘Plymouth’
dead link 1
Portland
Schneider Geospatial - ArcGIS server address is not public
Preston
https://dfgdfg.mapxpress.net/arcgis/rest/services/Preston
Preston
https://sgsdgf.mapxpress.net/arcgis/rest/services/Preston
Preston
https://server1.mapxpress.net/arcgis/rest/services/Preston
Prospect
https://dfgdfg.mapxpress.net/arcgis/rest/services/Prospect
Prospect
https://sgsdgf.mapxpress.net/arcgis/rest/services/Prospect
Prospect
https://server1.mapxpress.net/arcgis/rest/services/Prospect

## Page 100

Putnam
https://gisserver2.axisgis.com/arcgis/rest/services/PutnamCT
Not open to public
Redding
https://gis3.cdmsmithgis.com/arcgis/rest/services
Redding
https://arcgis.vgsi.com/server/rest/services/Redding_CT
Ridgefield
https://hostingdata2.tighebond.com/arcgis/rest/services/Ridgefield
CT
Ridgefield
https://hostingdata3.tighebond.com/arcgis/rest/services/Ridgefield
CT
Rocky Hill
https://gisserver2.axisgis.com/arcgis/rest/services/Rocky_HillCT
Not open to public
Roxbury
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Roxbury_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Roxbury’
Roxbury
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Roxbury_Adv_Viewer_Basemap_03062025/MapServer
Go to the top and search for ‘Roxbury’
Salem
https://dfgdfg.mapxpress.net/arcgis/rest/services/Salem
Salem
https://sgsdgf.mapxpress.net/arcgis/rest/services/Salem
Salem
https://server1.mapxpress.net/arcgis/rest/services/Salem
Salisbury
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Salisbury_Adv_Viewer_Parcels/FeatureServer
Go to the top and search for ‘Salisbury’
Salisbury
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Salisbury_Adv_Viewer_Basemap_08252025/MapServer
Go to the top and search for ‘Salisbury’
Scotland
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Scotland_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Scotland’
Scotland
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Scotland_Adv_Viewer_Basemap_03062025/MapServer
Go to the top and search for ‘Scotland’
Seymour
https://dfgdfg.mapxpress.net/arcgis/rest/services/Seymour
Seymour
https://sgsdgf.mapxpress.net/arcgis/rest/services/Seymour
Seymour
https://server1.mapxpress.net/arcgis/rest/services/Seymour
Sharon
Schneider Geospatial - ArcGIS server address is not public
Shelton
https://dfgdfg.mapxpress.net/arcgis/rest/services/Shelton

## Page 101

Shelton
https://sgsdgf.mapxpress.net/arcgis/rest/services/Shelton
Shelton
https://server1.mapxpress.net/arcgis/rest/services/Shelton
Sherman
https://gisserver2.axisgis.com/arcgis/rest/services/ShermanCT
Not open to public
Simsbury
https://dfgdfg.mapxpress.net/arcgis/rest/services/Simsbury
Simsbury
https://sgsdgf.mapxpress.net/arcgis/rest/services/Simsbury
Simsbury
https://server1.mapxpress.net/arcgis/rest/services/Simsbury
Somers
https://dfgdfg.mapxpress.net/arcgis/rest/services/Somers
Somers
https://sgsdgf.mapxpress.net/arcgis/rest/services/Somers
Somers
https://server1.mapxpress.net/arcgis/rest/services/Somers
South Windsor
https://dfgdfg.mapxpress.net/arcgis/rest/services/South_Windsor
South Windsor
https://sgsdgf.mapxpress.net/arcgis/rest/services/South_Windsor
South Windsor
https://services6.arcgis.com/VHrCjoSLvBIpoE7O/ArcGIS/rest/ser
vices
South Windsor
https://server1.mapxpress.net/arcgis/rest/services/South_Windsor
Southbury
https://dfgdfg.mapxpress.net/arcgis/rest/services/Southbury
Southbury
https://sgsdgf.mapxpress.net/arcgis/rest/services/Southbury
Southbury
https://server1.mapxpress.net/arcgis/rest/services/Southbury
Southington
https://hostingdata2.tighebond.com/arcgis/rest/services/Southingto
nCT
Sterling
https://hostingdata3.tighebond.com/arcgis/rest/services/SterlingCT
Stonington
https://gis.stonington-ct.gov/arcgis/rest/services
Stratford
https://maps.ctmetro.org/server/rest/services/Stratford
Stratford
           https://hostingdata2.tighebond.com/arcgis/rest/services/StratfordCT
Suffield
https://dfgdfg.mapxpress.net/arcgis/rest/services/Suffield
Suffield
https://sgsdgf.mapxpress.net/arcgis/rest/services/Suffield
Suffield
https://server1.mapxpress.net/arcgis/rest/services/Suffield
Thomaston
https://hostingdata3.tighebond.com/arcgis/rest/services/Thomaston
CT
Tolland
https://map.appgeo.com/arcgis/rest/services/TollandCT
Not open to public
Torrington
https://dfgdfg.mapxpress.net/arcgis/rest/services/Torrington
Torrington
https://sgsdgf.mapxpress.net/arcgis/rest/services/Torrington

## Page 102

Torrington
https://server1.mapxpress.net/arcgis/rest/services/Torrington
Trumbull
https://maps.ctmetro.org/server/rest/services/Trumbull
Trumbull
          https://hostingdata2.tighebond.com/arcgis/rest/services/TrumbullCT
Trumbull
https://services9.arcgis.com/QHwoM7KzeMggLpDm/ArcGIS/rest/
services
Wallingford
https://dfgdfg.mapxpress.net/arcgis/rest/services/Wallingford
Wallingford
https://sgsdgf.mapxpress.net/arcgis/rest/services/Wallingford
Wallingford
https://server1.mapxpress.net/arcgis/rest/services/Wallingford
Warren
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Warren_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Warren’
Warren
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Warren_Adv_Viewer_Basemap_03062025/MapServer
Go to the top and search for ‘Warren’
Washington
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Washington_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Washington’
Washington
_ttps://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Washington_Adv_Viewer_Annotation_12022025/MapSer
ver
Go to the top and search for ‘Washington’       dead link 1
Waterford
https://hostingdata2.tighebond.com/arcgis/rest/services/Waterford
CT
Not open to public
Waterford
https://hostingdata3.tighebond.com/arcgis/rest/services/Waterford
CT
Watertown
https://hostingdata2.tighebond.com/arcgis/rest/services/Watertown
CT
Watertown
https://hostingdata3.tighebond.com/arcgis/rest/services/Watertown
CT
West Hartford
They have a GIS based on Google maps.
West Haven
https://server1.mapxpress.net/arcgis/rest/services/WestHaven
Weston
https://dfgdfg.mapxpress.net/arcgis/rest/services/Weston
Weston
https://sgsdgf.mapxpress.net/arcgis/rest/services/Weston
Weston
https://server1.mapxpress.net/arcgis/rest/services/Weston
Windham
https://gisserver2.axisgis.com/arcgis/rest/services/WindhamCT
Not open to public

## Page 103

Wilton
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Wilton_Adv_Viewer_Parcels/FeatureServer
Go to the top and search for ‘Wilton’
Wilton
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Wilton_Adv_Viewer_1ft_Contours/MapServer
Go to the top and search for ‘Wilton’
Wolcott
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Wolcott_Adv_Viewer_Parcels_View/FeatureServer
Go to the top and search for ‘Wolcott’
Wolcott
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Wolcott_Adv_Viewer_Basemap_12012025/MapServer
Go to the top and search for ‘Wolcott’
Woodbridge
https://dfgdfg.mapxpress.net/arcgis/rest/services/Woodbridge
Woodbridge
https://sgsdgf.mapxpress.net/arcgis/rest/services/Woodbridge
Woodbridge
https://services1.arcgis.com/j6iFLXhyiD3XTMyD/ArcGIS/rest/ser
vices/CT_Woodbridge_Adv_Viewer_Parcels/FeatureServer
Go to the top and search for ‘Woodbridge’
Woodbridge
https://tiles.arcgis.com/tiles/j6iFLXhyiD3XTMyD/arcgis/rest/servi
ces/CT_Woodbridge_Adv_Viewer_Basemap_10082025/MapServe
r
Go to the top and search for ‘Woodbridge’
Woodbury
https://dfgdfg.mapxpress.net/arcgis/rest/services/Woodbury
Woodbury
https://sgsdgf.mapxpress.net/arcgis/rest/services/Woodbury
Woodbury
https://server1.mapxpress.net/arcgis/rest/services/Woodbury
Delaware State GIS Servers
Delaware Open Data
Website: https://data.delaware.gov/
Delaware First Map
Website: https://firstmap.delaware.gov/
GIS: https://enterprise.firstmap.delaware.gov/arcgis/rest/services
Parcel lines: PlanningCadastre/DE_StateParcels/MapServer/0
8-1-2023 No tiled data
GIS: https://apps.firstmaptest.delaware.gov/apps/rest/services
GIS: https://imagery.firstmap.delaware.gov/imagery/rest/services
Delaware Department of Natural Resources and Environmental Control
Website: https://dnrec.delaware.gov
GIS: https://services2.arcgis.com/JSw5FPLGACZknOZv/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/JSw5FPLGACZknOZv/arcgis/rest/services
Delaware Department of Transportation

## Page 104

Website: https://deldot.gov/Programs/gate/index.shtml
GIS: https://deldot.kci.com/arcgis/rest/services
8-1-2023 No tiled data
Delaware various layers
GIS: https://services1.arcgis.com/bFDgLqS5IyUBQLAd/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/bFDgLqS5IyUBQLAd/arcgis/rest/services
Delaware Regional
Delaware Valley Regional Planning Commission
Website: https://www.dvrpc.org
GIS: https://services1.arcgis.com/LWtWv6q6BJyKidj8/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/LWtWv6q6BJyKidj8/arcgis/rest/services
Delaware County GIS Servers
All counties are listed and have been checked for GIS
Kent
https://gis.kentcountyde.gov/server/rest/services
Kent
https://services1.arcgis.com/V9eFgKNI0ePRpU84/ArcGIS/rest/ser
vices
Kent
https://tiles.arcgis.com/tiles/V9eFgKNI0ePRpU84/arcgis/rest/servi
ces
New Castle
https://gis.nccde.org/agsserver/rest/services
New Castle
https://services6.arcgis.com/iiIgE8mTDBf4z99T/ArcGIS/rest/servi
ces
Sussex
https://map.sussexcountyde.gov/server/rest/services
Delaware City, Town, Village, etc GIS Servers
Dover
https://gis.dover.de.us/arcgis/rest/services
Dover
https://services.arcgis.com/ZrZWFC1SG7KRY5pf/arcgis/rest/servi
ces
Newark
https://services.arcgis.com/nQgBxn6WXyRCKVUz/arcgis/rest/ser
vices
Newark
https://tiles.arcgis.com/tiles/nQgBxn6WXyRCKVUz/arcgis/rest/se
rvices

Willmington
See New Castle County
Florida State GIS Servers
Florida Geographic Information Office
Website: https://www.floridagio.gov

## Page 105

Data portal: https://geodata.floridagio.gov
GIS: https://services9.arcgis.com/Gh9awoU677aKree0/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Gh9awoU677aKree0/arcgis/rest/services
Florida Division of Emergency
Website: https://www.floridadisaster.org
GIS: https://services.arcgis.com/3wFbqsFPLeKqOlIK/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/3wFbqsFPLeKqOlIK/arcgis/rest/services
Florida Department of Agriculture and Consumer Services
Website: https://www.fdacs.gov
GIS: https://gis.fdacs.gov/mapping/rest/services
GIS: https://services1.arcgis.com/T0NPfOCJr9tmBN93/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/T0NPfOCJr9tmBN93/arcgis/rest/services
Florida Department of Environmental Protection
Website: https://floridadep.gov/
GIS: https://ca.dep.state.fl.us/arcgis/rest/services
8-1-2023 No tiled data
Dynamic parcels: Map_Direct/Boundaries/MapServer/16
GIS: https://ags.dep.state.fl.us/arcgis/rest/services
GIS: https://castg.dep.state.fl.us/arcgis/rest/services
GIS: https://services1.arcgis.com/nRHtyn3uE1kyzoYc/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/nRHtyn3uE1kyzoYc/arcgis/rest/services
Florida Department of Health
Website: https://www.floridahealth.gov
GIS: https://gis.flhealth.gov/arcgis/rest/services
SSL problem
8-1-2023 No tiled data
GIS: https://services1.arcgis.com/CY1LXxl9zlJeBuRZ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/CY1LXxl9zlJeBuRZ/arcgis/rest/services
Florida Department of Transportation
Website: https://www.fdot.gov
GIS: https://gis.fdot.gov/arcgis/rest/services
8-1-2023 No tiled data
Dynamic parcels by county:  Parcels/MapServer
GIS: https://spatialags.vhb.com/arcgis/rest/services/FDOT_NWFL
8-1-2023 No tiled data
GIS: https://services1.arcgis.com/O1JpcwDW8sjYuddV/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/O1JpcwDW8sjYuddV/arcgis/rest/services
Florida Fish and Wildlife Conservation Commission
Website: https://myfwc.com
GIS: https://ocean.floridamarine.org/arcgis/rest/services
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”

## Page 106

GIS: https://atoll.floridamarine.org/arcgis/rest/services
8-1-2023 No tiled data
GIS: https://services2.arcgis.com/z6TmTIyYXEYhuNM0/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/z6TmTIyYXEYhuNM0/arcgis/rest/services
Florida Resources and Environmental Analysis Center
Website: https://freac.fsu.edu
GIS: https://maps.freac.fsu.edu/arcgis/rest/services
See LABINS layer with PLSS data
LABINS maps: https://www.labins.org
8-1-2023 No tiled data
Florida legislature
GIS: https://services6.arcgis.com/WNLWyVVqYEXv5C4T/ArcGIS/rest/services
Florida Fire Marshal
GIS: https://services6.arcgis.com/RTYCWyATq5TpQEkX/ArcGIS/rest/services
Florida Natural Areas Inventory
Website: https://www.fnai.org
GIS: https://services.arcgis.com/9Jk4Zl9KofTtvg3x/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/9Jk4Zl9KofTtvg3x/arcgis/rest/services
Florida Institute of Oceanography
Website: https://www.fio.usf.edu
GIS: https://services1.arcgis.com/KlG2Y19dgrmkvcGc/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/KlG2Y19dgrmkvcGc/arcgis/rest/services
University South Florida Water Institute
Website: https://waterinstitute.usf.edu
GIS: https://gis.waterinstitute.usf.edu/arcgis/rest/services
8-1-2023 No tiled data
University of Central Florida
GIS: https://services.arcgis.com/dVL5xxth19juhrDY/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/dVL5xxth19juhrDY/arcgis/rest/services
University of Southern Florida
Center for Digital Heritage and Geospatial Information
GIS: https://services3.arcgis.com/9lVOGNODRgsFxu7n/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/9lVOGNODRgsFxu7n/arcgis/rest/services
Florida International University GIS Center
Website: https://maps.fiu.edu/gis
GIS: _ttps://gisportal.fiu.edu/arcgisserver/rest/services
dead link 3
Includes Florida DOT (Department of Transportation)

## Page 107

8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Florida various layers
GIS: https://maps.floridadisaster.org/GIS/rest/services
8-1-2023 No tiled data
Dynamic parcels: Base/Parcels/MapServer
GIS: https://services.arcgis.com/3wFbqsFPLeKqOlIK/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/3wFbqsFPLeKqOlIK/arcgis/rest/services
All data is tiled.  Hurricane and evacuation layers.
GIS: https://geoservices.nwfwmd.state.fl.us/arcgis/rest/services
Florida Regional
Apalachee Regional Planning Council
Website: https://www.arpc.org
GIS: https://gis.arpc.org/server/rest/services
GIS: https://services8.arcgis.com/N3lCn6dEKCL6LidU/arcgis/rest/services
Broward Metropolitan Planning Organization
Website: https://www.browardmpo.org
GIS: https://services1.arcgis.com/vEO7zMZKFkKFr1Do/arcgis/rest/services
Central Florida Regional Transportation Authority    Serves 3 counties.
Website: https://www.golynx.com/
GIS: https://services2.arcgis.com/rp0R3ANPwsAdELpS/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/rp0R3ANPwsAdELpS/arcgis/rest/services
East Central Florida Regional Planning Council
Website: https://www.ecfrpc.org
GIS: https://gis.ecfrpc.org/arcgis/rest/services
Emerald Coast Regional Council
Website: https://www.ecrc.org
GIS: https://services2.arcgis.com/xDFo56nFuq1SBnBw/ArcGIS/rest/services
Northwest Florida Water Management District
Website: https://www.nwfwater.com/
GIS:
https://geoservices.nwfwmd.state.fl.us/arcgis/rest/services
GIS:
https://ca.dep.state.fl.us/arcgis/rest/services/OpenData/NWFWMD_LANDUSE/M
apServer
8-1-2023 No tiled data
GIS:
https://services5.arcgis.com/4S31IuHan7toVWys/ArcGIS/rest/services
Sarasota/Manatee Metropolitan Planning Organization
Website: https://www.mympo.org
GIS: https://services8.arcgis.com/xkIkAiBGhCeWE8V7/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/xkIkAiBGhCeWE8V7/arcgis/rest/services

## Page 108

South Florida Water Management District
Website: https://www.sfwmd.gov
GIS: https://geoweb.sfwmd.gov/agsext1/rest/services
GIS: https://geoweb.sfwmd.gov/agsext2/rest/services
GIS: https://geoweb.sfwmd.gov/agsimg1/rest/services
GIS: https://geoportal.sfwmd.gov/hosted/rest/services
GIS: https://services1.arcgis.com/sDAPyc2rGRn7vf9B/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/sDAPyc2rGRn7vf9B/arcgis/rest/services
Southwest Florida Water Management District
Website: https://www.swfwmd.state.fl.us
GIS: https://www25.swfwmd.state.fl.us/arcgis10/rest/services
8-1-2023 No tiled data
GIS: https://www25.swfwmd.state.fl.us/arcgis11/rest/services
8-1-2023 No tiled data
GIS: https://www25.swfwmd.state.fl.us/arcgis12/rest/services
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://www45.swfwmd.state.fl.us/arcgis10/rest/services
GIS: https://www45.swfwmd.state.fl.us/arcgis12/rest/services
GIS: https://www45.swfwmd.state.fl.us/arcgisimg/rest/services
GIS: https://services1.arcgis.com/gdr0FcZCwx1BmrQk/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/gdr0FcZCwx1BmrQk/arcgis/rest/services
Suwanee River Water Management District
Website: https://www.mysuwanneeriver.com
GIS: http://gis.srwmd.state.fl.us/arcgis/rest/services
not https
8-1-2023 No tiled data
Florida County GIS Servers
All counties are listed
Alachua
https://gis.alachuacounty.us/arcgis/rest/services
Alachua
https://services.arcgis.com/cNo3jpluyt69V8Ek/arcgis/rest/services
Alachua
https://tiles.arcgis.com/tiles/cNo3jpluyt69V8Ek/arcgis/rest/services
Baker
https://services6.arcgis.com/HSWu3dhzHf7nZfIa/arcgis/rest/servic
es
Baker
https://tiles.arcgis.com/tiles/HSWu3dhzHf7nZfIa/arcgis/rest/servic
es
Bay
https://gis.baycountyfl.gov/arcgis/rest/services
Bay
https://services1.arcgis.com/QB0VWfqR9MD4lF0F/arcgis/rest/ser
vices
Bay
https://tiles.arcgis.com/tiles/QB0VWfqR9MD4lF0F/arcgis/rest/ser
vices

## Page 109

Bradford
https://services5.arcgis.com/I5xnndVVpH5WlmgL/arcgis/rest/serv
ices
Bradford
https://tiles.arcgis.com/tiles/I5xnndVVpH5WlmgL/arcgis/rest/servi
ces
Brevard
https://gis.brevardfl.gov/gissrv/rest/services
Brevard
https://www.bcpao.us/arcgis/rest/services
Brevard
https://services2.arcgis.com/zfDSLldsAGQfwUz9/ArcGIS/rest/ser
vices
Brevard
https://tiles.arcgis.com/tiles/zfDSLldsAGQfwUz9/arcgis/rest/servi
ces
Brevard
https://services7.arcgis.com/D37PTvVn9GlIF4jl/ArcGIS/rest/servi
ces
Schools
Brevard
           https://tiles.arcgis.com/tiles/D37PTvVn9GlIF4jl/arcgis/rest/services
Broward
https://bcgishub.broward.org/image/rest/services
Broward
https://gisweb-adapters.bcpa.net/arcgis/rest/services
Table of contents disabled
Calhoun
Schneider Geospatial - ArcGIS server address is not public
Charlotte
https://agis3.charlottecountyfl.gov/arcgis/rest/services
Charlotte
https://agis2.charlottecountyfl.gov/arcgis/rest/services
Table of contents disabled
Charlotte
https://agis.charlottecountyfl.gov/arcgis/rest/services
Table of contents disabled
Citrus
https://gis.citruspa.org/arcgisweb/rest/services
Table of contents disabled
Clay
https://maps.claycountygov.com:6443/arcgis/rest/services
Clay
https://services1.arcgis.com/n3YQ5LxnPCvrTyvT/arcgis/rest/servi
ces
Collier
_ttps://gmdnags.colliercountyfl.gov/arcgis/rest/services
dead link 1
Collier
https://services1.arcgis.com/0iTcFO8FQRNaWoIk/arcgis/rest/servi
ces
Table of contents hidden by javascript
Collier
https://services2.arcgis.com/SlIq32SqARUHIhSx/arcgis/rest/servic
es
Collier
https://services2.arcgis.com/UJQ7Q9uboSWRAzxj/ArcGIS/rest/se
rvices
PUD
Collier
https://tiles.arcgis.com/tiles/UJQ7Q9uboSWRAzxj/arcgis/rest/serv
ices
Columbia
https://gis.columbiacountyfla.com/hosting/rest/services

## Page 110

Indian River
https://services9.arcgis.com/M0DpVhTwTZ42jNsw/ArcGIS/rest/s
ervices
Lake
https://gis.lakecountyfl.gov/lakegis/rest/services
Lake
https://services1.arcgis.com/7LNyA2emK1umjjot/arcgis/rest/servic
es
Lake
https://tiles.arcgis.com/tiles/7LNyA2emK1umjjot/arcgis/rest/servic
es
Miami-Dade
https://gisms.miamidade.gov/arcgis/rest/services
Miami-Dade
https://gisweb.miamidade.gov/arcgis/rest/services
Miami-Dade
https://imageserverintra.miamidade.gov/arcgis/rest/services
Miami-Dade
https://services.arcgis.com/8Pc9XBTAsYuxx9Ny/arcgis/rest/servic
es
Miami-Dade
https://tiles.arcgis.com/tiles/8Pc9XBTAsYuxx9Ny/arcgis/rest/servi
ces
Daytona Beach
https://gis2.codb.us/arcgis/rest/services
DeSoto
ArcGIS table of contents hidden behind Geocortex software
Dixie
Schneider Geospatial - ArcGIS server address is not public
Duval
See City of Jacksonville
Escambia
https://gismaps.myescambia.com/arcgis/rest/services
Escambia
https://maps.escpa.org/arcgis1/rest/services
Escambia
https://arcgis5.roktech.net/arcgis/rest/services/escambia
Flagler
https://gis.flaglercounty.gov/hosting/rest/services
Flagler
https://services3.arcgis.com/hSKL9bYjhP4rHxSD/arcgis/rest/servi
ces
Flagler
https://tiles.arcgis.com/tiles/hSKL9bYjhP4rHxSD/arcgis/rest/servi
ces
Franklin
https://gis.arpc.org/server/rest/services
See /Hosted/Franklin...
Franklin
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Franklin_County_Zoning_Map_WFL1/FeatureServer
Go to the top and search for ‘Franklin’
Franklin
https://tiles.arcgis.com/tiles/N3lCn6dEKCL6LidU/arcgis/rest/servi
ces/Franklin_Floodzone/MapServer
Gadsden
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Gadsden_FLUM/FeatureServer
Go to the top and search for ‘Gadsden’

## Page 111

Gadsden
https://tiles.arcgis.com/tiles/N3lCn6dEKCL6LidU/arcgis/rest/servi
ces/Gadsden_1988/MapServer
Gilchrist
Schneider - Schneider Geospatial - ArcGIS server address is not
public
Glades
https://services6.arcgis.com/90Aakxb3SLGcQGor/arcgis/rest/servi
ces
Gulf
https://arcgis4.roktech.net/arcgis/rest/services/gulf
Gulf
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Gulf_FLUM/FeatureServer
Go to the top and search for ‘Gulf’
Hamilton
Schneider - Schneider Geospatial - ArcGIS server address is not
public
Hardee
https://gis.hardeecounty.net/arcgis/rest/services
Hendry
https://services7.arcgis.com/8l7Qq5t0CPLAJwJK/arcgis/rest/servic
es
Hendry
https://tiles.arcgis.com/tiles/8l7Qq5t0CPLAJwJK/arcgis/rest/servic
es
Hernando
_ttps://server.hernandopa-fl.us/server/rest/services    dead link 1
Highlands
https://gis.highlandsfl.gov/server/rest/services
Highlands
https://services2.arcgis.com/xEhz4K4uxbjGXOPE/ArcGIS/rest/ser
vices
Highlands
https://tiles.arcgis.com/tiles/xEhz4K4uxbjGXOPE/arcgis/rest/servi
ces
Hillsborough
https://gis.hcpafl.org/arcgis/rest/services
Hillsborough
https://maps.hillsboroughcounty.org/arcgis/rest/services
Hillsborough
https://services.arcgis.com/apTfC6SUmnNfnxuF/arcgis/rest/servic
es
Hillsborough
https://tiles.arcgis.com/tiles/apTfC6SUmnNfnxuF/arcgis/rest/servi
ces
Hillsborough
https://services5.arcgis.com/Xh8HJhF6DUfG4Yjc/arcgis/rest/servi
ces
County sheriff
Hillsborough
https://services5.arcgis.com/YTApDBs0YanBdxkq/arcgis/rest/serv
ices
County Aviation Authority
Hillsborough
https://tiles.arcgis.com/tiles/YTApDBs0YanBdxkq/arcgis/rest/serv
ices
Holmes
          https://services6.arcgis.com/JuJ3otBHQoYlrmJI/arcgis/rest/services

## Page 112

Holmes
          https://tiles.arcgis.com/tiles/JuJ3otBHQoYlrmJI/arcgis/rest/services
Indian River
https://gisportal.ircgov.com/server3/rest/services
Table of contents disabled
Jackson
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Jackson_FLUM/FeatureServer
Go to the top and search for ‘Jackson’
Jackson
https://tiles.arcgis.com/tiles/N3lCn6dEKCL6LidU/arcgis/rest/servi
ces/Jackson_Floodzone/MapServer
Jefferson
https://webmap.trueautomation.com/arcgis/rest/services/JeffersonP
AMapSearchNoLabels/MapServer
Jefferson
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Jefferson_FLUM/FeatureServer
Go to the top and search for ‘Jefferson’
Jefferson
https://tiles.arcgis.com/tiles/N3lCn6dEKCL6LidU/arcgis/rest/servi
ces/Jefferson_Floodzone/MapServer
Lafayette
No GIS found
Lake
https://gis.lakecountyfl.gov/lakegis/rest/services
Lee
https://gismapserver.leegov.com/gisserver910/rest/services
Lee
https://gisimageserver.leegov.com/imageserver/rest/services
Lee
https://services2.arcgis.com/LvWGAAhHwbCJ2GMP/ArcGIS/rest
/services
Leon
https://interraster.leoncountyfl.gov/interraster/rest/services
Leon
https://intervector.leoncountyfl.gov/intervector/rest/services
Leon
https://cotinter.leoncountyfl.gov/cotinter/rest/services
Leon
https://tlcaccela.leoncountyfl.gov/accela/rest/services
Leon
https://services.arcgis.com/ptvDyBs1KkcwzQNJ/arcgis/rest/servic
es
Leon
https://tiles.arcgis.com/tiles/ptvDyBs1KkcwzQNJ/arcgis/rest/servic
es
Levy
https://services.arcgis.com/Y6ubaOgtVe9iI9sU/arcgis/rest/services
Liberty
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Liberty_FLUM/FeatureServer
Go to the top and search for ‘Liberty’

## Page 113

Liberty
https://tiles.arcgis.com/tiles/N3lCn6dEKCL6LidU/arcgis/rest/servi
ces/Liberty_Floodzone/MapServer
Madison
WMS server
Manatee
_ttps://www.mymanatee.org/arcgis04/rest/services     dead link 1
Manatee
https://www.mymanatee.org/gisbads/rest/services
Manatee
https://services1.arcgis.com/t03WDvnSR7gSDOB2/arcgis/rest/ser
vices
Manatee
https://tiles.arcgis.com/tiles/t03WDvnSR7gSDOB2/arcgis/rest/serv
ices
Marion
https://gis.marionfl.org/public/rest/services
Marion
https://gis.marionfl.org/server/rest/services
Marion
https://gis.marionfl.org/image/rest/services
Marion
https://gis.marionfl.org/erp/rest/services
Marion
https://services1.arcgis.com/oMGpBoZpy1Db2sAl/arcgis/rest/servi
ces
Marion
https://tiles.arcgis.com/tiles/oMGpBoZpy1Db2sAl/arcgis/rest/servi
ces
Martin
https://geoweb.martin.fl.us/arcgis/rest/services
Martin
https://geoweb.martin.fl.us/raster/rest/services
Martin
https://services.arcgis.com/DlijwkpixeIOmhue/arcgis/rest/services
Martin
https://tiles.arcgis.com/tiles/DlijwkpixeIOmhue/arcgis/rest/services
Miami-Dade
http://imageserverintra.miamidade.gov/arcgis/rest/services
Miami-Dade
_ttps://fhm.miamidade.gov/arcgis/rest/services
dead link 1
Miami-Dade
https://gisms.miamidade.gov/arcgis/rest/services
Miami-Dade
https://gisweb.miamidade.gov/arcgis/rest/services
Miami-Dade
https://gisws.miamidade.gov/arcgis/rest/services
Miami-Dade
https://giswspro.miamidade.gov/arcgis/rest/services
Miami-Dade
https://imageserverintra.miamidade.gov/arcgis/rest/services
Miami-Dade
https://services.arcgis.com/8Pc9XBTAsYuxx9Ny/arcgis/rest/servic
es
Miami-Dade
https://tiles.arcgis.com/tiles/8Pc9XBTAsYuxx9Ny/arcgis/rest/servi
ces
Monroe
https://mcgis4.monroecounty-fl.gov/public/rest/services
Nassau
https://maps.nassauflpa.com/ncflpa_arcgis/rest/services
Nassau
https://services5.arcgis.com/F73IhFZbCCYUexxB/ArcGIS/rest/ser
vices
Nassau
https://tiles.arcgis.com/tiles/F73IhFZbCCYUexxB/arcgis/rest/servi
ces

## Page 114

Okaloosa
https://ags.myokaloosa.com/arcgis/rest/services
Okaloosa
https://gis.myokaloosa.com/arcgis/rest/services
Okaloosa
https://okgis.myokaloosa.com/arcgis/rest/services
Okaloosa
https://services7.arcgis.com/lOFQguHNarTIBTRU/ArcGIS/rest/ser
vices
Okeechobee
WMS server
Orange
https://ocgis4.ocfl.net/arcgis/rest/services
Orange
https://services1.arcgis.com/0U8EQ1FrumPeIqDb/ArcGIS/rest/ser
vices
Orange
https://tiles.arcgis.com/tiles/0U8EQ1FrumPeIqDb/arcgis/rest/servi
ces
Osceola
https://gis.osceola.org/hosting/rest/services
Table of contents disabled
Osceola
https://paags.property-appraiser.org/server/rest/services
Palm Beach
https://maps.co.palm-beach.fl.us/arcgis/rest/services
Palm Beach
https://gis-apps.lake.k12.fl.us/server/rest/services
Palm Beach
https://services1.arcgis.com/ZWOoUZbtaYePLlPw/ArcGIS/rest/se
rvices
Palm Beach
https://tiles.arcgis.com/tiles/ZWOoUZbtaYePLlPw/arcgis/rest/serv
ices
Pasco
https://pascogis.pascocountyfl.net/gisweb/rest/services
Pasco
https://services6.arcgis.com/Mo4MddfRHpFwT7UF/ArcGIS/rest/s
ervices
Pasco
https://tiles.arcgis.com/tiles/Mo4MddfRHpFwT7UF/arcgis/rest/ser
vices
Pinellas
https://egis.pinellas.gov/gis/rest/services
Pinellas
https://services.arcgis.com/f5HgUpxURgEzTccH/arcgis/rest/servic
es
Polk
https://gis.polk-county.net/image/rest/services
Polk
https://services1.arcgis.com/YMN4aIYxPejzDjo2/ArcGIS/rest/serv
ices
Polk
https://tiles.arcgis.com/tiles/YMN4aIYxPejzDjo2/arcgis/rest/servic
es
Putnam
https://gis.putnam-fl.com/arcserver/rest/services
Putnam
https://services1.arcgis.com/YZc1OyqL6jbIOeOv/arcgis/rest/servic
es
Putnam
https://tiles.arcgis.com/tiles/YZc1OyqL6jbIOeOv/arcgis/rest/servic
es

## Page 115

St. Johns
https://www.gis.sjcfl.us/portal_sjcgis/rest/services
St. Johns
https://maps.sjcpw.us/pwags/rest/services
St. Johns
https://services.arcgis.com/EzsazWbpzy8Fv5VV/arcgis/rest/servic
es
St. Johns
https://tiles.arcgis.com/tiles/EzsazWbpzy8Fv5VV/arcgis/rest/servi
ces
St. Johns
https://services2.arcgis.com/CgQSNki2DdB53FbU/ArcGIS/rest/ser
vices
St. Johns
https://tiles.arcgis.com/tiles/CgQSNki2DdB53FbU/arcgis/rest/servi
ces
St. Lucie
https://map.paslc.gov/arcgis/rest/services
St. Lucie
https://slcgis.stlucieco.gov/hosting/rest/services
St. Lucie
https://services1.arcgis.com/2fk66zq5sgMBsD3C/ArcGIS/rest/serv
ices
St. Lucie
https://tiles.arcgis.com/tiles/2fk66zq5sgMBsD3C/arcgis/rest/servic
es
St. Lucie
https://services6.arcgis.com/UZU5YYWrSlE9YWnx/ArcGIS/rest/
services
Assessor
St. Lucie
https://tiles.arcgis.com/tiles/UZU5YYWrSlE9YWnx/arcgis/rest/ser
vices
Santa Rosa
_ttps://gis.santarosa.fl.gov/arcgis/rest/services
dead link 1
Santa Rosa
https://arcgis5.roktech.net/arcgis/rest/services/santarosa
Santa Rosa
          https://services.arcgis.com/Eg4L1xEv2R3abuQd/arcgis/rest/services
Santa Rosa
https://tiles.arcgis.com/tiles/Eg4L1xEv2R3abuQd/arcgis/rest/servic
es
Sarasota
https://services3.arcgis.com/AWDwYUpli8WqpWxQ/arcgis/rest/s
ervices
Sarasota
https://tiles.arcgis.com/tiles/AWDwYUpli8WqpWxQ/arcgis/rest/se
rvices
Sarasota
          https://services3.arcgis.com/icrWMv7eBkctFu1f/arcgis/rest/services
Sarasota
           https://tiles.arcgis.com/tiles/icrWMv7eBkctFu1f/arcgis/rest/services
Seminole
https://seminolearcgis.seminolecountyfl.gov:6443/arcgis/rest/servic
es
Seminole
https://arcgis5.roktech.net/arcgis/rest/services/SeminoleFL
Seminole
           https://services3.arcgis.com/n4VF6lyYfB5kizho/arcgis/rest/services
Seminole
           https://tiles.arcgis.com/tiles/n4VF6lyYfB5kizho/arcgis/rest/services
Sumter
https://gis.sumtercountyfl.gov/sumtergis/rest/services
Suwannee
WMS server
Taylor
Schneider Geospatial - ArcGIS server address is not public

## Page 116

Union
WMS server
Volusia
https://maps1.vcgov.org/arcgis/rest/services
Volusia
https://maps2.vcgov.org/arcgis/rest/services
Volusia
https://maps5.vcgov.org/arcgis/rest/services
Volusia
https://services.arcgis.com/YvSMAk2zZNXXVujI/arcgis/rest/servi
ces
Volusia
https://tiles.arcgis.com/tiles/YvSMAk2zZNXXVujI/arcgis/rest/serv
ices
Wakulla
https://services9.arcgis.com/vAltLjtfYIJc7pDt/arcgis/rest/services
Wakulla
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Wakulla_FLUM/FeatureServer
Go to the top and search for ‘’
Walton
https://services1.arcgis.com/TaXHPwWfIMuzJ7Ov/ArcGIS/rest/se
rvices
Walton
https://tiles.arcgis.com/tiles/TaXHPwWfIMuzJ7Ov/arcgis/rest/serv
ices
Washington
https://services2.arcgis.com/xDFo56nFuq1SBnBw/ArcGIS/rest/ser
vices/WashingtonParcelsAGOL/FeatureServer
Florida City, Town, Village, etc GIS Servers
Alford
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Alford_FLUM/FeatureServer
Go to the top and search for ‘Alford’
Altha
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Altha_FLUM/FeatureServer
Go to the top and search for ‘Altha’
Apalachicola
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Apalachicola_FLUM/FeatureServer
Go to the top and search for ‘Apalachicola’
Boca-Raton
https://bocagis.ci.boca-raton.fl.us/arcgis/rest/services
Boca-Raton
https://bocagis.ci.boca-raton.fl.us/arcgissql/rest/services
Bradenton
https://services6.arcgis.com/wl0q8tN2gn8MMx1p/ArcGIS/rest/ser
vices
Bradenton
https://tiles.arcgis.com/tiles/wl0q8tN2gn8MMx1p/arcgis/rest/servi
ces
Blountstown
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Blountstown_FLUM/FeatureServer

## Page 117

Go to the top and search for ‘Blountstown’
Bristol
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Bristol_FLUM/FeatureServer
Go to the top and search for ‘Bristol’
Campbellton
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Campbellton_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Campbellton’
Cape Coral
https://capeims.capecoral.gov/arcgis/rest/services
Cape Coral
https://services1.arcgis.com/MZl3VrkZJOk1VhY4/ArcGIS/rest/ser
vices
Cape Coral
https://tiles.arcgis.com/tiles/MZl3VrkZJOk1VhY4/arcgis/rest/servi
ces
Carrabelle
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Carrabelle_FLUM/FeatureServer
Go to the top and search for ‘Carrabelle’
Clermont
https://services1.arcgis.com/IXTu1IfQNbdPjhQW/ArcGIS/rest/ser
vices
Coral Gables
https://services1.arcgis.com/ug7Y0GY6kYE0tf0p/arcgis/rest/servic
es
Coral Gables
https://tiles.arcgis.com/tiles/ug7Y0GY6kYE0tf0p/arcgis/rest/servic
es
Coral Springs
https://services1.arcgis.com/mXWZ2wsX9klsJAJY/arcgis/rest/serv
ices
Coral Springs
https://tiles.arcgis.com/tiles/mXWZ2wsX9klsJAJY/arcgis/rest/serv
ices
Cottondale
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Cottondale_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Cottondale’
Cutler Bay
https://tcbgis.cutlerbay-fl.gov/arcgisdmz/rest/services
Dayton Beach
https://arcgis4.roktech.net/arcgis/rest/services/DaytonaBeach
Dayton Beach
https://arcgis5.roktech.net/arcgis/rest/services/DaytonaBeach
Dayton Beach
https://services2.arcgis.com/2rIG17xLqeJd2jOX/ArcGIS/rest/servi
ces
Deland
https://services.deland.org/arcgis/rest/services

## Page 118

Deland
_ttps://services1.arcgis.com/QWKU48xtAd3DKfwt/arcgis/rest/ser
vices
dead link 1
Deltona
https://arcgis4.roktech.net/arcgis/rest/services/deltona
Deltona
https://arcgis5.roktech.net/arcgis/rest/services/deltona/City_of_Delt
ona/MapServer
Doral
https://gis.cityofdoral.com/arcgis/rest/services
Doral
https://maps-stage.cityofdoral.com/arcgis/rest/services
Doral
https://services.arcgis.com/rMDYWPzHhH9byMxO/arcgis/rest/ser
vices
Doral
https://tiles.arcgis.com/tiles/rMDYWPzHhH9byMxO/arcgis/rest/se
rvices
Dunedin
https://services7.arcgis.com/KSOLN1N5mvPERkpg/ArcGIS/rest/s
ervices
Dunedin
https://tiles.arcgis.com/tiles/KSOLN1N5mvPERkpg/arcgis/rest/ser
vices
Fort Lauderdale
https://gis.fortlauderdale.gov/arcgis/rest/services
Fort Lauderdale
https://services2.arcgis.com/82LxCEC4N4AxRpwc/ArcGIS/rest/se
rvices
Fort Lauderdale
https://tiles.arcgis.com/tiles/82LxCEC4N4AxRpwc/arcgis/rest/serv
ices
Fort Myers
https://cfmgis.cityftmyers.com/arcgis/rest/services
Fort Myers
https://services1.arcgis.com/T37xMyv8DRNzouiI/ArcGIS/rest/ser
vices
Fort Pierce
https://services1.arcgis.com/oDRzuf2MGmdEHAbQ/ArcGIS/rest/s
ervices
Fort Walton Beach
https://gis.fwb.org/arcgis/rest/services
Fort Walton Beach
https://services2.arcgis.com/DsE4m2IKL5jJE7JP/ArcGIS/rest/serv
ices
Gainesville
https://services1.arcgis.com/MiBZ4u97DWldovjI/arcgis/rest/servic
es
Gainesville
https://tiles.arcgis.com/tiles/MiBZ4u97DWldovjI/arcgis/rest/servic
es
Gainesville
https://services2.arcgis.com/Zzhtlau4ccHkQgTu/ArcGIS/rest/servi
ces
Gainesville
           https://tiles.arcgis.com/tiles/Zzhtlau4ccHkQgTu/arcgis/rest/services
Graceville
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Graceville_FLUM_WFL1/FeatureServer

## Page 119

Go to the top and search for ‘Graceville’
Grand Ridge
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Grand_Ridge_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Grand_Ridge’
Greenacres
https://services8.arcgis.com/8uR4EgOk3nsP1tP5/ArcGIS/rest/servi
ces
Greensboro
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Greensboro_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Greensboro’
Greenwood
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Greenwood_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Greenwood’
Gretna
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Gretna_FLUM/FeatureServer
Go to the top and search for ‘Gretna’
Groveland
https://services.arcgis.com/xEgvNONu6FbcEW52/arcgis/rest/servi
ces
Havana
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Havana_FLUM/FeatureServer
Go to the top and search for ‘Havana’
Hillsborough
See Hillsborough county
Hollywood
https://maps.hollywoodfl.org/arcgis/rest/services
Table of contents disabled
Jacksonville
https://maps.coj.net/coj/rest/services
Jacksonville
https://gis.jtafla.com/arcgis/rest/services
Transportation Authority
Jacksonville
https://services.arcgis.com/x6HRgAVTK9nVHvrn/arcgis/rest/servi
ces
Transportation Authority
Jacksonville
https://tiles.arcgis.com/tiles/x6HRgAVTK9nVHvrn/arcgis/rest/ser
vices
Jacksonville
https://services1.arcgis.com/NXfNVaFp7QMxnE3j/ArcGIS/rest/se
rvices
Jacksonville
https://tiles.arcgis.com/tiles/NXfNVaFp7QMxnE3j/arcgis/rest/serv
ices

## Page 120

Jacob City
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Jacob_City_FLUM/FeatureServer
Go to the top and search for ‘Jacob_City’
Jupiter
https://gisweb.jupiter.fl.us/arcgis/rest/services
Jupiter
https://services1.arcgis.com/pQrVKbO4a0hhA72L/arcgis/rest/servi
ces
Jupiter
https://tiles.arcgis.com/tiles/pQrVKbO4a0hhA72L/arcgis/rest/servi
ces
Kissimmee
https://cw.kissimmee.gov/arcgis/rest/services
Lakeland
https://gismims.lakelandgov.net/portal/rest/services
Lakeland
https://services1.arcgis.com/mcbQY5xNGGGM1vBX/ArcGIS/rest
/services
Lakeland
https://tiles.arcgis.com/tiles/mcbQY5xNGGGM1vBX/arcgis/rest/s
ervices
Largo
https://services2.arcgis.com/nYo0QaOOsjBkTG7Y/arcgis/rest/serv
ices
Leesburg
https://map.leesburgflorida.gov/arcgis/rest/services
Malone
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Malone_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Malone’
Marco Island
https://gis.cityofmarcoisland.com/arcgis/rest/services
Marco Island
https://services.arcgis.com/4DF23ogcas8LJrIo/arcgis/rest/services
Marco Island
https://tiles.arcgis.com/tiles/4DF23ogcas8LJrIo/arcgis/rest/services
Marianna
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Marianna_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Marianna’
Marion
https://www.pa.marion.fl.us/arcgis/rest/services
Miami
https://gis.miami.gov/gis/rest/services
Miami
See Miami-Dade in the county section
Miami Beach
https://services3.arcgis.com/5KQFejGl1FEovEL6/ArcGIS/rest/serv
ices
Miami Beach
https://tiles.arcgis.com/tiles/5KQFejGl1FEovEL6/arcgis/rest/servic
es

## Page 121

Midway
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Midway_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Midway’
Miramar
https://services6.arcgis.com/dAtAhTJ12QXYHJYN/ArcGIS/rest/s
ervices
Miramar
https://tiles.arcgis.com/tiles/dAtAhTJ12QXYHJYN/arcgis/rest/ser
vices
Miramar
https://services7.arcgis.com/mYvLp9uIABiE1Eq6/arcgis/rest/servi
ces
Monticello
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Monticello_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Monticello’
Naples
https://g.naplesgov.com/arcgis/rest/services
North Bay
https://arcgis4.roktech.net/arcgis/rest/services/northbayvillage
North Bay
https://arcgis5.roktech.net/arcgis/rest/services/northbayvillage
North Lauderdale
https://cnlgis.nlauderdale.org/cnlent/rest/services
North Lauderdale
https://services8.arcgis.com/NyFoaw79e9c3wmAP/ArcGIS/rest/ser
vices
North Miami
https://services.arcgis.com/5SQTP6IEhcc1RTIi/arcgis/rest/services
North Miami Beach   https://services.arcgis.com/RGxZxInkfRiVFrU7/arcgis/rest/services
North Port
https://services3.arcgis.com/ziIiwjkPln8Myswu/ArcGIS/rest/servic
es
Ocala
https://gis.ocalafl.org/arcgis/rest/services
Orlando
https://gis.orlando.gov/server/rest/services
Orlando
https://services5.arcgis.com/mMuoPCaIYD4wEgDl/ArcGIS/rest/se
rvices
Orlando
https://tiles.arcgis.com/tiles/mMuoPCaIYD4wEgDl/arcgis/rest/serv
ices
Oviedo
https://services.arcgis.com/0EfLIvtSLPR9PKI2/arcgis/rest/services
Oviedo
           https://tiles.arcgis.com/tiles/0EfLIvtSLPR9PKI2/arcgis/rest/services
Palm Bay
https://gis.palmbayflorida.org/arcgis/rest/services
Palm Coast
https://services1.arcgis.com/tpnsCwhQRDqwL3mq/ArcGIS/rest/se
rvices

## Page 122

Palm Coast
https://tiles.arcgis.com/tiles/tpnsCwhQRDqwL3mq/arcgis/rest/serv
ices
Palmetto
https://services1.arcgis.com/L2Neyx2ylSeTBS0F/ArcGIS/rest/serv
ices
Palmetto
https://tiles.arcgis.com/tiles/L2Neyx2ylSeTBS0F/arcgis/rest/servic
es
Panama City Beach
https://services7.arcgis.com/HMHYRsYOvuxpp8zD/arcgis/rest/ser
vices
Panama City Beach
https://tiles.arcgis.com/tiles/HMHYRsYOvuxpp8zD/arcgis/rest/ser
vices
Parkland
https://services6.arcgis.com/dEuVlS3WgXNFkGxk/ArcGIS/rest/se
rvices
Pembroke Park
https://services3.arcgis.com/vtilYbC3YeF6EBJ1/ArcGIS/rest/servi
ces
Pensacola
https://arcgis4.roktech.net/arcgis/rest/services/Pensacola
Pensacola
https://arcgis5.roktech.net/arcgis/rest/services/Pensacola
Plantation

https://pgis.plantation.org/arcgis/rest/services
Port Orange
https://services1.arcgis.com/EHJIZRZ77WzgIElO/arcgis/rest/servi
ces
Port St. Joe
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Port_St_Joe_FLUM/FeatureServer
Go to the top and search for ‘Port_St_Joe’
Port St. Lucie
https://services1.arcgis.com/YdUP5V6WwzeG8T8r/arcgis/rest/ser
vices
Port St. Lucie
https://tiles.arcgis.com/tiles/YdUP5V6WwzeG8T8r/arcgis/rest/ser
vices
Quincy
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Quincy_FLUM/FeatureServer
Go to the top and search for ‘Quincy’
St. Augustine
https://services.arcgis.com/2HXAtOKdBRSMj8is/arcgis/rest/servi
ces
St. Augustine
https://tiles.arcgis.com/tiles/2HXAtOKdBRSMj8is/arcgis/rest/servi
ces
St. Petersburg
https://egis.stpete.org/arcgis/rest/services

## Page 123

St. Petersburg
https://services2.arcgis.com/9qPLjNtocjo438CJ/arcgis/rest/services
Sanibel
https://services7.arcgis.com/OnCt8XFWOgmkvMJE/ArcGIS/rest/s
ervices
Sarasota
          https://services3.arcgis.com/icrWMv7eBkctFu1f/arcgis/rest/services
Sarasota
          https://tiles.arcgis.com/tiles/icrWMv7eBkctFu1f/arcgis/rest/services
Sebastian
https://services3.arcgis.com/NkT47EHQsmn9GxB3/ArcGIS/rest/se
rvices
Sebastian
https://tiles.arcgis.com/tiles/NkT47EHQsmn9GxB3/arcgis/rest/ser
vices
Seminole
https://arcgis4.roktech.net/arcgis/rest/services/SeminoleFL
Seminole
https://arcgis5.roktech.net/arcgis/rest/services/SeminoleFL
Seminole
           https://services3.arcgis.com/n4VF6lyYfB5kizho/arcgis/rest/services
Seminole
           https://tiles.arcgis.com/tiles/n4VF6lyYfB5kizho/arcgis/rest/services
Sopchoppy
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Sopchoppy_FLUM_WFL1/FeatureServer
Go to the top and search for ‘Sopchoppy’
St Marks
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/St_Marks_FLUM_WFL1/FeatureServer
Go to the top and search for ‘St_Marks’
Stuart
https://services.arcgis.com/RyoFD3Lw9KSERnvQ/arcgis/rest/servi
ces
Stuart
https://tiles.arcgis.com/tiles/RyoFD3Lw9KSERnvQ/arcgis/rest/ser
vices
Sunny Isles Beach
https://arcgis5.roktech.net/arcgis/rest/services/SunnyIsles
Sunny Isles Beach
https://services9.arcgis.com/zfgyi0Gr8i5waYkS/ArcGIS/rest/servic
es
Sunny Isles Beach
https://tiles.arcgis.com/tiles/zfgyi0Gr8i5waYkS/arcgis/rest/services

Tallahassee
See Leon County
Tamarac
https://services7.arcgis.com/IchrybNtWtpg1fNo/ArcGIS/rest/servic
es
Tamarac
https://tiles.arcgis.com/tiles/IchrybNtWtpg1fNo/arcgis/rest/services
Tampa
https://arcgis.tampagov.net/arcgis/rest/services
Tampa
https://gis.tpcmaps.org/arcgis/rest/services
Tampa
https://services1.arcgis.com/IbNXlmt2RVVRCZ6M/ArcGIS/rest/s
ervices

## Page 124

Titusville
           https://services.arcgis.com/hAw9Xok8IFbYejf4/arcgis/rest/services
Titusville
https://tiles.arcgis.com/tiles/hAw9Xok8IFbYejf4/arcgis/rest/servic
es
Venice
https://geoport.venicefl.gov/server/rest/services
Vero Beach
https://services1.arcgis.com/mK9abRqiJFkUgbPZ/arcgis/rest/servi
ces
Vero Beach
https://tiles.arcgis.com/tiles/mK9abRqiJFkUgbPZ/arcgis/rest/servi
ces
Wellington
https://gis01.wellingtonfl.gov/imagery/rest/services
West Palm Beach
https://wpbgisportal.wpb.org/server/rest/services
West Palm Beach
https://services1.arcgis.com/RTiKiFNGzgAobBzy/ArcGIS/rest/ser
vices
West Palm Beach
https://tiles.arcgis.com/tiles/RTiKiFNGzgAobBzy/arcgis/rest/servi
ces
Weston
https://services3.arcgis.com/4n2k7CxEiosr7NFO/arcgis/rest/servic
es
Wewahitchka
https://services8.arcgis.com/N3lCn6dEKCL6LidU/ArcGIS/rest/ser
vices/Wewahitchka_FLUM/FeatureServer
Go to the top and search for ‘Wewahitchka’
Winter Springs
https://services5.arcgis.com/hbtBppF7t3PpouVf/ArcGIS/rest/servic
es
Winter Springs           https://tiles.arcgis.com/tiles/hbtBppF7t3PpouVf/arcgis/rest/services
Georgia State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Georgia Open Data
Website: https://data.georgia.gov
SSL problem
Website: https://data-hub.gio.georgia.gov
Georgia Department of Natural Resources
Website: https://gadnr.org
GIS: https://services6.arcgis.com/9QlSLDqa0P1cHLhu/ArcGIS/rest/services
Wildlife Resources Division
GIS: https://tiles.arcgis.com/tiles/9QlSLDqa0P1cHLhu/arcgis/rest/services
Georgia Emergency Management Agency
Website: https://gema.georgia.gov

## Page 125

GIS: https://gis.gema.ga.gov/ags/rest/services
GIS: https://services1.arcgis.com/2iUE8l8JKrP2tygQ/arcgis/rest/services
Georgia Department of Public Health
Website: https://dph.georgia.gov
GIS: https://services6.arcgis.com/t7DA9BjRElflTVpw/ArcGIS/rest/services
Georgia Department of Transportation
Website: https://www.dot.ga.gov
GIS: https://egis.dot.ga.gov/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://egisp.dot.ga.gov/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://rnhp.dot.ga.gov/hosting/rest/services
GIS: https://services3.arcgis.com/6RaeG1zfsIoM9Lze/ArcGIS/rest/services
Georgia elections
GIS: https://services5.arcgis.com/U7qTOvYXC7ZGLra4/arcgis/rest/services
Georgia Forestry Commission
Website: https://gatrees.org
GIS: https://services2.arcgis.com/iXA1dC6ldRMKRwra/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/iXA1dC6ldRMKRwra/arcgis/rest/services
Georgia Coastal Management Program
Website: https://coastalgadnr.org/CoastalManagement
GIS: https://services3.arcgis.com/r9yUQy2Mlp8XERvO/ArcGIS/rest/services
Georgia various layers
GIS: https://gfcarcserver.gfc.state.ga.us/server/rest/services
GIS: https://services2.arcgis.com/Gqyymy5JISeLzyNM/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Gqyymy5JISeLzyNM/arcgis/rest/services
GIS: https://services7.arcgis.com/Za9Nk6CPIPbvR1t7/ArcGIS/rest/services
University of Georgia - Institute of Government
Website: https://cviog.uga.edu/index.html
GIS: https://maps.itos.uga.edu/arcgis/rest/services
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
University of Georgia - Coastal Hazards
Website: https://gacoast.uga.edu/outreach/programs/coastal-hazards
GIS: https://services6.arcgis.com/Fr1St8uKGFocXUEL/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Fr1St8uKGFocXUEL/arcgis/rest/services
Georgia Tech

## Page 126

Website: https://www.gatech.edu
GIS: https://geospat.gatech.edu/arcgis/rest/services
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Georgia Regional
Georgia Coastal Regional Commission
Website: https://www.coastalrc.ga.gov
GIS: https://maps.crc.ga.gov/crcarcgis/rest/services
8-1-2023 No tiled data
Atlanta Regional Commission
Website: https://atlantaregional.org/
Open data portal: https://opendata.atlantaregional.com
GIS: https://arcgis.atlantaregional.com/arcgis/rest/services
8-1-2023 No tiled data
Metropolitan Atlanta Rapid Transit Authority
Website: https://www.itsmarta.com
GIS: https://services5.arcgis.com/xI2JERI5PvawmoWH/ArcGIS/rest/services
Middle Georgia Regional Commission
Website: https://www.middlegeorgiarc.org
GIS: _ttps://mgrcmaps.org/arcgis/rest/services
dead link 1
8-1-2023 No tiled data
Southern Georgia Regional Commission
Website: https://www.sgrc.us
GIS: https://www.sgrcmaps.com/arcgis/rest/services
8-1-2023 No tiled data
GIS: https://services5.arcgis.com/HA2thkMWRBDb77XN/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/HA2thkMWRBDb77XN/arcgis/rest/services
Tucker-Northlake Community Improvement District
Website: https://tuckernorthlakecid.com
GIS: https://services7.arcgis.com/Nyy2jc5etPxstAcD/ArcGIS/rest/services
Georgia County GIS Servers
All counties are listed.
Appling
Schneider Geospatial - ArcGIS server address is not public
Athens
See Clarke county
Atkinson
https://www.sgrcmaps.com/alma/rest/services/Atkinson

## Page 127

Bacon
Schneider Geospatial - ArcGIS server address is not public
Baker
Schneider Geospatial - ArcGIS server address is not public
Baldwin
https://services7.arcgis.com/Da8HZMsU25Hzzob3/arcgis/rest/serv
ices
Banks
Schneider Geospatial - ArcGIS server address is not public
Barrow
https://services5.arcgis.com/OVFGXfRTCVcPwl55/arcgis/rest/ser
vices
Bartow
https://services.arcgis.com/0tQ9yX5b2VG5RHei/arcgis/rest/servic
es
Ben Hill
https://www.sgrcmaps.com/alma/rest/services/BenHill
Berrien
https://www.sgrcmaps.com/alma/rest/services/Berrien
Bibb
https://services2.arcgis.com/zPFLSOZ5HzUzzTQb/ArcGIS/rest/se
rvices
Bibb
https://tiles.arcgis.com/tiles/zPFLSOZ5HzUzzTQb/arcgis/rest/serv
ices
Bleckley
Schneider Geospatial - ArcGIS server address is not public
Brantley
Schneider Geospatial - ArcGIS server address is not public
Brooks
https://www.sgrcmaps.com/alma/rest/services/Brooks
Bryan
https://bryangis.bryan-county.org/arcgis/rest/services
Bulloch
Schneider Geospatial - ArcGIS server address is not public
Burke
Schneider Geospatial - ArcGIS server address is not public
Butts
_ttps://wfs.schneidercorp.com/arcgis/rest/services/ButtsCountyGA
_WFS/MapServer
dead link 1
Calhoun
https://gis.calhouncounty.org/arcgis5/rest/services
Camden
https://maps.crc.ga.gov/crcarcgis/rest/services/Camden
Camden
https://maps.crc.ga.gov/crcarcgis/rest/services/CamdenCD
Camden
https://maps.crc.ga.gov/crcarcgis/rest/services/CamdenCountyVoti
ng
Camden
https://maps.crc.ga.gov/crcarcgis/rest/services/CamdenSchools

## Page 128

Camden
https://maps.crc.ga.gov/crcarcgis/rest/services/Geodata_Camden
Candler
Schneider Geospatial - ArcGIS server address is not public
Carroll
Schneider Geospatial - ArcGIS server address is not public
Catoosa
Schneider Geospatial - ArcGIS server address is not public
Charlton
Schneider Geospatial - ArcGIS server address is not public
Chatham
https://pub.sagis.org/arcgis/rest/services/ChathamCounty
Chatham
https://pub.sagis.org/arcgis/rest/services/CCSheriff
Chatham
https://maps.crc.ga.gov/crcarcgis/rest/services/Chatham
Chattahoochee
Schneider Geospatial - ArcGIS server address is not public
Chattooga
Schneider Geospatial - ArcGIS server address is not public
Cherokee
https://gis.cherokeega.com/arcgis/rest/services        SSL problem
Clarke
https://enigma.accgov.com/server/rest/services
Clarke
https://services2.arcgis.com/xSEULKvB31odt3XQ/ArcGIS/rest/ser
vices
Clarke
https://tiles.arcgis.com/tiles/xSEULKvB31odt3XQ/arcgis/rest/servi
ces
Clay
Schneider Geospatial - ArcGIS server address is not public
Clayton
https://services5.arcgis.com/m528W8U8YDYeMPrQ/arcgis/rest/se
rvices
Clayton
https://tiles.arcgis.com/tiles/m528W8U8YDYeMPrQ/arcgis/rest/se
rvices
Clinch
Schneider Geospatial - ArcGIS server address is not public
Cobb
https://services.arcgis.com/HYLRafMc4Ux6DA8c/arcgis/rest/servi
ces
Cobb
https://tiles.arcgis.com/tiles/HYLRafMc4Ux6DA8c/arcgis/rest/serv
ices
Cobb
https://services9.arcgis.com/J2VKjz9sdPePNEoo/ArcGIS/rest/serv
ices
Cumberland Community Investment District
Coffee
https://www.sgrcmaps.com/alma/rest/services/Coffee
Colquitt
Schneider Geospatial - ArcGIS server address is not public

## Page 129

Columbia
https://gis.columbiacountyga.gov/host/rest/services
Table of contents disabled
Columbia
_ttps://mapsonline.columbiacountyga.gov/arcgis/rest/services
dead link 1
Cook
https://www.sgrcmaps.com/arcgis/rest/services/Cook
Coweta
https://services1.arcgis.com/AaPyNbrJpNGryRqh/arcgis/rest/servic
es
Coweta
https://tiles.arcgis.com/tiles/AaPyNbrJpNGryRqh/arcgis/rest/servic
es
Crawford
Schneider Geospatial - ArcGIS server address is not public
Crisp
Schneider Geospatial - ArcGIS server address is not public
Dade
Assessor website has GIS but does not use ArcGIS
Dawson
https://services7.arcgis.com/Ptz860OPLeIY55cX/arcgis/rest/servic
es
Dawson
https://tiles.arcgis.com/tiles/Ptz860OPLeIY55cX/arcgis/rest/servic
es
Decatur
Schneider Geospatial - ArcGIS server address is not public

DeKalb
https://gis.dekalbcountyga.gov/arcgis/rest/services
SSL problem
DeKalb
https://dcgis.dekalbcountyga.gov/hosted/rest/services
DeKalb
https://dcgis.dekalbcountyga.gov/mapping/rest/services
DeKalb
https://dcgis.dekalbcountyga.gov/arcgis/rest/services
DeKalb
https://services2.arcgis.com/IxVN2oUE9EYLSnPE/ArcGIS/rest/se
rvices
DeKalb
https://tiles.arcgis.com/tiles/IxVN2oUE9EYLSnPE/arcgis/rest/serv
ices
Dodge
Schneider Geospatial - ArcGIS server address is not public
Dooly
Schneider Geospatial - ArcGIS server address is not public
Dougherty
Schneider Geospatial - ArcGIS server address is not public
Douglas
https://gis.dcga.us/arcgis/rest/services
SSL problem
Douglas
https://services.arcgis.com/S5A11uZvQ48OH97O/arcgis/rest/servi
ces
Early
Schneider Geospatial - ArcGIS server address is not public

## Page 130

Echols
https://www.sgrcmaps.com/arcgis/rest/services/Echols
Effingham
https://maps.crc.ga.gov/crcarcgis/rest/services/Effingham
Elbert
Schneider Geospatial - ArcGIS server address is not public
Emanuel
Schneider Geospatial - ArcGIS server address is not public
Evans
Schneider Geospatial - ArcGIS server address is not public
Fannin
Schneider Geospatial - ArcGIS server address is not public
Fannin
Schneider Geospatial - ArcGIS server address is not public
Floyd
WMS
Forsyth
https://geo.forsythco.com/gis/rest/services
Forsyth
https://services2.arcgis.com/StQaZGYzUARPnrpL/ArcGIS/rest/ser
vices
Forsyth
https://tiles.arcgis.com/tiles/StQaZGYzUARPnrpL/arcgis/rest/servi
ces
Franklin
Schneider Geospatial - ArcGIS server address is not public
Fulton
https://gismaps.fultoncountyga.gov/arcgispub/rest/services

Fulton
https://services1.arcgis.com/AQDHTHDrZzfsFsB5/ArcGIS/rest/se
rvices
Fulton
https://tiles.arcgis.com/tiles/AQDHTHDrZzfsFsB5/arcgis/rest/servi
ces
Fulton
https://services5.arcgis.com/buITjRsK0rZsAXbQ/arcgis/rest/servic
es
Fulton
https://tiles.arcgis.com/tiles/buITjRsK0rZsAXbQ/arcgis/rest/servic
es
Gilmer
Schneider Geospatial - ArcGIS server address is not public
Glascock
Schneider Geospatial - ArcGIS server address is not public
Glynn
https://maps.crc.ga.gov/crcarcgis/rest/services/Glynn
Glynn
https://webadaptor.glynncounty-ga.gov/webadaptor/rest/services
Glynn
          https://services.arcgis.com/5iWzb1srkjPDXmpL/arcgis/rest/services
Glynn
https://tiles.arcgis.com/tiles/5iWzb1srkjPDXmpL/arcgis/rest/servic
es
Gordon
Schneider Geospatial - ArcGIS server address is not public

## Page 131

Grady
Schneider Geospatial - ArcGIS server address is not public
Greene
Schneider Geospatial - ArcGIS server address is not public
Gwinnett
https://gis3.gwinnettcounty.com/mapvis/rest/services
Habersham
https://arcgis4.roktech.net/arcgis/rest/services/habersham
Habersham
https://arcgis5.roktech.net/arcgis/rest/services/habersham
Hall
https://webmap.hallcounty.org/server/rest/services
SSL problem
Table of contents disabled
Hancock
Schneider Geospatial - ArcGIS server address is not public
They might also have a WMS server
Haralson
Schneider Geospatial - ArcGIS server address is not public
Harris
Schneider Geospatial - ArcGIS server address is not public
Hart
Schneider Geospatial - ArcGIS server address is not public
Heard
Schneider Geospatial - ArcGIS server address is not public
Henry
https://arcgis.co.henry.ga.us/server/rest/services
Houston
Schneider Geospatial - ArcGIS server address is not public
Irwin
https://www.sgrcmaps.com/alma/rest/services/Irwin
Jackson
           https://services8.arcgis.com/bcbi4lYRFOsss0F5/arcgis/rest/services
Jasper
Schneider Geospatial - ArcGIS server address is not public
Jeff Davis
Schneider Geospatial - ArcGIS server address is not public
Jefferson
Schneider Geospatial - ArcGIS server address is not public
Jenkins
Schneider Geospatial - ArcGIS server address is not public
Johnson
Schneider Geospatial - ArcGIS server address is not public
Jones
Schneider Geospatial - ArcGIS server address is not public
Lamar
Schneider Geospatial - ArcGIS server address is not public
Lanier
https://www.sgrcmaps.com/alma/rest/services/Lanier

## Page 132

Laurens
https://services8.arcgis.com/XxLBcrikqFM0vkoy/arcgis/rest/servic
es
Lee
https://services7.arcgis.com/xWHrkwYCAX9v0Owj/arcgis/rest/ser
vices
Lee
https://tiles.arcgis.com/tiles/xWHrkwYCAX9v0Owj/arcgis/rest/ser
vices
Liberty
https://maps.crc.ga.gov/crcarcgis/rest/services/Liberty
Lincoln
Schneider Geospatial - ArcGIS server address is not public
Long
https://maps.crc.ga.gov/crcarcgis/rest/services/Long

Lowndes
https://www.valorgis.com/publicservices/rest/services
Lumpkin
Schneider Geospatial - ArcGIS server address is not public
Macon
Schneider Geospatial - ArcGIS server address is not public
Madison
Schneider Geospatial - ArcGIS server address is not public
Marion
Schneider Geospatial - ArcGIS server address is not public
McDuffie
Schneider Geospatial - ArcGIS server address is not public
McIntosh
https://maps.crc.ga.gov/crcarcgis/rest/services/McIntosh
McIntosh
https://maps.crc.ga.gov/crcarcgis/rest/services/Sapelo
Barrier island
Meriwether
Schneider Geospatial - ArcGIS server address is not public
Miller
Schneider Geospatial - ArcGIS server address is not public
Mitchell
Schneider Geospatial - ArcGIS server address is not public
Monroe
Schneider Geospatial - ArcGIS server address is not public
Montgomery
Schneider Geospatial - ArcGIS server address is not public
Morgan
Schneider Geospatial - ArcGIS server address is not public
Murray
Schneider Geospatial - ArcGIS server address is not public
Muscogee
See city of Columbus

## Page 133

Newton
https://gis.ncboc.com/arcgis/rest/services
Oconee
Schneider Geospatial - ArcGIS server address is not public
Oglethorpe
https://services1.arcgis.com/IX9GvidKl201KteW/arcgis/rest/servic
es
Paulding
https://arcgis4.roktech.net/arcgis/rest/services/Paulding
Paulding
https://arcgis5.roktech.net/arcgis/rest/services/Paulding
Peach
Schneider Geospatial - ArcGIS server address is not public
Pickens
Schneider Geospatial - ArcGIS server address is not public
Pierce
https://www.sgrcmaps.com/alma/rest/services/Pierce
Pike
Schneider Geospatial - ArcGIS server address is not public
Polk
Schneider Geospatial - ArcGIS server address is not public
Pulaski
_ttps://mgrcmaps.org/arcgis/rest/services/PulaskiCounty
dead link 1
Putnam
Schneider Geospatial - ArcGIS server address is not public
Quitman
Schneider Geospatial - ArcGIS server address is not public
Rabun
Schneider Geospatial - ArcGIS server address is not public
Randolph
Schneider Geospatial - ArcGIS server address is not public
Richmond
Schneider Geospatial - ArcGIS server address is not public
Rockdale
https://services.arcgis.com/Tbke9ca9DhtF4VIx/arcgis/rest/services
Rockdale
           https://tiles.arcgis.com/tiles/Tbke9ca9DhtF4VIx/arcgis/rest/services
Schley
Schneider Geospatial - ArcGIS server address is not public
Screven
Schneider Geospatial - ArcGIS server address is not public
Seminole
Schneider Geospatial - ArcGIS server address is not public
Spalding
Schneider Geospatial - ArcGIS server address is not public
Stephens
Schneider Geospatial - ArcGIS server address is not public

## Page 134

Stewart
Schneider Geospatial - ArcGIS server address is not public
Sumter
https://web4.kcsgis.com/kcsgis/rest/services/Americus_SumterCo_
GA
Not open to public
Sumter
https://ga31portal.kcsgis.com/ga31server/rest/services
Talbot
Schneider Geospatial - ArcGIS server address is not public
Taliaferro
Schneider Geospatial - ArcGIS server address is not public
Tattnall
Schneider Geospatial - ArcGIS server address is not public
Taylor
Schneider Geospatial - ArcGIS server address is not public
Telfair
Schneider Geospatial - ArcGIS server address is not public
Terrell
Schneider Geospatial - ArcGIS server address is not public
Thomas
https://www.thomascountymaps.org/arcgis/rest/services
Tift
https://www.sgrcmaps.com/alma/rest/services/Tift
Toombs
Schneider Geospatial - ArcGIS server address is not public
Towns
Schneider Geospatial - ArcGIS server address is not public
Treutlen
Schneider Geospatial - ArcGIS server address is not public
Troup
https://services.arcgis.com/V4Y8xIvXuYJiVZwF/arcgis/rest/servic
es
Turner
Schneider Geospatial - ArcGIS server address is not public
Twiggs
Schneider Geospatial - ArcGIS server address is not public
Union
https://services.arcgis.com/yghUoIoA2Cd2cWki/ArcGIS/rest/servi
ces
See beginning with Union
Upson
Schneider Geospatial - ArcGIS server address is not public
Walker
Schneider Geospatial - ArcGIS server address is not public
Walton
Schneider Geospatial - ArcGIS server address is not public
Ware
Schneider Geospatial - ArcGIS server address is not public

## Page 135

Warren
Schneider Geospatial - ArcGIS server address is not public
Washington
Schneider Geospatial - ArcGIS server address is not public
Wayne
Schneider Geospatial - ArcGIS server address is not public
Webster
Schneider Geospatial - ArcGIS server address is not public
Wheeler
Schneider Geospatial - ArcGIS server address is not public
White
Schneider Geospatial - ArcGIS server address is not public
Whitfield
https://gis.whitfieldcountyga.com/server/rest/services
Wilcox
Schneider Geospatial - ArcGIS server address is not public
Wilkes
Schneider Geospatial - ArcGIS server address is not public
Wilkinson
Schneider Geospatial - ArcGIS server address is not public
Worth
Schneider Geospatial - ArcGIS server address is not public
Georgia City, Town, Village, etc GIS Servers
Acworth
https://services2.arcgis.com/AkJuRTalqccxOHLu/ArcGIS/rest/serv
ices
Acworth
https://tiles.arcgis.com/tiles/AkJuRTalqccxOHLu/arcgis/rest/servic
es
Albany
https://services6.arcgis.com/VKHi8CC6pMIyYUIs/ArcGIS/rest/ser
vices
Alma
https://www.sgrcmaps.com/arcgis/rest/services/Alma
Alto
See https://arcgis5.roktech.net/arcgis/rest/services/habersham
Alpharetta
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/AlphaMiltonStatus/FeatureServer
Go to the top and search for ‘Alpharetta’
Alpharetta
https://alphagis.alpharetta.ga.us/arcgis/rest/services
Table of contents disabled
Alpharetta
https://alphagis.alpharetta.ga.us/imagery/rest/services
Table of contents disabled
Alpharetta
https://alphagis.alpharetta.ga.us/maps/rest/services
Table of contents disabled
Alpharetta
https://services1.arcgis.com/j3REJGFXNug7wAsB/ArcGIS/rest/se
rvices

## Page 136

Alpharetta
https://tiles.arcgis.com/tiles/j3REJGFXNug7wAsB/arcgis/rest/serv
ices
Athens
See Clarke county

Atlanta
https://gis.atlantaga.gov/dpcd/rest/services
Atlanta
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/ATL_Status_Service/FeatureServer
Go to the top and search for ‘Atlanta’
Atlanta
https://services5.arcgis.com/5RxyIIJ9boPdptdo/ArcGIS/rest/servic
es
Atlanta
https://tiles.arcgis.com/tiles/5RxyIIJ9boPdptdo/arcgis/rest/services
Augusta
https://gismap.augustaga.gov/arcgis/rest/services
Baldwin
See https://arcgis5.roktech.net/arcgis/rest/services/habersham
Ball Ground
https://services9.arcgis.com/CAVmSZdRT9pdZgEk/ArcGIS/rest/s
ervices
Ball Ground
https://tiles.arcgis.com/tiles/CAVmSZdRT9pdZgEk/arcgis/rest/ser
vices
Bloomingdale
https://maps.crc.ga.gov/crcarcgis/rest/services/Bloomingdale
Brookhaven
https://maps.brookhavenga.gov/arcgis/rest/services
Brookhaven
https://services.arcgis.com/hOnx0eXgrjDCJCZV/arcgis/rest/servic
es
Brookhaven
https://tiles.arcgis.com/tiles/hOnx0eXgrjDCJCZV/arcgis/rest/servi
ces
Brooks
https://www.sgrcmaps.com/arcgis/rest/services/Brooks
Bryan
https://maps.crc.ga.gov/crcarcgis/rest/services/Bryan
Butler
_________
Calhoun
https://services1.arcgis.com/sTpQq1U487B2x9RN/ArcGIS/rest/ser
vices
Canton
https://services6.arcgis.com/dpaY3zboICQILFY5/arcgis/rest/servic
es
Canton
https://tiles.arcgis.com/tiles/dpaY3zboICQILFY5/arcgis/rest/servic
es
Chamblee
https://gis.chambleega.gov/arcgis/rest/services

## Page 137

Chamblee
https://services7.arcgis.com/Wa5u3F8BOztWahRv/ArcGIS/rest/ser
vices
Clarkesville
See https://arcgis5.roktech.net/arcgis/rest/services/habersham
Columbus
https://ccggisprod.columbusga.org/server/rest/services
Cornelia
See https://arcgis5.roktech.net/arcgis/rest/services/habersham
Dasher
https://www.sgrcmaps.com/alma/rest/services/Dasher
Decatur
https://services.arcgis.com/36QtML6Mf01B1N0W/arcgis/rest/servi
ces
Decatur
https://tiles.arcgis.com/tiles/36QtML6Mf01B1N0W/arcgis/rest/ser
vices
Demorest
See https://arcgis5.roktech.net/arcgis/rest/services/habersham
Doraville
https://services5.arcgis.com/HPK9d3vzjakSFUjJ/arcgis/rest/servic
es
Doraville
          https://tiles.arcgis.com/tiles/HPK9d3vzjakSFUjJ/arcgis/rest/services
Dunwoody
https://dungisapp.dunwoodyga.gov/arcgis/rest/services
East Point
https://services7.arcgis.com/CPLm4MuWYjfnA2R9/ArcGIS/rest/s
ervices
East Point
https://tiles.arcgis.com/tiles/CPLm4MuWYjfnA2R9/arcgis/rest/ser
vices
Fitzgerald
https://www.sgrcmaps.com/alma/rest/services/Fitzgerald
Floyd
WMS server
Gainesville
See Hall County
Hinesville
https://maps.crc.ga.gov/crcarcgis/rest/services/HinesvilleView
Johns Creek
https://gis.johnscreekga.gov/jcgis/rest/services
Johns Creek
https://services1.arcgis.com/bqfNVPUK3HOnCFmA/arcgis/rest/se
rvices
Johns Creek
https://tiles.arcgis.com/tiles/bqfNVPUK3HOnCFmA/arcgis/rest/se
rvices
Kennesaw
https://services2.arcgis.com/XwGh5SYpBlXQGJEB/ArcGIS/rest/s
ervices

## Page 138

Kennesaw
https://tiles.arcgis.com/tiles/XwGh5SYpBlXQGJEB/arcgis/rest/ser
vices
LaGrange
https://maps.lagrange-ga.org/arcgis/rest/services        SSL problem
Live Oak
https://www.sgrcmaps.com/arcgis/rest/services/LiveOak/boundarie
s/MapServer
Macon
See Bibb County
Marietta
https://secure.mariettaga.gov/server/rest/services
Marietta
https://services2.arcgis.com/OKqf9cl3ItPM5Rid/ArcGIS/rest/servi
ces
Marietta
           https://tiles.arcgis.com/tiles/OKqf9cl3ItPM5Rid/arcgis/rest/services
Milton
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/AlphaMiltonStatus/FeatureServer
Go to the top and search for ‘Milton’
Milton
https://services2.arcgis.com/HgtLmZiOnoT105i1/ArcGIS/rest/serv
ices
Milton
https://tiles.arcgis.com/tiles/HgtLmZiOnoT105i1/arcgis/rest/servic
es
Mt. Airy
See https://arcgis5.roktech.net/arcgis/rest/services/habersham
Nashville
https://www.sgrcmaps.com/arcgis/rest/services/Nashville
Newnan
https://services6.arcgis.com/tjTJgu5ZqqixGP2v/ArcGIS/rest/servic
es
Norcross
https://services3.arcgis.com/ejWC2ajTUDNpZQe4/arcgis/rest/serv
ices
Patterson
https://www.sgrcmaps.com/arcgis/rest/services/Patterson
Peachtree City
https://services5.arcgis.com/ixWnd9c3gwqSeniI/ArcGIS/rest/servi
ces
Pembroke
https://maps.crc.ga.gov/crcarcgis/rest/services/Bryan
Includes Pembroke
Pooler
https://pub.sagis.org/arcgis/rest/services/Pooler
Powder Springs
https://services6.arcgis.com/hpvhAmRP1z50gTbO/arcgis/rest/servi
ces

## Page 139

Rome
WMS server
Roswell
https://gisweb.ci.roswell.ga.us/arcgis/rest/services
Roswell
https://services2.arcgis.com/8Jz6gNJAysC9KT9W/ArcGIS/rest/ser
vices
Roswell
https://tiles.arcgis.com/tiles/8Jz6gNJAysC9KT9W/arcgis/rest/servi
ces
St. Marys
           https://maps.crc.ga.gov/crcarcgis/rest/services/GeodataService_StM
St. Marys

https://services1.arcgis.com/AECh5O9fewZ8QE4X/ArcGIS/rest/se
rvices
Sandy Springs
https://gis2.sandyspringsga.gov/arcgis/rest/services
Savannah (city)
https://services6.arcgis.com/vAIFmkAWtpiZenSc/ArcGIS/rest/ser
vices
Savannah (city)
https://services6.arcgis.com/qv1nlKGEXHyUgE2M/ArcGIS/rest/s
ervices
Savannah (area)
https://pub.sagis.org/arcgis/rest/services
Savannah (area)
https://services2.arcgis.com/2SoNIbP3sKErGFHa/ArcGIS/rest/ser
vices
Savannah (area)
https://tiles.arcgis.com/tiles/2SoNIbP3sKErGFHa/arcgis/rest/servic
es
Savannah (city)
https://services3.arcgis.com/0m9qmmEbiydeqFeD/ArcGIS/rest/ser
vices
Savannah (city)
https://tiles.arcgis.com/tiles/0m9qmmEbiydeqFeD/arcgis/rest/servi
ces
Screven
https://maps.crc.ga.gov/crcarcgis/rest/services/Screven
South Fulton
https://services3.arcgis.com/y2BJK2GUfoTwH7py/ArcGIS/rest/ser
vices
Stonecrest
https://services8.arcgis.com/2Oj4p0oK7rnTYNHA/arcgis/rest/servi
ces
Stonecrest
https://tiles.arcgis.com/tiles/2Oj4p0oK7rnTYNHA/arcgis/rest/servi
ces
Tallulah
See https://arcgis5.roktech.net/arcgis/rest/services/habersham
Thomasville
https://cot-maps.org/citygis/rest/services
slow server
Thomasville
https://services.arcgis.com/BrciE7dKF0KqDF0U/arcgis/rest/servic
es
Thomasville
https://tiles.arcgis.com/tiles/BrciE7dKF0KqDF0U/arcgis/rest/servi
ces

## Page 140

Tifton
https://www.sgrcmaps.com/alma/rest/services/Tifton
Tucker
https://tuckergis.interdev.com:6443/arcgis/rest/services
Tucker
https://services6.arcgis.com/SoTK00Zs8aX8VVG4/ArcGIS/rest/se
rvices
Tucker
https://tiles.arcgis.com/tiles/SoTK00Zs8aX8VVG4/arcgis/rest/serv
ices
Tybee Island
https://maps.crc.ga.gov/crcarcgis/rest/services/Tybee
Union City
___________
Valdosta
See Lowndes County
Warner Robins
Schneider Geospatial - ArcGIS server address is not public
West Point
https://arcgis4.roktech.net/arcgis/rest/services/WestPoint
West Point
https://arcgis5.roktech.net/arcgis/rest/services/WestPoint
Woodstock
https://gis.woodstockga.gov/arcgis/rest/services
Hawaii State GIS Servers
Hawaii Geospatial Data Portal
Website: https://geoportal.hawaii.gov
Department of Land and Natural Resources
Website: https://dlnr.hawaii.gov
GIS: See ‘geodata’ link below
Hawaii various layers
GIS: https://geodata.hawaii.gov/arcgis/rest/services
Here is an excel file with a nice list of the layers on this server
https://files.hawaii.gov/dbedt/op/gis/data/REST_Map_Service_Cross_Walk.xlsx
Parcel lines:  ParcelsZoning/MapServer
several layers
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/HQ0xoN0EzDPBOEci/arcgis/rest/services
Hawaii County GIS Servers
Hawai'i
https://gis.hawaiicounty.gov/arcgis/rest/services
Hawai'i
https://services1.arcgis.com/C2LPusZs5OXNGFDn/ArcGIS/rest/se
rvices
Hawai'i
https://tiles.arcgis.com/tiles/C2LPusZs5OXNGFDn/arcgis/rest/serv
ices

## Page 141

Honolulu
https://services.arcgis.com/tNJpAOha4mODLkXz/arcgis/rest/servi
ces
Honolulu
https://tiles.arcgis.com/tiles/tNJpAOha4mODLkXz/arcgis/rest/serv
ices
Kauai
https://maps.kauai.gov/server/rest/services
Kauai
https://services1.arcgis.com/0DaVqrPt2eyXUS9g/ArcGIS/rest/serv
ices
Kauai
https://tiles.arcgis.com/tiles/0DaVqrPt2eyXUS9g/arcgis/rest/servic
es
Maui
https://services3.arcgis.com/fsrDo0QMPlK9CkZD/arcgis/rest/servi
ces
Maui
https://tiles.arcgis.com/tiles/fsrDo0QMPlK9CkZD/arcgis/rest/servi
ces
Hawaii City, Town, Village, etc GIS Servers

Honolulu
https://gis.aecomonline.net/arcgis/rest/services/Honolulu
Also see Honolulu county
Idaho State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Idaho Enterprise Open Data Portal
Website: https://data.gis.idaho.gov
Idaho Geospatial Data Clearinghouse
Website: https://data.gis.idaho.gov
GIS: https://insideidaho.org/arcgis/rest/services
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis2.idaho.gov/arcgis/rest/services
8-1-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Idaho Department of Environmental Quality
Website: https://www.deq.idaho.gov
GIS: https://global.deq.idaho.gov/arcgis/rest/services
8-1-2023 No tiled data
GIS: https://mapcase.deq.idaho.gov/arcgis/rest/services
8-1-2023 No tiled data
GIS: https://services1.arcgis.com/Kr5oFycwwDsdTyVH/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Kr5oFycwwDsdTyVH/arcgis/rest/services
Idaho Department of Lands
Website: https://www.idl.idaho.gov

## Page 142

GIS: https://gis1.idl.idaho.gov/arcgis/rest/services
GIS: https://gis1.idl.idaho.gov/image/rest/services
GIS: https://services2.arcgis.com/1cvrwLhZRFh3okEF/ArcGIS/rest/services
Idaho Transportation Department
Website: https://itd.idaho.gov
GIS: https://gis.itd.idaho.gov/arcgisprod/rest/services
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/Qqv4dYPC8Vv8e3c3/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Qqv4dYPC8Vv8e3c3/arcgis/rest/services
Idaho Department of Water Resources
Website: https://www.idwr.idaho.gov
GIS: https://gis.idwr.idaho.gov/hosting/rest/services
8-1-2023 No tiled data
GIS: https://services1.arcgis.com/iRCkLgFRU45VAYn3/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/iRCkLgFRU45VAYn3/arcgis/rest/services
Idaho Department of Fish and Game
Website: https://idfg.idaho.gov
GIS: https://gisportal-idfg.idaho.gov/hosting/rest/services
GIS: https://services.arcgis.com/FjJI5xHF2dUPVrgK/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/FjJI5xHF2dUPVrgK/arcgis/rest/services
Idaho State Tax Commission
Website: https://tax.idaho.gov/
GIS: https://services.arcgis.com/91hXl6NfvLGEi8x5/ArcGIS/rest/services
Idaho State University - GIS Center
Website: https://giscenter.isu.edu
GIS: https://services1.arcgis.com/z5tlnpYHokW9isdE/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/z5tlnpYHokW9isdE/arcgis/rest/services
Idaho various layers
https://services.arcgis.com/91hXl6NfvLGEi8x5/ArcGIS/rest/services
https://services1.arcgis.com/CNPdEkvnGl65jCX8/arcgis/rest/services
https://tiles.arcgis.com/tiles/CNPdEkvnGl65jCX8/arcgis/rest/services
Idaho Regional
Community Planning Association of Southwest Idaho
Website: https://compassidaho.org
GIS: https://services6.arcgis.com/2S9FP4vfcUQQ8G1T/arcgis/rest/services
Idaho County GIS Servers
Ada
https://www.adacountyassessor.org/arcgis/rest/services/External

## Page 143

Top of the table of contents is not public.
Ada
https://services1.arcgis.com/WHM6qC35aMtyAAlN/ArcGIS/rest/s
ervices
Ada
https://tiles.arcgis.com/tiles/WHM6qC35aMtyAAlN/arcgis/rest/ser
vices
Ada
https://services2.arcgis.com/9rTo9NcUHIKASKwi/ArcGIS/rest/ser
vices
Ada
https://tiles.arcgis.com/tiles/9rTo9NcUHIKASKwi/arcgis/rest/servi
ces
Ada
https://services2.arcgis.com/dgGjZc6xAH5m5JyP/ArcGIS/rest/ser
vices
Ada
https://tiles.arcgis.com/tiles/dgGjZc6xAH5m5JyP/arcgis/rest/servic
es
Adams
They have GIS but not ArcGIS.  Geomoose.
Bannock
https://maps.bannockcounty.us/server/rest/services
Bear Lake
They have GIS but not ArcGIS.  Geomoose.
Benewah
They have GIS but not ArcGIS.  Geomoose.
Bingham
https://web.binghamid.gov/arcgis/rest/services
Blaine
https://maps.co.blaine.id.us/server/rest/services
Boise
They have GIS but not ArcGIS.  Geomoose.
Bonner
https://cloudgis.bonnercountyid.gov/server/rest/services
Bonneville
https://bonneville.esriemcs.com/arcgis/rest/services
Bonneville
https://services2.arcgis.com/Xd5SMhLZ1h9t0F3b/ArcGIS/rest/ser
vices
Bonneville
https://tiles.arcgis.com/tiles/Xd5SMhLZ1h9t0F3b/arcgis/rest/servic
es
Boundary
They have GIS but not ArcGIS.  Geomoose.
Butte
They have GIS but not ArcGIS.  Geomoose.
Camas
They have GIS but not ArcGIS.  Geomoose.
Canyon
https://maps.canyonco.org/arcgisserver/rest/services
Table of contents disabled
Caribou
They have GIS but not ArcGIS.  Geomoose.

## Page 144

Cassia
They have GIS but not ArcGIS.  Geomoose.
Chubbuck
https://gis.cityofchubbuck.us/arcgis/rest/services
Clark
Greenwood WMS.
Clearwater
https://services2.arcgis.com/bkAz0G7Qq4dmkYCg/arcgis/rest/serv
ices
Clearwater
https://tiles.arcgis.com/tiles/bkAz0G7Qq4dmkYCg/arcgis/rest/serv
ices
Custer
Greenwood WMS.
Elmore
They have GIS but not ArcGIS.  Geomoose.
Franklin
They have GIS but not ArcGIS.  Geomoose.
Fremont
Greenwood WMS.
Gem
They have GIS but not ArcGIS.  Geomoose.
Gooding
They have GIS but not ArcGIS.  Geomoose.
Idaho
https://services7.arcgis.com/gqcDdwE7LMrYrEMJ/arcgis/rest/serv
ices
Idaho
https://tiles.arcgis.com/tiles/gqcDdwE7LMrYrEMJ/arcgis/rest/serv
ices
Jefferson
https://grant.co.jefferson.id.us/arcgis/rest/services  SSL problem
Jerome
They have GIS but not ArcGIS.  Geomoose.
Kootenai
https://gis.kcgov.us/arcgis/rest/services
Latah
https://gis.latah.id.us/arcgis/rest/services
Lemhi
They have GIS but not ArcGIS.  Geomoose.
Lewis
They have GIS but not ArcGIS.  Geomoose.
Madison
https://madison.rexburg.org/mrgis/rest/services
Madison
          https://services1.arcgis.com/EiEr2xT4gB5AIOtc/arcgis/rest/services
Madison
           https://tiles.arcgis.com/tiles/EiEr2xT4gB5AIOtc/arcgis/rest/services
Minidoka
They have GIS but not ArcGIS.  Geomoose.

## Page 145

Nezperce
https://gis.co.nezperce.id.us/arcgis/rest/services
Oneida
They have GIS but not ArcGIS.  Geomoose.
Owyhee
They have GIS but not ArcGIS.  Geomoose.
Payette
They have GIS but not ArcGIS.  Geomoose.
Power
They have GIS but not ArcGIS.  Geomoose.
Shoshone
They have GIS but not ArcGIS.  Geomoose.
Teton
https://services1.arcgis.com/as6biEYkl7PaUM4Y/ArcGIS/rest/serv
ices
Teton
https://tiles.arcgis.com/tiles/as6biEYkl7PaUM4Y/arcgis/rest/servic
es
Twin Falls
They have GIS but not ArcGIS.  Geomoose.
Valley
https://services6.arcgis.com/ikurHvtarxfN6u3u/arcgis/rest/services
Valley
https://tiles.arcgis.com/tiles/ikurHvtarxfN6u3u/arcgis/rest/services
Washington
GIS for internal use.
Idaho City, Town, Village, etc GIS Servers
Blaine
https://maps.co.blaine.id.us/imgserv/rest/services
Blaine
https://maps.co.blaine.id.us/server/rest/services

Boise
https://gismaps.cityofboise.org/arcgis/rest/services
Table of contents disabled

Boise
https://services1.arcgis.com/WHM6qC35aMtyAAlN/arcgis/rest/ser
vices

Boise
https://tiles.arcgis.com/tiles/WHM6qC35aMtyAAlN/arcgis/rest/ser
vices
Coeur d’Alene
https://gis.cdaid.org/server/rest/services
Coeur d’Alene
https://services3.arcgis.com/UpxXXtzETZbRfa6A/ArcGIS/rest/ser
vices
Idaho Falls
https://ifgis.idahofallsidaho.gov/arcgis/rest/services    SSL problem
Lewiston
https://webadaptor.cityoflewiston.org/server/rest/services
Lewiston
https://webadaptor.cityoflewiston.org/imageserver/rest/services
Lewiston
https://services5.arcgis.com/R6cBwHlkwfCfBjSM/ArcGIS/rest/ser
vices

## Page 146

Lewiston
https://tiles.arcgis.com/tiles/R6cBwHlkwfCfBjSM/arcgis/rest/servi
ces
Lexington
https://services3.arcgis.com/Z7ioXMhIaRIEQx1O/ArcGIS/rest/ser
vices
Lexington
https://tiles.arcgis.com/tiles/Z7ioXMhIaRIEQx1O/arcgis/rest/servi
ces
McCall
https://mccallgis.mccall.id.us/mcgis/rest/services
Moscow
See Latah County
Nampa
https://services7.arcgis.com/w6PtsxFChhUvYfXN/ArcGIS/rest/ser
vices
Pocatello
https://ext.pocatello.us/map/rest/services
Pocatello
https://map.pocatello.us/arcgis/rest/services
Pocatello
https://services3.arcgis.com/My1Vo0yFlHe2fnKB/ArcGIS/rest/ser
vices
Pocatello
https://tiles.arcgis.com/tiles/My1Vo0yFlHe2fnKB/arcgis/rest/servi
ces
Post Falls
https://gis.postfalls.gov/server/rest/services
Post Falls
https://services2.arcgis.com/NoBPxbwrHEVm6ZMy/ArcGIS/rest/s
ervices
Post Falls
https://tiles.arcgis.com/tiles/NoBPxbwrHEVm6ZMy/arcgis/rest/ser
vices
Rexburg
See Madison county
Sand Point
https://geo.sandpointidaho.gov/server/rest/services     SSL problem
Twin Falls
https://services1.arcgis.com/I78Ijvc0YuZijqmq/ArcGIS/rest/servic
es
Twin Falls
https://tiles.arcgis.com/tiles/I78Ijvc0YuZijqmq/arcgis/rest/services
Illinois State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Illinois Data Portal
Website: https://data.illinois.gov/
Illinois Emergency Management Agency
Website: https://iema.illinois.gov
GIS: https://maps.iema.state.il.us/arcgis/rest/services

## Page 147

8-2-2023 No tiled data
Illinois Department of Natural Resources
Website: https://dnr.illinois.gov
GIS: https://maps.dnr.illinois.gov/geoservices/rest/services
GIS: https://geoservices3.dnr.illinois.gov/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://services.arcgis.com/b9DHj1BjfdLLFv11/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/b9DHj1BjfdLLFv11/arcgis/rest/services
Illinois Department of Transportation
Website: https://idot.illinois.gov
GIS: https://gis1.dot.illinois.gov/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://services2.arcgis.com/aIrBD8yn1TDTEXoz/ArcGIS/rest/services
Illinois Environmental Protection Agency
Website: https://epa.illinois.gov
GIS: https://geoservices.epa.illinois.gov/arcgis/rest/services
8-2-2023 No tiled data
Illinois Environmental Protection Data via Resource Management Mapping Service
Website:
https://cybergis.illinois.edu/cybergis_resource/illinois-environmental-protection-data-via-
resource-management-mapping-service-rmms
GIS: _ttps://www.rmms.illinois.edu/iepa/rest/services
dead link 3
8-2-2023 No tiled data
Illinois State Geological Survey
Website: https://isgs.illinois.edu
GIS: https://data.isgs.illinois.edu/arcgis/rest/services
8-2-2023 No tiled data
Illinois Historic Preservation Agency
Website: https://www2.illinois.gov/dnrhistoric/Pages/default.aspx
GIS: New GIS coming soon
Illinois State Police
Website: https://isp.illinois.gov
GIS: https://services2.arcgis.com/3yCQWqEMIRwEdrth/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/3yCQWqEMIRwEdrth/arcgis/rest/services
Illinois State Water Survey
Website: https://www.isws.illinois.edu
GIS: https://gismaps.isws.illinois.edu/arcgis/rest/services
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”

## Page 148

Illinois miscellaneous
GIS: https://services3.arcgis.com/HESxeTbDliKKvec2/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/HESxeTbDliKKvec2/arcgis/rest/services
Illinois Regional
GIS Consortium (Chicago area)
Website: https://public.gisconsortium.org/about
GIS: https://ags.gisconsortium.org/arcgis/rest/services
Chicago Metropolitan Agency for Planning
Website: https://engage.cmap.illinois.gov
GIS: https://services5.arcgis.com/LcMXE3TFhi1BSaCY/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/LcMXE3TFhi1BSaCY/arcgis/rest/services
Metropolitan Planning Council (Chicago area)
Website: https://metroplanning.org
GIS: https://services8.arcgis.com/KMds2PknwsNs2BkX/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/KMds2PknwsNs2BkX/arcgis/rest/services
Metropolitan Water Reclamation District of Greater Chicago
Website: https://mwrd.org
GIS: https://services.arcgis.com/R2OqRHzOVTbwcOgY/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/R2OqRHzOVTbwcOgY/arcgis/rest/services
Tri-County Regional Planning Commission
Website: https://www.centralilmaps.com
GIS: https://www.centralilmaps.com/arcgis/rest/services
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/pPTAs43AFhhk0pXQ/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/pPTAs43AFhhk0pXQ/arcgis/rest/services
Northwest Central Dispatch System
Website: https://www.nwcds.org
GIS: https://services3.arcgis.com/hLnQegSAeUvQFw7w/ArcGIS/rest/services
Pace (Regional transportation)
Website: https://www.pacebus.com
GIS: https://maps.pacebus.com/arcgis/rest/services
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Illinois County GIS Servers
All counties are listed and have been checked for GIS
Adams
https://www.adamscountyarcserver.com/adamscountyarcserver/rest
/services

## Page 149

Adams
https://services3.arcgis.com/BXTAaNPMn1VANOeH/ArcGIS/rest
/services
Alexander
4/2024 No GIS found
Batavia
https://services2.arcgis.com/zmMUFcmVn3I9oaMp/ArcGIS/rest/s
ervices
Bond
https://services.arcgis.com/VbP0KHITyLTMBTy3/arcgis/rest/servi
ces
Boone
https://maps.boonecountyil.org/arcgis/rest/services
Brown
           https://services1.arcgis.com/aHxsJXn8GAlRIIIg/arcgis/rest/services
Brown
           https://tiles.arcgis.com/tiles/aHxsJXn8GAlRIIIg/arcgis/rest/services
Bureau
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/BureauILFeatures/FeatureServer
Go to the top and search for ‘BureauIL’
Bureau
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/BureauILCadastral/MapServer
Calhoun
https://services1.arcgis.com/Ggva1SWphWGX4bb8/ArcGIS/rest/s
ervices/CalhounCoGIS/FeatureServer
Calhoun
https://tiles.arcgis.com/tiles/Ggva1SWphWGX4bb8/arcgis/rest/ser
vices
Carroll
Must pay $ to access GIS
Cass
Schneider Geospatial - ArcGIS server address is not public
Champaign
https://services.ccgisc.org/portal/sharing/servers/151559648309453
d9e8bdec25ca2d7d3/rest/services

Not open to public
Jurisdiction is part of Champaign County GIS Consortium
Champaign
https://services5.arcgis.com/HBIN2hfRscrws7eM/arcgis/rest/servic
es
Champaign
https://tiles.arcgis.com/tiles/HBIN2hfRscrws7eM/arcgis/rest/servic
es
Christian
https://services.arcgis.com/Xn3XOQd1zDlYr9z7/arcgis/rest/servic
es
Christian
https://tiles.arcgis.com/tiles/Xn3XOQd1zDlYr9z7/arcgis/rest/servi
ces
Clark
Schneider Geospatial - ArcGIS server address is not public

## Page 150

Clay
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/ClayILFeatures/FeatureServer
Go to the top and search for ‘ClayIL’
Clinton
https://services3.arcgis.com/gnvxvf9aoRBjW15Q/ArcGIS/rest/serv
ices/ClintonILFeatures/FeatureServer
Clinton
https://tiles.arcgis.com/tiles/gnvxvf9aoRBjW15Q/arcgis/rest/servic
es
Coles
https://www.colesco.illinois.gov/arcgis/rest/services
Cook
https://gis11.cookcountyil.gov/arcgis/rest/services
Cook
https://gis12.cookcountyil.gov/arcgis/rest/services
Cook
https://gis.cookcountyil.gov/imagery/rest/services
Cook
https://gis.cookcountyil.gov/traditional/rest/services
Cook
https://img.cookcountyil.gov/arcgis/rest/services
Cook
https://img.cookcountyil.gov/imagery/rest/services
Cook
https://services2.arcgis.com/I5Or36sMcO7Y9vQ3/ArcGIS/rest/ser
vices
Crawford
Schneider Geospatial - ArcGIS server address is not public
Cumberland
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/CumberlandILFeatures/FeatureServer
Go to the top and search for ‘CumberlandIL’
Cumberland
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/CumberlandILCadastral/MapServer
DeKalb
https://services7.arcgis.com/hEXJrPwm89CLXBYe/arcgis/rest/ser
vices
DeKalb
https://tiles.arcgis.com/tiles/hEXJrPwm89CLXBYe/arcgis/rest/ser
vices
DeWitt
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/DeWittILFeatures/FeatureServer
Go to the top and search for ‘DeWittIL’
DeWitt
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/DeWittILAerial2017/MapServer
Go to the top and search for ‘DeWittIL’
Douglas
https://services3.arcgis.com/HXjsHxkFFcZquC8P/ArcGIS/rest/ser
vices
Douglas
https://tiles.arcgis.com/tiles/HXjsHxkFFcZquC8P/arcgis/rest/servi
ces
DuPage
https://gis.dupageco.org/arcgis/rest/services

## Page 151

DuPage
          https://services.arcgis.com/neJvtQ4PXvnQ86MJ/arcgis/rest/services
DuPage
https://tiles.arcgis.com/tiles/neJvtQ4PXvnQ86MJ/arcgis/rest/servic
es
Edgar
https://services5.arcgis.com/6VdFeKk2GI4rFk2D/arcgis/rest/servic
es
Edgar
https://tiles.arcgis.com/tiles/6VdFeKk2GI4rFk2D/arcgis/rest/servic
es
Edwards
https://services5.arcgis.com/anr3PwUmzQdlCbyr/arcgis/rest/servic
es
Edwards
https://tiles.arcgis.com/tiles/anr3PwUmzQdlCbyr/arcgis/rest/servic
es
Effingham
https://services.arcgis.com/vj0V9Lal6oiz0YXp/ArcGIS/rest/servic
es
Effingham
          https://tiles.arcgis.com/tiles/vj0V9Lal6oiz0YXp/arcgis/rest/services
Fayette
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/FayetteILFeatures/FeatureServer
Go to the top and search for ‘FayetteIL’
Fayette
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/FayetteILCadastral/MapServer
Go to the top and search for ‘FayetteIL’
Ford
https://services6.arcgis.com/rdrF6CgpwvNG5KF2/arcgis/rest/servi
ces
Ford
https://tiles.arcgis.com/tiles/rdrF6CgpwvNG5KF2/arcgis/rest/servi
ces
Franklin
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/FranklinILFeatures/FeatureServer
Go to the top and search for ‘FranklinIL’
Fulton
           https://services7.arcgis.com/O9Z7JkIFFJ6nOIIq/arcgis/rest/services
Fulton
           https://gis.fultoncountyil.gov/arcgis/rest/services
Gallatin
GIS is not ArcGIS
Greene
https://services1.arcgis.com/Ggva1SWphWGX4bb8/ArcGIS/rest/s
ervices/Greene_County/FeatureServer
Greene
https://tiles.arcgis.com/tiles/Ggva1SWphWGX4bb8/arcgis/rest/ser
vices
Grundy
https://maps.grundyco.org/arcgis/rest/services

## Page 152

Hamilton
https://services.arcgis.com/4YineAQdtmx0tv46/arcgis/rest/services
/HamiltonILFeatures/FeatureServer
Go to the top and search for ‘HamiltonIL’
Hamilton
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/HamiltonILCadastral/MapServer
Go to the top and search for ‘HamiltonIL’
Hancock
https://gis.wiu.edu/arcgis/rest/services/hancock/MapServer
Hardin
No GIS found
Henderson
https://gis.wiu.edu/arcgis/rest/services/Henderson_basemap_online
/MapServer
Henry
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/HenryILFeatures/FeatureServer
Go to the top and search for ‘HenryIL’
See also Stark County
Iroquois
https://services6.arcgis.com/6FZQl5a5SiSFMv8P/arcgis/rest/servic
es
Iroquois
https://tiles.arcgis.com/tiles/6FZQl5a5SiSFMv8P/arcgis/rest/servic
es
Jackson
https://services1.arcgis.com/23PZWuLADSqYBEO7/arcgis/rest/se
rvices
Jackson
https://tiles.arcgis.com/tiles/23PZWuLADSqYBEO7/arcgis/rest/ser
vices
Jasper
           https://services3.arcgis.com/11E0zsJ2JyIebDzH/arcgis/rest/services
Jasper
https://tiles.arcgis.com/tiles/11E0zsJ2JyIebDzH/arcgis/rest/services
Jefferson
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/JeffersonILFeatures/FeatureServer
Go to the top and search for ‘JeffersonIL’
Jefferson
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/JeffersonILCadastral/MapServer
Jersey
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/JerseyILFeatures/FeatureServer
Go to the top and search for ‘JerseyIL’
Jersey
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/JerseyILCadastral/MapServer
Not open to public
Jo Daviess
WMS server

## Page 153

Johnson
No GIS found
Kane
https://gistech.countyofkane.org/arcgis/rest/services
Kane
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/KaneILFeatures/FeatureServer
Go to the top and search for ‘KaneIL’
Kane
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/KaneILCadastral/MapServer
Go to the top and search for ‘KaneIL’
Kankakee
https://k3gis.com/arcgis/rest/services
Kankakee
https://services2.arcgis.com/wtCeg7DiC1GyX2L9/ArcGIS/rest/ser
vices
Kankakee
https://tiles.arcgis.com/tiles/wtCeg7DiC1GyX2L9/arcgis/rest/servi
ces
Kendall
https://maps.co.kendall.il.us/server/rest/services
Kendall
https://services6.arcgis.com/U1zX3Wx8hhY7Gb30/arcgis/rest/serv
ices
Knox
_ttps://co.knox.il.us/gisresources/rest/services
dead link 2
Lake
https://maps.lakecountyil.gov/arcgis/rest/services
Lake
https://maps.lakecountyil.gov/webservices/rest/services
Lake
https://pubaccess.lcfpd.org/arcgis/rest/services
LaSalle
https://gis.lasallecounty.org/arcgis/rest/services
LaSalle
https://services3.arcgis.com/H84yQSxNIj9pXjJ7/ArcGIS/rest/servi
ces
LaSalle
          https://tiles.arcgis.com/tiles/H84yQSxNIj9pXjJ7/arcgis/rest/services
Lawrence
https://services2.arcgis.com/AtoBX9sHdZu4i3gx/arcgis/rest/servic
es
Lawrence
https://tiles.arcgis.com/tiles/AtoBX9sHdZu4i3gx/arcgis/rest/servic
es
Lee
https://gis.leecountyil.gov/leecogis/rest/services
Livingston
Must pay $ to access GIS
Logan
https://www.centralilmaps.com/arcgis/rest/services
Macon
https://services1.arcgis.com/a3k0qIja5SolIRYR/arcgis/rest/services
Macon
https://tiles.arcgis.com/tiles/a3k0qIja5SolIRYR/arcgis/rest/services

## Page 154

Macoupin
https://services.arcgis.com/LYDdxoqTV7fw9teL/arcgis/rest/servic
es
Macoupin
https://tiles.arcgis.com/tiles/LYDdxoqTV7fw9teL/arcgis/rest/servi
ces
Madison
https://gisportal.co.madison.il.us/servera/rest/services
Table of contents disabled
Madison
https://services.arcgis.com/Z0kKj2K728ngqqrp/arcgis/rest/services
Marion
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MarionILFeatures/FeatureServer
Go to the top and search for ‘MaroinIL’
Marion
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MarionILCadastral/MapServer
Go to the top and search for ‘MaroinIL’
Marshall
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MarshallILFeatures/FeatureServer
Go to the top and search for ‘MarshallIL’
Marshall
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MarshallILCadastral/MapServer
Mason
GIS is not ArcGIS
Massac
https://services7.arcgis.com/BDZP61z0a0OeR13M/arcgis/rest/serv
ices
Massac
https://tiles.arcgis.com/tiles/BDZP61z0a0OeR13M/arcgis/rest/serv
ices
McDonough
https://gis.wiu.edu/arcgis/rest/services/mcdonough_highway/MapS
erver
McHenry
https://www.mchenrycountygis.org/ArcGIS/rest/services
McHenry
https://www.mchenrycountygis.org/arcgis/rest/services
McHenry
https://services1.arcgis.com/6iYC5AXXYapRVNzl/arcgis/rest/ser
vices
McHenry
https://tiles.arcgis.com/tiles/6iYC5AXXYapRVNzl/arcgis/rest/serv
ices
McLean
https://www.mcgisweb.org/mcgc/rest/services
McLean
https://gis.mcleancountyil.gov/arcgis/rest/services
McLean
https://services1.arcgis.com/BJrdGkaoNV5kaUCP/ArcGIS/rest/ser
vices
McLean
https://tiles.arcgis.com/tiles/BJrdGkaoNV5kaUCP/arcgis/rest/servi
ces

## Page 155

McLean
https://services3.arcgis.com/ZntpsilxOye7y1YF/ArcGIS/rest/servic
es
GIS consortium
McLean
https://tiles.arcgis.com/tiles/ZntpsilxOye7y1YF/arcgis/rest/services
Menard
https://wfs.schneidercorp.com/arcgis/rest/services/MenardCountyI
L_WFS/MapServer
Mercer
https://services1.arcgis.com/p5CKEkDVdYePfy0g/arcgis/rest/servi
ces
Monroe
https://services.arcgis.com/AZVIEb4WFZST2UYx/arcgis/rest/serv
ices
Montgomery
Schneider Geospatial - ArcGIS server address is not public
Morgan
https://services3.arcgis.com/95PFahBF8eyGEfuc/arcgis/rest/servic
es
Morgan
https://tiles.arcgis.com/tiles/95PFahBF8eyGEfuc/arcgis/rest/servic
es
Moultrie
_ttps://ags.bhamaps.com/arcgisserver/rest/services/MoultrieIL
dead link 2
Ogle
          https://services.arcgis.com/QIuff75cyUuYtSQm/arcgis/rest/services
Ogle
https://tiles.arcgis.com/tiles/QIuff75cyUuYtSQm/arcgis/rest/servic
es
Pekin
https://gis.ci.pekin.il.us/arcgis/rest/services
Peoria
https://gis.peoriacounty.org/arcgis/rest/services        SSL problem
Peoria
https://gis.peoriacounty.gov/arcgis/rest/services
Peoria
https://services.arcgis.com/iPiPjILCMYxPZWTc/arcgis/rest/servic
es
Peoria
https://tiles.arcgis.com/tiles/iPiPjILCMYxPZWTc/arcgis/rest/servi
ces
Perry
Schneider Geospatial - ArcGIS server address is not public
Piatt
https://services.ccgisc.org/portal/sharing/servers/7c88732ba0694b2
098f17c434ed3a56b/rest/services
Not open to public
Pike
GIS is not ArcGIS
Pope
No GIS found
Pulaski
No GIS found

## Page 156

Putnam
GIS is not ArcGIS
Randolph
https://services5.arcgis.com/pweYHqdOby1TE9DD/arcgis/rest/ser
vices
Randolph
https://tiles.arcgis.com/tiles/pweYHqdOby1TE9DD/arcgis/rest/ser
vices
Richland
GIS is not ArcGIS
Rock Island
https://gis.rockislandcountyil.gov/arcgis/rest/services
Saline
No GIS found
Sangamon
https://sangis.co.sangamon.il.us/image/rest/services
Schuyler
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/SchuylerILFeatures/FeatureServer
Go to the top and search for ‘SchuylerIL’
Schuyler
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/SchuylerILCadastral/MapServer
Go to the top and search for ‘SchuylerIL’
Scott
No GIS found
Shelby
_ttps://ags.bhamaps.com/arcgisserver/rest/services/ShelbyIL
dead link 2
St Clair
_ttps://publicmap01.co.st-clair.il.us/arcgis/rest/services
dead link 1
Stark
https://services6.arcgis.com/IMZwRRU1qL5MDxBH/arcgis/rest/s
ervices
Stark
https://tiles.arcgis.com/tiles/IMZwRRU1qL5MDxBH/arcgis/rest/se
rvices
Stephenson
https://maps.wingis.org/public/rest/services/StephensonPublicProp
ertySearch/MapServer
Not open to public
Tazewell
_ttps://gis.tazewell.com/arcgis/rest/services
dead link 2
Tazewell
https://www.centralilmaps.com/arcgis/rest/services/Tazewell
Tazewell
https://services.arcgis.com/LIEind9C2d6XYeOY/arcgis/rest/servic
es
Union
https://services5.arcgis.com/72ZZon8FQb6nYtKt/ArcGIS/rest/serv
ices/UnionIL_Parcels/FeatureServer

## Page 157

Vermilion
_ttps://ags.bhamaps.com/arcgisserver/rest/services/VermilionIL
dead link 2
Vermilion
https://services6.arcgis.com/am689ZyfXfdo9vCK/ArcGIS/rest/serv
ices
Vermilion
https://tiles.arcgis.com/tiles/am689ZyfXfdo9vCK/arcgis/rest/servic
es
Wabash
No GIS found
Warren
https://services9.arcgis.com/RIfeUk3WiZQO2Wv1/arcgis/rest/serv
ices
Warren
https://tiles.arcgis.com/tiles/RIfeUk3WiZQO2Wv1/arcgis/rest/serv
ices
Washington
https://services5.arcgis.com/72ZZon8FQb6nYtKt/arcgis/rest/servic
es/WashingtonIL_wEdgeParcels/FeatureServer
Wayne
ArcGIS server but cannot find address.
White
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/WhiteILFeatures/FeatureServer
Go to the top and search for ‘WhiteIL’
White
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/WhiteILCadastral/MapServer
Whiteside
https://services.arcgis.com/l0M0OC6J9QAHCiGx/arcgis/rest/servi
ces
Whiteside
https://tiles.arcgis.com/tiles/l0M0OC6J9QAHCiGx/arcgis/rest/serv
ices
Will
https://gis.willcountyillinois.com/server/rest/services
Will
https://services.arcgis.com/fGsbyIOAuxHnF97m/arcgis/rest/servic
es
Will
https://tiles.arcgis.com/tiles/fGsbyIOAuxHnF97m/arcgis/rest/servi
ces
Williamson
https://services7.arcgis.com/byqmKSJsXgoLI05S/arcgis/rest/servic
es
Williamson
https://tiles.arcgis.com/tiles/byqmKSJsXgoLI05S/arcgis/rest/servic
es
Winnebago
https://maps.wingis.org/public/rest/services/PublicPropertySearch/
MapServer
Woodford
_ttps://www.centralilmaps.com/arcgis/rest/services/Woodford
dead link 1

## Page 158

Illinois City, Town, Village, etc GIS Servers
Aurora
https://services1.arcgis.com/79UxTxnBeBW8JHY4/arcgis/rest/ser
vices
Bartlett
https://services6.arcgis.com/COXcDw4MjTwPS9Lu/arcgis/rest/ser
vices
Bartlett
https://tiles.arcgis.com/tiles/COXcDw4MjTwPS9Lu/arcgis/rest/ser
vices
Burlington
Integritygis - ArcGIS server address is not public
Champaign
https://gisweb.champaignil.gov/cb/rest/services
Champaign
https://gisportal.champaignil.gov/is/rest/services
Champaign
          https://services.arcgis.com/tpnvcOxxttZuMwYB/arcgis/rest/services
Champaign
https://tiles.arcgis.com/tiles/tpnvcOxxttZuMwYB/arcgis/rest/servic
es
Chicago
https://gisapps.cityofchicago.org/arcgis/rest/services
Chicago
https://services2.arcgis.com/t3tlzCPfmaQzSWAk/ArcGIS/rest/serv
ices
Chicago
https://services7.arcgis.com/A03QrhyHnDaUmK0W/ArcGIS/rest/s
ervices
Chicago
https://services7.arcgis.com/HpTF5nhGpVZolZvo/ArcGIS/rest/ser
vices
Park district
Chicago
https://tiles.arcgis.com/tiles/HpTF5nhGpVZolZvo/arcgis/rest/servi
ces
Chicago
https://services8.arcgis.com/JIh9xpU69QvVf5IC/arcgis/rest/servic
es
Clinton
Website says they have a GIS but could not find it.
Coal Valley
Integritygis - ArcGIS server address is not public
Danvers
https://services1.arcgis.com/seK2PXRM9wrYU3QB/ArcGIS/rest/s
ervices
Danville
https://gis.cityofdanville.org/arcgis/rest/services
Danville
https://services1.arcgis.com/5SgLK7rhBciydlkM/ArcGIS/rest/servi
ces
Decatur
https://maps.decaturil.gov/arcgis/rest/services
Decatur
https://services3.arcgis.com/cEATg7wEKTfd9Ssj/ArcGIS/rest/serv
ices
Decatur
https://tiles.arcgis.com/tiles/cEATg7wEKTfd9Ssj/arcgis/rest/servic
es

## Page 159

DeWitt
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/DeWittILFeatures/FeatureServer
Go to the top and search for ‘DeWittIL’
DeWitt
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/DeWittILCadastral/MapServer
Go to the top and search for ‘DeWittIL’
Diamond
__________
Downers Grove
https://parcels.downers.us/arcgis/rest/services
Elgin
https://gisdata.elginmapping.ca/arcgis/rest/services
Elgin
https://services5.arcgis.com/tsDpkyNqjjzAB8LP/ArcGIS/rest/servi
ces
Elgin
          https://tiles.arcgis.com/tiles/tsDpkyNqjjzAB8LP/arcgis/rest/services
Eureka
https://services8.arcgis.com/UBUuSWSkdFegkmHv/ArcGIS/rest/s
ervices
Evanston
https://maps.cityofevanston.org/arcgis/rest/services
Evanston
https://services3.arcgis.com/RVAJnWJd9M0xRdYG/ArcGIS/rest/s
ervices
Evanston
https://tiles.arcgis.com/tiles/RVAJnWJd9M0xRdYG/arcgis/rest/ser
vices
Franklin
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/FranklinILFeatures/FeatureServer
Go to the top and search for ‘FranklinIL’
Galesburg
https://gis.ci.galesburg.il.us/server/rest/services
Galesburg
https://redqueen.ci.galesburg.il.us/server/rest/services
Galesburg
https://services1.arcgis.com/T5ar9pn3YeFZ47Wh/ArcGIS/rest/ser
vices
Galesburg
https://tiles.arcgis.com/tiles/T5ar9pn3YeFZ47Wh/arcgis/rest/servic
es
Greenville
https://portal.greenvilleillinois.com/cog_server/rest/services
Greenville
https://services.arcgis.com/jvIdRKgHFjCLnr7p/arcgis/rest/services
Gurnee
https://webmaps.gurnee.il.us/arcgis/rest/services
Gurnee
https://services1.arcgis.com/maA4FBAqIkT6mqM6/ArcGIS/rest/s
ervices
Gurnee
https://tiles.arcgis.com/tiles/maA4FBAqIkT6mqM6/arcgis/rest/ser
vices

## Page 160

Hamilton
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/HamiltonILFeatures/FeatureServer
Go to the top and search for ‘HamiltonIL’
Henry
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/HenryILFeatures/FeatureServer
Go to the top and search for ‘HenryIL’
Hoffman Estates
https://services3.arcgis.com/wZbN8jfxpSCT3u1Y/ArcGIS/rest/ser
vices
Hoffman Estates
https://tiles.arcgis.com/tiles/wZbN8jfxpSCT3u1Y/arcgis/rest/servi
ces
Homewood
https://arcgis.mobile311.com/arcgis/rest/services/Illinois/Homewo
odIL/MapServer
Homewood
https://services1.arcgis.com/kZsOWCED80XbRyJ0/arcgis/rest/ser
vices
Many jurisdictions.  Search on Homewood.
Homewood
https://tiles.arcgis.com/tiles/kZsOWCED80XbRyJ0/arcgis/rest/ser
vices
Huntley
https://services5.arcgis.com/YlgRGCqs9G4jixvJ/ArcGIS/rest/servi
ces
Joliet
See Will County
Kane
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/KaneILFeatures/FeatureServer
Go to the top and search for ‘KaneIL’
Lisle
https://services2.arcgis.com/wDBqgmWyVJy4nPiT/ArcGIS/rest/se
rvices
Lombard
https://gismaps.villageoflombard.org/arcgis/rest/services
Lombard
https://services6.arcgis.com/vs0Q5ds549q7lQMm/ArcGIS/rest/ser
vices
Lombard
https://tiles.arcgis.com/tiles/vs0Q5ds549q7lQMm/arcgis/rest/servic
es
Macomb
https://gis.wiu.edu/arcgis/rest/services/macomb_public/MapServer
Mahomet
https://services.ccgisc.org/portal/sharing/servers/151559648309453
d9e8bdec25ca2d7d3/rest/services
Not open to public
Jurisdiction is part of Champaign County GIS Consortium
Marion
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MarionILFeatures/FeatureServer

## Page 161

Go to the top and search for ‘Marion’
Marshall
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MarshallILFeatures/FeatureServer
Go to the top and search for ‘Marshall’
Maryville
https://services2.arcgis.com/yA8uDYLwXT5AnxTb/arcgis/rest/ser
vices
Maryville
https://tiles.arcgis.com/tiles/yA8uDYLwXT5AnxTb/arcgis/rest/ser
vices
Monmouth
https://gis.wiu.edu/arcgis/rest/services/macomb_public/MapServer
Morton
https://services3.arcgis.com/1N8MvzKOD4JGoLTu/arcgis/rest/ser
vices
Morton
https://tiles.arcgis.com/tiles/1N8MvzKOD4JGoLTu/arcgis/rest/ser
vices
Mount Prospect
https://gisportal.mountprospect.org/server/rest/services
Naperville
https://portal.naperville.il.us/arcgis/rest/services
Naperville
https://portal.naperville.il.us/arcgis2/rest/services
Naperville
https://services1.arcgis.com/rXJ6QApc2sOtl1Pd/ArcGIS/rest/servi
ces
Naperville
           https://tiles.arcgis.com/tiles/rXJ6QApc2sOtl1Pd/arcgis/rest/services
Niles
https://gis.vniles.com/server/rest/services
Niles
https://gisuf.vniles.com:6443/arcgis/rest/services       SSL problem
Normal
https://services2.arcgis.com/iXvQvjNLkAH7PI1v/arcgis/rest/servi
ces
Normal
https://tiles.arcgis.com/tiles/iXvQvjNLkAH7PI1v/arcgis/rest/servic
es
O'Fallon
           https://services.arcgis.com/K8hCj4l2z1EMabnx/arcgis/rest/services
O'Fallon
https://tiles.arcgis.com/tiles/K8hCj4l2z1EMabnx/arcgis/rest/servic
es
Orland Park
https://services3.arcgis.com/sVDuYsm37AMvFL49/ArcGIS/rest/s
ervices
Orland Park
https://services6.arcgis.com/CTsBNAABsLr3KeH3/arcgis/rest/ser
vices
Orland Fire Protection District
Oswego
ArcGIS table of contents not available
Peoria
https://gis.peoriagov.org/copgis/rest/services

## Page 162

Peoria
https://gis.peoriagov.org/server/rest/services
Peoria
https://services1.arcgis.com/Vm4J3EDyqMzmDYgP/ArcGIS/rest/s
ervices
Pittsfield
Integritygis - ArcGIS server address is not public
Rantoul
https://services.ccgisc.org/portal/sharing/servers/151559648309453
d9e8bdec25ca2d7d3/rest/services
Not open to public
Jurisdiction is part of Champaign County GIS Consortium
Rockford
https://services2.arcgis.com/Fh2bD9911cyi2gO2/ArcGIS/rest/servi
ces
Rockford
          https://tiles.arcgis.com/tiles/Fh2bD9911cyi2gO2/arcgis/rest/services
St. Charles
          https://services6.arcgis.com/K7950S4bDbtsSspe/arcgis/rest/services
Savoy
https://services.ccgisc.org/portal/sharing/servers/151559648309453
d9e8bdec25ca2d7d3/rest/services
Not open to public
Jurisdiction is part of Champaign County GIS Consortium

Schaumburg
https://gispublic.schaumburg.com/arcgis/rest/services

Springfield
https://publicworks.springfield.il.us/arcgis/rest/services
Springfield
https://maps.springfield.il.us/server/rest/services
Springfield
https://services1.arcgis.com/iiIcolLRR8oBZQV6/ArcGIS/rest/servi
ces
Springfield
          https://tiles.arcgis.com/tiles/iiIcolLRR8oBZQV6/arcgis/rest/services
Urbana
https://services.ccgisc.org/portal/sharing/servers/151559648309453
d9e8bdec25ca2d7d3/rest/services
Not open to public
Jurisdiction is part of Champaign County GIS Consortium
Vernon Hills
https://services.arcgis.com/B6g1snvDJFY2QRqn/arcgis/rest/servic
es
Vernon Hills
https://tiles.arcgis.com/tiles/B6g1snvDJFY2QRqn/arcgis/rest/servi
ces
Villa Park
https://services5.arcgis.com/jmdi6ffhe45GMz1s/ArcGIS/rest/servic
es
Washington
https://services1.arcgis.com/KvhR4yxUNNPvtbwc/ArcGIS/rest/ser
vices
Washington
https://tiles.arcgis.com/tiles/KvhR4yxUNNPvtbwc/arcgis/rest/servi
ces

## Page 163

Western Springs
https://services1.arcgis.com/hh2VCtfzZp8V2Vbe/ArcGIS/rest/serv
ices
Westmont
https://services5.arcgis.com/XWUAZV69Zk3cPZHa/ArcGIS/rest/s
ervices
Wheaton
https://services2.arcgis.com/YyIQHvpylgCY7DEY/ArcGIS/rest/se
rvices
Wheaton
https://tiles.arcgis.com/tiles/YyIQHvpylgCY7DEY/arcgis/rest/servi
ces
Wood Dale
https://services3.arcgis.com/gtOFGDNHdftP2Pps/arcgis/rest/servic
es
Indiana State GIS Servers
Indiana imagery
GIS: https://di-ingov.img.arcgis.com/arcgis/rest/services
Indiana Map
Website: https://www.indianamap.org
GIS: https://gisdata.in.gov/server/rest/services
Primary source of state data
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Indiana Department of Homeland Security
Website: https://www.in.gov/dhs
GIS: https://gis.dhs.in.gov/arcgis/rest/services
8-2-2023 No tiled data
Indiana Department of Natural Resources
Website: https://www.in.gov/dnr
GIS: https://services.arcgis.com/2Mcx1M1MORKfBNPM/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/2Mcx1M1MORKfBNPM/arcgis/rest/services
Indiana Department of Transportation
Website: https://www.in.gov/indot
GIS: https://gis.indot.in.gov/ro/rest/services
Indiana Economic Development Corporation
Website: https://iedc.in.gov
GIS: https://services7.arcgis.com/8itH5a0w1RjR358N/arcgis/rest/services
Indiana Geological and Water Survey
Website: https://igws.iu.edu
GIS: https://services5.arcgis.com/IbvYBHPoRfsshd4f/arcgis/rest/services

## Page 164

Purdue University Center for Regional Development
Website: https://pcrd.purdue.edu
GIS: https://pcrdgis.agriculture.purdue.edu/arcgis/rest/services
GIS: https://prodgis2.agriculture.purdue.edu/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://services8.arcgis.com/jUmevr1H1ZuZxhaN/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/jUmevr1H1ZuZxhaN/arcgis/rest/services
Indiana various layers
GIS: https://services1.arcgis.com/I8z2b94vxVch7Rld/ArcGIS/rest/services
Monon South Trail
GIS: https://services2.arcgis.com/DXfJ1UFKElRbbqT4/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/DXfJ1UFKElRbbqT4/arcgis/rest/services
GIS: https://services3.arcgis.com/fAJUAyCk5qmGxuxo/arcgis/rest/services
GIS: https://services5.arcgis.com/f2aRfVsQG7TInso2/arcgis/rest/services
Indiana County GIS Servers
All counties are listed
Adams
https://adamsingis.adams.in.us/arcgis/rest/services
Allen
https://gis.acimap.us/projectservicesadmin/rest/services
Allen
https://gis1.acimap.us/projectservices/rest/services
Bartholomew
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/BartholomewINDynamic/MapServer
Benton
They have a GIS but it is not ArcGIS
Blackford
Schneider Geospatial - ArcGIS server address is not public
Boone
https://services3.arcgis.com/mHzLz9pyDvq3Hzze/arcgis/rest/servi
ces
Boone
https://tiles.arcgis.com/tiles/mHzLz9pyDvq3Hzze/arcgis/rest/servi
ces
Brown
They have a GIS but it is not ArcGIS
Carroll
Schneider Geospatial - ArcGIS server address is not public
Cass
Schneider Geospatial - ArcGIS server address is not public
Clark
_ttps://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/ClarkINDynamic/MapServer
dead link 1
Clay
They have a GIS but it is not ArcGIS

## Page 165

Clinton
Schneider Geospatial - ArcGIS server address is not public
Crawford
GIS is not ArcGIS
Clinton
Schneider Geospatial - ArcGIS server address is not public
Dearborn
https://gis.dearborncounty.in.gov/arcgis/rest/services
Decatur
https://wfs.schneidercorp.com/arcgis/rest/services/DecaturCountyI
N_WFS/MapServer
DeKalb
https://services5.arcgis.com/PaWckjuEwz6CBkgU/ArcGIS/rest/ser
vices
DeKalb
https://tiles.arcgis.com/tiles/PaWckjuEwz6CBkgU/arcgis/rest/servi
ces
Delaware
https://services.arcgis.com/VyRjdyMziYNF5Bwe/arcgis/rest/servic
es
Delaware
https://tiles.arcgis.com/tiles/VyRjdyMziYNF5Bwe/arcgis/rest/servi
ces
Dubois
They have a GIS but it is not ArcGIS
Elkhart
_ttps://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/ElkhartINDynamic/MapServer
dead link 2
Fayette
GIS is not ArcGIS
Floyd
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/FloydINDynamic/MapServer
Fountain
Schneider Geospatial - ArcGIS server address is not public
Franklin
They have a GIS but it is not ArcGIS
Fulton
They have a GIS but it is not ArcGIS
Gibson
Schneider Geospatial - ArcGIS server address is not public
Grant
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/GrantINDynamic/MapServer
Greene
They have a GIS but it is not ArcGIS
Hamilton
https://gis1.hamiltoncounty.in.gov/arcgis/rest/services

## Page 166

Hancock
https://wfs.schneidercorp.com/arcgis/rest/services/HancockCountyI
N_WFS/MapServer
Harrison
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/HarrisonINDynamic/MapServer
Hendricks
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/HendricksINDynamic/MapServer
Henry
Schneider Geospatial - ArcGIS server address is not public
Howard
Schneider Geospatial - ArcGIS server address is not public
Huntington
https://wfs.schneidercorp.com/arcgis/rest/services/HuntingtonCoun
tyIN_WFS/MapServer
Jackson
They have a GIS but it is not ArcGIS
Jasper
Schneider Geospatial - ArcGIS server address is not public
Jay
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/JayINDynamic/MapServer
Jefferson
They have a GIS but it is not ArcGIS
Jennings
They have a GIS but it is not ArcGIS
Johnson
https://wfs.schneidercorp.com/arcgis/rest/services/JohnsonCountyI
N_WFS/MapServer
Johnson
https://services2.arcgis.com/s5B7dXoVjGiD4IBE/ArcGIS/rest/serv
ices
Knox
GIS is not ArcGIS
Kosciusko
https://wfs.schneidercorp.com/arcgis/rest/services/KosciuskoCount
yIN_WFS/MapServer
LaGrange
https://wfs.schneidercorp.com/arcgis/rest/services/LaGrangeCount
yIN_WFS/MapServer
Lake
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/LakeINFeatures/FeatureServer
Go to the top and search for ‘LakeIN’
Lake
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/LakeINCadastral/MapServer
Go to the top and search for ‘LakeIN’

## Page 167

LaPorte
https://services1.arcgis.com/AVtBlY7uGIkiTrT0/arcgis/rest/servic
es
LaPorte
          https://tiles.arcgis.com/tiles/AVtBlY7uGIkiTrT0/arcgis/rest/services
Lawrence
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/LawrenceINDynamic/MapServer
Madison County Council of Governments
https://heartlandmpo.com/arcgis/rest/services
https://services.arcgis.com/WO41K9zxsNclVVfS/arcgis/rest/servic
es
https://tiles.arcgis.com/tiles/WO41K9zxsNclVVfS/arcgis/rest/servi
ces
Marion
https://xmaps.indy.gov/arcgis/rest/services
Marshall
Schneider Geospatial - ArcGIS server address is not public
Martin
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/MartinINDynamic/MapServer
Miami
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/MiamiINDynamic/MapServer
Miami
https://wfs.schneidercorp.com/arcgis/rest/services/MiamiCountyIN
_WFS/MapServer
Monroe
_ttps://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/MonroeINDynamic/MapServer
dead link 1
Monroe
https://wfs.schneidercorp.com/arcgis/rest/services/MonroeCountyI
N_WFS/MapServer
Monroe
https://services1.arcgis.com/nYfGJ9xFTKW6VPqW/ArcGIS/rest/s
ervices
Monroe
https://tiles.arcgis.com/tiles/nYfGJ9xFTKW6VPqW/arcgis/rest/ser
vices
Montgomery
Schneider Geospatial - ArcGIS server address is not public
Morgan
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/MorganINDynamic/MapServer
Morgan
https://wfs.schneidercorp.com/arcgis/rest/services/MorganCountyI
N_WFS/MapServer
Newton
Schneider Geospatial - ArcGIS server address is not public
Noble
https://gisserver.nobleco.us/server/rest/services

## Page 168

Ohio
Also have a GIS that is not ArcGIS
Orange
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/OrangeINDynamic/MapServer
Owen
GIS is not ArcGIS
Park
GIS is not ArcGIS
Perry
GIS is not ArcGIS
Pike
GIS is not ArcGIS
Porter
https://gispro.porterco.org/server/rest/services
Porter
https://services6.arcgis.com/TQ2Al5QIvv4tMBL7/ArcGIS/rest/ser
vices
Porter
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/PorterINFeatures/FeatureServer
Go to the top and search for ‘PorterIN’
Porter
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/PorterINCadastral/MapServer
Go to the top and search for ‘PorterIN’
Posie
GIS is not ArcGIS
Pulaski
GIS is not ArcGIS
Putnam
GIS is not ArcGIS
Randolph
GIS is not ArcGIS
Ripley
GIS is not ArcGIS
Rush
https://wfs.schneidercorp.com/arcgis/rest/services/RushCountyIN_
WFS/MapServer
St. Joseph
https://services.arcgis.com/OjftlhRHkAABcyiF/arcgis/rest/services
St. Joseph
          https://tiles.arcgis.com/tiles/OjftlhRHkAABcyiF/arcgis/rest/services
Scott
GIS is not ArcGIS
Shelby
GIS is not ArcGIS
Spencer
GIS is not ArcGIS
Starke
GIS is not ArcGIS

## Page 169

Steuben
https://wfs.schneidercorp.com/arcgis/rest/services/SteubenCountyI
N_WFS/MapServer
Sullivan
GIS is not ArcGIS
Switzerland
GIS is not ArcGIS
Tippecanoe
https://maps.tippecanoe.in.gov/server/rest/services
Table of contents disabled
Tippecanoe
_ttps://wfs.schneidercorp.com/arcgis/rest/services/TippecanoeCoun
tyIN_WFS/MapServer
dead link 1
Tipton
https://wfs.schneidercorp.com/arcgis/rest/services/TiptonCountyIN
_WFS/MapServer
Union
GIS is not ArcGIS
Vanderburgh
https://services.arcgis.com/yFpJgRYLVh30Ez7R/arcgis/rest/servic
es
Vanderburgh
See also city of Evansville
Vermillion
GIS is not ArcGIS
Vigo
GIS is not ArcGIS
Wabash
https://wfs.schneidercorp.com/arcgis/rest/services/WabashCountyI
N_WFS/MapServer
Warren
They have a GIS but not ArcGIS
Warrick
They have a GIS but not ArcGIS
Washington
They have a GIS but not ArcGIS
Wayne
https://gisweb3.co.wayne.in.us/arcgis/rest/services
Wayne
https://services3.arcgis.com/fhBemP00ea7p7i0U/ArcGIS/rest/servi
ces
Wayne
          https://tiles.arcgis.com/tiles/fhBemP00ea7p7i0U/arcgis/rest/services
Wells
https://wfs.schneidercorp.com/arcgis/rest/services/WellsCountyIN_
WFS/MapServer
White
Schneider Geospatial - ArcGIS server address is not public
Whitley
https://wfs.schneidercorp.com/arcgis/rest/services/WhitleyCountyI
N_WFS/MapServer

## Page 170

Indiana City, Town, Village, etc GIS Servers
Avon
Schneider Geospatial - ArcGIS server address is not public
Bloomington
https://bloomington.in.gov/arcgis-server/rest/services
Bloomington
https://services9.arcgis.com/47GwVXZ9a8thrviM/ArcGIS/rest/ser
vices
Bloomington
https://tiles.arcgis.com/tiles/47GwVXZ9a8thrviM/arcgis/rest/servi
ces
Brownsburg
https://wfs.schneidercorp.com/arcgis/rest/services/TownofBrownsb
urgIN/MapServer
Brownsburg
https://services7.arcgis.com/R9CVCgaSS8Zy2txP/ArcGIS/rest/ser
vices
Brownsburg
https://tiles.arcgis.com/tiles/R9CVCgaSS8Zy2txP/arcgis/rest/servi
ces
Carmel
https://services5.arcgis.com/nKFfYbLYNDrYHgoO/ArcGIS/rest/s
ervices
Carmel
See also Hamilton County
Crown Point
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/CrownPointINDynamic/MapServer
Danville
Schneider Geospatial - ArcGIS server address is not public
Demotte
https://services7.arcgis.com/1gs4qYbKcpLjZvTV/arcgis/rest/servic
es
Evansville
https://maps.evansvillegis.com/arcgis_server/rest/services
Evansville
https://services1.arcgis.com/iZyBOluseC8ffQc2/ArcGIS/rest/servic
es
Fishers
https://maps.fishers.in.us/arcgis/rest/services
Fishers
https://services.arcgis.com/CLuli6D9IiF45RRj/arcgis/rest/services
Fort Wayne
https://gis.acimap.us/reference/rest/services
Gary
https://services.arcgis.com/HON99YWuCBluGwYq/arcgis/rest/ser
vices
Gary
https://services7.arcgis.com/ZEo2rzqxSTElUpNo/arcgis/rest/servic
es
Goshen
https://services8.arcgis.com/trHxDV6stlqDdGWV/ArcGIS/rest/ser
vices
Goshen
https://tiles.arcgis.com/tiles/trHxDV6stlqDdGWV/arcgis/rest/servi
ces

## Page 171

Greenfield
https://wfs.schneidercorp.com/arcgis/rest/services/CityofGreenfield
IN_WFS/MapServer
Greensburg
https://services5.arcgis.com/JyUjaMA8RG5613cC/ArcGIS/rest/ser
vices
Greensburg
https://tiles.arcgis.com/tiles/JyUjaMA8RG5613cC/arcgis/rest/servi
ces
Greenwood
https://greenwoodgis.greenwood.in.gov/arcgis/rest/services
Hamilton
Hobart
https://gis.cityofhobart.org/arcgis/rest/services

Indianapolis
See Marion County
Jeffersonville
__________
Knox
https://services2.arcgis.com/cYVeFbfBzn7pCPPk/arcgis/rest/servic
es
Kokomo
See Howard County
Kouts
https://services3.arcgis.com/RuMMvs5Xi9tKqAgI/arcgis/rest/servi
ces
Lawrence
Schneider Geospatial - ArcGIS server address is not public
Lowell
https://elb.elevatemaps.io/arcgis/rest/services/eGISDynamicServic
es/LowellINDynamic/MapServer
McCordsville
Schneider Geospatial - ArcGIS server address is not public
Munster
https://services3.arcgis.com/iQAkxbE5rgLj88rC/ArcGIS/rest/servi
ces
Noblesville
https://services1.arcgis.com/HY8DpOvlbJ7tf8SU/ArcGIS/rest/serv
ices
Noblesville
https://tiles.arcgis.com/tiles/HY8DpOvlbJ7tf8SU/arcgis/rest/servic
es
North Liberty
https://services5.arcgis.com/dgRVxH8SlcSzEBc8/arcgis/rest/servi
ces
Plainfield
https://services6.arcgis.com/3ejT7DEfNyzKXZBD/ArcGIS/rest/ser
vices

## Page 172

Plainfield
Schneider Geospatial - ArcGIS server address is not public
Plymouth
https://wfs.schneidercorp.com/arcgis/rest/services/CityofPlymouthI
N_REST/MapServer
Seymour
https://arcgis.mobile311.com/arcgis/rest/services/Indiana/SeymourI
N/MapServer
South Bend
https://gis.southbendin.gov/arcgis/rest/services
South Bend
https://maps.southbendin.gov/arcgis/rest/services
South Bend
https://services1.arcgis.com/0n2NelSAfR7gTkr1/ArcGIS/rest/servi
ces
South Bend
          https://tiles.arcgis.com/tiles/0n2NelSAfR7gTkr1/arcgis/rest/services
Steuben Lakes
_________
Valparaiso
Schneider Geospatial - ArcGIS server address is not public
Walkerton
https://services8.arcgis.com/Js0MprtKdAByRc6M/arcgis/rest/servi
ces
Warsaw
https://maps.warsaw.in.gov/arcgis/rest/services
Westfield
https://maps.westfield.in.gov/arcgis/rest/services
Whitestown
See Boone County
Iowa State GIS Servers
 Iowa Open Data Portal
Website: https://data.iowa.gov/
Iowa Department of Homeland Security and Emergency Management
Website: https://homelandsecurity.iowa.gov/
GIS: https://eoc.iowa.gov/arcgis/rest/services
Parcel lines:  Public/parcels_da/MapServer/0
Parcel lines:  Public/AdminBoundaries/MapServer     2017 data
8-2-2023 No tiled data
Iowa Department of Natural Resources
Website: https://www.iowadnr.gov
GIS: https://programs.iowadnr.gov/geospatial/rest/services
8-2-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services2.arcgis.com/r6iFVcMJeA4kB4GC/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/r6iFVcMJeA4kB4GC/arcgis/rest/services

## Page 173

Iowa Department of Transportation
Website: https://www.iowadot.gov/#/services
GIS: https://gis.iowadot.gov/agshost/rest/services
8-2-2023 No tiled data
GIS: https://gis.iowadot.gov/imagery/rest/services
GIS: https://services.arcgis.com/8lRhdTsQyJpO52F1/arcgis/rest/services
Traffic_Cameras_View
GIS: https://tiles.arcgis.com/tiles/8lRhdTsQyJpO52F1/arcgis/rest/services
Iowa legislature
Website: https://www.legis.iowa.gov
GIS: https://gis.legis.iowa.gov/arcgis/rest/services
8-2-2023 No tiled data
Iowa State University GIS Support and Research Facility
Website: https://www.gis.iastate.edu/about/facility
GIS: https://ortho.gis.iastate.edu/arcgis/rest/services
8-2-2023 No tiled data
Iowa various layers
GIS: https://geoservices.iowa.gov/arcgis/rest/services
8-2-2023 No tiled data
GIS: https://services.arcgis.com/vPD5PVLI6sfkZ5E4/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/vPD5PVLI6sfkZ5E4/arcgis/rest/services
Iowa Regional
Des Moines Area Metropolitan Planning Organization
Website: https://dmampo.org
GIS: https://services1.arcgis.com/6oz1ALkDiRZ7VlIc/ArcGIS/rest/services
Iowa County GIS Servers
Adair
https://wfs.schneidercorp.com/arcgis/rest/services/AdairCountyIA_
WFS/MapServer
Adams
Schneider Geospatial - ArcGIS server address is not public
Allamakee
Schneider Geospatial - ArcGIS server address is not public
Audubon
Schneider Geospatial - ArcGIS server address is not public
Benton
Schneider Geospatial - ArcGIS server address is not public
Black Hawk
Schneider Geospatial - ArcGIS server address is not public

## Page 174

Boone
https://services3.arcgis.com/ScA2Liqz4XcDow5L/arcgis/rest/servi
ces
Boone
https://tiles.arcgis.com/tiles/ScA2Liqz4XcDow5L/arcgis/rest/servi
ces
Bremer
Schneider Geospatial - ArcGIS server address is not public
Buena Vista
https://wfs.schneidercorp.com/arcgis/rest/services/BuenaVistaCoun
tyIA_WFS/MapServer
Butler
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/ButlerIAFeatures/FeatureServer
Go to the top and search for ‘ButlerIA’
Butler
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/ButlerIACadastral/MapServer
Go to the top and search for ‘ButlerIA’
Cass
https://wfs.schneidercorp.com/arcgis/rest/services/CassCountyIA_
WFS/MapServer
Cedar
Schneider Geospatial - ArcGIS server address is not public
Cerro Gordo
https://services7.arcgis.com/qyyoWTywHfayX67L/arcgis/rest/servi
ces
Cerro Gordo
https://wfs.schneidercorp.com/arcgis/rest/services/CerroGordoCou
ntyIA_WFS/MapServer
Cherokee
Schneider Geospatial - ArcGIS server address is not public
Chickasaw
https://wfs.schneidercorp.com/arcgis/rest/services/ChickasawCoun
tyIA_WFS/MapServer
Clay
Schneider Geospatial - ArcGIS server address is not public
Clayton
Schneider Geospatial - ArcGIS server address is not public
Clinton
Assessor has WMS server
Crawford
https://services3.arcgis.com/uwUOPltmS5vV1WmH/ArcGIS/rest/s
ervices
Crawford
https://tiles.arcgis.com/tiles/uwUOPltmS5vV1WmH/arcgis/rest/ser
vices/CrawfordIACadastral/MapServer
Dallas
https://gis.dallascountyiowa.gov/arcgis/rest/services
Dallas
          https://services1.arcgis.com/wrUBAnz4bstesdy3/arcgis/rest/services
Dallas
           https://tiles.arcgis.com/tiles/wrUBAnz4bstesdy3/arcgis/rest/services

## Page 175

Davis
Schneider Geospatial - ArcGIS server address is not public
Decatur
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/DecaturIAFeatures/FeatureServer
Go to the top and search for ‘DecaturIA’
Decatur
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/DecaturIACadastral/MapServer
Delaware
https://wfs.schneidercorp.com/arcgis/rest/services/DelawareCounty
IA_WFS/MapServer
Des Moines
https://www.dmcwebgis.com/arcgis/rest/services
Des Moines
https://services.arcgis.com/HT7H9QGiZQoRJDpJ/arcgis/rest/servi
ces
Dickinson
Schneider Geospatial - ArcGIS server address is not public
Dubuque
https://gis.dubuquecounty.us/server/rest/services
Dubuque
https://services.arcgis.com/527lum9o4TRWxIoH/ArcGIS/rest/servi
ces
Dubuque
https://tiles.arcgis.com/tiles/527lum9o4TRWxIoH/arcgis/rest/servi
ces
Dubuque
https://services5.arcgis.com/lCfrR7MoHN9FsfMi/arcgis/rest/servic
es
Emmet
Schneider Geospatial - ArcGIS server address is not public
Fayette
Schneider Geospatial - ArcGIS server address is not public
Franklin
https://services7.arcgis.com/vkK9gWXr5NOvX1LA/ArcGIS/rest/s
ervices
Fremont
Schneider Geospatial - ArcGIS server address is not public
Greene
Schneider Geospatial - ArcGIS server address is not public
Grundy
Schneider Geospatial - ArcGIS server address is not public
Guthrie
Schneider Geospatial - ArcGIS server address is not public
Guthrie
Integritygis - ArcGIS server address is not public
Hamilton
Schneider Geospatial - ArcGIS server address is not public
Hardin
https://wfs.schneidercorp.com/arcgis/rest/services/HardinCountyIA
_AGS/MapServer

## Page 176

Harrison
https://wfs.schneidercorp.com/arcgis/rest/services/HarrisonCountyI
A_WFS/MapServer
Henry
Schneider Geospatial - ArcGIS server address is not public
Humboldt
https://wfs.schneidercorp.com/arcgis/rest/services/HumboldtCount
yIA_WFS/MapServer
Ida
Schneider Geospatial - ArcGIS server address is not public
Iowa
Schneider Geospatial - ArcGIS server address is not public
Jackson
Schneider Geospatial - ArcGIS server address is not public
Jasper
Schneider Geospatial - ArcGIS server address is not public
Jefferson
https://wfs.schneidercorp.com/arcgis/rest/services/JeffersonCounty
IA_WFS/MapServer
Johnson
https://gis.johnsoncountyiowa.gov/arcgis/rest/services
Johnson
https://services1.arcgis.com/kinOpEPqSpu5VOlu/ArcGIS/rest/serv
ices
Johnson
https://tiles.arcgis.com/tiles/kinOpEPqSpu5VOlu/arcgis/rest/servic
es
Jones
Schneider Geospatial - ArcGIS server address is not public
Keokuk
Schneider Geospatial - ArcGIS server address is not public
Kossuth
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/KossuthIAFeatures/FeatureServer
Go to the top and search for ‘KossuthIA’
Kossuth
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/KossuthIACadastral/MapServer
Go to the top and search for ‘KossuthIA’
Lee
Schneider Geospatial - ArcGIS server address is not public
Linn
https://gis.linncountyiowa.gov/ags/rest/services
Linn
https://gis.linncountyiowa.gov/bgs/rest/services
Linn
https://services.arcgis.com/i14SLLmXo7Hn9vNc/arcgis/rest/servic
es
Linn
https://tiles.arcgis.com/tiles/i14SLLmXo7Hn9vNc/arcgis/rest/servi
ces

## Page 177

Louisa
https://wfs.schneidercorp.com/arcgis/rest/services/LouisaCountyIA
_WFS/MapServer
Lyon
https://wfs.schneidercorp.com/arcgis/rest/services/LyonCountyIA_
EngineerWFS/MapServer
Lyon
https://wfs.schneidercorp.com/arcgis/rest/services/LyonCountyIA_
WFS/MapServer
Madison
Schneider Geospatial - ArcGIS server address is not public
Mahaska
Schneider Geospatial - ArcGIS server address is not public
Marion
Schneider Geospatial - ArcGIS server address is not public
Marshall
Schneider Geospatial - ArcGIS server address is not public
Mason
Schneider Geospatial - ArcGIS server address is not public
Mills
Schneider Geospatial - ArcGIS server address is not public
Mitchell
https://wfs.schneidercorp.com/arcgis/rest/services/MitchellCountyI
A_WFS/MapServer
Mitchell
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MitchellIAFeatures/FeatureServer
Go to the top and search for ‘MitchellIA’
Mitchell
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MitchellIACadastral/MapServer
Go to the top and search for ‘MitchellIA’
Monona
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MononaIAFeatures/FeatureServer
Go to the top and search for ‘MononaIA_’
Monona
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MononaIACadastral/MapServer
Go to the top and search for ‘MononaIA_’
Montgomery
Schneider Geospatial - ArcGIS server address is not public
Muscatine
https://magic-gis.com/arcgis/rest/services
O’Brien
Schneider Geospatial - ArcGIS server address is not public
Osceola
https://wfs.schneidercorp.com/arcgis/rest/services/OsceolaCountyI
A_WFS/MapServer
Page
Schneider Geospatial - ArcGIS server address is not public

## Page 178

Palo Alto
Schneider Geospatial - ArcGIS server address is not public
Plymouth
Schneider Geospatial - ArcGIS server address is not public
Pocahontas
Schneider Geospatial - ArcGIS server address is not public
Polk
https://gis4.polkcountyiowa.gov/server/rest/services
Pottawattamie
https://gis.pottcounty-ia.gov/arcgis/rest/services
Pottawattamie
https://services3.arcgis.com/uQ5BTVJ0Rm1FsbQ5/arcgis/rest/serv
ices
Pottawattamie
https://tiles.arcgis.com/tiles/uQ5BTVJ0Rm1FsbQ5/arcgis/rest/serv
ices
Poweshiek
Schneider Geospatial - ArcGIS server address is not public
Ringgold
Schneider Geospatial - ArcGIS server address is not public
Sac
Schneider Geospatial - ArcGIS server address is not public
Scott
Schneider Geospatial - ArcGIS server address is not public
Scott
https://services.arcgis.com/ovln19YRWV44nBqV/arcgis/rest/servi
ces
Scott
https://tiles.arcgis.com/tiles/ovln19YRWV44nBqV/arcgis/rest/serv
ices
Shelby
Schneider Geospatial - ArcGIS server address is not public
Sioux
Schneider Geospatial - ArcGIS server address is not public
Tama
They use camavision.  Not ArcGIS, not WMS.
Union
Schneider Geospatial - ArcGIS server address is not public
Wapello
https://wfs.schneidercorp.com/arcgis/rest/services/WapelloCountyI
A_WFS/MapServer
Warren
Schneider Geospatial - ArcGIS server address is not public
Washington
Schneider Geospatial - ArcGIS server address is not public
Webster
Schneider Geospatial - ArcGIS server address is not public
Winnebago
_ttps://wfs.schneidercorp.com/arcgis/rest/services/WinnebagoCoun
tyIA_WFS/MapServer
dead link 1

## Page 179

Winneshiek
Schneider Geospatial - ArcGIS server address is not public
Woodbury
Schneider Geospatial - ArcGIS server address is not public
Worth
https://wfs.schneidercorp.com/arcgis/rest/services/WorthCountyIA
_WFS/MapServer
Wright
Schneider Geospatial - ArcGIS server address is not public
Iowa City, Town, Village, etc GIS Servers
Adair
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Adair_I
A_MGMT/MapServer
Table of contents disabled
Adel
Integritygis - ArcGIS server address is not public
Amana Colonies
Integritygis - ArcGIS server address is not public
Ames
https://gis.cityofames.org/arcgis/rest/services
Table of contents disabled
Ames
https://services.arcgis.com/GM5KudYVoaALNBe2/arcgis/rest/ser
vices
Ames
https://tiles.arcgis.com/tiles/GM5KudYVoaALNBe2/arcgis/rest/ser
vices
Ankeny
https://maps.ankenyiowa.gov/arcgis/rest/services
Asbury
https://services3.arcgis.com/PrTZmkroPpgHkCEC/ArcGIS/rest/ser
vices
Avoca
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Avoca_I
A_MGMT/MapServer
Table of contents disabled
Belmond
Integritygis - ArcGIS server address is not public
Bondurant
Integritygis - ArcGIS server address is not public
Carter Lake
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Carter_
Lake_IA_MGMT/MapServer
Table of contents disabled
Carter Lake
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Carter_
Lake_IA_MGMT_Feature/FeatureServer
Table of contents disabled
Cascade
Schneider Geospatial - ArcGIS server address is not public
Cedar Falls
https://gis.cedarfalls.com/arcgis/rest/services

## Page 180

Cedar Rapids
https://crgis.cedar-rapids.org/arcgis/rest/services
Cedar Rapids
https://crgis.cedar-rapids.org/arcgis/rest/services/Parcels/FeatureSe
rver
Charles City
Integritygis - ArcGIS server address is not public
Clear Lake
Integritygis - ArcGIS server address is not public
Colfax
Integritygis - ArcGIS server address is not public
Coralville
See Johnson county
Council Bluffs
https://gispublic.councilbluffs-ia.gov/publicserver/rest/services
Crescent
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Crescent
_IA_MGMT/MapServer
Table of contents disabled
Cresco
Integritygis - ArcGIS server address is not public
Davenport
https://gis.ci.davenport.ia.us/arcgis/rest/services
SSL problem
See Scott county

Des Moines
https://maps.dsm.city/p2/rest/services
DeSoto
Integritygis - ArcGIS server address is not public
Durant
           https://services9.arcgis.com/uyzjiPlMBrqja6St/ArcGIS/rest/services
Earling
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Earling_
IA_MGMT/MapServer
Table of contents disabled
Estherville
Schneider Geospatial - ArcGIS server address is not public
Fairfax
Integritygis - ArcGIS server address is not public
Fort Dodge
Schneider Geospatial - ArcGIS server address is not public
Gilbertville
Integritygis - ArcGIS server address is not public
Greene
Schneider Geospatial - ArcGIS server address is not public
Greenfield
https://gis3.gisworkshop.com/arcgis/rest/services/Greenfield_Muni
cipal_Utilities_IA_MGMT/MapServer  Table of contents disabled

## Page 181

Grimes
https://services8.arcgis.com/pEwQPXNIzqMmHnxT/ArcGIS/rest/s
ervices
Grimes
https://tiles.arcgis.com/tiles/pEwQPXNIzqMmHnxT/arcgis/rest/ser
vices
Hamilton
_________
Hospers
Integritygis - ArcGIS server address is not public
Hudson
Integritygis - ArcGIS server address is not public
Independence
https://services7.arcgis.com/fzDLiP8WlHKP2SAn/arcgis/rest/servi
ces
Iowa City
See Johnson county
Kanawha
Integritygis - ArcGIS server address is not public
Lenox
Integritygis - ArcGIS server address is not public
Long Grove
Integritygis - ArcGIS server address is not public
Marion
https://gis2.gisworkshop.com/arcgis/rest/services/Marion_County_
IA_Rural_Water_District_MGMT/MapServer
Table of contents disabled

Mason City
https://services1.arcgis.com/84FpxbPitJq31AWu/ArcGIS/rest/servi
ces

Mason City
          https://tiles.arcgis.com/tiles/84FpxbPitJq31AWu/arcgis/rest/services
Mediapolis
Integritygis - ArcGIS server address is not public
Mitchell
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MitchellIAFeatures/FeatureServer
Go to the top and search for ‘MitchellIA’
Mitchell
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MitchellIACadastral/MapServer
Go to the top and search for ‘MitchellIA’
Monona
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MononaIAFeatures/FeatureServer
Go to the top and search for ‘MononaIA’
Monona
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MononaIACadastral/MapServer
Go to the top and search for ‘MononaIA’

## Page 182

Monticello
Integritygis - ArcGIS server address is not public
Mount Ayr
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Mount_
Ayr_IA_MGMT/MapServer
Table of contents disabled
Mt Pleasant
Integritygis - ArcGIS server address is not public
Mt Vernon
Integritygis - ArcGIS server address is not public
North Liberty
Integritygis - ArcGIS server address is not public
Neola
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Neola_I
A_MGMT/MapServer
Table of contents disabled
New Hampton
Schneider Geospatial - ArcGIS server address is not public
Newton
Schneider Geospatial - ArcGIS server address is not public
Ogden
Integritygis - ArcGIS server address is not public
Onawa
Integritygis - ArcGIS server address is not public
Onslow
https://arcgis4.roktech.net/arcgis/rest/services/Onslow
Orange City
Integritygis - ArcGIS server address is not public
Osceola
Integritygis - ArcGIS server address is not public
Ottumwa
Integritygis - ArcGIS server address is not public
Palo
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Palo_IA
_MGMT/MapServer
Table of contents disabled

Perry
Integritygis - ArcGIS server address is not public
Reinbeck
Integritygis - ArcGIS server address is not public
Roland
Integritygis - ArcGIS server address is not public
St Charles
Integritygis - ArcGIS server address is not public
Shelby
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Shelby_I
A_MGMT/MapServer
Table of contents disabled
Sidney
See Fremont county

## Page 183

Sigourney
Schneider Geospatial - ArcGIS server address is not public
Sioux
Schneider Geospatial - ArcGIS server address is not public
Sioux Center
Integritygis - ArcGIS server address is not public
Solon
Integritygis - ArcGIS server address is not public
Springville
https://services3.arcgis.com/RoeZcYlBd4xNfnBX/ArcGIS/rest/ser
vices
Story City
Integritygis - ArcGIS server address is not public
Tiffin
Integritygis - ArcGIS server address is not public
Ute
Integritygis - ArcGIS server address is not public
Villisca
Integritygis - ArcGIS server address is not public
Walnut
See Pottawattamie county
Washington
Schneider Geospatial - ArcGIS server address is not public
Waverly
Integritygis - ArcGIS server address is not public
Webster City
Integritygis - ArcGIS server address is not public
West Des Moines
https://maps.wdm.iowa.gov/server/rest/services
Table of contents disabled
Kansas State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Kansas GIS - Data Access and Support Center (DASC)
Website: https://kansasgis.org/
GIS: https://services.kansasgis.org/arcgis/rest/services
8-3-2023 No tiled data
Kansas Division of Emergency Management
Website: https://www.kansastag.gov/101/KDEM
GIS: https://services9.arcgis.com/TBjVrb472JlHWFf7/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/TBjVrb472JlHWFf7/arcgis/rest/services
Kansas Department of Agriculture
Website: https://agriculture.ks.gov

## Page 184

GIS: https://gis2.kda.ks.gov/arcgis/rest/services
8-3-2023 No tiled data
Kansas Department of Health and Environment
Website: https://www.kdhe.ks.gov
GIS: https://maps.kdhe.ks.gov/kdhe_doe/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services9.arcgis.com/Q6wTdPdCh608iNrJ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Q6wTdPdCh608iNrJ/arcgis/rest/services
Kansas Department of Transportation
Website: https://www.ksdot.org
GIS: https://wfs.ksdot.org/arcgis_web_adaptor/rest/services
8-3-2023 No tiled data
GIS: https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services
Kansas Adjutant General's Department
Website: https://www.kansastag.gov
GIS: _ttps://maps.kansastag.gov/tagmaps/rest/services
dead link 3
Kansas Groundwater Management Districts
Website:  https://www.kgs.ku.edu/Hydro/gmd.html
GIS: https://gis3.gisworkshop.com/arcgis/rest/services/GMD_StateWide/MapServer
8-3-2023 No tiled data
Table of contents disabled
University of Kansas - Applied Remote Sensing (KARS)
Website:  https://kars.geoplatform.ku.edu
GIS: https://services.kars.geoplatform.ku.edu/arcgis/rest/services
8-3-2023 No tiled data
Kansas various layers
https://services.kansasgis.org/arcgis3/rest/services
8-3-2023 No tiled data
https://services.kansasgis.org/arcgis4/rest/services
8-3-2023 No tiled data
https://services.kansasgis.org/arcgis5/rest/services
8-3-2023 No tiled data
https://services.kansasgis.org/arcgis6/rest/services
8-3-2023 No tiled data
https://services.kansasgis.org/arcgis7/rest/services
8-3-2023 No tiled data
https://services.kansasgis.org/arcgis8/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
https://services.kansasgis.org/arcgis9/rest/services
8-3-2023 No tiled data
https://services.kansasgis.org/arcgis10/rest/services

## Page 185

8-3-2023 No tiled data
https://services1.arcgis.com/q2CglofYX6ACNEeu/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/q2CglofYX6ACNEeu/arcgis/rest/services
Kansas Regional
Mid-America Regional Council
Website: https://www.marc.org
GIS: https://gis2.marc2.org/arcgis/rest/services
Kansas County GIS Servers
Anderson
__________
Barber
__________
Bourbon
__________
Brown
__________
Butler
https://ww1.bucoks.com/bucogis1/rest/services
Butler
https://services5.arcgis.com/SU4Aj97XUNDcwkDb/ArcGIS/rest/s
ervices
Cheyenne
__________
Clay
__________
Coffey
__________
Cowley
Schneider Geospatial - ArcGIS server address is not public
Decatur
__________
Dickinson
https://services6.arcgis.com/XBUaJ9z59sKeDhyY/ArcGIS/rest/ser
vices
Douglas
https://gis.dgcoks.gov/server/rest/services
Douglas
https://services5.arcgis.com/oaDPYH6vLrOqci8X/arcgis/rest/servi
ces
Rural Water District 4
Edwards
__________
Finney
https://www.finneycountygis.com/arcgis/rest/services
Finney
https://services2.arcgis.com/PRSAN33Jrc6Rh3tB/arcgis/rest/servic
es

## Page 186

Graham
__________
Greenwood
__________
Jackson
__________
Johnson
https://maps.jocogov.org/arcgis/rest/services
Johnson
https://services.arcgis.com/VI7SIDfzMs53TTMm/arcgis/rest/servic
es
Johnson
https://tiles.arcgis.com/tiles/VI7SIDfzMs53TTMm/arcgis/rest/servi
ces
Kearny
__________
Leavenworth
Integritygis - ArcGIS server address is not public
Linn
https://gis.linncountyks.com/server/rest/services
Linn
https://services3.arcgis.com/TKhOZbXZBgxGSTZN/arcgis/rest/se
rvices
Logan
__________
Lyon
Schneider Geospatial - ArcGIS server address is not public
Marion
__________
Miami
Schneider Geospatial - ArcGIS server address is not public
Neosho
__________
Osage
__________
Pottawatomie
https://services6.arcgis.com/Zt2LWLYlpbYKRPfg/arcgis/rest/servi
ces
Rawlins
__________
Reno
Schneider Geospatial - ArcGIS server address is not public
Republic
__________
Riley
https://gis.rileycountyks.gov/arcgis/rest/services
Shawnee
https://gis.sncoapps.us/arcgis2/rest/services
Shawnee
https://services2.arcgis.com/2XE514jeVQMWNKHX/ArcGIS/rest/
services

## Page 187

Shawnee
https://tiles.arcgis.com/tiles/2XE514jeVQMWNKHX/arcgis/rest/se
rvices
Thomas
__________
Wilson
Schneider Geospatial - ArcGIS server address is not public
Wyandotte
https://gisweb.wycokck.org/arcgis/rest/services
Wyandotte
https://gisweb.wycokck.org/server/rest/services
Wyandotte
https://services1.arcgis.com/Qo2HHQp8vgPs2wg3/ArcGIS/rest/ser
vices
Wyandotte
https://tiles.arcgis.com/tiles/Qo2HHQp8vgPs2wg3/arcgis/rest/servi
ces
Kansas City, Town, Village, etc GIS Servers
Abilene
Integritygis - ArcGIS server address is not public
Allen
__________
Andale
Integritygis - ArcGIS server address is not public
Augusta
Integritygis - ArcGIS server address is not public
Basehor
Integritygis - ArcGIS server address is not public
Beloit
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Beloit_
KS_MGMT/MapServer
Table of contents disabled
Chase
__________
Colby
Integritygis - ArcGIS server address is not public
Concordia
Integritygis - ArcGIS server address is not public
El Dorado
Integritygis - ArcGIS server address is not public
Ellsworth
__________
Eudora
Integritygis - ArcGIS server address is not public
Ford
__________
Fort Scott
Integritygis - ArcGIS server address is not public
Franklin
__________

## Page 188

Garnett
Integritygis - ArcGIS server address is not public
Girard
Integritygis - ArcGIS server address is not public
Gove
__________
Greleey
__________
Hays
__________
Hiawatha
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Hiawath
a_KS_MGMT/MapServer
Table of contents disabled
Hugoton
Integritygis - ArcGIS server address is not public
Kansas City
See Wyandotte County
Kingman
__________
Kiowa
__________
Labette
__________
Lansing
https://services9.arcgis.com/1bWTvtvBCBaErVYC/ArcGIS/rest/se
rvices
Lansing
https://tiles.arcgis.com/tiles/1bWTvtvBCBaErVYC/arcgis/rest/serv
ices
Lawrence
https://services.arcgis.com/8O9UlSTnqjKptoda/arcgis/rest/services
Lawrence
           https://tiles.arcgis.com/tiles/8O9UlSTnqjKptoda/arcgis/rest/services
Lenexa
https://gis.lenexa.com/arcgis/rest/services
Lenexa
          https://services.arcgis.com/rQNf5tVFXFoS6EhP/arcgis/rest/services
Lincoln Center
Integritygis - ArcGIS server address is not public
Marysville
Integritygis - ArcGIS server address is not public
McPherson
Integritygis - ArcGIS server address is not public
Meade
__________
Medicine Lodge
Integritygis - ArcGIS server address is not public
Olathe
https://arcgis.olatheks.org/arcgis/rest/services

## Page 189

Olathe
_ttps://services1.arcgis.com/V5kJ9QPOiI1K62Ac/arcgis/rest/servic
es
dead link 1
Osage City
Integritygis - ArcGIS server address is not public
Osawatomie
Schneider Geospatial - ArcGIS server address is not public
Osborne
__________
Ottawa
Integritygis - ArcGIS server address is not public
Overland Park
https://maps.opkansas.org/mapping/rest/services
Paola
Integritygis - ArcGIS server address is not public
Pratt
__________
Rose Hill
Integritygis - ArcGIS server address is not public
St John
Integritygis - ArcGIS server address is not public
Shawnee
https://services1.arcgis.com/1x5fJy2NAFJGIL2b/arcgis/rest/servic
es
Shawnee
          https://tiles.arcgis.com/tiles/1x5fJy2NAFJGIL2b/arcgis/rest/services
Stafford
__________

Topeka
https://services1.arcgis.com/EvtgI3PZ9PyCGJZS/ArcGIS/rest/servi
ces
Topeka
https://tiles.arcgis.com/tiles/EvtgI3PZ9PyCGJZS/arcgis/rest/servic
es
Wabaunsee
__________
Wamego
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Wameg
o_KS_MGMT/MapServer
Table of contents disabled
Wichita
https://gismaps.wichita.gov/ageweb/rest/services
Wichita
https://services5.arcgis.com/lOHEurd1BgncOSk1/ArcGIS/rest/serv
ices
Kentucky State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Kentucky Open GIS Data

## Page 190

Website: https://opengisdata.ky.gov
Kentucky Emergency Management
Website: https://www.kyem.ky.gov
GIS: https://services2.arcgis.com/jNL8GAN3Ejyqxy3x/ArcGIS/rest/services
Kentucky Energy and Environment Cabinet (EEC)
Website: https://eec.ky.gov/Pages/index.aspx
GIS: https://services.arcgis.com/TosFUe3nXUAksqSj/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/TosFUe3nXUAksqSj/arcgis/rest/services
Kentucky Office of Broadband Development
Website: https://broadband.ky.gov/Pages/index.aspx
GIS: https://services3.arcgis.com/tXnUNh1UBIKfO37H/arcgis/rest/services
Kentucky Transportation Cabinet (KYTC)
Website: https://transportation.ky.gov
GIS: https://maps.kytc.ky.gov/arcgis/rest/services

8-3-2023 No tiled data
GIS: https://services2.arcgis.com/CcI36Pduqd0OR4W9/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/CcI36Pduqd0OR4W9/arcgis/rest/services
University of Kentucky - Kentucky Geological Survey (KGS)
Website: https://www.uky.edu/KGS
GIS: https://kgs.uky.edu/arcgis/rest/services
Kentucky various layers
GIS: https://kygisserver.ky.gov/arcgis/rest/services

8-3-2023 No tiled data
GIS: https://kygisserver.ky.gov/ArcGIS/rest/services

8-3-2023 No tiled data
GIS: https://kyraster.ky.gov/arcgis/rest/services

8-3-2023 No tiled data
GIS: https://eppcgis.ky.gov/arcgis/rest/services
8-3-2023 No tiled data
GIS: https://watermaps.ky.gov/arcgis/rest/services
8-3-2023 No tiled data
GIS: https://services3.arcgis.com/ghsX9CKghMvyYjBU/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/ghsX9CKghMvyYjBU/arcgis/rest/services
Kentucky Regional
Barren River Area Development District
Website: https://www.bradd.org
GIS: https://services6.arcgis.com/LledJs8ADlUCS7Cz/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/LledJs8ADlUCS7Cz/arcgis/rest/services

## Page 191

Link GIS (northern Kentucky)
Website: https://linkgis.org
GIS: https://maps.linkgis.org/server/rest/services
8-3-2023 No tiled data
GIS: https://services2.arcgis.com/90vxQoG8CT8O1MXs/ArcGIS/rest/services
Gateway Area Development District
Website: https://gwadd.org
GIS: https://services3.arcgis.com/aaZhjjkUqOHS7oRg/arcgis/rest/services
Kentucky County GIS Servers
Adair
Schneider Geospatial - ArcGIS server address is not public
Allen
Schneider Geospatial - ArcGIS server address is not public
Anderson
_ttps://maps2.bgadd.org/arcgis/rest/services/Anderson   dead link 1
Ballard
Schneider Geospatial - ArcGIS server address is not public
Barren
Schneider Geospatial - ArcGIS server address is not public
Bath
Schneider Geospatial - ArcGIS server address is not public
Bell
Schneider Geospatial - ArcGIS server address is not public
Boone
https://secure.boonecountygis.com/server/rest/services
Bourbon
Schneider Geospatial - ArcGIS server address is not public
Boyd
Schneider Geospatial - ArcGIS server address is not public
Boyle
_ttps://maps2.bgadd.org/arcgis/rest/services/Boyle     dead link 1
Bracken
Schneider Geospatial - ArcGIS server address is not public
Breathitt
Schneider Geospatial - ArcGIS server address is not public
Breckinridge
Schneider Geospatial - ArcGIS server address is not public
Bullitt
https://services.lojic.org/arcgis/rest/services/Lojic
Butler
Schneider Geospatial - ArcGIS server address is not public
Caldwell
Schneider Geospatial - ArcGIS server address is not public
Calloway
Schneider Geospatial - ArcGIS server address is not public

## Page 192

Campbell
https://maps.linkgis.org/server/rest/services/Campbell_County
Carlisle
Schneider Geospatial - ArcGIS server address is not public
Carroll
Schneider Geospatial - ArcGIS server address is not public
Carter
Schneider Geospatial - ArcGIS server address is not public
Casey
Schneider Geospatial - ArcGIS server address is not public
Christian
Schneider Geospatial - ArcGIS server address is not public
Clark
https://gis.ccgisonline.com:6443/arcgis/rest/services
Clark
https://services.lojic.org/arcgis/rest/services/Lojic
Clay
Schneider Geospatial - ArcGIS server address is not public
Clinton
Schneider Geospatial - ArcGIS server address is not public
Crittenden
Schneider Geospatial - ArcGIS server address is not public
Cumberland
Schneider Geospatial - ArcGIS server address is not public
Daviess
Schneider Geospatial - ArcGIS server address is not public
Edmonson
Schneider Geospatial - ArcGIS server address is not public
Elliott
Schneider Geospatial - ArcGIS server address is not public
Estill
_ttps://maps2.bgadd.org/arcgis/rest/services/Estill    dead link 1
Fayette
Schneider Geospatial - ArcGIS server address is not public
Fayette
https://services1.arcgis.com/Mg7DLdfYcSWIaDnu/arcgis/rest/serv
ices
Lexington Fayette Urban County Government
Fleming
Schneider Geospatial - ArcGIS server address is not public
Floyd
Schneider Geospatial - ArcGIS server address is not public
Franklin
Schneider Geospatial - ArcGIS server address is not public
Fulton
Schneider Geospatial - ArcGIS server address is not public
Gallatin
Schneider Geospatial - ArcGIS server address is not public
Garrard
_ttps://maps2.bgadd.org/arcgis/rest/services/Garrard    dead link 1

## Page 193

Grant
Schneider Geospatial - ArcGIS server address is not public
Graves
Schneider Geospatial - ArcGIS server address is not public
Grayson
Schneider Geospatial - ArcGIS server address is not public
Green
Schneider Geospatial - ArcGIS server address is not public
Greenup
Schneider Geospatial - ArcGIS server address is not public
Hancock
Schneider Geospatial - ArcGIS server address is not public
Hardin
https://services1.arcgis.com/fYwcHOBzInDTQxh0/arcgis/rest/serv
ices
Harlan
Schneider Geospatial - ArcGIS server address is not public
Harrison
_ttps://maps2.bgadd.org/arcgis/rest/services/Harrison    dead link 1
Harrison
https://services.lojic.org/arcgis/rest/services/Lojic
Hart
Schneider Geospatial - ArcGIS server address is not public
Henderson
Schneider Geospatial - ArcGIS server address is not public
Henry
https://services.lojic.org/arcgis/rest/services/Lojic
Hopkins
Schneider Geospatial - ArcGIS server address is not public
Hopkins
https://services5.arcgis.com/TbfgSCnhZia1FQla/ArcGIS/rest/servi
ces
Hopkins
           https://tiles.arcgis.com/tiles/TbfgSCnhZia1FQla/arcgis/rest/services
Jackson
Schneider Geospatial - ArcGIS server address is not public
Jefferson
Louisville/Jefferson County Information Consortium (LOJIC)
https://services.lojic.org/arcgis/rest/services
Jefferson
https://services1.arcgis.com/79kfd2K6fskCAkyg/ArcGIS/rest/servi
ces
Jefferson
          https://tiles.arcgis.com/tiles/79kfd2K6fskCAkyg/arcgis/rest/services
Jessamine
_ttps://maps2.bgadd.org/arcgis/rest/services/Jessamine  dead link 1
Johnson
Schneider Geospatial - ArcGIS server address is not public

Kenton
https://kcgis.kentoncounty.org:6443/arcgis/rest/services
Knott
Schneider Geospatial - ArcGIS server address is not public

## Page 194

Knox
Schneider Geospatial - ArcGIS server address is not public
LaRue
Schneider Geospatial - ArcGIS server address is not public
Laurel
Schneider Geospatial - ArcGIS server address is not public
Lee
Schneider Geospatial - ArcGIS server address is not public
Leslie
Schneider Geospatial - ArcGIS server address is not public
Letcher
Schneider Geospatial - ArcGIS server address is not public
Lewis
Schneider Geospatial - ArcGIS server address is not public
Lincoln
Schneider Geospatial - ArcGIS server address is not public
Livingston
Schneider Geospatial - ArcGIS server address is not public
Logan
Schneider Geospatial - ArcGIS server address is not public
Madison
https://arcserver.madisoncountyky.us/arcgis/rest/services
Madison
https://services2.arcgis.com/vr7o7tw2Aw3SpBdd/ArcGIS/rest/serv
ices
Madison
https://tiles.arcgis.com/tiles/vr7o7tw2Aw3SpBdd/arcgis/rest/servic
es
McCracken
https://services1.arcgis.com/xkOPDyh2DVxtFEGe/arcgis/rest/servi
ces
McCracken
https://tiles.arcgis.com/tiles/xkOPDyh2DVxtFEGe/arcgis/rest/servi
ces
Meade
https://services.lojic.org/arcgis/rest/services
Mercer
_ttps://maps2.bgadd.org/arcgis/rest/services/Mercer    dead link 1
Oldham
https://services.lojic.org/arcgis/rest/services
Oldham
https://services5.arcgis.com/4eBIYcSR3sVL9y0D/arcgis/rest/servi
ces
Oldham
https://services1.arcgis.com/Dxt6DUfHbT0B7f4e/arcgis/rest/servic
es
Pendleton
https://maps.linkgis.org/server/rest/services         Three counties
Powell
_ttps://maps2.bgadd.org/arcgis/rest/services/Powell    dead link 1
Shelby
https://services.lojic.org/arcgis/rest/services

## Page 195

Spencer
https://services.lojic.org/arcgis/rest/services
Trimble
https://services.lojic.org/arcgis/rest/services
Union
https://services1.arcgis.com/k2n3aN0z854TRTGp/arcgis/rest/servi
ces
Warren
https://webgis.bgky.org/server/rest/services/CCPC
CCPC = City County Planning Commission
Woodford
 _ttps://maps2.bgadd.org/arcgis/rest/services/Woodford dead link 1
Kentucky City, Town, Village, etc GIS Servers
Bowling Green
https://webgis.bgky.org/server/rest/services
Bowling Green
https://services5.arcgis.com/o6ioDArHE4is3oSE/ArcGIS/rest/servi
ces
Bowling Green          https://tiles.arcgis.com/tiles/o6ioDArHE4is3oSE/arcgis/rest/services
Calvert
_________
Elizabethtown
https://services.arcgis.com/jQAeHpE1f8SVxxNo/arcgis/rest/servic
es

Frankfort
https://services2.arcgis.com/1Mn98EWnWi3Ezwj3/arcgis/rest/serv
ices
Franklin
https://services8.arcgis.com/D3RgmiBYTvYcNK2j/arcgis/rest/serv
ices
Franklin
https://tiles.arcgis.com/tiles/D3RgmiBYTvYcNK2j/arcgis/rest/serv
ices
Georgetown
https://gis.gscplanning.com/arcgis/rest/services
Hardin
https://services.lojic.org/arcgis/rest/services/Lojic
Jeffersontown
_________
Lexington
https://maps.lexingtonky.gov/lfucggis/rest/services
Table of contents disabled
Lexington
https://services1.arcgis.com/Mg7DLdfYcSWIaDnu/arcgis/rest/serv
ices
Lexington Fayette Urban County Government
Louisville
See Jefferson County
Owensboro
https://gis.owensboro.org/arcgis/rest/services

## Page 196

Paducah
https://gis.paducahky.gov/arcgis/rest/services
Louisiana State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Louisiana Atlas
Website: https://atlas.ga.lsu.edu
Louisiana Department of Culture - Recreation and Tourism
Website: https://www.crt.state.la.us
GIS: https://crt-esri.crt.state.la.us:6443/arcgis/rest/services
8-3-2023 No tiled data
Louisiana Department of Environmental Quality
Website: https://www.deq.louisiana.gov
GIS: https://arcgis.deq.la.gov/ldeq/rest/services
Department of Health
Website: https://ldh.la.gov
GIS: _ttps://gis.dhh.louisiana.gov/arcgis/rest/services
dead link 3
Louisiana Department of Transportation and Development
Website: http://wwwsp.dotd.la.gov/Pages/default.aspx
not https
GIS: https://giswebnew.dotd.la.gov/arcgis/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: http://gisweb.dotd.la.gov/arcgis/rest/services
not https
GIS: https://maps.dotd.la.gov/imagery/rest/services
GIS: https://services.arcgis.com/PLiuXYMBpMK5h36e/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/PLiuXYMBpMK5h36e/arcgis/rest/services
Louisiana Department of Wildlife and Fisheries
Website: https://www.wlf.louisiana.gov
GIS: https://gis.wlf.la.gov/arcgis/rest/services
8-3-2023 No tiled data
Louisiana Coastal Information Management System (CIMS)
Website: https://cims.coastal.la.gov/
GIS: https://cimsgeo.coastal.louisiana.gov/arcgis/rest/services
8-3-2023 No tiled data
GIS: https://cimsgeo3.coastal.louisiana.gov/arcgis/rest/services
8-3-2023 No tiled data
Louisiana Office of State Climatology
Website: https://losc.climate.lsu.edu
GIS: _ttps://ebi.losco.lsu.edu/gis/rest/services
dead link 3

## Page 197

LSU Ag Center
Website: https://www.lsuagcenter.com
GIS: https://services.maps.lsuagcenter.com/arcgis/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Alexandria International Airport
GIS: https://services5.arcgis.com/CYPq8qz3sioNJZoQ/ArcGIS/rest/services
Louisiana Regional
Acadiana Planning Commission
Website: https://www.planacadiana.org
GIS: https://services6.arcgis.com/evfpsq4DPUft8Uyf/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/evfpsq4DPUft8Uyf/arcgis/rest/services
Northwest Council of Governments (NLCOG)
Shreveport-Bossier City Metropolitan Area.  Caddo Parish.
Website: https://www.nlcog.org
GIS: https://services5.arcgis.com/3hVHthldVKlbxWEH/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/3hVHthldVKlbxWEH/arcgis/rest/services
Pearl River Valley area
GIS:
https://gis.cmpdd.org/server/rest/services/Hosted/Pearl_River_Valley_Feature_La
yer/FeatureServer
GIS: https://services5.arcgis.com/6Qp6wyDp6qSjhd56/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/6Qp6wyDp6qSjhd56/arcgis/rest/services
Louisiana Parishes GIS Servers
Ascension
https://gis.ascensionparishla.gov/server/rest/services
Assumption
They have a GIS but it is not ArcGIS
Avoyelles
https://www.efsedge.com/arcgis/rest/services/Avoyelles_Parish
Bearegard
They have a GIS but not ArcGIS
Bossier
WMS server
Caddo
See Northwest Council of Government
Calcasieu
https://lak-dc-arcgis.cppj.net/arcgis/rest/services
Calcasieu
https://services7.arcgis.com/T7YR8Q3OOFw14uBe/ArcGIS/rest/s
ervices
Calcasieu
https://tiles.arcgis.com/tiles/T7YR8Q3OOFw14uBe/arcgis/rest/ser
vices

## Page 198

Catahoula
https://www.efsedge.com/arcgis/rest/services/Catahoula_Parish
Claiborne
WMS server
Concordia
WMS server
DeSoto
WMS server
East Baton Rouge
https://services.arcgis.com/KYvXadMcgf0K1EzK/arcgis/rest/servi
ces
East Baton Rouge
https://tiles.arcgis.com/tiles/KYvXadMcgf0K1EzK/arcgis/rest/serv
ices
Franklin
WMS server
Grant
WMS server
Iberia
https://services1.arcgis.com/ZPPrBdbq4892XaIK/ArcGIS/rest/serv
ices
Iberia
Also a WMS server
Jefferson
https://eweb.jeffparish.net/arcgis/rest/services
Jefferson
https://webmap.jeffparish.net/arcgis/rest/services
Jefferson
https://services2.arcgis.com/bsK00WEpBiA0imM5/ArcGIS/rest/se
rvices
Lafayette
https://maps.lafayettela.gov/arcgis/rest/services
Table of contents disabled
Lafayette
https://services.arcgis.com/fOr4AY8t0ujnJsua/arcgis/rest/services
Lafayette
https://tiles.arcgis.com/tiles/fOr4AY8t0ujnJsua/arcgis/rest/services
Lafayette
Schneider Geospatial - ArcGIS server address is not public
Assessor
LaFourche
https://services1.arcgis.com/hg2WR9ukwQebQrXp/arcgis/rest/serv
ices
LaFourche
https://tiles.arcgis.com/tiles/hg2WR9ukwQebQrXp/arcgis/rest/serv
ices
LaSalle
WMS server
Livingston
https://gis.lpao.org/lpaogis/rest/services
Madison
______________
Pointe Coupee
WMS server

## Page 199

Red River
WMS server
Richland
WMS server
St. Charles
WMS server
St. John
WMS server
St. Martin
WMS server
St. Mary
WMS server
St Tammany
WMS server
St Tammany
https://services2.arcgis.com/GjsLOwYbSm9HRagZ/arcgis/rest/ser
vices
Tangipahoa
https://services9.arcgis.com/GFjf8leC8Mas9DyE/arcgis/rest/servic
es
Terrebonne
https://gis.tpcg.org/server/rest/services
Vernon
https://www.efsedge.com/arcgis/rest/services/Vernon_Parish
Washington
WMS server
Webster
WMS server
West Feliciana
WMS server
Louisiana City, Town, Village, etc GIS Servers
Abita Springs
WMS
Albany
________

Baton Rouge
https://maps.brla.gov/gis/rest/services

Baton Rouge
https://maps.brla.gov/pscop/rest/services
Bienville
GIS data is hidden behind a proxy server
Bossier
https://services1.arcgis.com/jh7pbmmfSzUSNziy/ArcGIS/rest/serv
ices
Catahoula
See Catahoula parish
Claiborne
WMS server

## Page 200

Clinton
https://gis.cmpdd.org/server/rest/services/Hosted/Clinton_Feature_
Layer/FeatureServer
Clinton
https://gis.cmpdd.org/server/rest/services/Hosted/Clinton_Feature_
Layer_2/FeatureServer
Covington
WMS server
Denham Springs
WMS server
Deridder
WMS server
Flora
https://gis.cmpdd.org/server/rest/services/Hosted/Flora_Feature_La
yer/FeatureServer
Gluckstadt
https://gis.cmpdd.org/server/rest/services/Hosted/Gluckstadt_Featu
re_Layer/FeatureServer
Gonzales
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/Gonzal
esLA_Basemap/MapServer
Gonzales
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/Gonzal
esLA_Operational/MapServer
See also Ascension Parish
Gretna
WMS server
Jackson
https://gis.cmpdd.org/server/rest/services/Hosted/City_of_Jackson_
Feature_Layer/FeatureServer
Kenner
WMS server.  See also Jefferson Parish
Kosciusko
https://gis.cmpdd.org/server/rest/services/Hosted/Kosciusko_Featu
re_Layer/FeatureServer
Lafayette
See Lafayette Parish
Madisonville
WMS server
Magee
https://gis.cmpdd.org/server/rest/services/Hosted/Magee_Feature_
Layer/FeatureServer
Mandeville
https://services6.arcgis.com/h1LBEEg2MI7tkz4N/arcgis/rest/servi
ces
Mandeville
https://tiles.arcgis.com/tiles/h1LBEEg2MI7tkz4N/arcgis/rest/servic
es

## Page 201

Mendenhall
https://gis.cmpdd.org/server/rest/services/Hosted/Mendenhall_Feat
ure_Layer/FeatureServer
Minden
WMS server
Natchitoches
WMS server
New Iberia
WMS server
New Orleans
https://gis.nola.gov/arcgis/rest/services
New Orleans
https://maps.nola.gov/server/rest/services
New Orleans
https://gis.nola.gov:6443/arcgis/rest/services
New Orleans
https://cop.nola.gov:6443/arcgis/rest/services
New Orleans
http://gis.nola.gov:6080/arcgis/rest/services
not https
New Orleans            https://services.arcgis.com/VhMjCzR3cIjEkh7L/arcgis/rest/services
New Orleans
https://tiles.arcgis.com/tiles/VhMjCzR3cIjEkh7L/arcgis/rest/servic
es
Pearl
https://gis.cmpdd.org/server/rest/services/Hosted/CityofPearl_Map
_Feature_Service/FeatureServer
Pearl
https://gis.cmpdd.org/server/rest/services/Hosted/Pearl_Structures_
Search_Feature_Service/FeatureServer
Pearl
https://gis.cmpdd.org/server/rest/services/Hosted/Pearl_Viewer_Fe
ature_Service/FeatureServer
Pelahatchie
https://gis.cmpdd.org/server/rest/services/Hosted/Pelahatchie_Feat
ure_Layer/FeatureServer
Pelahatchie
https://gis.cmpdd.org/server/rest/services/Hosted/Pelahatchie_Tran
sportation/FeatureServer
Puckett
https://gis.cmpdd.org/server/rest/services/Hosted/Puckett_Feature_
Layer/FeatureServer
Richland
https://gis.cmpdd.org/server/rest/services/Hosted/Richland_Feature
_Layer/FeatureServer
Slidell
WMS server
Terry
https://gis.cmpdd.org/server/rest/services/Hosted/Terry_Feature_La
yer/FeatureServer
Yazoo
https://gis.cmpdd.org/server/rest/services/Hosted/Yazoo_City_Feat
ure_Layer/FeatureServer
Yazoo
https://gis.cmpdd.org/server/rest/services/Hosted/Yazoo_City_Tran
sportation_Plan/FeatureServer

## Page 202

Maine State GIS Servers
Maine Open Data Portal
Website: https://www.maine.gov/megis/catalog
Maine various layers
GIS: https://arcgisserver.maine.gov/arcgis/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.maine.gov/arcgis/rest/services
Parcel lines:  mrs/Maine_Parcels_Unorganized_Territory/MapServer/0
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/RbMX0mRVOFNTdLzd/arcgis/rest/services
Parcel lines:  Maine_Parcels_Organized_Towns/FeatureServer/0
GIS: https://tiles.arcgis.com/tiles/RbMX0mRVOFNTdLzd/arcgis/rest/services
Maine Regional
Androscoggin Valley Council of Governments
Website: https://www.avcog.org
GIS: https://services.arcgis.com/kDP7jYU14mbNILNN/arcgis/rest/services
Greater Portland Council of Governments
Website: https://www.gpcog.org
GIS: https://services3.arcgis.com/0UEH6aSHSRlnunGR/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/0UEH6aSHSRlnunGR/arcgis/rest/services
Kennebec Valley Council of Governments
Website: https://www.kvcog.org
GIS: _________
Lincoln County Regional Planning Commission
Website: https://www.lcrpc.org
GIS: _________
Northern Maine Development Commission
Website: https://www.nmdc.org
GIS: _________
Southern Maine Planning and Development Commission
Website: https://smpdc.org
GIS: https://services.arcgis.com/EDmXP1QjmSmZlvBw/arcgis/rest/services
Maine County GIS Servers
Knox
https://services8.arcgis.com/EvllkkFm8v8CygAm/ArcGIS/rest/ser
vices

## Page 203

Maine City, Town, Village, etc GIS Servers
Auburn
https://maps2.auburnmaine.gov/arcgis/rest/services
Auburn
          https://services1.arcgis.com/4nU7cbKqLfftauX2/arcgis/rest/services
Auburn
          https://tiles.arcgis.com/tiles/4nU7cbKqLfftauX2/arcgis/rest/services
Baldwin
https://arcgis.vgsi.com/server/rest/services/Baldwin_ME
Bangor
https://mapping.bangormaine.gov/server/rest/services
Bangor
https://services1.arcgis.com/yIxdYDwtUG29jfAN/ArcGIS/rest/ser
vices
Bangor
https://tiles.arcgis.com/tiles/yIxdYDwtUG29jfAN/arcgis/rest/servi
ces
Biddeford
https://arcgis.vgsi.com/server/rest/services/Biddeford_ME
Biddeford
https://services5.arcgis.com/QWn8PC1cSwbsBBh6/arcgis/rest/ser
vices
Biddeford
https://tiles.arcgis.com/tiles/QWn8PC1cSwbsBBh6/arcgis/rest/serv
ices
Burlington
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/BurlingtonMEFeatures/FeatureServer
Go to the top and search for ‘BurlingtonME’
Burlington
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/BurlingtonMEAnnotations/MapServer
Go to the top and search for ‘BurlingtonME’
Casco
https://gisserver1.axisgis.com/arcgis/rest/services/CascoME
Not open to public
Falmouth
https://arcgis.vgsi.com/server/rest/services/Falmouth_ME
Falmouth
https://services6.arcgis.com/b0Lrou1DkvqyYSvR/ArcGIS/rest/serv
ices
Falmouth
https://tiles.arcgis.com/tiles/b0Lrou1DkvqyYSvR/arcgis/rest/servic
es
Gardiner
https://gisserver2.axisgis.com/arcgis/rest/services/GardinerME

Not open to public
Gorham
https://arcgis.vgsi.com/server/rest/services/Gorham_ME
Harpswell
https://arcgis.vgsi.com/server/rest/services/Harpswell_ME
Harpswell
https://services2.arcgis.com/hFtURr7dqquonDPF/ArcGIS/rest/serv
ices
Harpswell
https://tiles.arcgis.com/tiles/hFtURr7dqquonDPF/arcgis/rest/servic
es

## Page 204

Kennebunk
https://arcgis.vgsi.com/server/rest/services/Kennebunk_ME
Kittery
https://gisserver2.axisgis.com/arcgis/rest/services/KitteryME

Not open to public
Lewiston
https://maps2.lewistonmaine.gov/arcgis/rest/services
Old Orchard Beach
https://services5.arcgis.com/RZTrYQP8JmfsPLQG/ArcGIS/rest/se
rvices
Old Orchard Beach
https://tiles.arcgis.com/tiles/RZTrYQP8JmfsPLQG/arcgis/rest/serv
ices

Portland
https://gis.portlandmaine.gov/maps/rest/services
Saco
https://arcgis.vgsi.com/server/rest/services/Saco_ME
Sanford
https://services6.arcgis.com/r42ivGMv7dqAE150/ArcGIS/rest/serv
ices
Sanford
https://tiles.arcgis.com/tiles/r42ivGMv7dqAE150/arcgis/rest/servic
es
South Portland
https://services5.arcgis.com/OpN4013XQ19WlWn4/ArcGIS/rest/s
ervices
South Portland
https://tiles.arcgis.com/tiles/OpN4013XQ19WlWn4/arcgis/rest/ser
vices
Standish
https://arcgis.vgsi.com/server/rest/services/Standish_ME
Waterville
https://gisserver1.axisgis.com/arcgis/rest/services/WatervilleME

Not open to public
Westbrook
https://services5.arcgis.com/Cxl8RQ4PEBjdRbtW/ArcGIS/rest/ser
vices
Westbrook
https://tiles.arcgis.com/tiles/Cxl8RQ4PEBjdRbtW/arcgis/rest/servi
ces
Windham
https://arcgis.vgsi.com/server/rest/services/Windham_ME
Winslow
https://arcgis.vgsi.com/server/rest/services/Winslow_ME
York
https://services1.arcgis.com/3WqUflJyxCOQjBCT/ArcGIS/rest/ser
vices
York
https://tiles.arcgis.com/tiles/3WqUflJyxCOQjBCT/arcgis/rest/servi
ces

## Page 205

Maryland State GIS Servers
Maryland Mapping and GIS Data Portal
Website: https://imap.maryland.gov
GIS: https://mdgeodata.md.gov/imap/rest/services
GIS: https://mdgeodata.md.gov/lidar/rest/services
GIS: https://mdgeodata.md.gov/imagery/rest/services
GIS: https://geodata.md.gov/appdata/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://spatialags.vhb.com/arcgis/rest/services/55526     Basemaps
8-3-2023 No tiled data
GIS: https://mdewin64.mde.state.md.us/arcgis/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS:
Maryland - Department of Planning
Website: https://planning.maryland.gov/Pages/default.aspx
GIS: https://mdpgis.mdp.state.md.us/arcgis/rest/services
8-3-2023 Tiled data.  Several.  Go to top of this PDF file and search for ‘wmts'.
Maryland Department of Natural Resources
Website: https://dnr.maryland.gov/Pages/default.aspx
GIS: https://dnr.geodata.md.gov/dnrdata/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Maryland Department of Transportation
Website: https://www.mdot.maryland.gov
GIS: https://maps.roads.maryland.gov/ArcGIS/rest/services
8-3-2023 No tiled data
GIS: https://maps.roads.maryland.gov/arcgis/rest/services
8-3-2023 No tiled data
GIS: https://chartimap1.sha.maryland.gov/arcgis/rest/services
Includes traffic cameras
8-3-2023 No tiled data
Maryland Department of the Environment
Website: https://mde.maryland.gov/Pages/index.aspx
GIS: https://mdewin64.mde.state.md.us/arcgis/rest/services
8-3-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Maryland Department of Health
Website: https://health.maryland.gov/Pages/Home.aspx
GIS: https://maps.health.maryland.gov/gis/rest/services
Table of contents disabled
Maryland various layers
GIS: https://services.arcgis.com/njFNhDsUCentVYJW/ArcGIS/rest/services

## Page 206

dead link 1
GIS: https://tiles.arcgis.com/tiles/njFNhDsUCentVYJW/arcgis/rest/services
Maryland Regional
Baltimore Metropolitan Council (BMC)
Website: https://sites.google.com/baltometro.org/home
GIS: https://gis.baltometro.org/arcgis/rest/services
8-3-2023 No tiled data

GIS: https://services5.arcgis.com/viVzbt0JWVlYD2i9/ArcGIS/rest/services

GIS: https://tiles.arcgis.com/tiles/viVzbt0JWVlYD2i9/arcgis/rest/services
Maryland County GIS Servers
All counties are listed and have been checked for GIS
Allegany
https://alleganygis.allconet.org/allcogis/rest/services
Anne Arundel
https://gis.aacounty.org/image/rest/services
Anne Arundel
https://gis.aacounty.org/arcgis/rest/services
Anne Arundel
https://services2.arcgis.com/nUoGCkM6W8Wqdvvh/ArcGIS/rest/
services
Anne Arundel
https://tiles.arcgis.com/tiles/nUoGCkM6W8Wqdvvh/arcgis/rest/ser
vices
Baltimore
https://bcgis.baltimorecountymd.gov/arcgis/rest/services
Baltimore
https://bcgisimagery.baltimorecountymd.gov/arcgis/rest/services
Baltimore
https://services2.arcgis.com/Ynpzre7M7vSGY7dh/ArcGIS/rest/ser
vices
Baltimore
https://tiles.arcgis.com/tiles/Ynpzre7M7vSGY7dh/arcgis/rest/servi
ces
Calvert
https://gis.calvertcountymd.gov/server/rest/services
Calvert
https://services2.arcgis.com/svdkKIzwWblQ8cKK/ArcGIS/rest/ser
vices
Caroline
https://services3.arcgis.com/yjhbpLpwDyUohPHk/ArcGIS/rest/ser
vices
Focus is history and culture
Caroline
https://tiles.arcgis.com/tiles/yjhbpLpwDyUohPHk/arcgis/rest/servi
ces
Carroll
https://services.arcgis.com/Uf0DiYpD9NOFO5YH/arcgis/rest/serv
ices
Carroll
https://tiles.arcgis.com/tiles/Uf0DiYpD9NOFO5YH/arcgis/rest/ser
vices

## Page 207

Cecil
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Cecil_DamgAsmt/FeatureServer
Go to the top and search for ‘Cecil’
Charles
https://services7.arcgis.com/3BMWkdyrt45RNCrq/arcgis/rest/servi
ces
Charles
https://tiles.arcgis.com/tiles/3BMWkdyrt45RNCrq/arcgis/rest/servi
ces
Collier
https://services2.arcgis.com/SlIq32SqARUHIhSx/ArcGIS/rest/serv
ices
Dorchester
           https://services7.arcgis.com/yqhlYKSnzjiOzQig/arcgis/rest/services
Dorchester
           https://tiles.arcgis.com/tiles/yqhlYKSnzjiOzQig/arcgis/rest/services
Frederick
https://fcgis.frederickcountymd.gov/server/rest/services
Frederick
https://services5.arcgis.com/o8KSxSzYaulbGcFX/ArcGIS/rest/ser
vices
Frederick
https://tiles.arcgis.com/tiles/o8KSxSzYaulbGcFX/arcgis/rest/servic
es
Garrett
https://gis.garrettcounty.org/server/rest/services
Harford
https://hcggis.harfordcountymd.gov/public/rest/services
Harford
https://hcggis.harfordcountymd.gov/arcgis/rest/services
Harford
https://services.arcgis.com/q8r0H9SbF6PzNpYE/arcgis/rest/servic
es
Harford
https://tiles.arcgis.com/tiles/q8r0H9SbF6PzNpYE/arcgis/rest/servi
ces
Howard
WMS server
Kent
https://services6.arcgis.com/RWHujKM5TItecIqp/arcgis/rest/servi
ces
Kent
https://tiles.arcgis.com/tiles/RWHujKM5TItecIqp/arcgis/rest/servic
es
Montgomery
https://gis.montgomerycountymd.gov/ArcGIS/rest/services
Montgomery
https://mcatlas.org/arcgis5/rest/services
Montgomery
https://gis2.montgomerycountymd.gov/arcgis/rest/services
Montgomery
https://gis3.montgomerycountymd.gov/arcgis/rest/services
Montgomery
https://gis4.montgomerycountymd.gov/arcgis/rest/services
Montgomery
https://gis5.montgomerycountymd.gov/arcgis/rest/services
Montgomery
https://www7.montgomerycountymd.gov/arcgis/rest/services
Montgomery
https://depgis.montgomerycountymd.gov/arcgis/rest/services

## Page 208

Montgomery
https://services.arcgis.com/hdlG36cOubTzNDBb/ArcGIS/rest/servi
ces
Montgomery
https://tiles.arcgis.com/tiles/hdlG36cOubTzNDBb/arcgis/rest/servi
ces
Prince George’s
https://gisdata.pgplanning.org/arcgis/rest/services
Prince George’s
https://gis.pgatlas.com/pgatlas/rest/services
Queen Anne’s
https://gis.qac.org/arcgis/rest/services
Queen Anne’s
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/QA_WaterSewer/FeatureServer
Go to the top and search for ‘Queen Anne’
Queen Anne’s
https://services5.arcgis.com/C97Ug2An2cCjc1ox/arcgis/rest/servic
es
Queen Anne’s
https://tiles.arcgis.com/tiles/C97Ug2An2cCjc1ox/arcgis/rest/servic
es
Somerset
No GIS found
St. Mary’s
https://stmgis.stmarysmd.com/arcgis/rest/services
Talbot
https://gis.talbotdes.org/hosting/rest/services
Washington
https://maps.washco-md.net/arcgis/rest/services
Washington
https://services2.arcgis.com/uxxyl33jRTSmjre5/arcgis/rest/services
Washington
https://tiles.arcgis.com/tiles/uxxyl33jRTSmjre5/arcgis/rest/services
Wicomico
https://gisapps.wicomicocounty.org/server/rest/services
Worcester
https://wcg-gisweb.co.worcester.md.us/arcgis/rest/services
Maryland City, Town, Village, etc GIS Servers

Annapolis
https://services.arcgis.com/7ww0md22RA7aTw3W/arcgis/rest/ser
vices
Annapolis
https://tiles.arcgis.com/tiles/7ww0md22RA7aTw3W/arcgis/rest/ser
vices
The city of Baltimore is also referred to as a “city county”.  This should not be confused
with Baltimore County which is an entirely different entity.
Baltimore
https://gis.baltimorecity.gov/egis/rest/services
Baltimore
https://geodata.baltimorecity.gov/egis/rest/services
Baltimore
https://services1.arcgis.com/UWYHeuuJISiGmgXx/ArcGIS/rest/se
rvices
Baltimore
https://tiles.arcgis.com/tiles/UWYHeuuJISiGmgXx/arcgis/rest/serv
ices

## Page 209

Baltimore
https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/serv
ices
Baltimore Neighborhood Indicators Alliance
Baltimore
https://services3.arcgis.com/mbYrzb5fKcXcAMNi/ArcGIS/rest/ser
vices
Public schools
Baltimore
https://tiles.arcgis.com/tiles/mbYrzb5fKcXcAMNi/arcgis/rest/servi
ces
Public schools
Bel Air
https://services5.arcgis.com/9jfGg288K34UNiRe/ArcGIS/rest/serv
ices
Bel Air
https://tiles.arcgis.com/tiles/9jfGg288K34UNiRe/arcgis/rest/servic
es
Bowie
https://gis.cityofbowie.org/arcgis/rest/services
Bowie
https://services3.arcgis.com/tczkZqMA7I4DlcvK/ArcGIS/rest/serv
ices
Bowie
https://tiles.arcgis.com/tiles/tczkZqMA7I4DlcvK/arcgis/rest/servic
es
Cambridge
https://services2.arcgis.com/AB4o41cT2GQ69z4k/ArcGIS/rest/ser
vices
Frederick
https://spires.cityoffrederick.com/ArcGIS/rest/services
Gaithersburg
https://maps.gaithersburgmd.gov/arcgis/rest/services
Laurel
https://services1.arcgis.com/AwDuFhONE9qxjJjX/ArcGIS/rest/ser
vices
Laurel
https://tiles.arcgis.com/tiles/AwDuFhONE9qxjJjX/arcgis/rest/servi
ces
Ocean City
https://services1.arcgis.com/jjVcwHv9AQEq3DH3/ArcGIS/rest/se
rvices
Ocean City
https://tiles.arcgis.com/tiles/jjVcwHv9AQEq3DH3/arcgis/rest/serv
ices
Rockville
https://maps.rockvillemd.gov/arcgis/rest/services
Rockville
https://maps.rockvillemd.gov/agsint/rest/services
Rockville
https://maps.rockvillemd.gov/rkvimg/rest/services
Rockville
https://services.arcgis.com/J65Mns15CRcll4iw/arcgis/rest/services
Rockville
           https://tiles.arcgis.com/tiles/J65Mns15CRcll4iw/arcgis/rest/services
Massachusetts State GIS Servers
Massachusetts GIS Data Layers
Website: https://www.mass.gov/orgs/massachusetts-digital-service
GIS: https://arcgisserver.digital.mass.gov/arcgisserver/rest/services

## Page 210

8-3-2023 No tiled data
GIS: https://services1.arcgis.com/hGdibHYSPO59RG1h/arcgis/rest/services

GIS: https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services
Parcel lines:   /MassGIS_Level3_Parcels/MapServer/tile/{z}/{y}/{x}
Massachusetts Department of Transportation
Website: https://www.mass.gov/orgs/massachusetts-department-of-transportation
GIS: https://gis.massdot.state.ma.us/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://gis.massdot.state.ma.us/image/rest/services
GIS: https://gisstg.massdot.state.ma.us/arcgis/rest/services
GIS: https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/ceiitspzDAHrdGO1/arcgis/rest/services
Massachusetts Department of Conservation and Recreation
Website: https://www.mass.gov/orgs/department-of-conservation-recreation
GIS: https://spatialags.vhb.com/arcgis/rest/services/DCR
8-4-2023 No tiled data
GIS: https://services1.arcgis.com/a94ppUcoV4uYTEpm/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/a94ppUcoV4uYTEpm/arcgis/rest/services
Executive Office of Energy and Environmental Affairs
Website:
https://www.mass.gov/orgs/executive-office-of-energy-and-environmental
-affairs
GIS: https://gis.eea.mass.gov/imgsvr/rest/services
GIS: https://services1.arcgis.com/7iJyYTjCtKsZS1LR/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/7iJyYTjCtKsZS1LR/arcgis/rest/services
Massachusetts Regional
Berkshire Regional Planning Commission
Website:  www.berkshireplanning.org
GIS: ________
Boston Region Metropolitan Planning Organization (Mpo)
Website:  www.bostonmpo.org
WMS GIS: _ttps://www.bostonmpo.org/map/wms
dead link  2
Cape Cod Commission
Website: www.capecodcommission.org
GIS: https://gis-services.capecodcommission.org/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/Cx6nu3bxRHgwsm05/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Cx6nu3bxRHgwsm05/arcgis/rest/services
Central Massachusetts Regional Planning Commission
Website:  www.cmrpc.org

## Page 211

GIS: https://services3.arcgis.com/wid5AQd6BHjWWq1h/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/wid5AQd6BHjWWq1h/arcgis/rest/services
Franklin Regional Council of Governments
Website:  www.frcog.org
GIS: ________
Martha’s Vineyard Commission
Website: www.mvcommission.org
GIS: https://services1.arcgis.com/FNsEJ848HT5uDOHD/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/FNsEJ848HT5uDOHD/arcgis/rest/services
Merrimack Valley Planning Commission
Website: www.mvpc.org
GIS: _ttps://aws.mvpc.org/arcgis/rest/services
dead link 1
8-4-2023 No tiled data
GIS: https://services.arcgis.com/S00hjvka5ISEVpTh/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/S00hjvka5ISEVpTh/arcgis/rest/services
Metropolitan Area Planning Council  (Boston area)
Website: www.mapc.org
GIS: https://geo.mapc.org/server/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/c5WwApDsDjRhIVkH/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/c5WwApDsDjRhIVkH/arcgis/rest/services
Montachusett Regional Planning Commission
Website: www.mrpc.org
GIS: https://mrmapper.mrpc.org/arcgis6443/rest/services
8-4-2023 Tiled data.  Several.  Go to top of this PDF file and search for ‘wmts'.
Nantucket Planning and Economic Development Commission
Website:
https://www.nantucket-ma.gov/306/Planning-Economic-Development-Commission
GIS: MapGeo
Northern Middlesex Council of Governments
Website: www.nmcog.org
GIS: https://services.arcgis.com/kNW4lBgGBMDtxPiV/ArcGIS/rest/services
GIS: https://services2.arcgis.com/8sfNXBvIUURUO8wz/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/8sfNXBvIUURUO8wz/arcgis/rest/services
Pioneer Valley Planning Commission
Website:  www.pvpc.org
GIS: https://services1.arcgis.com/JOJ3LXzkOX5MOLCK/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/JOJ3LXzkOX5MOLCK/arcgis/rest/services

## Page 212

Old Colony Planning Council
Website: www.ocpcrpa.org
GIS: ________
Southeastern Regional Planning and Economic Development District
Website:  www.srpedd.org
GIS: ________
Massachusetts County GIS Servers
Several New England states do not have an active form of county government
Massachusetts City, Town, Village, etc GIS Servers
Abington
Uses state GIS data hub
Agawam
          https://hostingdata3.tighebond.com/arcgis/rest/services/AgawamMA
Amesbury
_ttps://aws.mvpc.org/arcgis/rest/services/Amesbury   dead link 1
Amherst
https://gis.amherstma.gov/arcgis/rest/services
Amherst
           https://services.arcgis.com/fvEtUQQPvELjRlqy/arcgis/rest/services
Amherst
https://tiles.arcgis.com/tiles/fvEtUQQPvELjRlqy/arcgis/rest/servic
es
Andover
_ttps://aws.mvpc.org/arcgis/rest/services/Andover     dead link 1
Aquinnah
https://gisserver2.axisgis.com/arcgis/rest/services/AquinnahMA
Not open to public
Arlington
https://toagis.town.arlington.ma.us/server/rest/services
Ashland
           https://hostingdata2.tighebond.com/arcgis/rest/services/AshlandMA
Ayer
https://mrmapper.mrpc.org/arcgis6443/rest/services/Ayer
Barnstable
https://arcgis.mobile311.com/arcgis/rest/services/Massachusetts/Ba
rnstableMA/MapServer
Bellingham
https://gisserver2.axisgis.com/arcgis/rest/services/BellinghamMA
Not open to public
Belmont
https://spatialags.vhb.com/arcgis/rest/services/Belmont
Berlin
https://arcgis.vgsi.com/server/rest/services/Berlin_MA
Beverly
https://map.appgeo.com/arcgis/rest/services/BeverlyMA

## Page 213

Not open to public
Blackstone
https://gisserver2.axisgis.com/arcgis/rest/services/BlackstoneMA
Not open to public
Bolton
https://gisserver2.axisgis.com/arcgis/rest/services/BoltonMA
Not open to public
Boston
https://gis.boston.gov/arcgis/rest/services
Boston
https://gis.bostonplans.org/hosting/rest/services

Boston
https://maps.cityofboston.gov/arcgis/rest/services     SSL problem
Boston
https://gisportal.boston.gov/arcgis/rest/services
Boston
https://gisportal.boston.gov/image/rest/services
Boston
https://services.arcgis.com/sFnw0xNflSi8J0uh/arcgis/rest/services
Boston
https://tiles.arcgis.com/tiles/sFnw0xNflSi8J0uh/arcgis/rest/services
Boxford
_ttps://aws.mvpc.org/arcgis/rest/services/Boxford      dead link 1
Braintree
https://services9.arcgis.com/wMoJraMZWuVPEmGK/ArcGIS/rest
/services
Braintree
https://tiles.arcgis.com/tiles/wMoJraMZWuVPEmGK/arcgis/rest/s
ervices
Bridgewater
https://gisserver2.axisgis.com/arcgis/rest/services/BridgewaterMA
Not open to public
Brockton
         https://hostingdata3.tighebond.com/arcgis/rest/services/BrocktonMA
Brockton
https://spatialags.vhb.com/arcgis/rest/services/14428_Brockton
Brookline
https://gisweb.brooklinema.gov/arcgis/rest/services
Brookline
https://services1.arcgis.com/Oknk0tvfHOElpgGU/ArcGIS/rest/serv
ices
Burlington
They have a GIS based on Google maps
Cambridge
https://gis.cambridgema.gov/arcgis/rest/services
Cambridge
https://services1.arcgis.com/WnzC35krSYGuYov4/arcgis/rest/serv
ices
Cambridge
https://tiles.arcgis.com/tiles/WnzC35krSYGuYov4/arcgis/rest/servi
ces
Canton
https://ws.town.canton.ma.us/arcgis/rest/services
Carver
https://hostingdata2.tighebond.com/arcgis/rest/services/CarverMA
Chelmsford
https://map.appgeo.com/arcgis/rest/services/ChelmsfordMA

## Page 214

Chelsea
https://services9.arcgis.com/diuwWhOq89A0FdTw/arcgis/rest/serv
ices
Chicopee
         https://hostingdata3.tighebond.com/arcgis/rest/services/ChicopeeMA
Chicopee
https://services6.arcgis.com/YOvBy1qjcG3M90vp/ArcGIS/rest/ser
vices
Chicopee
https://tiles.arcgis.com/tiles/YOvBy1qjcG3M90vp/arcgis/rest/servi
ces
Chilmark
https://gisserver2.axisgis.com/arcgis/rest/services/ChilmarkMA
Not open to public
Clinton
https://arcgis.vgsi.com/server/rest/services/Clinton_MA
Clinton
https://mrmapper.mrpc.org/arcgis6443/rest/services/Clinton
Concord
https://gis.concordma.gov/arcgis/rest/services
Concord
https://arcgis.vgsi.com/server/rest/services/Concord_MA
Conway
https://gisserver2.axisgis.com/arcgis/rest/services/ConwayMA
Not open to public
Dartmouth
https://arcgis.vgsi.com/server/rest/services/Dartmouth_MA
Dartmouth
         https://hostingdata2.tighebond.com/arcgis/rest/services/DartmoutMA
Dedham
https://gis.dedham-ma.gov/arcgis/rest/services
Dedham
https://services1.arcgis.com/me41C4ZTLmDO2rPK/ArcGIS/rest/s
ervices
Dedham
https://tiles.arcgis.com/tiles/me41C4ZTLmDO2rPK/arcgis/rest/ser
vices
Deerfield
https://gisserver1.axisgis.com/arcgis/rest/services/DeerfieldMA
Not open to public
Douglas
https://gisserver2.axisgis.com/arcgis/rest/services/DouglasMA
Not open to public
Dracut
https://gisweb.dracutma.gov/dracutexternal/rest/services
Duxbury
https://gisserver2.axisgis.com/arcgis/rest/services/DuxburyMA
Not open to public
East Bridgewater
https://gisserver2.axisgis.com/arcgis/rest/services/East_Bridgewate
rMA
Not open to public
East Longmeadow
https://maps.eastlongmeadowma.gov/arcgis/rest/services

## Page 215

Easthampton
https://hostingdata2.tighebond.com/arcgis/rest/services/Easthampto
nMA
Easton
https://services2.arcgis.com/G6TP4SnXQoFs2r0T/ArcGIS/rest/ser
vices
Easton
https://tiles.arcgis.com/tiles/G6TP4SnXQoFs2r0T/arcgis/rest/servi
ces
Edgartown
https://gisserver2.axisgis.com/arcgis/rest/services/EdgartownMA
Not open to public
Erving
https://arcgis.mobile311.com/arcgis/rest/services/Massachusetts/Er
vingMA/MapServer
Essex
https://gisserver2.axisgis.com/arcgis/rest/services/EssexMA
Not open to public
Everett
          https://services2.arcgis.com/xJ0MjVdyImL1ajyn/arcgis/rest/services
Everett
          https://tiles.arcgis.com/tiles/xJ0MjVdyImL1ajyn/arcgis/rest/services
Fairhaven
https://gisserver2.axisgis.com/arcgis/rest/services/FairhavenMA
Not open to public
Fall River
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/FallRiv
erMA_Basemap_Ortho2020/MapServer
Fall River
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/FallRiv
erMA_Basemap_Ortho/MapServer
Fall River
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/FallRiv
erMA_Basemap_Plan/MapServer
Fall River
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/FallRiv
erMA_Basemap_Topo/MapServer
Fall River
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/FallRiv
erMA_Ops_Layers/MapServer
Foxborough
https://arcgis.vgsi.com/server/rest/services/Foxborough_MA
Foxborough
https://services5.arcgis.com/lpGxT11GBKtwDtDA/ArcGIS/rest/se
rvices
Foxborough
https://tiles.arcgis.com/tiles/lpGxT11GBKtwDtDA/arcgis/rest/serv
ices
Franklin
https://services.arcgis.com/RnGD2wABK1ZIJL6a/arcgis/rest/servi
ces
Franklin
https://tiles.arcgis.com/tiles/RnGD2wABK1ZIJL6a/arcgis/rest/serv
ices
Georgetown
_ttps://aws.mvpc.org/arcgis/rest/services/Georgetown   dead link 1

## Page 216

Gloucester
https://map.appgeo.com/arcgis/rest/services/Gloucester
Goshen
https://gisserver2.axisgis.com/arcgis/rest/services/GoshenMA
Not open to public
Grafton
https://hostingdata2.tighebond.com/arcgis/rest/services/GraftonMA
Greenfield
https://gisserver2.axisgis.com/arcgis/rest/services/GreenfieldMA
Not open to public
Groveland
_ttps://aws.mvpc.org/arcgis/rest/services/Groveland      dead link 1
Hadley
https://hostingdata2.tighebond.com/arcgis/rest/services/HadleyMA
Hamilton
https://gisserver1.axisgis.com/arcgis/rest/services/HamiltonMA
Not open to public

Hampden
         https://hostingdata2.tighebond.com/arcgis/rest/services/HampdenMA
Harwich
https://gisserver2.axisgis.com/arcgis/rest/services/HarwichMA
Not open to public
Hatfield
https://gisserver2.axisgis.com/arcgis/rest/services/HatfieldMA
Not open to public
Hingham
https://arcgis.vgsi.com/server/rest/services/Hingham_MA
Holyoke
They have a GIS based on Google maps
Hopedale
https://gisserver2.axisgis.com/arcgis/rest/services/HopedaleMA
Not open to public
Hopkinton
https://services8.arcgis.com/J2feNVZf8bqxrw4t/ArcGIS/rest/servic
es
Ipswich
https://gisserver2.axisgis.com/arcgis/rest/services/IpswichMA

Not open to public
Lakeville
https://gisserver1.axisgis.com/arcgis/rest/services/LakevilleMA

Not open to public
Leverett
https://gisserver2.axisgis.com/arcgis/rest/services/LeverettMA

Not open to public
Lawrence
_ttps://aws.mvpc.org/arcgis/rest/services/Lawrence     dead link 1

## Page 217

Lawrence
https://services9.arcgis.com/XU2wS4n9EQTNKS9Q/ArcGIS/rest/s
ervices
Lawrence
https://tiles.arcgis.com/tiles/XU2wS4n9EQTNKS9Q/arcgis/rest/ser
vices
Lee
https://gisserver2.axisgis.com/arcgis/rest/services/LeeMA

Not open to public
Leominster
https://hostingdata3.tighebond.com/arcgis/rest/services/Leominster
MA
Leyden
https://gisserver2.axisgis.com/arcgis/rest/services/LeydenMA

Not open to public
Littleton
          https://hostingdata2.tighebond.com/arcgis/rest/services/LittletonMA
Longmeadow
https://hostingdata2.tighebond.com/arcgis/rest/services/Longmeado
wMA
Longmeadow
https://hostingdata3.tighebond.com/arcgis/rest/services/Longmeado
wMA
Lowell
           https://services1.arcgis.com/ee8aYF9sH8nrhkjZ/arcgis/rest/services
Lowell
           https://tiles.arcgis.com/tiles/ee8aYF9sH8nrhkjZ/arcgis/rest/services
Ludlow
https://hostingdata3.tighebond.com/arcgis/rest/services/LudlowMA
Lunenburg
https://gisserver2.axisgis.com/arcgis/rest/services/LunenburgMA
Not open to public
Lynn
https://gisserver2.axisgis.com/arcgis/rest/services/LynnMA
Not open to public
Malden
https://services2.arcgis.com/MtnqIKHuMcAgIo2K/ArcGIS/rest/ser
vices
Malden
https://tiles.arcgis.com/tiles/MtnqIKHuMcAgIo2K/arcgis/rest/servi
ces
Manchester
https://map.appgeo.com/arcgis/rest/services/ManchesterMA
Not open to public
Manchester-By-The-Sea
https://services8.arcgis.com/EvnSQRphNDboBLpY/ArcGI
S/rest/services
Mansfield
https://gisserver2.axisgis.com/arcgis/rest/services/MansfieldMA
Not open to public
Marblehead
https://gisserver2.axisgis.com/arcgis/rest/services/MarbleheadMA

## Page 218

Not open to public
Mashpee
https://services3.arcgis.com/i6sQi3PaY7S1nPsB/ArcGIS/rest/servi
ces
Mashpee
           https://tiles.arcgis.com/tiles/i6sQi3PaY7S1nPsB/arcgis/rest/services
Medford
https://gisserver2.axisgis.com/arcgis/rest/services/MedfordMA
Not open to public
Merrimac
_ttps://aws.mvpc.org/arcgis/rest/services/Merrimac    dead link 1
Methuen
_ttps://aws.mvpc.org/arcgis/rest/services/Methuen
    dead link 1
Middleborough
https://map.appgeo.com/arcgis/rest/services/MiddleboroughMA
Middleton
https://gisserver2.axisgis.com/arcgis/rest/services/MiddletonMA
Not open to public
Millbury
          https://hostingdata3.tighebond.com/arcgis/rest/services/MillburyMA
Millis
https://gisserver2.axisgis.com/arcgis/rest/services/MillisMA
Not open to public
Millville
https://gisserver2.axisgis.com/arcgis/rest/services/MillvilleMA
Not open to public
Monson
           https://hostingdata2.tighebond.com/arcgis/rest/services/MonsonMA
Monson
           https://hostingdata3.tighebond.com/arcgis/rest/services/MonsonMA
Montague
https://gisserver2.axisgis.com/arcgis/rest/services/MontagueMA
Not open to public
Montgomery
https://gisserver2.axisgis.com/arcgis/rest/services/MontgomeryMA
Not open to public
Nahant
https://gisserver2.axisgis.com/arcgis/rest/services/NahantMA
Not open to public
Natick
https://map.appgeo.com/arcgis/rest/services/NatickMA
Needham
https://services9.arcgis.com/v9Q3Kk8Ytwk8t3ZA/ArcGIS/rest/ser
vices
New Marlborough
https://gisserver2.axisgis.com/arcgis/rest/services/New_Marlborou
ghMA
Not open to public

## Page 219

New Salem
https://gisserver2.axisgis.com/arcgis/rest/services/New_SalemMA
Not open to public
Newton
https://gisweb.newtonma.gov/server/rest/services
Newbury
_ttps://aws.mvpc.org/arcgis/rest/services/Newbury   dead link 1
Newburyport
_ttps://aws.mvpc.org/arcgis/rest/services/Newburyport   dead link 1
Norfolk
https://gisserver2.axisgis.com/arcgis/rest/services/NorfolkMA
Not open to public
North Andover
_ttps://aws.mvpc.org/arcgis/rest/services/NorthAndover
dead link 1
North Andover
https://map.appgeo.com/arcgis/rest/services/NorthAndoverMA
Not open to public
North Attleboro
https://arcgis.vgsi.com/server/rest/services/North_Attleboro_MA
Northborough
https://hostingdata2.tighebond.com/arcgis/rest/services/Northborou
ghMA
Northborough
https://map.appgeo.com/arcgis/rest/services/NorthboroughMA
Not open to public
Norwell
https://arcgis.vgsi.com/server/rest/services/Norwell_MA
Norwood
https://gisserver2.axisgis.com/arcgis/rest/services/NorwoodMA

Not open to public
Oak Bluffs
https://gisserver2.axisgis.com/arcgis/rest/services/Oak_BluffsMA

Not open to public
Orleans
WMS server
Oxford
https://gisserver2.axisgis.com/arcgis/rest/services/OxfordMA

Not open to public
Palmer
https://hostingdata2.tighebond.com/arcgis/rest/services/PalmerMA
Palmer
https://hostingdata3.tighebond.com/arcgis/rest/services/PalmerMA
Paxton
https://arcgis.vgsi.com/server/rest/services/Paxton_MA
Peabody
https://map.appgeo.com/arcgis/rest/services/PeabodyMA
Not open to public
Pepperell
https://spatialags.vhb.com/arcgis/rest/services/14678_Pepperell

## Page 220

Pittsfield
https://map.appgeo.com/arcgis/rest/services/PittsfieldMA
Not open to public
Plainfield
https://gisserver2.axisgis.com/arcgis/rest/services/PlainfieldMA
Not open to public
Plympton
They have a GIS based on Google maps
Quincy
https://arcgis.vgsi.com/server/rest/services/Quincy_MA
Quincy
https://map.appgeo.com/arcgis/rest/services/QuincyMA
Not open to public
Randolph
https://map.appgeo.com/arcgis/rest/services/RandolphMA
Not open to public
Raynham
         https://hostingdata2.tighebond.com/arcgis/rest/services/RaynhamMA
Reading
https://services2.arcgis.com/nOtdc9zO41L2RxCc/ArcGIS/rest/serv
ices
Reading
https://tiles.arcgis.com/tiles/nOtdc9zO41L2RxCc/arcgis/rest/servic
es
Rockport
https://services5.arcgis.com/M3HWiWPZtHfjKOLc/arcgis/rest/ser
vices
Rockport
https://tiles.arcgis.com/tiles/M3HWiWPZtHfjKOLc/arcgis/rest/ser
vices
Rowley
_ttps://aws.mvpc.org/arcgis/rest/services/Rowley
dead link 1
Royalston
https://mrmapper.mrpc.org/arcgis6443/rest/services/Royalston
Rutland
https://gisserver2.axisgis.com/arcgis/rest/services/RutlandMA
Not open to public
Salem
https://services9.arcgis.com/nPsFhwkdebYjxn1R/ArcGIS/rest/serv
ices
Salem
https://tiles.arcgis.com/tiles/nPsFhwkdebYjxn1R/arcgis/rest/servic
es
Salisbury
_ttps://aws.mvpc.org/arcgis/rest/services/Salisbury    dead link 1
Salisbury
https://services6.arcgis.com/Hx8jJ6McXQ0jnqLk/ArcGIS/rest/serv
ices
Salisbury
https://tiles.arcgis.com/tiles/Hx8jJ6McXQ0jnqLk/arcgis/rest/servic
es
Sandisfield
https://gisserver2.axisgis.com/arcgis/rest/services/SandisfieldMA

## Page 221

Not open to public
Scituate
           https://hostingdata2.tighebond.com/arcgis/rest/services/ScituateMA
Seekonk
https://map.appgeo.com/arcgis/rest/services/SeekonkMA
Not open to public
Sharon
https://arcgis.vgsi.com/server/rest/services/Sharon_MA
Shirley
https://mrmapper.mrpc.org/arcgis6443/rest/services/Shirley
Shutesbury
https://gisserver2.axisgis.com/arcgis/rest/services/ShutesburyMA
Not open to public
Somerville
https://arcgis.vgsi.com/server/rest/services/Somerville_MA
South Hadley           https://gisserver2.axisgis.com/arcgis/rest/services/South_HadleyMA
Not open to public
Southborough           https://gisserver2.axisgis.com/arcgis/rest/services/SouthboroughMA
Not open to public
Southbridge
https://gisserver2.axisgis.com/arcgis/rest/services/SouthbridgeMA
Not open to public
Springfield
https://maps.springfield-ma.gov/arcgis/rest/services
Sterling
https://gisserver2.axisgis.com/arcgis/rest/services/SterlingMA
Not open to public
Stockbridge
https://gisserver2.axisgis.com/arcgis/rest/services/StockbridgeMA
Not open to public
Stow
https://arcgis.vgsi.com/server/rest/services/Stow_MA
Sturbridge
https://hostingdata2.tighebond.com/arcgis/rest/services/Sturbridge
MA
Sturbridge
https://hostingdata3.tighebond.com/arcgis/rest/services/Sturbridge
MA
Sturbridge
https://arcgis.vgsi.com/server/rest/services/Sturbridge_MA
Swampscott
See Essex County
Swansea
https://gisserver2.axisgis.com/arcgis/rest/services/SwanseaMA

Not open to public

## Page 222

Taunton
https://map.appgeo.com/arcgis/rest/services/TauntonMA
Tisbury
https://gisserver2.axisgis.com/arcgis/rest/services/TisburyMA

Not open to public
Topsfield
https://gisserver1.axisgis.com/arcgis/rest/services/TopsfieldMA

Not open to public
Townsend
https://mrmapper.mrpc.org/arcgis6443/rest/services/Townsend
Truro
Uses state GIS data hub
Uxbridge
https://gisserver2.axisgis.com/arcgis/rest/services/UxbridgeMA

Not open to public
Walpole
https://arcgis.vgsi.com/server/rest/services/Walpole_MA
Ware
https://hostingdata2.tighebond.com/arcgis/rest/services/WareMA
Wayland
https://gisserver2.axisgis.com/arcgis/rest/services/WaylandMA

Not open to public
Webster
           https://hostingdata2.tighebond.com/arcgis/rest/services/WebsterMA
Webster
           https://hostingdata3.tighebond.com/arcgis/rest/services/WebsterMA
Wellesley
https://maps.wellesleyma.gov/server/rest/services
Wellesley
https://spatialags.vhb.com/arcgis/rest/services/14624_Wellesley
Wellesley
https://services6.arcgis.com/f6G5SbcwuEVmR1CW/ArcGIS/rest/s
ervices
Wellesley
https://tiles.arcgis.com/tiles/f6G5SbcwuEVmR1CW/arcgis/rest/ser
vices
Wellfleet
https://gisserver2.axisgis.com/arcgis/rest/services/WaylandMA
Not open to public
Wenham
https://gisserver2.axisgis.com/arcgis/rest/services/WenhamMA

Not open to public
West Boylston
https://gisserver2.axisgis.com/arcgis/rest/services/West_Boylston
MA
Not open to public
West Newbury
_ttps://aws.mvpc.org/arcgis/rest/services/WestNewbury
dead link 1
West Springfield
https://services6.arcgis.com/F2k7GfbV5LllUPHE/ArcGIS/rest/serv
ices

## Page 223

West Tisbury           https://gisserver2.axisgis.com/arcgis/rest/services/West_TisburyMA

Not open to public
Westborough
https://services3.arcgis.com/9eghs4bJoZAGYedu/ArcGIS/rest/serv
ices
Westborough
https://tiles.arcgis.com/tiles/9eghs4bJoZAGYedu/arcgis/rest/servic
es
Westhampton            https://gisserver2.axisgis.com/arcgis/rest/services/WesthamptonMA

Not open to public
Westminster
https://mrmapper.mrpc.org/arcgis6443/rest/services/Westminster
Westwood
https://services8.arcgis.com/e79da2LBxIrnj0jp/arcgis/rest/services
Westwood
https://tiles.arcgis.com/tiles/e79da2LBxIrnj0jp/arcgis/rest/services
Wilbraham
https://hostingdata2.tighebond.com/arcgis/rest/services/Wilbraham
MA
Williamstown
https://hostingdata2.tighebond.com/arcgis/rest/services/Williamsto
wnMA
Winthrop
https://gisserver2.axisgis.com/arcgis/rest/services/WinthropMA

Not open to public
Woburn
https://services1.arcgis.com/ePzCWD2awZlZQ5jd/arcgis/rest/servi
ces
Woburn
https://tiles.arcgis.com/tiles/ePzCWD2awZlZQ5jd/arcgis/rest/servi
ces
Worcester
https://services1.arcgis.com/j8dqo2DJE7mVUBU1/arcgis/rest/serv
ices
Worcester
https://tiles.arcgis.com/tiles/j8dqo2DJE7mVUBU1/arcgis/rest/servi
ces
Yarmouth
https://arcgis.vgsi.com/server/rest/services/Yarmouth_MA

Michigan State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Michigan GIS Open Data
Website: https://gis-michigan.opendata.arcgis.com
 Michigan Department of Environment, Great Lakes and Energy
Website: https://www.michigan.gov/egle

## Page 224

GIS: https://services1.arcgis.com/FNjlrOFR0aGJ71Tg/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/FNjlrOFR0aGJ71Tg/arcgis/rest/services
 Michigan Department of Technology - Management and Budget (DTMB)
Website: https://www.michigan.gov/dtmb/services/maps
GIS: https://gisago3.mcgi.state.mi.us/arcgis/rest/services
SSL problem
8-4-2023 No tiled data
GIS: https://gisago-qa.mcgi.state.mi.us/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://gisp.mcgi.state.mi.us/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gisp.mcgi.state.mi.us/maps/rest/services
Recreation  MDOT/DEGR_MapService2/MapServer
GIS: https://gisuat.mcgi.state.mi.us/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://www.mcgi.state.mi.us/arcgis/rest/services
Michigan Department of Transportation
Website: https://www.michigan.gov/mdot
GIS: https://mdotgis.state.mi.us/arcgis/rest/services
GIS: https://gisagomdot.state.mi.us/arcgis/rest/services
GIS: https://services2.arcgis.com/67lKNkQ2TO1I3lhR/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/67lKNkQ2TO1I3lhR/arcgis/rest/services
Michigan Department of Natural Resources
Website: https://www.michigan.gov/dnr
GIS: https://services3.arcgis.com/Jdnp1TjADvSDxMAX/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Jdnp1TjADvSDxMAX/arcgis/rest/services
Michigan state police
Website: https://www.michigan.gov/msp
GIS: https://mspmaps.state.mi.us/micims/rest/services
SSL problem
8-4-2023 No tiled data
GIS: https://services5.arcgis.com/ZqUZ99cjRiEOyN05/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/ZqUZ99cjRiEOyN05/arcgis/rest/services
Variety of Michigan layers
GIS: https://imagery.michigan.gov/server/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gisagocss.state.mi.us/arcgis/rest/services
GIS: https://gisagoegle.state.mi.us/arcgis/rest/services
GIS: https://services3.arcgis.com/dxRQUfTDNtfqZ301/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/dxRQUfTDNtfqZ301/arcgis/rest/services
GIS: https://services9.arcgis.com/uHvF7MqLbcZt7JoZ/arcgis/rest/services
Michigan Natural Features Inventory

## Page 225

Website: https://mnfi.anr.msu.edu
GIS: https://services1.arcgis.com/7w1SUsLNZbGKoz6h/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/7w1SUsLNZbGKoz6h/arcgis/rest/services
Western Michigan University - Geology and Earth Sciences
Website: https://wmich.edu/geology
GIS: https://www.esrs.wmich.edu/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Eastern Upper Peninsula Intermediate School District
GIS: https://services4.arcgis.com/IVO7bqspY7CXFUTU/ArcGIS/rest/services
Michigan Regional
Central Upper Peninsula Planning and Development Regional Commission
Website: https://cuppad.org
GIS: https://services5.arcgis.com/VxT1UTIFTgaEp7hM/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/VxT1UTIFTgaEp7hM/arcgis/rest/services
Grand Valley Metro Council
Website: https://www.gvmc.org
GIS: https://regis-apps-login.gvmc-regis.org/arcgis/rest/services
GIS: https://services5.arcgis.com/X42k956XlfnIoN3d/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/X42k956XlfnIoN3d/arcgis/rest/services
Huron-Clinton Metroparks
Website: https://www.metroparks.com
GIS: https://services.arcgis.com/W8lmhbiyq5nrZIV6/arcgis/rest/services
Southeast Michigan Council of Governments
Website: https://semcog.org/About-SEMCOG
GIS: https://arcgisserver.semcog.org/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://services1.arcgis.com/xUx8EjNc6egUPYWh/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/xUx8EjNc6egUPYWh/arcgis/rest/services
Tri-County Regional Planning Commission
Website: https://www.mitcrpc.org
GIS: https://services7.arcgis.com/f1RRY3KdfLkWdWvF/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/f1RRY3KdfLkWdWvF/arcgis/rest/services
Michigan Township GIS Servers
Canton
https://maps.canton-mi.org/server/rest/services
Waterford
https://services3.arcgis.com/kRCuM0PjgVVVv4tK/arcgis/rest/serv
ices

## Page 226

Michigan County GIS Servers
As of 12-30-2019 all Michigan counties have been checked for a public-facing GIS server.  All
counties not listed below fall into one of the following categories.
1.
County GIS is hosted on a WMS server that is hidden behind a proxy and therefore
cannot be accessed directly by GISsurfer.
2.
County GIS is hosted on some other kind of GIS server that cannot be accessed directly
by GISsurfer.  Most of these have just a few layers of data which are related to parcels.
3.
County has no GIS.
Allegan
https://services7.arcgis.com/abcn8A25PPQFVHHF/arcgis/rest/serv
ices
Allegan
https://tiles.arcgis.com/tiles/abcn8A25PPQFVHHF/arcgis/rest/serv
ices
Antrim
https://services6.arcgis.com/ZcCP0G3kEnUDVego/arcgis/rest/serv
ices
Antrim
https://tiles.arcgis.com/tiles/ZcCP0G3kEnUDVego/arcgis/rest/serv
ices
Arenac
https://services8.arcgis.com/SWvtgOskziun2bFF/arcgis/rest/servic
es
Arenac
          https://tiles.arcgis.com/tiles/SWvtgOskziun2bFF/arcgis/rest/services
Barry
https://services3.arcgis.com/blE8NdGZSd9Sfngv/arcgis/rest/servic
es
Real table of contents hidden by Fetch GIS
Barry
https://tiles.arcgis.com/tiles/blE8NdGZSd9Sfngv/arcgis/rest/servic
es
Real table of contents hidden by Fetch GIS
Calhoun
https://gis.calhouncountymi.gov/server/rest/services
If you see a message asking you to sign-in then click ‘Cancel’ and
the table of contents should work OK.
Cheboygan
https://services6.arcgis.com/j6ueqNZduqQcCpQQ/arcgis/rest/servi
ces
Delta
https://gis.deltami.gov/arcgis/rest/services
Eaton
https://ecgis.eatoncounty.org/ecgis_ssl/rest/services
Eaton
https://services2.arcgis.com/c9l1e4fKpsCnqD7H/ArcGIS/rest/servi
ces
Eaton
          https://tiles.arcgis.com/tiles/c9l1e4fKpsCnqD7H/arcgis/rest/services
Emmet
https://gis.emmetcounty.org/arcgis/rest/services
Genesee
https://services2.arcgis.com/5ckbIY7K9TUKoseK/arcgis/rest/servi
ces

## Page 227

Genesee
https://tiles.arcgis.com/tiles/5ckbIY7K9TUKoseK/arcgis/rest/servi
ces
Grand Traverse
https://gis.gtcountymi.gov/arcgis/rest/services
Ingham
WMS server
Ionia
https://services9.arcgis.com/i2awudUyJK8gxxEe/arcgis/rest/servic
es
Ionia
https://tiles.arcgis.com/tiles/i2awudUyJK8gxxEe/arcgis/rest/servic
es
Iron
https://services8.arcgis.com/ahtZbIJBv5S4YTzC/arcgis/rest/servic
es
Jackson
https://gis.mijackson.org/countygis/rest/services
Kalamazoo
https://services3.arcgis.com/RGltUbqpl4h9E3Qh/arcgis/rest/servic
es
Kalamazoo
https://tiles.arcgis.com/tiles/RGltUbqpl4h9E3Qh/arcgis/rest/servic
es
Kent
https://gis.kentcountymi.gov/agisprod/rest/services
Kent
https://gis.kentcountymi.gov/agisimageprod/rest/services
Kent
https://services2.arcgis.com/CzKZD1UCo3l2beRZ/ArcGIS/rest/ser
vices
Kent
https://tiles.arcgis.com/tiles/CzKZD1UCo3l2beRZ/arcgis/rest/servi
ces
Leelanau
https://services.arcgis.com/F7SeTaZ2Nijdg6lG/arcgis/rest/services
Leelanau
           https://tiles.arcgis.com/tiles/F7SeTaZ2Nijdg6lG/arcgis/rest/services
Livingston
https://services1.arcgis.com/cL47lSDX9wW9Ylgx/arcgis/rest/servi
ces
Livingston
https://tiles.arcgis.com/tiles/cL47lSDX9wW9Ylgx/arcgis/rest/servi
ces
Macomb
https://gis.macombgov.org/arcgis1/rest/services
Macomb
https://services6.arcgis.com/K0qS4r8AEJxrE8em/ArcGIS/rest/serv
ices
Marquette
https://webportal.co.marquette.wi.us/publicags/rest/services
Midland
https://services6.arcgis.com/9ALftzD3ElQ7KAgT/arcgis/rest/servi
ces

## Page 228

Midland
https://tiles.arcgis.com/tiles/9ALftzD3ElQ7KAgT/arcgis/rest/servi
ces
Monroe
https://gis.monroemi.gov/server/rest/services
Monroe
https://services2.arcgis.com/vn6CmLDc5f5u0ONG/ArcGIS/rest/se
rvices
Monroe
https://tiles.arcgis.com/tiles/vn6CmLDc5f5u0ONG/arcgis/rest/serv
ices
Muskegon
https://maps.muskegoncountygis.com/arcgis/rest/services

Newaygo
https://arcgisweb.countyofnewaygo.com/hosting/rest/services
Oakland
https://gisservices.oakgov.com/arcgis/rest/services
Oceana
https://services9.arcgis.com/WUMuyB4xpXjBnX9E/arcgis/rest/ser
vices
They likely have other collections of feature services
Ottawa
https://gis.miottawa.org/arcgis/rest/services
Ottawa
https://services2.arcgis.com/ixRLoNIl4gmM9jgg/arcgis/rest/servic
es
Ottawa
https://tiles.arcgis.com/tiles/ixRLoNIl4gmM9jgg/arcgis/rest/servic
es
St. Clair
https://maps.stclaircounty.org/geocortex_wa/rest/services
Table of contents disabled
St. Clair
https://services5.arcgis.com/t6ndwcHpE4BmkrKP/ArcGIS/rest/ser
vices
Washtenaw
https://webmapssecure.ewashtenaw.org/arcgisshared/rest/services
Washtenaw
https://a2maps.a2gov.org/a2arcgis/rest/services
Washtenaw
https://services2.arcgis.com/xRI3cTw3hPVoEJP0/ArcGIS/rest/serv
ices
Washtenaw
https://tiles.arcgis.com/tiles/xRI3cTw3hPVoEJP0/arcgis/rest/servic
es
Wayne
http://waynecounty.com/gisserver/rest/services
not https
Wayne
https://services1.arcgis.com/b6rkZNtCd6Mx2gvB/arcgis/rest/servi
ces
Wayne
https://tiles.arcgis.com/tiles/b6rkZNtCd6Mx2gvB/arcgis/rest/servic
es
Michigan Township GIS Servers

## Page 229

Delta (Eaton county)
https://services5.arcgis.com/kau6A2teN2KmzzZT/arcgis/rest/servi
ces
Michigan City, Town, Village, etc GIS Servers
Ann Arbor
https://a2maps.a2gov.org/a2arcgis/rest/services
Ann Arbor
https://services2.arcgis.com/cenCPuKxOZuq6BCE/ArcGIS/rest/ser
vices
Ann Arbor
https://tiles.arcgis.com/tiles/cenCPuKxOZuq6BCE/arcgis/rest/servi
ces
Battle Creek
https://services6.arcgis.com/cuKwt0IKP5B84jop/ArcGIS/rest/servi
ces
Battle Creek
          https://tiles.arcgis.com/tiles/cuKwt0IKP5B84jop/arcgis/rest/services
Brighton
https://gis.brightoncity.org/arcgis/rest/services
Brooklyn
__________
Corunna
__________
Detroit
https://egis.detroitmi.gov/image/rest/services

Detroit
https://services2.arcgis.com/HsXtOCMp1Nis1Ogr/ArcGIS/rest/ser
vices
Detroit
https://services2.arcgis.com/HsXtOCMp1Nis1Ogr/arcgis/rest/servi
ces
Detroit
https://services2.arcgis.com/qvkbeam7Wirps6zC/arcgis/rest/servic
es
Detroit
          https://tiles.arcgis.com/tiles/qvkbeam7Wirps6zC/arcgis/rest/services
East Lansing
https://gis2.cityofeastlansing.com/arcgis/rest/services
Ferndale
https://services1.arcgis.com/GE4Idg9FL97XBa3P/arcgis/rest/servi
ces
Ferndale
https://tiles.arcgis.com/tiles/GE4Idg9FL97XBa3P/arcgis/rest/servic
es
Ferndale
https://services6.arcgis.com/kpe5MwFGvZu9ezGW/arcgis/rest/ser
vices
Ferndale
https://tiles.arcgis.com/tiles/kpe5MwFGvZu9ezGW/arcgis/rest/ser
vices
Ferndale
https://services6.arcgis.com/2TPYEzbyXSiAqSUs/ArcGIS/rest/ser
vices
Ferndale
https://tiles.arcgis.com/tiles/2TPYEzbyXSiAqSUs/arcgis/rest/servi
ces

## Page 230

Flint
https://services5.arcgis.com/lqqWNtSxx8Akj04A/ArcGIS/rest/serv
ices
Frankfort
_________
Grand Rapids
https://maps.grcity.us/arcgis/rest/services
Grand Rapids
https://maps.ci.grand-rapids.mn.us/server/rest/services
Grand Rapids
https://services2.arcgis.com/L81TiOwAPO1ZvU9b/arcgis/rest/serv
ices
Grand Rapids
https://tiles.arcgis.com/tiles/L81TiOwAPO1ZvU9b/arcgis/rest/serv
ices
Holland
https://gis.hollandbpw.com/arcgis/rest/services
Holland
https://services1.arcgis.com/QNHFBm4iXVHdb5Xv/ArcGIS/rest/s
ervices
Holland
https://tiles.arcgis.com/tiles/QNHFBm4iXVHdb5Xv/arcgis/rest/ser
vices
Kalamazoo
https://gis.kalamazoocity.org/hosting/rest/services
Lansing
https://imagery.lansingmi.gov/arcgis/rest/services
Madison Heights
https://services2.arcgis.com/RSm8IFpeYSInb9rO/ArcGIS/rest/serv
ices
Midland
https://arcgis1.midland-mi.org/arcgis/rest/services
Midland
https://services5.arcgis.com/f1fDjWaPeXDdlPzr/ArcGIS/rest/servi
ces
Midland
           https://tiles.arcgis.com/tiles/f1fDjWaPeXDdlPzr/arcgis/rest/services
Petoskey
See Emmet County
Plymouth
https://services5.arcgis.com/vD63F8HZc4ljO6eE/arcgis/rest/servic
es
Portage
https://services7.arcgis.com/AujU6g0cAkL5JYsn/ArcGIS/rest/serv
ices
Portage
https://tiles.arcgis.com/tiles/AujU6g0cAkL5JYsn/arcgis/rest/servic
es
Rochester Hills
https://services2.arcgis.com/mAHz4TNZ3K1d0hNn/ArcGIS/rest/s
ervices
Royal Oak
https://gis.romi.gov/arcgis/rest/services
Sandusky
_________

## Page 231

Southfield
_ttps://maps.cityofsouthfield.com/arcgis/rest/services   dead link 3
Sylvan
_________
Taylor
https://services1.arcgis.com/Sj7BOyGDEieKGELM/arcgis/rest/ser
vices
Taylor
https://tiles.arcgis.com/tiles/Sj7BOyGDEieKGELM/arcgis/rest/ser
vices
Traverse City
https://tcgis.traversecitymi.gov/arcgis/rest/services
Traverse City
https://services9.arcgis.com/nCl6vSi6bRmwCKkk/ArcGIS/rest/ser
vices
Troy
https://gis.troymi.gov/arcgis/rest/services
Westland
https://services2.arcgis.com/y7VShPA3gGO9NJCc/ArcGIS/rest/se
rvices
Westland
https://tiles.arcgis.com/tiles/y7VShPA3gGO9NJCc/arcgis/rest/serv
ices
Yale
___________
Minnesota State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Minnesota Geospatial Commons
Website: https://gisdata.mn.gov
Minnesota Department of Transportation
Website: https://www.dot.state.mn.us
GIS: _ttps://dotapp9.dot.state.mn.us/lrs/rest/services/emma
dead link 1
8-4-2023 No tiled data
GIS: http://mndotgis.dot.state.mn.us/egis12/rest/services
Not open to public
GIS: https://services.arcgis.com/qWbGMYB49y8mLbRt/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/qWbGMYB49y8mLbRt/arcgis/rest/services
Minnesota Department of Natural Resources
Website: https://www.dnr.state.mn.us/index.html
The following addresses do have data but some odd reason you can not display the layer
lists by drilling down on these links
GIS: https://arcgis.dnr.state.mn.us/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://arcgis.dnr.state.mn.us/ArcGIS/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://arcgis.dnr.state.mn.us/public/rest/services

## Page 232

8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://arcgis.dnr.state.mn.us/mndnr/rest/services
8-4-2023 No tiled data
Minnesota Department of Public Safety
Website: https://dps.mn.gov
GIS: https://services2.arcgis.com/V12PKGiMAH7dktkU/arcgis/rest/services
Minnesota Department of Education
Website: https://education.mn.gov
GIS: https://services.arcgis.com/GXwOsvnLQI6EDOp7/ArcGIS/rest/services
8-4-2023 No tiled data
Minnesota Department of Agriculture
Website: https://www.mda.state.mn.us
GIS: https://gis.mda.state.mn.us/arcgis/rest/services
GIS: https://gis.bah.state.mn.us/arcgis/rest/services
GIS: https://services2.arcgis.com/buyLfpPRzGI7AGAC/ArcGIS/rest/services
Minnesota Pollution Control Agency
Website: https://www.pca.state.mn.us/
GIS: https://pca-gis02.pca.state.mn.us/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://gis-ext-aqi.pca.mn.gov/arcgis/rest/services
GIS: https://services2.arcgis.com/7QMLozViUIV7KGFq/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/7QMLozViUIV7KGFq/arcgis/rest/services
Minnesota Board of Water and Soil Resources
Website: https://www.bwsr.state.mn.us
GIS: https://apps.bwsr.state.mn.us/arcgis/rest/services
University of Minnesota Research Computing
Website: https://rc.umn.edu/uspatial
GIS: https://gis4.uspatial.umn.edu/arcgis/rest/services
Table of contents disabled
GIS: https://gis6.uspatial.umn.edu/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
University of Minnesota
GIS: https://services.arcgis.com/8df8p0NlLFEShl0r/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/8df8p0NlLFEShl0r/arcgis/rest/services
Minnesota various layers
GIS: https://feat.gisdata.mn.gov/arcgis/rest/services
GIS: https://services.arcgis.com/9OIuDHbyhmH91RfZ/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/9OIuDHbyhmH91RfZ/arcgis/rest/services

## Page 233

Minnesota Regional
Arrowhead Regional Development Commission
Website: https://www.ardc.org
GIS: https://services1.arcgis.com/XcwN27e6wZ49zF8i/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/XcwN27e6wZ49zF8i/arcgis/rest/services
Metropolitan Council
Website: https://metrocouncil.org
GIS: https://gis.metc.state.mn.us/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://arcgis.metc.state.mn.us/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://arcgis.metc.state.mn.us/ds1/rest/services
GIS: https://arcgis.metc.state.mn.us/server/rest/services
GIS: https://services1.arcgis.com/KoDrdxDCTDvfgddz/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/KoDrdxDCTDvfgddz/arcgis/rest/services
Saint Paul Regional Water Services
Website: https://www.stpaul.gov/departments/saint-paul-regional-water-services
GIS: https://services9.arcgis.com/OhApV2tSBivqSpuX/ArcGIS/rest/services
Minnesota County GIS Servers
All counties are listed.  Any showing _______ need to be checked for a GIS server.

Aitkin
https://gisweb.co.aitkin.mn.us/arcgis/rest/services
Anoka
https://gisservices.co.anoka.mn.us/anoka_gis/rest/services
Anoka
https://gis.anokacountymn.gov/anoka_gis/rest/services
Becker
https://gis-server.co.becker.mn.us/arcgis/rest/services
Table of contents disabled
Beltrami
https://arcgis.co.beltrami.mn.us/arcgis/rest/services
Table of contents disabled
Beltrami
https://services5.arcgis.com/FgDWCkI65RQBnNsp/ArcGIS/rest/se
rvices
Beltrami
https://tiles.arcgis.com/tiles/FgDWCkI65RQBnNsp/arcgis/rest/serv
ices
Benton
https://services.arcgis.com/cHtpFLI4WlqULV8k/arcgis/rest/services
Big Stone
https://gis.bigstonecounty.gov/arcgis/rest/services
Table of contents disabled
Big Stone
https://services8.arcgis.com/W9NtgmEXTNYySaSq/arcgis/rest/ser
vices

## Page 234

Blue Earth
_ttps://gis.blueearthcountymn.gov/arcgis/rest/services   dead link 1
Bricelyn
https://services6.arcgis.com/Pl3nNNLxrVrD3nxE/ArcGIS/rest/serv
ices
Brown
Schneider Geospatial - ArcGIS server address is not public
Carlton
https://gis.co.carlton.mn.us/arcgis/rest/services
Carlton
           https://services.arcgis.com/GaVfJCelmMSe6faF/arcgis/rest/services
Carlton
https://tiles.arcgis.com/tiles/GaVfJCelmMSe6faF/arcgis/rest/servic
es
Carver
https://gis.co.carver.mn.us/arcgis_ea/rest/services
Carver
https://gis.co.carver.mn.us/arcgis_ca/rest/services
Carver
https://gis.co.carver.mn.us/arcgis_app/rest/services
Carver
https://services.arcgis.com/wMZT8kNwa6tOxhKg/arcgis/rest/servi
ces
Carver
https://tiles.arcgis.com/tiles/wMZT8kNwa6tOxhKg/arcgis/rest/ser
vices
Cass
https://cassweb.casscountymn.gov/arcgis/rest/services
Chippewa
https://gis.chippewa.mn/arcgis/rest/services
Table of contents disabled
Chippewa
https://services2.arcgis.com/SnCfeG9WCK26XimW/arcgis/rest/ser
vices
Chisago
https://gis.chisagocountymn.gov/arcgis/rest/services
Table of contents disabled
Clay
https://arcgis.claycountymn.gov/arcgis/rest/services
Clay
https://map.claycountymn.gov/arcgis/rest/services
Clay
https://gis23.claycountymn.gov/arcgis/rest/services
Clay
https://services6.arcgis.com/mS1vc6dGT4od9xCB/ArcGIS/rest/ser
vices
Clay
https://tiles.arcgis.com/tiles/mS1vc6dGT4od9xCB/arcgis/rest/servi
ces
Clearwater
https://map.co.clearwater.mn.us/arcgis/rest/services
Cook
https://services.arcgis.com/L3KwVADPEG6iD24f/arcgis/rest/servi
ces
Cook
https://tiles.arcgis.com/tiles/L3KwVADPEG6iD24f/arcgis/rest/serv
ices

## Page 235

Cottonwood
https://services6.arcgis.com/HWNeJO1BX8XvS0O8/ArcGIS/rest/s
ervices
Crow Wing
https://gis.crowwing.us/cwc_external_main/rest/services
Crow Wing
https://services2.arcgis.com/uqzY8RRiGhwsxu6K/arcgis/rest/servi
ces
Crow Wing
https://tiles.arcgis.com/tiles/uqzY8RRiGhwsxu6K/arcgis/rest/servi
ces
Dakota
https://gis2.co.dakota.mn.us/arcgis/rest/services
Dakota
https://gisimg.co.dakota.mn.us/arcgis/rest/services
Dakota
https://services2.arcgis.com/CfhoRi2v351nuUH7/ArcGIS/rest/serv
ices
Dakota
https://tiles.arcgis.com/tiles/CfhoRi2v351nuUH7/arcgis/rest/servic
es
Dodge
See Goodhue County and look for “DC” layers.
Douglas
https://dc-web-2.co.douglas.mn.us/server/rest/services
slow server
Douglas
https://dc-web-2.co.douglas.mn.us/imageserver/rest/services
slow server
Douglas
https://services2.arcgis.com/8iQOd6RvhPL17pJd/ArcGIS/rest/serv
ices
Eagle Bend
https://services8.arcgis.com/nkCzekRmxhrymQwF/arcgis/rest/serv
ices
Faribault
https://apps.ci.faribault.mn.us/arcgis/rest/services
Faribault
https://services2.arcgis.com/fxB2C8mQfjMb1848/ArcGIS/rest/ser
vices
Faribault
https://tiles.arcgis.com/tiles/fxB2C8mQfjMb1848/arcgis/rest/servic
es
Fillmore
http://gis.co.fillmore.mn.us/arcgis/rest/services
not https
Freeborn
Schneider Geospatial - ArcGIS server address is not public
Goodhue
https://maps.co.goodhue.mn.us/server/rest/services
Goodhue
https://services5.arcgis.com/zCDVc272xQCnwjzc/ArcGIS/rest/ser
vices
Grant
https://gis.co.grant.mn.us/arcgis/rest/services
Hennepin
https://gis.hennepin.us/arcgis/rest/services
Hennepin

## Page 236

Houston
Schneider Geospatial - ArcGIS server address is not public

Hubbard
https://gis.co.hubbard.mn.us/arcgis/rest/services

Hubbard
https://services.arcgis.com/auNjCUvKlkSqV04X/arcgis/rest/servic
es

Hubbard
https://tiles.arcgis.com/tiles/auNjCUvKlkSqV04X/arcgis/rest/servi
ces
Isanti
https://gis.co.isanti.mn.us/arcgis/rest/services
Isanti
https://wfs.schneidercorp.com/arcgis/rest/services/IsantiCountyMN
_WFS/MapServer
Isanti
https://services6.arcgis.com/8oXJ0xFdajDkQ6Xz/arcgis/rest/servic
es
Isanti
https://tiles.arcgis.com/tiles/8oXJ0xFdajDkQ6Xz/arcgis/rest/servic
es
Itasca
https://maps.co.itasca.mn.us/arcgis/rest/services
Jackson
https://maps.co.jackson.mn.us/arcgis/rest/services
Table of contents disabled
Jackson
https://services6.arcgis.com/48kcymtZKUOOXIj8/ArcGIS/rest/ser
vices
Kanabec
https://wfs.schneidercorp.com/arcgis/rest/services/KanabecCounty
MN_WFS/MapServer
Kandiyohi
https://gis.kcmn.us/arcgis/rest/services
Kandiyohi
https://www.gismidwest.com/arcgis/rest/services/Kandiyohi
Kittson
Schneider Geospatial - ArcGIS server address is not public
Koochiching
https://services3.arcgis.com/8mdusDCY0WncdJVw/arcgis/rest/ser
vices
Lac qui Parle
Geomoose WMS
Lake
https://services1.arcgis.com/NlvHF2FHoAfPIDvG/arcgis/rest/servi
ces
Lake
https://tiles.arcgis.com/tiles/NlvHF2FHoAfPIDvG/arcgis/rest/servi
ces
Lake of The Woods
Schneider Geospatial - ArcGIS server address is not public
LeSueur
https://gis.co.le-sueur.mn.us/server/rest/services
LeSueur
https://wfs.schneidercorp.com/arcgis/rest/services/LeSueurCounty
MN_WFS/MapServer

## Page 237

Lincoln
Geomoose WMS
Lyon
https://services.arcgis.com/WSCKzjfnubMgUOk8/arcgis/rest/servi
ces
Lyon
https://tiles.arcgis.com/tiles/WSCKzjfnubMgUOk8/arcgis/rest/serv
ices
McLeod
WMS server
Mahnomen
https://services8.arcgis.com/eORKbx5CWReJmkoa/arcgis/rest/ser
vices
Mahnomen
https://tiles.arcgis.com/tiles/eORKbx5CWReJmkoa/arcgis/rest/serv
ices
Marshall
https://gismap.co.marshall.mn.us/arcgis/rest/services
Marshall
https://gis.co.marshall.mn.us/server/rest/services
Martin
Schneider Geospatial - ArcGIS server address is not public
Meeker
Schneider Geospatial - ArcGIS server address is not public
Mille Lacs
https://gis.co.mille-lacs.mn.us/arcgis/rest/services
Mille Lacs
https://services6.arcgis.com/msGTRvdwc9dcDoMX/ArcGIS/rest/s
ervices
Mille Lacs
https://tiles.arcgis.com/tiles/msGTRvdwc9dcDoMX/arcgis/rest/ser
vices
Morrison
Schneider Geospatial - ArcGIS server address is not public
Mower
https://gisweb.co.mower.mn.us/server/rest/services
Mower
https://services8.arcgis.com/WpaOptirDnb1fPwm/ArcGIS/rest/serv
ices
Murray
Geomoose WMS
Nicollet
Schneider Geospatial - ArcGIS server address is not public
Nobles
Schneider Geospatial - ArcGIS server address is not public
Norman
https://gismap.co.norman.mn.us/arcgis/rest/services
Norman
https://gismap.co.marshall.mn.us/arcgis/rest/services/Norman
Olmsted
https://gis.co.olmsted.mn.us/arcgis/rest/services
Olmsted
https://gweb01.co.olmsted.mn.us/arcgis/rest/services
Olmsted
https://services7.arcgis.com/tC18nF87RnYBtzwI/ArcGIS/rest/servi
ces

## Page 238

Olmsted
https://tiles.arcgis.com/tiles/tC18nF87RnYBtzwI/arcgis/rest/servic
es
Otter Tail
https://web2.co.ottertail.mn.us/arcgis/rest/services
Otter Tail
https://services3.arcgis.com/Pg1yLLk3jMuhxBKI/ArcGIS/rest/serv
ices
Otter Tail
https://tiles.arcgis.com/tiles/Pg1yLLk3jMuhxBKI/arcgis/rest/servic
es
Pennington
https://gismap.co.pennington.mn.us/arcgis/rest/services
Pennington
https://gismap.co.marshall.mn.us/arcgis/rest/services/Pennington
Pine
Schneider Geospatial - ArcGIS server address is not public
Pipestone
https://gis.pcmn.us/arcgis/rest/services
Pipestone
https://services6.arcgis.com/BmOPNud8bDJ12jtE/arcgis/rest/servi
ces
Pipestone
https://tiles.arcgis.com/tiles/BmOPNud8bDJ12jtE/arcgis/rest/servi
ces
Polk
https://gis.co.polk.mn.us/arcgis/rest/services
Table of contents disabled
Polk
https://services2.arcgis.com/O9tnbvDaQkJJ8hGN/ArcGIS/rest/ser
vices
Polk
https://tiles.arcgis.com/tiles/O9tnbvDaQkJJ8hGN/arcgis/rest/servic
es
Pope
https://gis.popecountymn.gov/arcgis/rest/services
Ramsey
https://maps.co.ramsey.mn.us/arcgis/rest/services
Ramsey
https://maps.co.ramsey.mn.us/ArcGIS/rest/services
Ramsey
https://services2.arcgis.com/527XtFVf9JKOTqu5/arcgis/rest/servic
es
Ramsey
https://tiles.arcgis.com/tiles/527XtFVf9JKOTqu5/arcgis/rest/servic
es
Red Lake
https://gismap.co.marshall.mn.us/arcgis/rest/services/RedLake
Redwood
Schneider Geospatial - ArcGIS server address is not public
Renville
https://gis.renvillecountymn.gov/arcgis/rest/services
Renville
https://services2.arcgis.com/bEOhwGpTpOM9eaNX/arcgis/rest/ser
vices
Rice
ArcGIS REST services are not public

## Page 239

Rock
WMS
Rose Creek
https://services8.arcgis.com/uwyqtf0if1YRrrx1/arcgis/rest/services
Roseau
https://gis.co.roseau.mn.us/arcgis/rest/services
Table of contents disabled
St. Louis
https://gis.stlouiscountymn.gov/server2/rest/services
St. Louis
https://gis.stlouiscountymn.gov/imgserver/rest/services

Scott
https://gis.co.scott.mn.us/arcgis/rest/services
Scott
          https://services.arcgis.com/DqIh9WAsIZcPlBEF/arcgis/rest/services
Scott
https://services8.arcgis.com/ktxC6HFuwsKFSbAV/ArcGIS/rest/ser
vices
Prior Lake - Spring Lake Watershed District
Sherburne
https://gis.co.sherburne.mn.us/arcgis/rest/services
Sherburne
https://gis.co.sherburne.mn.us/arcgis3/rest/services
Sherburne
https://services3.arcgis.com/A86cpFIY5mfMGCej/ArcGIS/rest/ser
vices
Sibley
https://gis.co.sibley.mn.us/arcgis/rest/services        SSL problem
Sibley
https://services1.arcgis.com/ca9pZxSKQMiPIqAL/ArcGIS/rest/ser
vices
Sibley
https://tiles.arcgis.com/tiles/ca9pZxSKQMiPIqAL/arcgis/rest/servi
ces
Stearns
https://gis.co.stearns.mn.us/arcgis/rest/services
Steele
https://services3.arcgis.com/PhDlW50qzuHSLgLK/arcgis/rest/serv
ices
Steele
https://tiles.arcgis.com/tiles/PhDlW50qzuHSLgLK/arcgis/rest/servi
ces
Stevens
https://gis.co.stevens.mn.us/arcgis/rest/services
Stevens
https://services2.arcgis.com/7iPhaYyq6PkRoVhV/ArcGIS/rest/ser
vices
Stewart
https://services.arcgis.com/VXD4EYDM1LKWq5HV/arcgis/rest/s
ervices
Swift
https://www.gismidwest.com/arcgis/rest/services/Swift
Swift
https://www.gismidwest.com/arcgis/rest/services/SwiftCounty
Todd
https://gis.mytoddcounty.com/toddcounty/rest/services
Traverse
https://gis.co.traverse.mn.us/arcgis/rest/services

## Page 240

Traverse
Wabasha
Schneider Geospatial - ArcGIS server address is not public
Wadena
https://gis.co.wadena.mn.us/arcgis/rest/services
Waseca
Schneider Geospatial - ArcGIS server address is not public
Washington
https://maps.co.washington.mn.us/arcgis/rest/services
Washington
https://services1.arcgis.com/3fjYPqJf7qalQMlb/arcgis/rest/services
Washington
https://tiles.arcgis.com/tiles/3fjYPqJf7qalQMlb/arcgis/rest/services
Watonwan
Schneider Geospatial - ArcGIS server address is not public
Wilkin
https://gisweb.co.wilkin.mn.us/arcgis/rest/services
Wilkin
https://services3.arcgis.com/24KKFNDTiXmntYMH/arcgis/rest/se
rvices       5-1-2025 no data
Winona
_ttps://web1.winonaco.com/arcgis/rest/services
dead link 1
Wright
https://web.co.wright.mn.us/arcgisserver/rest/services
Wright
https://services2.arcgis.com/CiQCvRGImIxsaFnM/arcgis/rest/servi
ces
Wright
https://tiles.arcgis.com/tiles/CiQCvRGImIxsaFnM/arcgis/rest/servi
ces
Yellow Medicine
https://gis.co.ym.mn.gov/arcgis/rest/services
Minnesota City, Town, Village, etc GIS Servers
There is something a bit odd here.  Many small towns appear to have an ArcGIS Online
account with what I think are three default layers to serve as examples.  Maybe there is a
state program that is funding those accounts.  I am including those links since perhaps at
some point some of those accounts will have useful data.
Adams
https://services6.arcgis.com/Rf7hXk2wqfpwo6qJ/ArcGIS/rest/serv
ices
Alden
https://services9.arcgis.com/nuFzRokPE7bUkoiz/ArcGIS/rest/servi
ces
Altura
https://services3.arcgis.com/Lex2p5tDOFHEz9gj/arcgis/rest/servic
es
Anoka
See Anoka County

## Page 241

Arden Hills
See Ramsey County
Askov
https://services2.arcgis.com/CnyHr4CxdG4Lvwbt/arcgis/rest/servi
ces
Aurora
https://services.arcgis.com/Ku3HX9hvZjhcqt90/arcgis/rest/services
Austin
https://services9.arcgis.com/iboXOCvm4DGtJZJG/ArcGIS/rest/ser
vices
Bellechester
https://services8.arcgis.com/z0zzSlw5eoqQ9F0W/arcgis/rest/servic
es
Birchwood Village
https://services5.arcgis.com/qvVUaUzEwaZTGf5j/ArcGIS/rest/ser
vices
Bloomington
https://gis.bloomingtonmn.gov/arcgis/rest/services
Bloomington
https://services6.arcgis.com/eXHnzGr3m1c2gSiA/ArcGIS/rest/ser
vices
Bloomington
https://tiles.arcgis.com/tiles/eXHnzGr3m1c2gSiA/arcgis/rest/servic
es
Brainerd
See Crow Wing County
Brooklyn Park
https://services1.arcgis.com/PNZiYeVBN73VJW7o/ArcGIS/rest/s
ervices
Brooklyn Park
https://tiles.arcgis.com/tiles/PNZiYeVBN73VJW7o/arcgis/rest/ser
vices
Browerville
https://services6.arcgis.com/M8iffIV4ZFFuwbBV/arcgis/rest/servi
ces
Burnsville
https://services5.arcgis.com/dsWKodDzlanHpGY2/ArcGIS/rest/ser
vices
Burnsville
https://tiles.arcgis.com/tiles/dsWKodDzlanHpGY2/arcgis/rest/servi
ces
Carlos
https://services8.arcgis.com/SNuwnYOflhOXRoSQ/arcgis/rest/ser
vices
Center City
https://services5.arcgis.com/fSfxeG0xW9BEwgdb/ArcGIS/rest/ser
vices
Chisago City
https://services3.arcgis.com/4NMrbHaBYK1nqBhv/arcgis/rest/ser
vices

## Page 242

Claremont
https://services8.arcgis.com/uXZPcO2CZLVuVG5v/arcgis/rest/ser
vices
Clements
https://services3.arcgis.com/eNzBteYwGCpeS9Oh/arcgis/rest/servi
ces
Coon Rapids
https://services5.arcgis.com/B4M0GvwRaKduZ9Wo/ArcGIS/rest/s
ervices
Coon Rapids
https://tiles.arcgis.com/tiles/B4M0GvwRaKduZ9Wo/arcgis/rest/ser
vices
Cottonwood
           https://services3.arcgis.com/sgh1gLt0IcH0Kzb9/arcgis/rest/services
Crosby
https://services6.arcgis.com/Fwt6JwzKSvuxJYmt/ArcGIS/rest/serv
ices
Detroit Lakes
Integritygis - ArcGIS server address is not public
Duluth
https://services.arcgis.com/DgKyOSWnVuXUe0Jp/arcgis/rest/serv
ices
Duluth
https://tiles.arcgis.com/tiles/DgKyOSWnVuXUe0Jp/arcgis/rest/ser
vices
Dunnell
https://services7.arcgis.com/wJjDPyVuNaQhXMe2/arcgis/rest/serv
ices
Eagan
https://gis.cityofeagan.com/arcgis/rest/services
Eagan
https://services1.arcgis.com/6KEQnrFDevRaxA3V/arcgis/rest/serv
ices
Eagle Lake
https://services9.arcgis.com/H2Ax0mzcd73FTvUB/arcgis/rest/serv
ices
Eden Prairie
https://gis.edenprairie.org/maps/rest/services
Eden Valley
https://services9.arcgis.com/LnW8sO9MvUucY0Hn/ArcGIS/rest/s
ervices
Ellendale
https://services8.arcgis.com/wZMAKiJBkZGFiANj/ArcGIS/rest/se
rvices
Elmore
https://services6.arcgis.com/61DaIUTuKJSHYUAB/ArcGIS/rest/s
ervices
Ely
https://services5.arcgis.com/RWK3pcEgu3ahFmCL/ArcGIS/rest/se
rvices

## Page 243

Empire
https://services3.arcgis.com/U948OQ2UEpqJgH70/arcgis/rest/serv
ices
Excelsior
https://services9.arcgis.com/ZiBRokjbmzeL227D/ArcGIS/rest/serv
ices
Fairfax
https://services9.arcgis.com/VnTQE68eMmFQUd9q/ArcGIS/rest/s
ervices
Fairmont
https://services6.arcgis.com/pfYVZeetxp5mgzO5\/arcgis/rest/servi
ces
Fairmont
https://tiles.arcgis.com/tiles/pfYVZeetxp5mgzO5/arcgis/rest/servic
es
Franklin
https://services6.arcgis.com/lomoDt4aa3jEg3Jp/arcgis/rest/services
Geneva
https://services3.arcgis.com/FfPtI7LaUG5QDDps/arcgis/rest/servic
es
Grand Meadow
https://services9.arcgis.com/gyK3uyJkTpZUG4Rd/arcgis/rest/servi
ces
Hampton
https://services3.arcgis.com/U948OQ2UEpqJgH70/arcgis/rest/serv
ices
Hanska
https://services2.arcgis.com/SAbqPztTpUkQ26i7/arcgis/rest/servic
es
Hayfield
https://services6.arcgis.com/OHDS3gFyChDBYuFd/arcgis/rest/ser
vices
Hill City
https://services2.arcgis.com/IRti1IzjEAkCnb88/arcgis/rest/services
Hinckley
https://services6.arcgis.com/ct7C8Kl9aGqzxP8V/ArcGIS/rest/servi
ces
Hokah
https://services8.arcgis.com/KT96CcjFbBElrBCZ/arcgis/rest/servic
es
Hollandale
https://services2.arcgis.com/rUXbIXwDrK9hxaUj/arcgis/rest/servi
ces
Hoyt Lakes
https://services3.arcgis.com/uP7asNK4Igh0XCmV/ArcGIS/rest/ser
vices

## Page 244

Ivanhoe
https://services2.arcgis.com/IoGKcpNyNjXkVjqU/arcgis/rest/servi
ces
Kenyon
https://services6.arcgis.com/DZRT5Xp8izxHwuPX/ArcGIS/rest/se
rvices
Kiester
https://services3.arcgis.com/MStjpubTscdJAUxy/arcgis/rest/servic
es
Lake City
https://arcgis.mobile311.com/arcgis/rest/services/Minnesota/CityO
fLakeCity/MapServer
Lake Crystal
https://services3.arcgis.com/ZjFWLlxTqN0pFua7/arcgis/rest/servic
es
Lakeville
https://services2.arcgis.com/lUR6upI2RKmjdugJ/ArcGIS/rest/servi
ces
Lakeville
https://tiles.arcgis.com/tiles/lUR6upI2RKmjdugJ/arcgis/rest/servic
es
Lanesboro
https://services9.arcgis.com/b3QaYjNvS1xM7ANx/ArcGIS/rest/se
rvices
Le Center
https://services1.arcgis.com/iMQnh9VVrtEGTTgR/arcgis/rest/serv
ices
Le Center
https://tiles.arcgis.com/tiles/iMQnh9VVrtEGTTgR/arcgis/rest/serv
ices
Le Sueur
           https://services.arcgis.com/w7IJAy3oT3LkA67y/arcgis/rest/services
Lester Prairie
https://services3.arcgis.com/YjcluNfmT8wGNtwk/arcgis/rest/servi
ces
Lewiston
https://services.arcgis.com/ocohsj0WeThFXNMW/arcgis/rest/servi
ces
Lindstrom
https://services7.arcgis.com/pd8ANYL84a98nzUX/arcgis/rest/serv
ices
Lindstrom
https://tiles.arcgis.com/tiles/pd8ANYL84a98nzUX/arcgis/rest/servi
ces
Little Falls
https://services3.arcgis.com/q9rik8Don3p98Q8m/arcgis/rest/servic
es
Long Prairie
https://services8.arcgis.com/qaZExL6PjG3sD5H8/arcgis/rest/servi
ces

## Page 245

Mabel
https://services6.arcgis.com/ChH6sHMioq3yf2Es/arcgis/rest/servic
es
Madison
https://services8.arcgis.com/ZVvZzE75mTJBsyZA/arcgis/rest/serv
ices
Madison Lake
https://services3.arcgis.com/Mv0B8cLwl3Fqj3Wp/ArcGIS/rest/ser
vices
Maple Grove
https://gis.maplegrovemn.gov/arcgis/rest/services
Maple Plain
https://services3.arcgis.com/iA7S73Vdig0Gn69X/ArcGIS/rest/serv
ices
Marble
https://services5.arcgis.com/QskAEX2pHKDjjwxW/ArcGIS/rest/s
ervices
Mazeppa
https://services5.arcgis.com/nQLOKDa0KwHwWTI1/ArcGIS/rest/
services
Minneapolis
https://eagsprod.ci.minneapolis.mn.us/arcgis/rest/services
Minneapolis
https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/servi
ces
Minneapolis
https://tiles.arcgis.com/tiles/afSMGVsC7QlRK1kZ/arcgis/rest/serv
ices
Minnetonka
https://services.arcgis.com/vAmq2qjze38HN5HF/arcgis/rest/servic
es
Minnetonka
https://tiles.arcgis.com/tiles/vAmq2qjze38HN5HF/arcgis/rest/servi
ces
Montgomery
https://services7.arcgis.com/xbGo5NvbuIXHD731/arcgis/rest/servi
ces
Montgomery
https://tiles.arcgis.com/tiles/xbGo5NvbuIXHD731/arcgis/rest/servi
ces
Montrose
https://services6.arcgis.com/VyIAktRTFeOGdJMO/arcgis/rest/serv
ices
Moorhead
https://services.arcgis.com/t2tplTEKxuL7eSvF/arcgis/rest/services
Moorhead
           https://tiles.arcgis.com/tiles/t2tplTEKxuL7eSvF/arcgis/rest/services
Morgan
           https://services3.arcgis.com/s5RJU55OFatftP26/arcgis/rest/services
Morton
https://services6.arcgis.com/L5SL0pQu7CVi7bWr/arcgis/rest/servi
ces

## Page 246

Morton
https://tiles.arcgis.com/tiles/L5SL0pQu7CVi7bWr/arcgis/rest/servi
ces
Mound
https://services8.arcgis.com/s2AmbaM5Siqr95vE/arcgis/rest/servic
es
New London
https://services9.arcgis.com/gCXI27oRJv8J1y6W/ArcGIS/rest/serv
ices
New Richland
https://services.arcgis.com/joqhuvtne8KVLZ48/arcgis/rest/services
Nicollet
https://services9.arcgis.com/6YgiahTKOAAST9YH/arcgis/rest/ser
vices
Northfield
https://gis.ci.northfield.mn.us/arcgis/rest/services
Oakdale
https://gis.ci.oakdale.mn.us/server/rest/services
Oakdale
https://services3.arcgis.com/OsRVJYCQQeln9HQP/ArcGIS/rest/s
ervices
Oakdale
https://tiles.arcgis.com/tiles/OsRVJYCQQeln9HQP/arcgis/rest/ser
vices
Oak Grove
https://services6.arcgis.com/f79xZ44vfYtaG5qt/arcgis/rest/services
Oak Grove
https://tiles.arcgis.com/tiles/f79xZ44vfYtaG5qt/arcgis/rest/services
Paynesville
https://services9.arcgis.com/jmVLD0efnIr7PhG7/arcgis/rest/servic
es
Pine River
https://services7.arcgis.com/6SKVt3m2tFSl2AkF/arcgis/rest/servic
es
Plainview
https://services7.arcgis.com/rGLYj2qaZKi4p4aW/arcgis/rest/servic
es
Red Wing
https://services3.arcgis.com/7ddsbiDMSCjGzyYI/arcgis/rest/servic
es
Red Wing
https://tiles.arcgis.com/tiles/7ddsbiDMSCjGzyYI/arcgis/rest/servic
es
Rochester
See also Olmsted County
Rochester
https://services1.arcgis.com/zC7pGkrIoR451W0i/ArcGIS/rest/serv
ices
Rochester
https://tiles.arcgis.com/tiles/zC7pGkrIoR451W0i/arcgis/rest/servic
es
Rosemount
https://rs-gis.ci.rosemount.mn.us/server/rest/services

## Page 247

Rosemount
https://services2.arcgis.com/g9tzqCz1E9uQq6Yy/ArcGIS/rest/serv
ices
Saint Anthony
https://services.arcgis.com/nD1JmvAORRtTorXS/arcgis/rest/servi
ces
Saint Bonifacius
https://services6.arcgis.com/0bqmtGqSECb2nCMz/arcgis/rest/serv
ices
St. James
__________
Saint Leo
https://services.arcgis.com/SNgTV8aGlXKMHd7T/arcgis/rest/serv
ices
St. Louis Park           https://services.arcgis.com/4lIwEMiZ9qRQrLvh/arcgis/rest/services

St. Paul
           https://services1.arcgis.com/9meaaHE3uiba0zr8/arcgis/rest/services
St. Paul
           https://tiles.arcgis.com/tiles/9meaaHE3uiba0zr8/arcgis/rest/services
Shakopee
https://services3.arcgis.com/XMlKSb5fLzy2Uagk/ArcGIS/rest/ser
vices
Shakopee
https://tiles.arcgis.com/tiles/XMlKSb5fLzy2Uagk/arcgis/rest/servic
es
Sherburn
https://services2.arcgis.com/Q2ZlPM0NbfMsTbAF/arcgis/rest/serv
ices
Silver Bay
https://services2.arcgis.com/J2zx8wapsMlGAUSq/ArcGIS/rest/ser
vices
Spring Park
https://services.arcgis.com/wDHaTgVOO0S0gECO/arcgis/rest/ser
vices
Spring Valley
https://services5.arcgis.com/BzN5ykp9QsEPpguL/ArcGIS/rest/ser
vices
Storden
https://services9.arcgis.com/fSHcwWj9gjhkhsXq/arcgis/rest/servic
es
Taylors Falls
https://services3.arcgis.com/hWJGQDUBTZgylShy/arcgis/rest/ser
vices
Thief River Falls
https://services6.arcgis.com/PZH7SMMue6M4l4UQ/ArcGIS/rest/s
ervices
Thief River Falls
https://tiles.arcgis.com/tiles/PZH7SMMue6M4l4UQ/arcgis/rest/ser
vices

## Page 248

Trimont
https://services3.arcgis.com/FsTvT16Obriyj2hv/arcgis/rest/services
Tyler
           https://services7.arcgis.com/pyFZzcCIxSJKrrpP/arcgis/rest/services
Utica
https://services3.arcgis.com/PsFrvdQQULCFTXcX/arcgis/rest/serv
ices
Vermillion
https://services5.arcgis.com/bjkRxHLah2muZgCc/arcgis/rest/servi
ces
Wabasha
https://services3.arcgis.com/GfXwj1Bv0GWbD5QP/ArcGIS/rest/s
ervices
Wabasso
https://services5.arcgis.com/hILfQTpFhkozHrmK/ArcGIS/rest/serv
ices
Waterville
https://services6.arcgis.com/ieQl20HI1ttvhWxu/arcgis/rest/services
Watkins
https://services3.arcgis.com/SkHVMakAzJ4cQxOt/ArcGIS/rest/ser
vices
Westbrook
https://services9.arcgis.com/EHlQEmHoj1lep2T3/arcgis/rest/servic
es
Westbrook
https://tiles.arcgis.com/tiles/EHlQEmHoj1lep2T3/arcgis/rest/servic
es
Welcome
           https://services9.arcgis.com/mdbalJcjPnD2wtJ2/arcgis/rest/services
Willernie
https://services6.arcgis.com/Ll6jBgmrWww9zMo1/arcgis/rest/serv
ices
Willmar
https://services3.arcgis.com/9lHFAdqL2IKmaKW4/arcgis/rest/serv
ices
Municipal Utilities Commission
Willmar
See also Kandiyohi county
Windom
https://services8.arcgis.com/Gw90jBZm8VXzA53X/ArcGIS/rest/s
ervices
Winnebago
https://services6.arcgis.com/y1jJmkOM3JMQxMqo/arcgis/rest/ser
vices
Winsted
https://services3.arcgis.com/tSJqWGqu8aqZHWiQ/arcgis/rest/serv
ices
Woodbury
https://gis.ci.woodbury.mn.us/webgis/rest/services     SSL problem

## Page 249

Mississippi State GIS Servers
Mississippi Open Data
Website: https://opendata.gis.ms.gov
Mississippi Geospatial Clearinghouse
Website: https://www.gis.ms.gov
Mississippi Automated Resource Information System (MARIS)
Website: https://maris.mississippi.edu
GIS: https://gis.mississippi.edu/server/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Mississippi Department of Environmental Quality
Website: https://www.deq.state.ms.us/
Might be slow
GIS: https://gis.deq.ms.gov/ArcGIS/rest/services
8-4-2023 No tiled data
GIS: https://opcgis.deq.state.ms.us/opcgis/rest/services
8-4-2023 No tiled data
Mississippi Department of Transportation
Website: https://mdot.ms.gov
GIS: https://www.gisonline.ms.gov/arcgis/rest/services
Parcel lines:  MDEQ/Download/MapServer/57
Parcel lines:  MDEQ/Viewer/MapServer/41
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Mississippi Department of Marine Resources
Website: https://dmr.ms.gov
GIS: https://gis.dmr.ms.gov/server/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Mississippi Emergency Management Agency
Website: https://www.msema.org
GIS: https://services1.arcgis.com/fI7ToVSY6ywRM8Si/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/fI7ToVSY6ywRM8Si/arcgis/rest/services
Mississippi Forestry Commission
Website: https://www.mfc.ms.gov

GIS: https://arcsrv.mfc.ms.gov/server/rest/services
8-4-2023 No tiled data
Mississippi Regional
Central Mississippi Planning and Development District
Website: https://www.cmpdd.org

## Page 250

GIS: https://gis.cmpdd.org/server/rest/services
8-4-2023 No tiled data
Southern Mississippi Planning and Development
Website: https://smpdd.com
GIS: Dead link removed
Mississippi County GIS Servers
Adams
WMS server
Alcorn
https://services7.arcgis.com/rctJwRL1kWp2v5Fa/ArcGIS/rest/serv
ices/AlcornMS_Service/FeatureServer
Amite
WMS server
Attala
WMS server
Benton
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/BentonService/FeatureServer
Chickasaw
https://services3.arcgis.com/wtSztI8X9HW88PUR/ArcGIS/rest/ser
vices/Chickasaw_Service/FeatureServer
Coahoma
https://www.efsedge.com/arcgis/rest/services/Coahoma_County
Copiah
https://gis.cmpdd.org/server/rest/services/Hosted/Copiah_County_
Feature_Layer/FeatureServer

DeSoto
https://maps.desotocountyms.gov/arcgis/rest/services
DeSoto
https://gis.desotocountyms.gov/arcgis/rest/services
DeSoto
https://services6.arcgis.com/4Zxj9BGpFPVGgwpo/ArcGIS/rest/ser
vices
Forrest
https://services8.arcgis.com/LORmbCB5yqZHgkD7/arcgis/rest/ser
vices
Grenada
https://services3.arcgis.com/YHsqEaxGSqCBZLEH/arcgis/rest/ser
vices
Hancock
WMS server
Harrison
https://geo.co.harrison.ms.us/server/rest/services
Harrison
https://services1.arcgis.com/HMvCOUg20YqJBIY9/ArcGIS/rest/s
ervices
Harrison
https://tiles.arcgis.com/tiles/HMvCOUg20YqJBIY9/arcgis/rest/ser
vices

## Page 251

Hinds
https://services3.arcgis.com/vv3YkTdKe8qzmf0Z/ArcGIS/rest/ser
vices/Hinds_Service/FeatureServer
Hinds
https://gis.cmpdd.org/server/rest/services/Hosted/Hinds_County_M
ap/FeatureServer
Holmes
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Holmes_Service/FeatureServer
Go to the top and search for ‘Holmes’
Jackson
https://webmap.co.jackson.ms.us/arcgis107/rest/services
Jasper
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/JasperService/FeatureServer
Jefferson
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Jefferson_Service/FeatureServer
Go to the top and search for ‘Jefferson’
Lafayette
https://services3.arcgis.com/Z8bz0UY32UcDoe6G/ArcGIS/rest/ser
vices/Lafayette_Service/FeatureServer
Lamar
WMS server
Lauderdale
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/LauderdaleService/FeatureServer
Lawrence
https://services3.arcgis.com/16eAx5Gb99bCfEGw/arcgis/rest/servi
ces/Lawrence_Service/FeatureServer
Leake
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/LeakeService/FeatureServer
Leake
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Leake_County_AddressPoints_Service/FeatureServer
Go to the top and search for ‘Leake’
Lee
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Lee_Service/FeatureServer
Go to the top and search for ‘Lee’
Leflore
https://services8.arcgis.com/LjOIwJPFdUCsqx6B/arcgis/rest/servic
es
Lincoln
          https://ags.agdmaps.com/arcgis/rest/services/LincolnMS/MapServer
Lincoln
https://lincoln.msmaps.org/arcgis/rest/services

## Page 252

Lowndes
https://services9.arcgis.com/IX0iMrnqj0M8ZIjn/ArcGIS/rest/servic
es/Lowndes_Service1/FeatureServer
Madison
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/Madison_Service/FeatureServer
Madison
https://gis.cmpdd.org/server/rest/services/Hosted/Madison_County
_Map/FeatureServer
Madison
https://gis.cmpdd.org/server/rest/services/Madison_County
Not open to public
Marion
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/MarionMS_Service/FeatureServer
Go to the top and search for ‘Marion’
Monroe
https://services3.arcgis.com/4AaqjZXP6VsiwqAE/arcgis/rest/servi
ces/MonroeMS_Service/FeatureServer
Neshoba
https://services5.arcgis.com/ZMdhv2O0udo61dNH/arcgis/rest/serv
ices/Neshoba_Service/FeatureServer
Newton
https://services3.arcgis.com/V4n00OYh74DKT1AA/arcgis/rest/ser
vices
Noxubee
https://services3.arcgis.com/dcmid0r7lFL6vKDX/arcgis/rest/servic
es
Oktibbeha
https://services3.arcgis.com/04ut98nBnbmQo8Q0/arcgis/rest/servi
ces/Oktibbeha_Service/FeatureServer
Pearl River
https://services6.arcgis.com/9h5t9CkNYcgSXrCh/ArcGIS/rest/serv
ices
Pike
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/PikeMS_Service/FeatureServer
Go to the top and search for ‘Pike’
Pontotoc
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Pontotoc_Service/FeatureServer
Go to the top and search for ‘Pontotoc’
Prentiss
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Prentiss_Service/FeatureServer
Go to the top and search for ‘Prentiss’
Quitman
https://www.efsedge.com/arcgis/rest/services/Quitman_County

## Page 253

Rankin
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Rankin_Service/FeatureServer
Go to the top and search for ‘Rankin’
Rankin
https://gis.cmpdd.org/server/rest/services/Hosted/Rankin_County_
Feature_Layer/FeatureServer
Simpson
https://services5.arcgis.com/Leo27bLmBYQ9pcCt/arcgis/rest/servi
ces/SimpsonService/FeatureServer
Simpson
https://gis.cmpdd.org/server/rest/services/Hosted/Simpson_County
_Feature_Layer/FeatureServer
Simpson
https://gis.cmpdd.org/server/rest/services/Hosted/Simpson_Health_
Feature_Layer/FeatureServer
Smith
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Smith_Service/FeatureServer
Go to the top and search for ‘Smith’
Stone
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/Stone_Service/FeatureServer
Tate
https://gis.cmpdd.org/server/rest/services/Hosted/Tate_County_Fea
ture_Layer/FeatureServer
Tippah
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/TippahService/FeatureServer
Tishomingo
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/Tishomingo_Service/FeatureServer
Tishomingo
https://services7.arcgis.com/deoj2Y8l1tBr7P5X/ArcGIS/rest/servic
es/Tishomingo_Zoning/FeatureServer
Union
https://services3.arcgis.com/nA9zIjStWYJO1Fiu/arcgis/rest/servic
es/UnionMS_Service/FeatureServer
Walthall
https://services3.arcgis.com/OqdQxdZa7T1cTgDz/arcgis/rest/servi
ces
Warren
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/WarrenService_911/FeatureServer
Go to the top and search for ‘Warren’
Warren
https://gis.cmpdd.org/server/rest/services/Hosted/Warren_County_
Feature_Layer/FeatureServer
Winston
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Winston_Service/FeatureServer
Go to the top and search for ‘Winston’

## Page 254

Yazoo
https://gis.cmpdd.org/server/rest/services/Hosted/Yazoo_County_F
eature_Layer/FeatureServer
Yazoo
https://gis.cmpdd.org/server/rest/services/Hosted/Yazoo_Co_Addr
ess_Ranges/FeatureServer
Mississippi City, Town, Village, etc GIS Servers
Bay St. Louis
WMS server
Biloxi
http://gis.biloxi.ms.us:6080/arcgis/rest/services
not https
Davis Island
WMS server
Diamondhead
See Hancock county
D’Iberville
WMS server

Gulfport
https://maps.gulfport-ms.gov/arcgis/rest/services
Gulfport
https://services1.arcgis.com/pOPaG0zaJUnBvD2F/ArcGIS/rest/ser
vices
Louisville
__________
Ocean Springs
WMS server
Oxford
https://services3.arcgis.com/HJKXwJwr6cXL7ioD/ArcGIS/rest/ser
vices
Southhaven
See DeSoto County
Vicksburg
WMS server
Yazoo City
https://gis.cmpdd.org/server/rest/services/Hosted/Yazoo_City_Feat
ure_Layer/FeatureServer
Yazoo City
https://gis.cmpdd.org/server/rest/services/Hosted/Yazoo_City_Tran
sportation_Plan/FeatureServer
Missouri State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Missouri Data Portal
Website: https://data.mo.gov/
GIS: https://gis.mo.gov/arcgis/rest/services
Missouri Office of Geospatial Information

## Page 255

Website:
https://oa.mo.gov/information-technology-itsd/it-governance/office-geospa
tial-information
GIS: https://services2.arcgis.com/kNS2ppBA4rwAQQZy/ArcGIS/rest/services
GIS: https://services6.arcgis.com/r9ddpXHABk7voAmS/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/r9ddpXHABk7voAmS/arcgis/rest/services
Missouri State Emergency Management Agency
Website: https://sema.dps.mo.gov
GIS: https://services2.arcgis.com/jWXb6JPWtBjOCalT/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/jWXb6JPWtBjOCalT/arcgis/rest/services
Missouri Department of Conservation
Website: https://mdc.mo.gov/
GIS: https://gisblue.mdc.mo.gov/arcgis/rest/services
8-4-2023 No tiled data
Department of Natural Resources
Website: https://dnr.mo.gov
GIS: https://gis.dnr.mo.gov/host/rest/services
GIS: https://gis.dnr.mo.gov/server/rest/services
GIS: https://services8.arcgis.com/RPgcHScWtnrsNIP7/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/RPgcHScWtnrsNIP7/arcgis/rest/services
Missouri Department of Transportation
Website: https://www.modot.org
GIS: https://mapping.modot.org/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://mappingsit2ext.modot.mo.gov/arcgis/rest/services
Missouri Department of Health and Senior Services
Website: https://health.mo.gov
GIS: https://services6.arcgis.com/Bd4MACzvEukoZ9mR/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Bd4MACzvEukoZ9mR/arcgis/rest/services
University of Missouri Spatial Data Information Service
Website: https://msdis.missouri.edu
GIS: https://moimagery.missouri.edu/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://stateimagery.msdis.missouri.edu/arcgis/rest/services
Lots of aerial photos.
https://images.integritygis.com/arcgis/rest/services/MO
Metropolitan Saint Louis Transit Agency
Website: https://www.metrostlouis.org
GIS: https://services2.arcgis.com/ZV8Mb62EedSw2aTU/ArcGIS/rest/services

## Page 256

GIS: https://tiles.arcgis.com/tiles/ZV8Mb62EedSw2aTU/arcgis/rest/services
Missouri Regional
Southeast Missouri Regional Planning Commission
Website: https://www.semorpc.org
GIS: https://maps.semogis.com/server/rest/services      Has layers for various jurisdictions
Missouri County GIS Servers
All counties are listed
Adair
Integritygis - ArcGIS server address is not public
Andrew
Integritygis - ArcGIS server address is not public
Atchison
Integritygis - ArcGIS server address is not public
Audrain
Integritygis - ArcGIS server address is not public
Barry
Custom tile server
Barton
WMS server
Bates
____________
Benton
____________
Bollinger
____________
Boone
https://gis.showmeboone.com/arcgis/rest/services

Table of contents disabled
Buchanan
Integritygis - ArcGIS server address is not public
Butler
Integritygis - ArcGIS server address is not public
Caldwell
____________
Callaway
https://services7.arcgis.com/SjRufDd1cFK2SuD3/arcgis/rest/servic
es
Callaway
https://tiles.arcgis.com/tiles/SjRufDd1cFK2SuD3/arcgis/rest/servic
es
Camden
____________
Cape Girardeau
See Southeast Missouri Regional Planning Commission (above)

## Page 257

Cape Girardeau
https://gis.capecounty.us/arcgis/rest/services
Cape Girardeau
https://services3.arcgis.com/iGXvjlKTUcBWNV3d/ArcGIS/rest/se
rvices
Cape Girardeau
https://tiles.arcgis.com/tiles/iGXvjlKTUcBWNV3d/arcgis/rest/serv
ices
Carroll
____________
Carter
____________
Cass
____________
Cedar
____________
Chariton
____________
Christian
____________
Clark
____________
Clay
https://services7.arcgis.com/3c8lLdmDNevrTlaV/ArcGIS/rest/serv
ices
Clinton
____________
Cole
https://www.midmogis.org/server/rest/services

Table of contents disabled
Cooper
____________
Crawford
____________
Dade
____________
Dallas
____________
Daviess
Integritygis - ArcGIS server address is not public
DeKalb
____________
Dent
____________
Douglas
Integritygis - ArcGIS server address is not public
Dunklin
https://services4.integritygis.com/arcgis/rest/services/MO/Dunklin
_Assessor_Data/MapServer
Not open to public

## Page 258

Dunklin
https://images.integritygis.com/arcgis/rest/services/MO/Dunklin_P
hotography_2015/ImageServer
Dunklin
Integritygis - ArcGIS server address is not public
Franklin
____________
Gasconade
Integritygis - ArcGIS server address is not public
Gentry
Integritygis - ArcGIS server address is not public
Greene
Integritygis - ArcGIS server address is not public
Grundy
____________
Harrison
____________
Henry
Integritygis - ArcGIS server address is not public
Hickory
____________
Holt
____________
Howard
____________
Howell
____________
Iron
See Southeast Missouri Regional Planning Commission (above)
Jackson
https://jcgis.jacksongov.org/arcgis/rest/services
Jackson
https://services3.arcgis.com/4LOAHoFXfea6Y3Et/ArcGIS/rest/ser
vices
Jackson
https://tiles.arcgis.com/tiles/4LOAHoFXfea6Y3Et/arcgis/rest/servi
ces
Jasper
https://wfs.schneidercorp.com/arcgis/rest/services/JasperCountyM
O_WFS4326/MapServer
Jasper
https://wfs.schneidercorp.com/arcgis/rest/services/JasperCountyM
O_WFS/MapServer
Jasper
https://services6.arcgis.com/f6278XvXrNz6PmsX/ArcGIS/rest/ser
vices
Jasper
https://tiles.arcgis.com/tiles/f6278XvXrNz6PmsX/arcgis/rest/servi
ces
Jefferson
https://services1.arcgis.com/Sfc8glAOQGBwsYa4/arcgis/rest/servi
ces

## Page 259

Jefferson
https://tiles.arcgis.com/tiles/Sfc8glAOQGBwsYa4/arcgis/rest/servi
ces
Johnson
Integritygis - ArcGIS server address is not public
Knox
____________
Laclede
Integritygis - ArcGIS server address is not public
Lafayette
Integritygis - ArcGIS server address is not public
Lawrence
____________
Lewis
____________
Lincoln
Integritygis - ArcGIS server address is not public
Linn
Integritygis - ArcGIS server address is not public
Livingston
____________
McDonald
____________
Macon
Integritygis - ArcGIS server address is not public
Madison
See Southeast Missouri Regional Planning Commission (above)
Maries
Integritygis - ArcGIS server address is not public
Marion
Integritygis - ArcGIS server address is not public
Mercer
____________
Miller
Integritygis - ArcGIS server address is not public
Mississippi
Integritygis - ArcGIS server address is not public
Moniteau
Integritygis - ArcGIS server address is not public
Monroe
____________
Montgomery
Integritygis - ArcGIS server address is not public
Morgan
Integritygis - ArcGIS server address is not public
New Madrid
____________

## Page 260

Newton
____________
Nodaway
____________
Oregon
Integritygis - ArcGIS server address is not public
Osage
Integritygis - ArcGIS server address is not public
Ozark
____________
Pemiscot County
____________
Perry
See Southeast Missouri Regional Planning Commission (above)
Pettis
____________
Phelps
Integritygis - ArcGIS server address is not public
Pike
____________
Platte
____________
Polk
____________
Pulaski
____________
Putnam
Integritygis - ArcGIS server address is not public
Ralls
____________
Randolph
____________
Ray
____________
Reynolds
____________
Ripley
Integritygis - ArcGIS server address is not public
St. Charles
https://gis.sccmo.org/scc_gis/rest/services
St. Clair
Integritygis - ArcGIS server address is not public
Ste. Genevieve
See Southeast Missouri Regional Planning Commission (above)
St. Francois
See Southeast Missouri Regional Planning Commission (above)

## Page 261

St. Louis
https://maps.stlouisco.com/hosting/rest/services
St. Louis
https://services2.arcgis.com/w657bnjzrjguNyOy/ArcGIS/rest/servi
ces
St. Louis
           https://tiles.arcgis.com/tiles/w657bnjzrjguNyOy/arcgis/rest/services
St. Louis
https://services6.arcgis.com/wkbq75VVf2MvUvs7/ArcGIS/rest/ser
vices
Election board
St. Louis City County
Saline
____________
Schuyler
____________
Scotland
____________
Scott
See Southeast Missouri Regional Planning Commission (above)
Shannon
____________
Shelby
____________
Stoddard
____________
Stone
Integritygis - ArcGIS server address is not public
Sullivan
Integritygis - ArcGIS server address is not public
Taney
____________
Texas
____________
Vernon
Integritygis - ArcGIS server address is not public
Warren
Integritygis - ArcGIS server address is not public
Washington
See Southeast Missouri Regional Planning Commission (above)
Wayne
____________
Webster
Integritygis - ArcGIS server address is not public
Worth
____________

Wright
____________
Missouri City, Town, Village, etc GIS Servers

## Page 262

Albany
Integritygis - ArcGIS server address is not public
Bloomsdale
See Southeast Missouri Regional Planning Commission (above)
Blue Springs
https://services6.arcgis.com/gZ3VxPnluEA1r99L/ArcGIS/rest/serv
ices
Bonne Terre
See Southeast Missouri Regional Planning Commission (above)
Branson
https://gis.bransonmo.gov/application/rest/services
Branson
https://gis.bransonmo.gov/webgis/rest/services
Branson
https://services2.arcgis.com/NIkzUpjDtspiBG0j/ArcGIS/rest/servic
es
Branson
https://tiles.arcgis.com/tiles/NIkzUpjDtspiBG0j/arcgis/rest/services
Brookfield
Integritygis - ArcGIS server address is not public
Cameron
Integritygis - ArcGIS server address is not public
Cape Girardeau
https://arcgis.cityofcapegirardeau.org:6443/arcgis/rest/services
Table of contents disabled
Carthage
https://services.integritygis.com/arcgis/rest/services/Public/Carthag
e_SEMS_Basemap/MapServer
Chesterfield
https://mapping.chesterfield.mo.us/arcgis/rest/services
Table of contents disabled
Chillicothe
Integritygis - ArcGIS server address is not public
Columbia
https://gis.gocolumbiamo.com/arcgis/rest/services
Columbia
https://services.arcgis.com/GHhNHT1xiCkCAXvo/arcgis/rest/serv
ices
Columbia
https://tiles.arcgis.com/tiles/GHhNHT1xiCkCAXvo/arcgis/rest/ser
vices
Deslogel
See Southeast Missouri Regional Planning Commission (above)
Fredericktown
See Southeast Missouri Regional Planning Commission (above)
Frontenac
Integritygis - ArcGIS server address is not public
Gordonville
See Southeast Missouri Regional Planning Commission (above)
Grain Valley
___________

## Page 263

Higginsville
Integritygis - ArcGIS server address is not public
Independence
See also Jackson County
Independence
https://services.arcgis.com/sbDzK061dd6DNPHv/arcgis/rest/servic
es
Independence
https://tiles.arcgis.com/tiles/sbDzK061dd6DNPHv/arcgis/rest/servi
ces
Ironton
See Southeast Missouri Regional Planning Commission (above)
Jackson
See Southeast Missouri Regional Planning Commission (above)
Jefferson City
See also Cole County

Jefferson City
https://services6.arcgis.com/rXa0aMElf2BPjgBA/ArcGIS/rest/serv
ices
Jefferson City
https://tiles.arcgis.com/tiles/rXa0aMElf2BPjgBA/arcgis/rest/servic
es
Joplin
           https://services1.arcgis.com/5olyYd7fCfTTiVp8/arcgis/rest/services
Joplin
           https://tiles.arcgis.com/tiles/5olyYd7fCfTTiVp8/arcgis/rest/services
Kansas City
https://mapd.kcmo.org/kcgis/rest/services
Table of contents disabled
Kansas City
https://services.arcgis.com/4o5uMWTHuOhUVJPd/arcgis/rest/serv
ices
Kansas City
https://tiles.arcgis.com/tiles/4o5uMWTHuOhUVJPd/arcgis/rest/ser
vices
Kearney
Integritygis - ArcGIS server address is not public
Kirksville
Integritygis - ArcGIS server address is not public
Kirkwood
https://gis.kirkwoodmo.org/arcgis/rest/services
Ladue
Integritygis - ArcGIS server address is not public
Lake Tishomingo
See Southeast Missouri Regional Planning Commission (above)
Lamar
Integritygis - ArcGIS server address is not public
Liberty
https://maps.libertymo.gov/arcgis/rest/services
Table of contents disabled
Liberty
           https://services.arcgis.com/70vcD5tpfNSJmyxA/arcgis/rest/services
Liberty
https://tiles.arcgis.com/tiles/70vcD5tpfNSJmyxA/arcgis/rest/servic
es

## Page 264

Macon
Integritygis - ArcGIS server address is not public
Marceline
Integritygis - ArcGIS server address is not public
Marshfield
Integritygis - ArcGIS server address is not public
Memphis
Integritygis - ArcGIS server address is not public
Moberly
Integritygis - ArcGIS server address is not public
Neosho
Integritygis - ArcGIS server address is not public
Oak Grove
Integritygis - ArcGIS server address is not public
Oak Ridge
See Southeast Missouri Regional Planning Commission (above)
Park Hills City
See Southeast Missouri Regional Planning Commission (above)
Perryville City
See Southeast Missouri Regional Planning Commission (above)
Pilot Knob
See Southeast Missouri Regional Planning Commission (above)
Plattsburg
Integritygis - ArcGIS server address is not public
Pleasant Hill
Integritygis - ArcGIS server address is not public
Republic
https://maps.republicmo.com/arcgis/rest/services
Raytown
Integritygis - ArcGIS server address is not public
St. Charles
https://services.arcgis.com/p44fQSGBTnSRR4hh/arcgis/rest/servic
es
St. Charles
https://tiles.arcgis.com/tiles/p44fQSGBTnSRR4hh/arcgis/rest/servi
ces
St. James
Integritygis - ArcGIS server address is not public
St Joseph
Integritygis - ArcGIS server address is not public
St. Louis
https://stlgis.stlouis-mo.gov/arcgis/rest/services
St. Louis
https://maps6.stlouis-mo.gov/arcgis/rest/services
Some folders are public facing and some require a login.
St. Louis
https://services6.arcgis.com/HZXbCkpCSqbGd0vK/ArcGIS/rest/se
rvices
St. Louis
https://tiles.arcgis.com/tiles/HZXbCkpCSqbGd0vK/arcgis/rest/serv
ices

## Page 265

St. Mary
See Southeast Missouri Regional Planning Commission (above)
Ste. Genevieve
See Southeast Missouri Regional Planning Commission (above)
Savannah
Integritygis - ArcGIS server address is not public
Sedalia
Integritygis - ArcGIS server address is not public
Sikeston
Integritygis - ArcGIS server address is not public
Springfield
Integritygis - ArcGIS server address is not public
Springfield
https://maps.springfieldmo.gov/arcgis/rest/services
Table of contents disabled
Springfield
https://services1.arcgis.com/aOss8CrQf3pARS5q/ArcGIS/rest/serv
ices
Springfield
https://tiles.arcgis.com/tiles/aOss8CrQf3pARS5q/arcgis/rest/servic
es
Tipton
Integritygis - ArcGIS server address is not public
Trenton
Integritygis - ArcGIS server address is not public
Vandalia
Integritygis - ArcGIS server address is not public
Wentzville
https://services2.arcgis.com/PhrOBa64VhLxWQwF/ArcGIS/rest/s
ervices
Wentzville
https://tiles.arcgis.com/tiles/PhrOBa64VhLxWQwF/arcgis/rest/ser
vices
West Plains
https://gis.westplains.net/arcgis/rest/services
West Plains
https://services5.arcgis.com/vlbfeUFWgxfykYSC/ArcGIS/rest/serv
ices
Montana State GIS Servers
Montana Geographic Information Clearinghouse
Website: https://geoinfo.msl.mt.gov/data
GIS: https://gisservicemt.gov/arcgis/rest/services
Parcel lines:  DOR/WebMerc_Parcels/MapServer/0
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Montana Department of Natural Resources and Conservation
Website: https://dnrc.mt.gov
GIS: https://gis.dnrc.mt.gov/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://gis.dnrc.mt.gov/imagery/rest/services

## Page 266

Montana Department of Transportation
Website: https://www.mdt.mt.gov
GIS: https://app.mdt.mt.gov/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://gisservicemt.gov/arcgis/rest/services
GIS: https://services1.arcgis.com/dKlvxNSUvl36IGMp/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/dKlvxNSUvl36IGMp/arcgis/rest/services
Montana Department of Commerce
Website: https://commerce.mt.gov
GIS: https://services.arcgis.com/iTQUx5ZpNUh47Geb/arcgis/rest/services
Montana Fish, Wildlife and Parks
Website: https://fwp.mt.gov
GIS: https://fwp-gis.mt.gov/arcgis/rest/services
8-4-2023 No tiled data
Montana Bureau of Mines and Geology
Website: https://www.mbmg.mtech.edu
GIS: https://mbmgmap.mtech.edu/server/rest/services
8-4-2023 No tiled data
GIS: https://services1.arcgis.com/WzgaGdfxzjVsajbb/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/WzgaGdfxzjVsajbb/arcgis/rest/services
Montana Department of Environmental Quality
Website: https://deq.mt.gov
GIS: https://gis.mtdeq.us/hosting/rest/services
8-4-2023 No tiled data
GIS: https://gis.mtdeq.us/mapping/rest/services
GIS: https://services3.arcgis.com/W9iqPyJhy06cNrrs/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/W9iqPyJhy06cNrrs/arcgis/rest/services
Montana Departmentof Public Health and Human Services
Website: https://dphhs.mt.gov
GIS: https://services3.arcgis.com/juqcZ3KnfEqg8N1S/ArcGIS/rest/services
Montana various layers
GIS: https://services.arcgis.com/qnjIrwR8z5Izc0ij/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/qnjIrwR8z5Izc0ij/arcgis/rest/services
GIS: https://services1.arcgis.com/ERdCHt0sNM6dENSD/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/ERdCHt0sNM6dENSD/arcgis/rest/services
GIS: https://services2.arcgis.com/DRQySz3VhPgOv7Bo/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/DRQySz3VhPgOv7Bo/arcgis/rest/services
Montana County GIS Servers

## Page 267

Blaine
https://services.arcgis.com/fYeFHi4UCpNh5pxM/arcgis/rest/servic
es
Cascade
https://services7.arcgis.com/JtiGtls94CNeeD7u/ArcGIS/rest/servic
es
Flathead
https://maps.flathead.mt.gov/server/rest/services
Flathead
https://services5.arcgis.com/K08Ti8IHU6QaR33e/ArcGIS/rest/ser
vices
Gallatin
https://gis.gallatin.mt.gov/arcgis/rest/services
Lewis and Clark
See Helena
Missoula
https://gis.missoulacounty.us/arcgis/rest/services
Missoula
https://services1.arcgis.com/NQWYt9dWr9BlL9QE/arcgis/rest/ser
vices
Missoula
https://tiles.arcgis.com/tiles/NQWYt9dWr9BlL9QE/arcgis/rest/ser
vices
Park
https://services3.arcgis.com/De8iY1SoM3l4PKku/ArcGIS/rest/ser
vices
Park
https://tiles.arcgis.com/tiles/De8iY1SoM3l4PKku/arcgis/rest/servic
es
Yellowstone
https://gis.yellowstonecountymt.gov/arcgis/rest/services
Montana City, Town, Village, etc GIS Servers
Billings
https://billingsgis.com/arcgis_public/rest/services
Bozeman
https://gisweb.bozeman.net/arcgis/rest/services
Bozeman
https://gisweb.bozeman.net/image/rest/services
Bozeman
https://gisweb.bozeman.net/hosted/rest/services
Bozeman
https://services3.arcgis.com/f4hk1qcfxRJ0L2BU/arcgis/rest/services
Bozeman
          https://tiles.arcgis.com/tiles/f4hk1qcfxRJ0L2BU/arcgis/rest/services

Helena
https://helenamontanamaps.org/arcgisadp/rest/services
Data sharing with Lewis and Clark County
Kalispell
https://services6.arcgis.com/o8tYBvi7zCbkyszZ/ArcGIS/rest/servi
ces
Kalispell
           https://tiles.arcgis.com/tiles/o8tYBvi7zCbkyszZ/arcgis/rest/services
Livingston
See Park County
Missoula
https://missoulamaps.ci.missoula.mt.us/arcgis/rest/services

## Page 268

Missoula
https://services.arcgis.com/HfwHS0BxZBQ1E5DY/arcgis/rest/serv
ices
Missoula
https://tiles.arcgis.com/tiles/HfwHS0BxZBQ1E5DY/arcgis/rest/ser
vices
Nebraska State GIS Servers
Nebraska Open Data
Website: https://www.nebraska.gov/government/open-data
Nebraska Department of Transportation
Web site: https://dot.nebraska.gov
GIS: https://giscat.ne.gov/agency/rest/services
8-4-2023 No tiled data
Nebraska Game and Parks Commission
Web site: https://outdoornebraska.gov
GIS: https://services5.arcgis.com/IOshH1zLrIieqrNk/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/IOshH1zLrIieqrNk/arcgis/rest/services
Nebraska Department of Environment and Energy
Website: http://www.deq.state.ne.us
not https
GIS: https://gis2.gisworkshop.com/arcgis/rest/services/DEQ/MapServer
Table of contents disabled
Parcel lines:  Statewide_NE_MGMT/MapServer/0
8-4-2023 No tiled data
Nebraska Public Power District (NPPD)
Website: https://www.nppd.com
GIS:
https://gis2.gisworkshop.com/arcgis/rest/services/Nebraska_Public_Power_Distric
t_NE_MGMT/MapServer
Table of contents disabled
8-4-2023 No tiled data
Central Platte Natural Resources District
Website: https://cpnrd.org
GIS:
https://gis3.gisworkshop.com/arcgis/rest/services/CPNRD_WaterBanking/MapSer
ver
Table of contents disabled
8-4-2023 No tiled data
Upper Elkhorn Natural Resource District
Website: https://www.uenrd.org
GIS: https://gis2.gisworkshop.com/arcgis/rest/services/UENRD/MapServer
Table of contents disabled
8-4-2023 No tiled data
Upper Republican Natural Resources District

## Page 269

Website:
https://www.urnrd.org
GIS: https://gis2.gisworkshop.com/arcgis/rest/services/URNRD/MapServer
Table of contents disabled
8-4-2023 No tiled data
Middle Republican Natural Resource District
Website: https://www.mrnrd.org
GIS:
https://gis2.gisworkshop.com/arcgis/rest/services/MiddleRepublicanNRDsub/Map
Server
Table of contents disabled
8-4-2023 No tiled data
GIS:
https://gis2.gisworkshop.com/arcgis/rest/services/MiddleRepublicanNRD/MapSer
ver
Table of contents disabled
8-4-2023 No tiled data
Nebraska various layers
GIS: https://gis.ne.gov/Enterprise/rest/services
Table of contents disabled
8-4-2023 No tiled data
GIS: https://gis.ne.gov/agency/rest/services
Table of contents disabled
GIS: https://gis.ne.gov/image/rest/services
Table of contents disabled
GIS:
https://gis2.gisworkshop.com/arcgis/rest/services/Statewide_NE_MGMT/MapSer
ver
Table of contents disabled
8-4-2023 No tiled data
GIS: https://services1.arcgis.com/Sj9eBhzWwOMzQCfI/ArcGIS/rest/services
GIS: https://services4.arcgis.com/erGCd11dHpRk1LWW/arcgis/rest/services
Nebraska County GIS Servers
Special note:  Unfortunately the ArcGIS servers at gis3.gworks (counties and cities) and
gis2.gworks (counties) do *not* use a folder for each jurisdiction.  As a result, the top of the
table of contents for these servers have multiple entries for each county and city.  IMHO, this is a
goofy way to organize data on a server.
    Counties:  This county section includes one or two links for each county on these two servers.
Not all county links are shown below since there is a greeat deal of duplication in the layers
within each folder.
Adams
https://gis.adamscounty.org/arcgis/rest/services
Antelope
https://mapserver01.gworks.com/arcgis/rest/services/Antelope_Co
unty_NE_Assessor/MapServer

Go to the top and search for ‘Antelope’
Arthur
https://mapserver01.gworks.com/arcgis/rest/services/Arthur_Count
y_NE_Assessor/MapServer

Go to the top and search for ‘Arthur’
Banner
https://mapserver01.gworks.com/arcgis/rest/services/Banner_Coun
ty_NE_Assessor/MapServer

## Page 270

Go to the top and search for ‘Banner’
Blaine
https://mapserver01.gworks.com/arcgis/rest/services/Blaine_Count
y_NE_Assessor/MapServer

Go to the top and search for ‘Blaine’
Boone
https://mapserver01.gworks.com/arcgis/rest/services/Boone_Count
y_NE_Assessor/MapServer

Go to the top and search for ‘Boone’
Box Butte
https://mapserver01.gworks.com/arcgis/rest/services/Box_Butte_C
ounty_NE_Assessor/MapServer

Go to the top and search for ‘Box_Butte’
Boyd
https://mapserver01.gworks.com/arcgis/rest/services/Boyd_County
_NE_Assessor/MapServer

Go to the top and search for ‘Boyd’
Brown
https://mapserver01.gworks.com/arcgis/rest/services/Brown_Count
y_NE_Assessor/MapServer

Go to the top and search for ‘Brown’
Buffalo
https://mapserver01.gworks.com/arcgis/rest/services/Buffalo_Coun
ty_NE_Assessor/MapServer

Go to the top and search for ‘Buffalo’
Burt
https://mapserver01.gworks.com/arcgis/rest/services/Burt_County_
NE_Assessor/MapServer

Go to the top and search for ‘Burt’
Butler
https://mapserver01.gworks.com/arcgis/rest/services/Butler_Count
y_NE_Assessor/MapServer

Go to the top and search for ‘Butler’
Cass
https://mapserver01.gworks.com/arcgis/rest/services/Cass_County
_NE_Assessor/MapServer

Go to the top and search for ‘Cass’
Cass
https://services3.arcgis.com/oIhWXTph9P1clNT3/arcgis/rest/servi
ces
Cass
https://tiles.arcgis.com/tiles/oIhWXTph9P1clNT3/arcgis/rest/servi
ces
Cedar
https://mapserver01.gworks.com/arcgis/rest/services/Cedar_Count
y_NE_Assessor/MapServer

Go to the top and search for ‘Cedar’

## Page 271

Chase
https://mapserver01.gworks.com/arcgis/rest/services/Chase_Count
y_NE_Assessor/MapServer

Go to the top and search for ‘Chase’
Cherry
They have GIS but not public ArcGIS
Cheyenne
https://mapserver01.gworks.com/arcgis/rest/services/Cheyenne_Co
unty_NE_Assessor/MapServer

Go to the top and search for ‘Cheyenne’
Clay
https://mapserver01.gworks.com/arcgis/rest/services/Clay_County
_NE_Assessor/MapServer
Go to the top and search for ‘Clay’
Colfax
https://gis3.gworks.com/arcgis/rest/services/Colfax_County_NE_A
ssessor_Sub/MapServer
Table of contents disabled
Colfax
https://gis3.gworks.com/arcgis/rest/services/Colfax_County_NE_P
Z_Sub/MapServer
Table of contents disabled
Cuming
https://mapserver01.gworks.com/arcgis/rest/services/Cuming_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Cuming’
Custer
https://mapserver01.gworks.com/arcgis/rest/services/Custer_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Custer’
Dakota
https://mapserver01.gworks.com/arcgis/rest/services/Dakota_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Dakota’
Dawes
https://mapserver01.gworks.com/arcgis/rest/services/Dawes_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Dawes’
Dawson
https://mapserver01.gworks.com/arcgis/rest/services/Dawson_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Dawson’
Deuel
https://mapserver01.gworks.com/arcgis/rest/services/Deuel_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Deuel’
Dixon
https://mapserver01.gworks.com/arcgis/rest/services/Dixon_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Dixon’

## Page 272

Dodge
https://mapserver01.gworks.com/arcgis/rest/services/Dodge_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Dodge’
Douglas
https://gis.dogis.org/arcgis/rest/services
Douglas
https://services.arcgis.com/pDAi2YK0L0QxVJHj/arcgis/rest/servic
es
Douglas
https://tiles.arcgis.com/tiles/pDAi2YK0L0QxVJHj/arcgis/rest/servi
ces
Dundy
https://mapserver01.gworks.com/arcgis/rest/services/Dundy_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Dundy’
Fillmore
https://mapserver01.gworks.com/arcgis/rest/services/Fillmore_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Fillmore’
Franklin
https://mapserver01.gworks.com/arcgis/rest/services/Franklin_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Franklin’
Frontier
https://mapserver01.gworks.com/arcgis/rest/services/Frontier_Cou
nty_NE_Clerk/MapServer
Go to the top and search for ‘Frontier’
Furnas
https://mapserver01.gworks.com/arcgis/rest/services/Furnas_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Furnas’
Gage
https://mapserver01.gworks.com/arcgis/rest/services/Gage_County
_NE_Assessor/MapServer
Go to the top and search for ‘Gage’
Garden
https://mapserver01.gworks.com/arcgis/rest/services/Garden_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Garden’
Garfield
https://mapserver01.gworks.com/arcgis/rest/services/Garfield_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Garfield’
Gosper
https://mapserver01.gworks.com/arcgis/rest/services/Gosper_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Gosper’

## Page 273

Grant
https://mapserver01.gworks.com/arcgis/rest/services/Grant_County
_NE_Assessor/MapServer
Go to the top and search for ‘Grant’
Greeley
https://mapserver01.gworks.com/arcgis/rest/services/Greeley_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Greeley’
Hamilton
https://mapserver01.gworks.com/arcgis/rest/services/Hamilton_Co
unty_NE_Assessor/MapServer
Go to the top and search for ‘Hamilton’
Harlan
https://mapserver01.gworks.com/arcgis/rest/services/Harlan_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Harlan’
Hayes
https://mapserver01.gworks.com/arcgis/rest/services/Hayes_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Hayes’
Hitchcock
https://mapserver01.gworks.com/arcgis/rest/services/Hitchcock_Co
unty_NE_Assessor/MapServer
Go to the top and search for ‘Hitchcock’
Hooker
https://mapserver01.gworks.com/arcgis/rest/services/Hooker_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Hooker’
Howard
https://mapserver01.gworks.com/arcgis/rest/services/Howard_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Howard’
Jefferson
https://mapserver01.gworks.com/arcgis/rest/services/Jefferson_Co
unty_NE_Clerk/MapServer
Go to the top and search for ‘Jefferson’
Johnson
https://mapserver01.gworks.com/arcgis/rest/services/Johnson_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Johnson’
Kearney
https://mapserver01.gworks.com/arcgis/rest/services/Kearney_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Kearney’
Keith
https://mapserver01.gworks.com/arcgis/rest/services/Keith_County
_NE_Assessor/MapServer

## Page 274

Go to the top and search for ‘Keith’
Keya Paha
https://mapserver01.gworks.com/arcgis/rest/services/Keya_Paha_C
ounty_NE_Assessor/MapServer
Go to the top and search for ‘Keya Paha’
Kimball
https://mapserver01.gworks.com/arcgis/rest/services/Kimball_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Kimball’
Knox
https://mapserver01.gworks.com/arcgis/rest/services/Knox_County
_NE_Assessor/MapServer
Go to the top and search for ‘Knox’
Lincoln
https://mapserver01.gworks.com/arcgis/rest/services/Lincoln_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Lincoln’
Logan
https://mapserver01.gworks.com/arcgis/rest/services/Logan_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Logan’
Loup
https://mapserver01.gworks.com/arcgis/rest/services/Loup_County
_NE_Assessor/MapServer
Go to the top and search for ‘Loup’
Madison
https://mapserver01.gworks.com/arcgis/rest/services/Madison_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Madison’
McPherson
https://mapserver01.gworks.com/arcgis/rest/services/Mcpherson_C
ounty_NE_Assessor/MapServer
Go to the top and search for ‘McPherson’
Merrick
https://mapserver01.gworks.com/arcgis/rest/services/Merrick_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Merrick’
Morrill
https://mapserver01.gworks.com/arcgis/rest/services/Morrill_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Morrill’
Nance
https://mapserver01.gworks.com/arcgis/rest/services/Nance_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Nance’

## Page 275

Nemaha
https://mapserver01.gworks.com/arcgis/rest/services/Nemaha_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Nemaha’
Nuckolls
https://mapserver01.gworks.com/arcgis/rest/services/Nuckolls_Co
unty_NE_Assessor/MapServer
Go to the top and search for ‘Nuckolls’
Otoe
https://mapserver01.gworks.com/arcgis/rest/services/Otoe_County
_NE_Assessor/MapServer
Go to the top and search for ‘Otoe’
Pawnee
https://mapserver01.gworks.com/arcgis/rest/services/Pawnee_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Pawnee’
Perkins
https://mapserver01.gworks.com/arcgis/rest/services/Pawnee_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Perkins’
Phelps
https://mapserver01.gworks.com/arcgis/rest/services/Phelps_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Phelps’
Pierce
https://mapserver01.gworks.com/arcgis/rest/services/Pierce_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Pierce’
Platte
https://mapserver01.gworks.com/arcgis/rest/services/Platte_County
_NE_Assessor/MapServer
Go to the top and search for ‘Platte’
Polk
https://mapserver01.gworks.com/arcgis/rest/services/Polk_County_
NE_Assessor/MapServer
Go to the top and search for ‘Polk’
Red Willow
https://mapserver01.gworks.com/arcgis/rest/services/Red_Willow_
County_NE_Treasurer/MapServer
Go to the top and search for ‘Red_Willow’
Richardson
https://mapserver01.gworks.com/arcgis/rest/services/Richardson_C
ounty_NE_Assessor/MapServer
Go to the top and search for ‘Richardson’
Rock
https://mapserver01.gworks.com/arcgis/rest/services/Rock_County
_NE_Assessor/MapServer

## Page 276

Go to the top and search for ‘Rock’
Saline
https://mapserver01.gworks.com/arcgis/rest/services/Saline_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Saline’
Sarpy
https://geodata.sarpy.com/arcgis/rest/services
Table of contents disabled
Sarpy
https://services.arcgis.com/pDAi2YK0L0QxVJHj/arcgis/rest/servic
es
Sarpy
https://tiles.arcgis.com/tiles/pDAi2YK0L0QxVJHj/arcgis/rest/servi
ces
Sarpy
https://tiles.arcgis.com/tiles/OiG7dbwhQEWoy77N/arcgis/rest/serv
ices
Saunders
https://mapserver01.gworks.com/arcgis/rest/services/Saunders_Co
unty_NE_Assessor/MapServer
Go to the top and search for ‘Saunders’
Scotts Bluff
https://wfs.schneidercorp.com/arcgis/rest/services/ScottsBluffCoun
tyNE_WFS/MapServer
Seward
https://mapserver01.gworks.com/arcgis/rest/services/Seward_Coun
ty_NE_Assessor/MapServer
Go to the top and search for ‘Seward’
Sheridan
https://mapserver01.gworks.com/arcgis/rest/services/Sheridan_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Sheridan’
Sherman
https://mapserver01.gworks.com/arcgis/rest/services/Sherman_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Sherman’
Sioux
https://mapserver01.gworks.com/arcgis/rest/services/Sioux_County
_NE_Assessor/MapServer
Go to the top and search for ‘Sioux’
Stanton
Schneider Geospatial - ArcGIS server address is not public
Thayer
https://mapserver01.gworks.com/arcgis/rest/services/Thayer_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Thayer’
Thomas
https://mapserver01.gworks.com/arcgis/rest/services/Thomas_Cou
nty_NE_Assessor/MapServer

## Page 277

Go to the top and search for ‘Thayer’
Thurston
https://mapserver01.gworks.com/arcgis/rest/services/Thurston_Co
unty_NE_Assessor/MapServer
Go to the top and search for ‘Thurston’
Valley
https://mapserver01.gworks.com/arcgis/rest/services/Valley_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Valley’
Washington
https://mapserver01.gworks.com/arcgis/rest/services/Washington_
County_NE_Assessor/MapServer
Go to the top and search for ‘Washington’
Wayne
https://mapserver01.gworks.com/arcgis/rest/services/Wayne_Count
y_NE_Assessor/MapServer
Go to the top and search for ‘Wayne’
Webster
https://mapserver01.gworks.com/arcgis/rest/services/Webster_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Webster’
Wheeler
https://mapserver01.gworks.com/arcgis/rest/services/Wheeler_Cou
nty_NE_Assessor/MapServer
Go to the top and search for ‘Wheeler’
York
_________ check for new server
Nebraska City, Town, Village, etc GIS Servers
Alma
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Alma_N
E_MGMT/MapServer
Table of contents disabled
Ashland
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Ashland
_NE_MGMT/MapServer
Table of contents disabled
Beatrice
https://services3.arcgis.com/I2jzMcLnq8BDWpwz/arcgis/rest/servi
ces
Central City
See Merrick County
Chadron
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Chadron
_NE_MGMT/MapServer
Table of contents disabled
Columbus
https://services8.arcgis.com/VdGaBUXUfZ3ETyKd/ArcGIS/rest/s
ervices

## Page 278

Crete
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Crete_N
E_MGMT/MapServer
Table of contents disabled
David City
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_David_
City_NE_MGMT/MapServer
Table of contents disabled
Eagle
https://gis3.gisworkshop.com/arcgis/rest/services/Village_of_Eagle
_NE_MGMT/MapServer
Table of contents disabled
Elgin
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Elgin_N
E_MGMT/MapServer
Table of contents disabled
Falls City
See Richardson County
Gibbon
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Gibbon_
NE_MGMT/MapServer
Table of contents disabled
Gordon
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Gordon_
NE_MGMT/MapServer
Table of contents disabled
Grand Island
https://gis.grand-island.com/arcgis/rest/services
Grand Island
https://services3.arcgis.com/H1fomogcAqX4720J/ArcGIS/rest/serv
ices
Grand Island
https://tiles.arcgis.com/tiles/H1fomogcAqX4720J/arcgis/rest/servic
es
Grant
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Grant_N
E_MGMT/MapServer
Table of contents disabled
Imperial
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Imperial
_NE_MGMT/MapServer
Table of contents disabled
Lexington
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Lexingt
on_NE_MGMT/MapServer
Table of contents disabled

Lincoln
https://gis.lincoln.ne.gov/public/rest/services
Lincoln
https://gisext.lincoln.ne.gov/arcgis/rest/services
Lincoln
https://gis.lincoln.ne.gov/image/rest/services
Lincoln
https://services1.arcgis.com/wpJGOi6N4Rq5cqFv/arcgis/rest/servi
ces
Lincoln
https://tiles.arcgis.com/tiles/wpJGOi6N4Rq5cqFv/arcgis/rest/servi
ces
Loup City
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Loup_Ci
ty_NE_MGMT/MapServer
Table of contents disabled

## Page 279

Madison
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Madison
_NE_MGMT/MapServer
Table of contents disabled
McCook
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_McCook
_NE_MGMT/MapServer
Table of contents disabled
Milford
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Milford
_NE_MGMT/MapServer
Table of contents disabled
Mullen
https://gis3.gisworkshop.com/arcgis/rest/services/Village_of_Mull
en_NE_MGMT/MapServer
Table of contents disabled
Nebraska City
See Otoe county
Nemaha
https://gis2.gisworkshop.com/arcgis/rest/services/Nemaha_Rural_
Water_District_Two_NE_MGMT/MapServer
Table of contents disabled
Nemaha
https://gis2.gisworkshop.com/arcgis/rest/services/Nemaha_Rural_
Water_District_One_NE_MGMT/MapServer
Table of contents disabled
Ogallala
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Ogallala
_NE_MGMT/MapServer
Table of contents disabled
Omaha
https://services1.arcgis.com/tIBLyYZX96jUntYm/arcgis/rest/servi
ces
Omaha
https://tiles.arcgis.com/tiles/tIBLyYZX96jUntYm/arcgis/rest/servic
es
Red Cloud
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Red_Clo
ud_NE_MGMT/MapServer
Table of contents disabled
Seward
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Seward_
NE_MGMT/MapServer
Table of contents disabled
Sutherland
https://gis3.gisworkshop.com/arcgis/rest/services/Village_of_Suthe
rland_NE_MGMT/MapServer
Table of contents disabled
Tecumseh
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Tecums
eh_NE_MGMT
Table of contents disabled
Utica
https://gis3.gisworkshop.com/arcgis/rest/services/Village_of_Utica
_NE_MGMT/MapServer
Table of contents disabled
Wahoo
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Wahoo_
NE_MGMT/MapServer
Table of contents disabled

## Page 280

Nevada State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server

Nevada Clearinghouse for Geographic Information
Website: http://www.nbmg.unr.edu/Maps&Data/VirtualClearinghouse.html      not https
Nevada Department of Conservation and Natural Resources
Website: https://dcnr.nv.gov
GIS: _ttp://arcgis.dcnr.nv.gov/arcgis/rest/services
dead link 1
8-4-2023 No tiled data
Nevada Division of Water Resources
Website: https://water.nv.gov
GIS: https://arcgis.water.nv.gov/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://services7.arcgis.com/AFD9b7ZqGkVnr1SF/arcgis/rest/services
Nevada Division of Environmental Protection
Website: https://ndep.nv.gov/
GIS: https://ndep-emap.ndep.nv.gov/arcgis/rest/services
8-4-2023 No tiled data
Nevada Division of Forestry
Website: https://forestry.nv.gov
GIS: _ttps://arcgis.shpo.nv.gov/arcgis/rest/services
dead link 1
GIS: https://services2.arcgis.com/bDmJlFHtkbwdyhN7/ArcGIS/rest/services
Nevada Division of Minerals
Website: https://minerals.nv.gov
GIS: https://services.arcgis.com/CXYUMoYknZtf5Qr3/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/CXYUMoYknZtf5Qr3/arcgis/rest/services
Nevada Department of Transportation
Website: https://www.nevadadot.com
GIS: https://gis.dot.nv.gov/agsphs/rest/services
GIS: https://gis.dot.nv.gov/arcgis/rest/services
GIS: https://services1.arcgis.com/9Y4hSlLf13E9S0Eo/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/9Y4hSlLf13E9S0Eo/arcgis/rest/services
Nevada Department of Wildlife
Website: https://www.ndow.org
GIS: https://services.arcgis.com/RyxlXSfFi87rAosq/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/RyxlXSfFi87rAosq/arcgis/rest/services

## Page 281

Office of Science, Innovation and Technology
Website: https://www.osit.nv.gov
GIS: https://services8.arcgis.com/6zoy8FhqGf9FaeLx/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/6zoy8FhqGf9FaeLx/arcgis/rest/services
Nevada Bureau of Mines and Geology - University of Nevada
Website: http://www.nbmg.unr.edu
not https
GIS:https://gisweb.unr.edu/nbmg/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/vzOMEctizHS6Qg17/arcgis/rest/services
Nevada legislature
Website: https://www.leg.state.nv.us
GIS: https://services9.arcgis.com/UU5yXg9PV67U0ebq/arcgis/rest/services
Nevada State Historic Preservation Office
Website: https://shpo.nv.gov
GIS: _ttps://arcgis.shpo.nv.gov/arcgis/rest/services
dead link 1
8-4-2023 No tiled data
Regional Transportation Commission of Southern Nevada
Website: https://www.rtcsnv.com/
GIS: https://gis.rtcsnv.com/arcgis/rest/services
Table of contents disabled
8-4-2023 No tiled data
Nevada County GIS Servers
All counties are listed and have been checked for GIS
Churchill
https://services2.arcgis.com/uPb1UC2HwTkBAlth/ArcGIS/rest/ser
vices
Clark
https://maps.clarkcountynv.gov/arcgis/rest/services
Clark
https://gisgate.co.clark.nv.us/arcgis/rest/services       SSL problem
Clark
https://services2.arcgis.com/MLoS3Qx4BXmDoTIY/arcgis/rest/ser
vices
Clark
https://tiles.arcgis.com/tiles/MLoS3Qx4BXmDoTIY/arcgis/rest/ser
vices
Douglas
https://services1.arcgis.com/F0m0hYDU3ywcMEEC/arcgis/rest/se
rvices
Douglas
https://tiles.arcgis.com/tiles/F0m0hYDU3ywcMEEC/arcgis/rest/ser
vices
Elko
https://gis.elkocountynv.net/server/rest/services
Table of contents disabled

## Page 282

Esmeralda
No GIS found
Eureka
https://services7.arcgis.com/npQRqzUHX9auAwvE/arcgis/rest/ser
vices
Humboldt
https://services7.arcgis.com/cbx6hozJyAREK9DB/arcgis/rest/servi
ces
Humboldt
https://tiles.arcgis.com/tiles/cbx6hozJyAREK9DB/arcgis/rest/servi
ces
Lander
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/LanderNVFeatures/FeatureServer
Go to the top and search for ‘LanderNV’
Lander
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/LanderNVCadastral/MapServer
Lincoln
https://sei.cloudsmartgis.com/arcgis/rest/services
Table of contents disabled
Lyon
https://gis.lyon-county.org/server/rest/services
Mineral
No GIS found
Nye
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/NyeNVFeatures/FeatureServer
Go to the top and search for ‘NyeNV’
Nye
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/NyeNVCadastralQuadrant1/MapServer
Go to the top and search for ‘NyeNV’
Pershing
https://services9.arcgis.com/qOD0sKAJC4zVpWPR/arcgis/rest/ser
vices
Storey
No GIS found
Sun Valley General Improvement District
https://services1.arcgis.com/piaA9iyFfFZWT5F7/arcgis/rest/servic
es
Washoe
https://gis.washoecounty.us/arcgis/rest/services
Washoe
https://wcgisweb.washoecounty.us/arcgis/rest/services
White Pine
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es
Go to the top and search for ‘WhitePineNV’
White Pine
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/WhitePineNVAerial2010/MapServer

## Page 283

White Pine
https://services9.arcgis.com/ihyPHe2KRRmOsTPa/arcgis/rest/servi
ces
White Pine
https://tiles.arcgis.com/tiles/ihyPHe2KRRmOsTPa/arcgis/rest/servi
ces
Nevada City, Town, Village, etc GIS Servers
Boulder City
https://services6.arcgis.com/ENlYDFfLXlpg7FOQ/arcgis/rest/servi
ces
Carlin
_ttps://gisdata.farrwestengineering.com/arcgis/rest/services/City_of
_Carlin
dead link 3

Carson City
http://ccapps.org/arcgis/rest/services
not https
Carson City
https://services5.arcgis.com/C0ejqMIMxJZHALms/ArcGIS/rest/se
rvices
Carson City
https://tiles.arcgis.com/tiles/C0ejqMIMxJZHALms/arcgis/rest/serv
ices
Douglas
https://gisservices.douglasnv.us/server/rest/services
Elko
https://gis.elkocountynv.net/server/rest/services
Table of contents disabled
Fernley
https://services6.arcgis.com/WSZL7KCp5ZvBFw3M/arcgis/rest/se
rvices
Fernley
https://tiles.arcgis.com/tiles/WSZL7KCp5ZvBFw3M/arcgis/rest/se
rvices
Gardnerville
See Douglas County
Henderson
https://maps.cityofhenderson.com/arcgis/rest/services
Henderson
https://services2.arcgis.com/naGsY5NZWVbd6bwD/ArcGIS/rest/s
ervices
Lander
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/LanderNVFeatures/FeatureServer
Go to the top and search for ‘LanderNV’
Lander
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/LanderNVCadastral/MapServer
Go to the top and search for ‘LanderNV’
Las Vegas
https://mapdata.lasvegasnevada.gov/clvgis/rest/services
Las Vegas
https://services1.arcgis.com/F1v0ufATbBQScMtY/arcgis/rest/servi
ces
Las Vegas
https://tiles.arcgis.com/tiles/F1v0ufATbBQScMtY/arcgis/rest/servi
ces

## Page 284

Mesquite
https://mapserv.mesquitenv.gov/arcgis_maps/rest/services
Mesquite
https://services7.arcgis.com/47djI2dDVjy1gZox/ArcGIS/rest/servic
es
Reno
https://citymaps.reno.gov/image/rest/services
Reno
https://citymaps.reno.gov/server/rest/services
Sparks
_______
New Hampshire State GIS Servers
New Hampshire Geographic Information System Clearinghouse (GRANIT)
Website: https://www.granit.unh.edu
 GIS: https://nhgeodata.unh.edu/nhgeodata/rest/services
Parcel lines:  CAD/ParcelMosiac/MapServer/0
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://nhgeodata.unh.edu/image/rest/services
GIS: https://services2.arcgis.com/7ivVdBiPNDE6XrFG/arcgis/rest/services
Table of contents hidden by javascript
GIS: https://services9.arcgis.com/wnvDDrXX8EouLkZP/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/wnvDDrXX8EouLkZP/arcgis/rest/services
New Hampshire Department of Environmental Services
Website: https://www.des.nh.gov/
GIS: https://gis.des.nh.gov/server/rest/services
8-4-2023 No tiled data
GIS: https://services1.arcgis.com/MAcUimSes4gPY4sM/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/MAcUimSes4gPY4sM/arcgis/rest/services
GIS: https://services5.arcgis.com/urxZLx0I3Y688Iho/arcgis/rest/services
Community Service Line Inventory.  The inventory is intended to identify the
location and material of all lead service lines (LSL) within public water systems.
New Hampshire Environmental Public Health Tracking
Website:
https://www.dhhs.nh.gov/programs-services/environmental-health-and-yo
u/environmental-public-health-tracking
GIS: _ttps://nhvieww.nh.gov/ephtwa/rest/services
dead link 3
New Hampshire Department of Transportation
Website: https://www.dot.nh.gov
GIS: https://services3.arcgis.com/mB6GMjOL4lVKAyZO/ArcGIS/rest/services
New Hampshire Regional
Central NH Regional Planning Commission (CNHRPC)
Website: https://www.cnhrpc.org
GIS: ______

## Page 285

Lakes Region Planning Commission (LRPC)
Website: _ttps://www.lakesrpc.org
dead link 1
GIS: ______
Nashua Regional Planning Commission
Website: https://www.nashuarpc.org
GIS: https://gishost.nashuarpc.org/arcgis/rest/services
SSL problem
8-4-2023 No tiled data
GIS: https://services6.arcgis.com/2ZriDy2NFXltCIFR/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/2ZriDy2NFXltCIFR/arcgis/rest/services
North Country Council, Inc. (NCC)
Website: https://www.nccouncil.org
GIS: https://services3.arcgis.com/KWaf86BdDV65JO5o/ArcGIS/rest/services
Rockingham Planning Commission (RPC)
Website: https://www.therpc.org
GIS: ______
Southern NH Planning Commission (SNHPC)
Website: https://www.snhpc.org
GIS: ______
Southwest Region Planning Commission (SwRPC)
Website: https://www.swrpc.org/index.php
GIS: ______
Strafford Regional Planning Commission (SRPC)
Website: https://www.strafford.org
Slow server
GIS: https://services1.arcgis.com/NWUiNpFLGIf9gkGi/arcgis/rest/services
Upper Valley Lake Sunapee Regional Planning Commission (UVLSRPC)
Website: https://www.uvlsrpc.org
GIS: https://services1.arcgis.com/Lxx6ZzbB9K8v0kCg/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Lxx6ZzbB9K8v0kCg/arcgis/rest/services
New Hampshire County GIS Servers
New Hampshire City, Town, Village, etc GIS Servers
Amherst
GIS but not ArcGIS
Bedford
https://services7.arcgis.com/14BiTE6uy1ugBpOk/ArcGIS/rest/serv
ices
Bedford
https://tiles.arcgis.com/tiles/14BiTE6uy1ugBpOk/arcgis/rest/servic
es

## Page 286

Bow
https://gisserver1.axisgis.com/arcgis/rest/services/BowNH
Not open to public
Concord
https://gis.concordnh.gov/arc1061/rest/services
Table of contents disabled
Derry
http://extranet2.derrynh.org:6080/arcgis/rest/services    not https
Derry
https://services5.arcgis.com/3ElMJIt82N0XVQto/ArcGIS/rest/serv
ices
Derry
https://tiles.arcgis.com/tiles/3ElMJIt82N0XVQto/arcgis/rest/servic
es
Goffstown
https://services.arcgis.com/9Ryy1DsyVOP8MR2j/arcgis/rest/servic
es
Goffstown
https://tiles.arcgis.com/tiles/9Ryy1DsyVOP8MR2j/arcgis/rest/servi
ces
Jaffrey
https://hostingdata3.tighebond.com/arcgis/rest/services/JaffreyNH
Litchfield
https://services3.arcgis.com/RIV6S09O6nOSAOo1/ArcGIS/rest/se
rvices
Litchfield
https://tiles.arcgis.com/tiles/RIV6S09O6nOSAOo1/arcgis/rest/serv
ices

Manchester
https://ags.manchesternh.gov/agsgis7/rest/services
Merrimack
https://spatialags.vhb.com/arcgis/rest/services/Merrimack
Milford
https://gisserver1.axisgis.com/arcgis/rest/services/MilfordNH

Not open to public
Nashua
https://newgis.nashuanh.gov/arcgisapp3/rest/services
Nashua
https://services1.arcgis.com/WwJAqA4K2ienzdKW/arcgis/rest/ser
vices
Nashua
https://tiles.arcgis.com/tiles/WwJAqA4K2ienzdKW/arcgis/rest/ser
vices
Plymouth
https://services7.arcgis.com/2ArBaN9Y1gCVWKyj/ArcGIS/rest/se
rvices
Rochester
https://services.arcgis.com/tslDSeWNuCpGNCV9/arcgis/rest/servi
ces
Rochester
https://tiles.arcgis.com/tiles/tslDSeWNuCpGNCV9/arcgis/rest/serv
ices
Seabrook
https://arcgis.vgsi.com/server/rest/services/Seabrook_NH

## Page 287

Tilton
https://gisserver1.axisgis.com/arcgis/rest/services/TiltonNH
Not open to public
New Jersey State GIS Servers

New Jersey Geographic Information Network
Website: https://nj.gov/njgin
New Jersey Office of Emergency Management
Website: https://www.nj.gov/njoem
GIS: https://services2.arcgis.com/mRHXO9pm6rJHovVd/ArcGIS/rest/services
New Jersey Department of Children and Families
Website: https://www.nj.gov/dcf
GIS: https://services2.arcgis.com/lswjyu51B31ijq9v/ArcGIS/rest/services
New Jersey Department of Community Affairs
Website:  https://www.nj.gov/dca
GIS: https://services.arcgis.com/Aur8tCo478N3VovT/arcgis/rest/services
New Jersey Department of Environmental Protection
Website: https://dep.nj.gov/gis
GIS: https://mapsdep.nj.gov/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Parcels:  Applications/RSP_Base_Layers/MapServer
GIS: https://services1.arcgis.com/QWdNfRs7lkPq4g4Q/ArcGIS/rest/services
New Jersey Department of Transportation
Website: https://www.nj.gov/transportation/refdata/gis
GIS: https://services.arcgis.com/HggmsDF7UJsNN1FK/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/HggmsDF7UJsNN1FK/arcgis/rest/services
New Jersey various layers
GIS: https://maps.nj.gov/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://geo.nj.gov/arcgis/rest/services
8-4-2023 No tiled data
Links to geocoding service
GIS: https://maps.nj.gov/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://map.appgeo.com/arcgis/rest/services/NJDOT
Not open to public
GIS: https://services2.arcgis.com/XVOqAjTOJ5P6ngMu/ArcGIS/rest/services
4-26-2024 staff says most current parcel lines is:
Hosted_Parcels_Test_WebMer_20201016/FeatureServer
GIS: https://tiles.arcgis.com/tiles/XVOqAjTOJ5P6ngMu/arcgis/rest/services

## Page 288

Meadowlands Research and Restoration Institute
Website: https://meadowlandsrri.com
GIS: _ttp://arcgis5.njmeadowlands.gov/webmaps/rest/services
dead link 3
Rutgers university
GIS: https://njmaps1.rad.rutgers.edu/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
New Jersey Regional
New Jersey Highlands Council
Website: https://www.nj.gov/njhighlands
GIS: https://services6.arcgis.com/ZrVlS0wslq8Nvq5I/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/ZrVlS0wslq8Nvq5I/arcgis/rest/services
North Jersey Transportation Planning Authority
Website: https://njtpa.org/home
GIS: https://gis.njtpa.org/arcgis/rest/services
8-4-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/62BbyekYOM5s5n0K/ArcGIS/rest/services
GIS: https://services6.arcgis.com/M0t0HPE53pFK525U/ArcGIS/rest/services
GIS: https://services3.arcgis.com/UyOm3tye2T3XpM10/ArcGIS/rest/services
Pinelands Commission
Website: https://www.nj.gov/pinelands/
GIS: https://services1.arcgis.com/nCm6SZaiGMuGX35l/arcgis/rest/services
Includes a parcel layer
New Jersey Township GIS Servers
West Deptford
https://services1.arcgis.com/tTe6sx5o86d0H206/ArcGIS/rest/servi
ces
New Jersey County GIS Servers
All counties are listed and have been checked for GIS
Atlantic
https://services1.arcgis.com/z18KTAVDZDXq9ZmQ/arcgis/rest/se
rvices
Atlantic
https://tiles.arcgis.com/tiles/z18KTAVDZDXq9ZmQ/arcgis/rest/se
rvices
Atlantic
https://services7.arcgis.com/ItUoEIWvqsXZpKZ1/ArcGIS/rest/ser
vices
Atlantic
https://tiles.arcgis.com/tiles/ItUoEIWvqsXZpKZ1/arcgis/rest/servi
ces
Bergen
https://bchapeweb.co.bergen.nj.us/arcgis/rest/services

## Page 289

Burlington
https://gisportal.co.burlington.nj.us/hosting/rest/services
Camden
https://services3.arcgis.com/JGF6qCAQFbROcocK/ArcGIS/rest/se
rvices
Camden
https://tiles.arcgis.com/tiles/JGF6qCAQFbROcocK/arcgis/rest/serv
ices
Cape May
https://ims.capemaycountynj.gov/arcgisweb/rest/services
Cumberland
          https://services3.arcgis.com/n57TaxATizczF7nd/arcgis/rest/services
Essex
No GIS found
Gloucester
https://services5.arcgis.com/ALQeR5k3182nooX1/arcgis/rest/servi
ces
Hudson
https://gis.hcnj.us/arcgis/rest/services
Hudson
https://services3.arcgis.com/Stu7jwuXrnM0myT0/arcgis/rest/servi
ces
Hudson
https://tiles.arcgis.com/tiles/Stu7jwuXrnM0myT0/arcgis/rest/servic
es
Hunterdon
http://gis.co.hunterdon.nj.us/arcgis/rest/services
not https
Mercer
https://maps.mercercounty.org/arcgis/rest/services
Middlesex
____________
Monmouth
https://mapsdep.nj.gov/arcgis/rest/services
Monmouth
           https://services1.arcgis.com/PsDtSYIjNsyfjwcX/arcgis/rest/services
Monmouth
           https://tiles.arcgis.com/tiles/PsDtSYIjNsyfjwcX/arcgis/rest/services
Morris
https://morrisgisapps.co.morris.nj.us/arcgis105/rest/services
Ocean
https://services.arcgis.com/VBdTQMELLnfudIA5/arcgis/rest/servi
ces
Ocean
https://tiles.arcgis.com/tiles/VBdTQMELLnfudIA5/arcgis/rest/serv
ices
Passaic
https://gis.passaiccountynj.org/arcgis/rest/services
Salem
No GIS found
Somerset
https://services2.arcgis.com/2g2XvfUywwLJoF2c/arcgis/rest/servi
ces

## Page 290

Sussex
https://services.arcgis.com/opPd2BqYeMe7vELn/ArcGIS/rest/serv
ices
Sussex
https://tiles.arcgis.com/tiles/opPd2BqYeMe7vELn/arcgis/rest/servi
ces
 Union
_ttps://oms.ucnj.org/Geocortex/Essentials/REST/sites/IncidentMan
agement/map/mapservices/7/rest/services
dead link 1
Warren
https://services3.arcgis.com/4mb1fO9eRe47EZZx/arcgis/rest/servi
ces
Warren
https://tiles.arcgis.com/tiles/4mb1fO9eRe47EZZx/arcgis/rest/servi
ces
New Jersey Township GIS Servers
Lakewood
___________
Mount Laurel Fire
https://services2.arcgis.com/V5LBi9AV7Us2RBaI/ArcGIS/rest/ser
vices
New Jersey City, Town, Village, etc GIS Servers
Hammonton
https://services6.arcgis.com/oB6C7s98yFFYeAC0/arcgis/rest/servi
ces
Hoboken
https://services8.arcgis.com/LDmC4ZVHdfKcEzxl/ArcGIS/rest/se
rvices
Jersey City
https://services2.arcgis.com/UXbywc7dSkfgdPp4/ArcGIS/rest/serv
ices
Lavallette (Borough)  https://services9.arcgis.com/3ZbvjvguXtD6Gajr/arcgis/rest/services
Margate
https://services1.arcgis.com/LImghJvc0PVJcmCV/arcgis/rest/servi
ces
Newark
https://njgin.ci.newark.nj.us/arcgis/rest/services

Newark
https://services1.arcgis.com/WAUuvHqqP3le2PMh/arcgis/rest/ser
vices
Newark
https://tiles.arcgis.com/tiles/WAUuvHqqP3le2PMh/arcgis/rest/serv
ices
Newton
__________
Raritan
__________

## Page 291

Toms River
https://services2.arcgis.com/7a7OULZOTqe87h9O/ArcGIS/rest/ser
vices
Toms River
https://tiles.arcgis.com/tiles/7a7OULZOTqe87h9O/arcgis/rest/servi
ces
Trenton
https://services3.arcgis.com/Enb6y4sKdtGAvo2y/arcgis/rest/servic
es
New Mexico State GIS Servers
New Mexico Resource Geographic Information System
Website: https://rgis.unm.edu
The Geospatial Coordination Center of New Mexico
GIS: https://services3.arcgis.com/btGPJYeJkAc5Bpuh/ArcGIS/rest/services
New Mexico Energy, Minerals and Natural Resources Department
Website: https://www.emnrd.nm.gov
GIS: https://gis.emnrd.nm.gov/arcgis/rest/services
Table of contents disabled
New Mexico Environment Department
Website: https://www.env.nm.gov/
GIS: https://mercator.env.nm.gov/server/rest/services
New Mexico Department of Transportation
Website: https://nmdot.maps.arcgis.com/home/index.html
GIS: https://services.arcgis.com/hOpd7wfnKm16p9D9/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/hOpd7wfnKm16p9D9/arcgis/rest/services
New Mexico State Land Office
Website: https://www.nmstatelands.org
GIS: https://mapservice.nmstatelands.org/arcgis/rest/services
8-4-2023 No tiled data
New Mexico Broadband Program
Website: https://www.doit.state.nm.us/broadband
GIS: https://nmbbmapping.org/arcgis/rest/services
8-4-2023 No tiled data
New Mexico Office of State Engineer
Website: https://www.ose.state.nm.us
SSL problem
GIS: https://gis.ose.nm.gov/server_s/rest/services
GIS: https://services2.arcgis.com/qXZbWTdPDbTjl7Dy/ArcGIS/rest/services
GIS:  https://tiles.arcgis.com/tiles/qXZbWTdPDbTjl7Dy/arcgis/rest/services
University of New Mexico - Earth Data Analysis Center

## Page 292

Website: https://edac.unm.edu
GIS: https://edacarc.unm.edu/arcgis/rest/services
8-4-2023 No tiled data
GIS: https://services3.arcgis.com/BACyfsAaJBcJ33md/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/BACyfsAaJBcJ33md/arcgis/rest/services
Various New Mexico layers:
GIS: https://services.arcgis.com/LGtNQDlIZBdntoA9/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/LGtNQDlIZBdntoA9/arcgis/rest/services
GIS: https://services5.arcgis.com/umw3NOuKROeuP1iR/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/umw3NOuKROeuP1iR/arcgis/rest/services
New Mexico Regional
Mid-Region Metropolitan Planning Organization
Website: https://www.mrcog-nm.gov/233/Metropolitan-Planning-Organization
GIS: https://services1.arcgis.com/i3mLmgyL55IkFf81/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/i3mLmgyL55IkFf81/arcgis/rest/services
New Mexico County GIS Servers
All counties are listed and have been checked for GIS
Bernalillo
https://pdsmaps.bernco.gov/server/rest/services
Bernalillo
https://services5.arcgis.com/p6HCRGxaSNtBefla/ArcGIS/rest/serv
ices
Albuquerque Bernalillo County Water Utility
Authority
Bernalillo
https://services6.arcgis.com/NiLPE6S5bwjCDk9X/ArcGIS/rest/ser
vices
Bernalillo
https://tiles.arcgis.com/tiles/NiLPE6S5bwjCDk9X/arcgis/rest/servi
ces
Catron
          https://services3.arcgis.com/fneA3L2J0387Pb3S/arcgis/rest/services
Chaves
https://services3.arcgis.com/2P9mvTRBkjNHMsaa/arcgis/rest/serv
ices
Cibola
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/CibolaNMFeatures/FeatureServer
Go to the top and search for ‘CibolaNM’
Cibola
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/CibolaNMCadastral/MapServer
Colfax
No GIS found
Curry
https://maps.currycounty.org/server/rest/services

## Page 293

De Baca
No GIS found
Dona Ana
https://services7.arcgis.com/JMIoqakAkedEx0oU/arcgis/rest/servic
es
Eddy
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/EddyNMFeatures/FeatureServer
Go to the top and search for ‘EddyNM’
Eddy
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/EddyNMCadastral/MapServer
Go to the top and search for ‘EddyNM’
Grant
No GIS found
Guadalupe
No GIS found
Harding
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/HardingNMFeatures/FeatureServer
Go to the top and search for ‘HardingNM’
Harding
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/HardingNMCadastral/MapServer
Go to the top and search for ‘HardingNM’
Henrico
https://services.arcgis.com/LxWK4CxNTBBlLshT/arcgis/rest/servi
ces
Henrico
https://tiles.arcgis.com/tiles/LxWK4CxNTBBlLshT/arcgis/rest/ser
vices
Hidalgo
They have ArcGIS data but could not find server address.
Lea
https://services3.arcgis.com/haQkIWW9RWRd8Arf/ArcGIS/rest/s
ervices
Lea
https://tiles.arcgis.com/tiles/haQkIWW9RWRd8Arf/arcgis/rest/ser
vices
Lincoln
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/LincolnNMFeatures/FeatureServer
Go to the top and search for ‘LincolnNM’
Lincoln
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/LincolnNMCadastral/MapServer
Los Alamos
https://gis.losalamosnm.us/securegis/rest/services
Luna
https://services2.arcgis.com/K9P1N7Y1EilGjehZ/arcgis/rest/servic
es

## Page 294

McKinley
No public access to GIS server.  Type of server is unknown.
Mora
No GIS server found

Otero
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/OteroNMFeatures/FeatureServer
Go to the top and search for ‘OteroNM’
Otero
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/OteroNMAerial2015/MapServer
Quay
No GIS server found
Rio Arriba
           https://services6.arcgis.com/6gDz3aQl2Pya7uIo/arcgis/rest/services
Roosevelt
https://services3.arcgis.com/ZEb47Ho06RmXcN4j/ArcGIS/rest/ser
vices
Roosevelt
https://tiles.arcgis.com/tiles/ZEb47Ho06RmXcN4j/arcgis/rest/servi
ces
Sandoval
https://services5.arcgis.com/04AQv4PgUZUh16VF/arcgis/rest/serv
ices
Sandoval
https://tiles.arcgis.com/tiles/04AQv4PgUZUh16VF/arcgis/rest/serv
ices
San Juan
https://webmaps.sjcounty.net/arcgis/rest/services
San Juan
https://services.arcgis.com/Iq7du96UAXAOM1at/arcgis/rest/servic
es
San Miguel
https://services5.arcgis.com/kpHNTxyC2khk5uUM/arcgis/rest/serv
ices
San Miguel
https://tiles.arcgis.com/tiles/kpHNTxyC2khk5uUM/arcgis/rest/serv
ices
Santa Fe
https://sfcomaps.santafecountynm.gov/restsvc/rest/services
Sierra
https://services3.arcgis.com/wLaEYnmUFNVmiBI3/ArcGIS/rest/s
ervices
Sierra
https://tiles.arcgis.com/tiles/wLaEYnmUFNVmiBI3/arcgis/rest/ser
vices
Socorro
https://nm.gis.axiomnh.com/server/rest/services
Taos
https://services1.arcgis.com/XSUObhM9CdLiddkA/arcgis/rest/ser
vices

## Page 295

Torrance
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es
Go to the top and search for ‘TorranceNM’
Torrance
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/TorranceNMAerial2014/MapServer
Union
No public access to GIS server.  Type of server is unknown.
Valencia
https://arcgisce2.co.valencia.nm.us/arcgis/rest/services
New Mexico City, Town, Village, etc GIS Servers
Alamogordo
https://services1.arcgis.com/tZhkGVr1gXGPSz0S/arcgis/rest/servi
ces
Alamogordo
https://tiles.arcgis.com/tiles/tZhkGVr1gXGPSz0S/arcgis/rest/servi
ces

Albuquerque
https://coagisweb.cabq.gov/arcgis/rest/services
Albuquerque
https://dmdmaps.cabq.gov/serverext/rest/services
Albuquerque
https://services.arcgis.com/CWv1abTnC3urn4bV/arcgis/rest/servic
es
Albuquerque
https://tiles.arcgis.com/tiles/CWv1abTnC3urn4bV/arcgis/rest/servi
ces
Albuquerque
https://services5.arcgis.com/p6HCRGxaSNtBefla/ArcGIS/rest/serv
ices
Albuquerque Bernalillo County Water Utility
Authority
Cloudcroft
https://services5.arcgis.com/MuetKt2X4gaxiKvl/ArcGIS/rest/servi
ces
Cloudcroft
           https://tiles.arcgis.com/tiles/MuetKt2X4gaxiKvl/arcgis/rest/services
Clovis
https://maps.cityofclovis.org/arcgis/rest/services
Farmington
https://services.arcgis.com/cakQzytYZtvfbh5z/arcgis/rest/services
Las Cruces
https://maps.las-cruces.org/gis/rest/services
Las Cruces
https://services1.arcgis.com/ejcbAsQEUUGWEyzb/arcgis/rest/serv
ices
Las Cruces
https://tiles.arcgis.com/tiles/ejcbAsQEUUGWEyzb/arcgis/rest/serv
ices
Lincoln
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/LincolnNMFeatures/FeatureServer
Go to the top and search for ‘LincolnNM’
Lincoln
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/LincolnNMCadastral/MapServer
Go to the top and search for ‘LincolnNM’

## Page 296

Los Alamos
See Los Alamos county
Rio Rancho
https://gis.rrnm.gov/arcgis/rest/services
Rio Rancho
https://services2.arcgis.com/KQGAxSQd2SGmmuxN/ArcGIS/rest/
services
Rio Rancho
https://tiles.arcgis.com/tiles/KQGAxSQd2SGmmuxN/arcgis/rest/se
rvices
Ruidoso
https://services2.arcgis.com/Rj8QhN9Wb2hxHgpN/arcgis/rest/serv
ices
Ruidoso
https://tiles.arcgis.com/tiles/Rj8QhN9Wb2hxHgpN/arcgis/rest/serv
ices
Santa Fe
https://gis.santafenm.gov/server/rest/services
Santa Fe
https://services7.arcgis.com/p0Gk2nDbPs7KEqSZ/ArcGIS/rest/ser
vices
Taos
https://services8.arcgis.com/AUzB6nOCWYow3ofS/arcgis/rest/ser
vices
Taos
https://tiles.arcgis.com/tiles/AUzB6nOCWYow3ofS/arcgis/rest/ser
vices
New York State GIS Servers
New York Open Data
Website: https://data.ny.gov
New York State Geographic Information Systems (GIS) Clearinghouse
Website: https://gis.ny.gov/sharegis
GIS: https://services6.arcgis.com/EbVsqZ18sv1kVJ3k/ArcGIS/rest/services
New York Division of Homeland Security and Emergency Services
Website: https://www.dhses.ny.gov
GIS: https://orthos.its.ny.gov/arcgis/rest/services
8-5-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Aerials
New York State Department of Environmental Conservation
Website: https://www.dec.ny.gov
GIS: https://gisservices.dec.ny.gov/arcgis/rest/services
8-5-2023 No tiled data
GIS: https://services6.arcgis.com/DZHaqZm9cxOD4CWM/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/DZHaqZm9cxOD4CWM/arcgis/rest/services
New York Department of State
Website: https://www.dos.ny.gov/

## Page 297

GIS: https://services2.arcgis.com/okXm0pb6aWH6XOGI/arcgis/rest/services
Lots of shoreline related layers
GIS: https://tiles.arcgis.com/tiles/okXm0pb6aWH6XOGI/arcgis/rest/services
New York Department of Transportation
Website: https://www.dot.ny.gov/index
GIS: https://gis.dot.ny.gov/hostingny/rest/services
8-5-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gisportalnyqa.dot.ny.gov/hostingny/rest/services
New York State Office of Information Technology Services
Website: https://its.ny.gov/
GIS: https://gisservices.its.ny.gov/arcgis/rest/services
Parcel lines:  NYS_Tax_Parcels_Public/MapServer/1
layer 0 shows the counties that have provided parcel data
8-5-2023 No tiled data
GIS: https://elevation.its.ny.gov/arcgis/rest/services
8-5-2023 No tiled data
New York State Energy Research and Development Authority
Website: https://www.nyserda.ny.gov
GIS: https://services.nyserda.ny.gov/arcgis/rest/services
New York various layers
GIS: https://services.arcgis.com/1xFZPtKn1wKC6POA/ArcGIS/rest/services
Lots of recreation layers
New York Regional
Adirondack Park Agency
Website: https://apa.ny.gov/
GIS: https://services2.arcgis.com/8krRUWgifzA4cgL3/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/8krRUWgifzA4cgL3/arcgis/rest/services
Capital District Regional Planning Commission
Website: https://cdrpc.org
GIS: _____
Capital District Transportation Authority
Website: https://www.cdta.org
GIS: https://services2.arcgis.com/A3lMfLhXIUtyxP6p/arcgis/rest/services
Central New York Regional Planning and Development Board
Website: https://www.cnyrpdb.org
GIS: _____
Development Authority of the North Country

## Page 298

Website: https://www.danc.org
GIS: https://maps.dancgis.org/server/rest/services
8-5-2023 No tiled data
Genesee/Finger Lakes Regional Planning Council
Website: https://www.gflrpc.org
GIS: _____
Herkimer-Oneida Counties Comprehensive Planning Program
Website: https://www.ocgov.net//oneida/planning
GIS: http://maps.ocgov.net/arcgis/rest/services
GIS: https://services3.arcgis.com/6x801hFkTeoDflcw/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/6x801hFkTeoDflcw/arcgis/rest/services
Hudson Valley Regional Council
Website: https://hudsonvalleyregionalcouncil.org
GIS:
Lake Champlain-Lake George Regional Planning and Development Board
Website: https://lclgrpb.org
GIS: _____
Southern Tier Central Regional Planning and Development Board
Website: https://www.stcplanning.org
GIS: _____
Southern Tier 8
Website: https://southerntier8.org
GIS: _____

Southern Tier West Regional Planning and Development Board
Website: https://www.southerntierwest.org
GIS: _____
New York Thruway Authority
Website: https://www.thruway.ny.gov/index.shtml
GIS: https://services2.arcgis.com/gubH6kG9JCAsMX2M/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/gubH6kG9JCAsMX2M/arcgis/rest/services
New York County GIS Servers
All counties are listed and have been checked for GIS
Albany
https://services8.arcgis.com/MVX6tbvWftyS3KBR/arcgis/rest/serv
ices

## Page 299

Allegany
https://services5.arcgis.com/WcotYUBrYwlGLzUr/arcgis/rest/serv
ices
Bronx
See New York City
Broome
https://gis.broomecountyny.gov/arcgis/rest/services
Cattaraugus
https://maps2.cattco.org/arcgiswebadaptor/rest/services
Cayuga
https://ccgis.cayugacounty.us/arcgis/rest/services
Chautauqua
https://maps.chautauquacounty.com/server/rest/services
Chautauqua
https://services1.arcgis.com/ejbgqcCL0yNBugWr/ArcGIS/rest/serv
ices
Chautauqua
https://tiles.arcgis.com/tiles/ejbgqcCL0yNBugWr/arcgis/rest/servic
es
Chemung
https://ccgcportal.chemungcountyny.gov/production/rest/services
Chenengo
Schneider Geospatial - ArcGIS server address is not public
They charge for access
Clinton
https://services3.arcgis.com/33FPYaVQYNa7sFJ5/arcgis/rest/servi
ces
Columbia
https://services3.arcgis.com/F5762GA30C3SyZFy/ArcGIS/rest/ser
vices
Cortland
https://services2.arcgis.com/fRWb1mz1huf3Aqyy/arcgis/rest/servi
ces
Delaware
https://spatialags.vhb.com/arcgis/rest/services/29822_Delaware
Delaware
https://services3.arcgis.com/n2RXARD7dbpeC4OO/ArcGIS/rest/s
ervices
Dutchess
https://gis.dutchessny.gov/server/rest/services
Table of contents disabled
Erie
https://gis.erie.gov/server/rest/services
Essex
https://essex-gis.co.essex.ny.us/arcgis/rest/services
Franklin
https://maps.dancgis.org/server/rest/services/Franklin_Infrastructur
e_P_24/MapServer
Go to the top and search for ‘Franklin’

## Page 300

Genesee
_ttps://gisp.co.genesee.ny.us/arcgis/rest/services
dead link 1
Greene
https://gis.gcgovny.com/arcgis/rest/services
Hamilton
_ttps://spatialags.vhb.com/arcgis/rest/services/29824_Hamilton
dead link 1
Jefferson
https://maps.dancgis.org/server/rest/services/Jefferson_Infrastructu
re_P_24/MapServer
Go to the top and search for ‘Jefferson’
Jefferson
_ttps://spatialags.vhb.com/arcgis/rest/services/29823_Jefferson/La
yers/MapServer
dead link 1
Kings
See New York City
Lewis
https://maps.dancgis.org/server/rest/services/Lewis_Infrastructure_
P_24/MapServer
Go to the top and search for ‘Lewis’
Livingston
https://gis.livingstoncountyny.gov/arcgis/rest/services
Madison
_ttps://spatialags.vhb.com/arcgis/rest/services/20389_Madison
dead link 1
Monroe
https://maps.monroecounty.gov/server/rest/services
Montgomery
Public parcel map no longer maintained and not ArcGIS
Nassau
https://gis.nassaucountyny.gov/server/rest/services
Nassau
https://legacygis.nassaucountyny.gov/arcgis/rest/services
Nassau
https://services1.arcgis.com/rsOafHhKLHpnpr4t/ArcGIS/rest/servi
ces
Nassau
           https://tiles.arcgis.com/tiles/rsOafHhKLHpnpr4t/arcgis/rest/services
New York (Manhattan)
See New York City
Niagara
https://gis.niagaracounty.com/arcgis/rest/services
Table of contents disabled
Oneida
https://maps.ocgov.net/arcgis/rest/services
Onondaga
https://spatialags.vhb.com/arcgis/rest/services/29821_Syr_Ononda
ga
Ontario
https://oncorng.co.ontario.ny.us/arcgis/rest/services

## Page 301

Orange
https://gis.orangecountygov.com/arcgis/rest/services
Orange
https://services8.arcgis.com/vnLjOWzL0KMXNN0y/ArcGIS/rest/s
ervices
Orange
https://tiles.arcgis.com/tiles/vnLjOWzL0KMXNN0y/arcgis/rest/ser
vices
Orleans
https://services6.arcgis.com/AGRzZ0TKgr5syAM6/arcgis/rest/serv
ices
Oswego
https://maps.dancgis.org/server/rest/services/Oswego_Infrastructur
e_P_24/MapServer
Go to the top and search for ‘Oswego’
Oswego
https://services3.arcgis.com/0dC3T96jvK0z64NH/arcgis/rest/servi
ces
Oswego
https://tiles.arcgis.com/tiles/0dC3T96jvK0z64NH/arcgis/rest/servic
es
Otsego
https://dfgdfg.mapxpress.net/arcgis/rest/services/Otsego
Otsego
https://sgsdgf.mapxpress.net/arcgis/rest/services/Otsego
Putnam
https://services2.arcgis.com/dU6jdOIkCUj2UDe9/arcgis/rest/servic
es
Putnam
https://tiles.arcgis.com/tiles/dU6jdOIkCUj2UDe9/arcgis/rest/servic
es
Queens
See New York City
Rensselaer
Do not have a public GIS
Richmond (Staten Island)
See New York City
Rockland
https://services1.arcgis.com/Fh5t2TadzXuiUPwK/ArcGIS/rest/serv
ices
Table of contents hidden by javascript
St. Lawrence
https://maps.dancgis.org/server/rest/services/StLawrence_Infrastru
cture_P/MapServer
Go to the top and search for ‘St. Lawrence’
Saratoga
https://spatialags.vhb.com/arcgis/rest/services/29820_Saratoga
Saratoga
https://services2.arcgis.com/Rl5JqTf1a26nunTO/ArcGIS/rest/servi
ces
Schenectady
https://services8.arcgis.com/o8Qc4eWOVfjafsaS/arcgis/rest/servic
es
Schoharie
https://spatialags.vhb.com/arcgis/rest/services/20327_Schoharie

## Page 302

Schuyler
https://services9.arcgis.com/wGGTeQ7ADSSKDWnb/arcgis/rest/s
ervices
Schuyler
https://tiles.arcgis.com/tiles/wGGTeQ7ADSSKDWnb/arcgis/rest/s
ervices
Seneca
No public GIS
Steuben
https://services2.arcgis.com/NZkLeERo9XICXiuy/arcgis/rest/servi
ces
Suffolk
https://gis.suffolkcountyny.gov/server/rest/services
Table of contents disabled
parcels: Applications/GISViewer/MapServer/57
Suffolk
           https://gis.suffolkcountyny.gov/image/rest/services
Suffolk
           https://services.arcgis.com/JsDD4qdG5r2a7hR5/arcgis/rest/services
Suffolk
https://tiles.arcgis.com/tiles/JsDD4qdG5r2a7hR5/arcgis/rest/servic
es
Sullivan
https://gis.sullivanny.us/arcgis/rest/services
Sullivan
https://services7.arcgis.com/bx3OlIPqiDclwaja/arcgis/rest/services

Table of contents hidden by javascript
Tioga
https://services3.arcgis.com/PvkAiSMFS7cpxnJP/arcgis/rest/servic
es
Tioga
https://tiles.arcgis.com/tiles/PvkAiSMFS7cpxnJP/arcgis/rest/servic
es
Tompkins
https://services.arcgis.com/oJbAAWNInLrxvF0A/arcgis/rest/servic
es
Tompkins
https://tiles.arcgis.com/tiles/oJbAAWNInLrxvF0A/arcgis/rest/servi
ces
Ulster
https://gis.ulstercountyny.gov/server/rest/services
Ulster
https://services2.arcgis.com/18GPlQz4EhvHT4ph/ArcGIS/rest/ser
vices
Ulster
https://tiles.arcgis.com/tiles/18GPlQz4EhvHT4ph/arcgis/rest/servic
es
Warren
https://services6.arcgis.com/Fg3XpDIUTR3JZZES/arcgis/rest/serv
ices
Warren
https://tiles.arcgis.com/tiles/Fg3XpDIUTR3JZZES/arcgis/rest/servi
ces
Washington
https://gis.washingtoncountyny.gov/arcgis/rest/services
Wayne
No public GIS

## Page 303

Westchester
https://giswww.westchestergov.com/arcgis/rest/services
Westchester
https://giswww.westchestergov.com/ArcGIS/rest/services
Westchester
https://services.arcgis.com/XKEHpOulfycN9cGC/arcgis/rest/servic
es
Westchester
https://tiles.arcgis.com/tiles/XKEHpOulfycN9cGC/arcgis/rest/servi
ces
Wyoming
Not open to public
Yates
No public GIS
New York City, Town, Village, etc GIS Servers
Albany
https://services6.arcgis.com/JJzptGyn7EDStgyp/ArcGIS/rest/servic
es
Albany
https://tiles.arcgis.com/tiles/JJzptGyn7EDStgyp/arcgis/rest/services
Albany
https://services9.arcgis.com/0sUXe1ZlggF9tBHD/arcgis/rest/servic
es
Bath
https://services5.arcgis.com/GdWjpNVUqrExORRt/ArcGIS/rest/se
rvices
Gas, water and electric
Buffalo
https://gis.buffalony.gov/server/rest/services
Table of contents disabled
Buffalo
https://services8.arcgis.com/BMPgiPHUrkqJdtki/ArcGIS/rest/servi
ces
Cobleskill
_ttps://72.10.206.73/arcgis/rest/services/Cobleskill    dead link 3
Colonie
https://spatialags.vhb.com/arcgis/rest/services/29800_Colonie/NY_
Town_Colonie/MapServer
East Hampton
https://eh-gis.ehamptonny.gov/arcgis/rest/services
Esopus
See Ulster county
Huntington
https://geo.huntingtonny.gov/arcgis/rest/services
Ithaca
https://services5.arcgis.com/R1JbITZvSQHJsl5r/ArcGIS/rest/servi
ces
New York
https://services.arcgis.com/uKN48PkxmWiqJM9q/ArcGIS/rest/ser
vices
New York
https://tiles.arcgis.com/tiles/uKN48PkxmWiqJM9q/arcgis/rest/serv
ices
New York
          https://services.arcgis.com/v09SvJE7IY8GgvSx/arcgis/rest/services
Department of Design and Construction

## Page 304

New York
https://tiles.arcgis.com/tiles/v09SvJE7IY8GgvSx/arcgis/rest/servic
es
New York
           https://services3.arcgis.com/hEQy6nIL6IiyuNf1/arcgis/rest/services
Focus is on data related to buildings
New York
https://services5.arcgis.com/GfwWNkhOj9bNBqoJ/arcgis/rest/serv
ices
New York
https://tiles.arcgis.com/tiles/GfwWNkhOj9bNBqoJ/arcgis/rest/serv
ices
New York
          https://services6.arcgis.com/yG5s3afENB5iO9fj/arcgis/rest/services
New York
          https://tiles.arcgis.com/tiles/yG5s3afENB5iO9fj/arcgis/rest/services
Otsego
https://server1.mapxpress.net/arcgis/rest/services/Otsego

Rochester
https://maps.cityofrochester.gov/arcssl/rest/services
Rochester
https://maps.cityofrochester.gov/arcgis/rest/services
Rochester
https://maps.cityofrochester.gov/server/rest/services
Rochester
https://services2.arcgis.com/yoz1ZtATTCokO9nU/ArcGIS/rest/ser
vices
Rochester
https://tiles.arcgis.com/tiles/yoz1ZtATTCokO9nU/arcgis/rest/servi
ces
Rochester
https://services7.arcgis.com/wMvCpnbQEKXZsPSQ/ArcGIS/rest/s
ervices
Syracuse
https://services6.arcgis.com/bdPqSfflsdgFRVVM/arcgis/rest/servic
es
Syracuse
https://tiles.arcgis.com/tiles/bdPqSfflsdgFRVVM/arcgis/rest/servic
es
Tonawanda
https://gis1.tonawanda.ny.us/arcgis/rest/services
Watertown
https://maps.watertown-ny.gov/server/rest/services
White Plains
           https://services8.arcgis.com/JF5Jl1feo5zKtyZI/ArcGIS/rest/services
Planning
White Plains
https://tiles.arcgis.com/tiles/JF5Jl1feo5zKtyZI/arcgis/rest/services
Yonkers
See Westchester County
Yorktown
https://services8.arcgis.com/Imn7lbHecK3g17wG/arcgis/rest/servi
ces
North Carolina State GIS Servers
North Carolina Geospatial Data
Website: https://www.nconemap.gov
GIS: https://services.nconemap.gov/secure/rest/services

## Page 305

Parcel lines:  NC1Map_Parcels/MapServer/1
 8-5-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”

Tiled latest aerials: Imagery/Orthoimagery_Latest_cached/ImageServer
GIS: https://services5.arcgis.com/mSDBiLWaIfH92NqI/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/mSDBiLWaIfH92NqI/arcgis/rest/services
Emergency response
GIS: _ttps://sera.nc.gov/arcgis/rest/services
dead link 1
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://spartagis.ncem.org/arcgis/rest/services/Public
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://spartagis3.ncem.org/arcgis/rest/services
GIS: https://services1.arcgis.com/YBWrN5qiESVpqi92/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/YBWrN5qiESVpqi92/arcgis/rest/services
North Carolina Department of Administration
Website: https://www.doa.nc.gov
GIS: https://services3.arcgis.com/zMTrRjxZirPAKsKd/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/zMTrRjxZirPAKsKd/arcgis/rest/services
North Carolina Department of Commerce
Website: https://www.commerce.nc.gov
GIS: https://services7.arcgis.com/SEKZuPu27jfvDQ5b/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/SEKZuPu27jfvDQ5b/arcgis/rest/services
North Carolina Department of Environmental Quality
Website open data portal: https://data-ncdenr.opendata.arcgis.com
GIS: https://maps.deq.nc.gov/arcgis/rest/services
GIS: https://services2.arcgis.com/kCu40SDxsCGcuUWO/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/kCu40SDxsCGcuUWO/arcgis/rest/services
North Carolina Department of Natural and Cultural Resources
Website: https://www.ncdcr.gov/
GIS: https://gis2.ncdcr.gov/dncrgis/rest/services
8-9-2023 No tiled data
North Carolina Department of Public Instruction
Website: https://www.dpi.nc.gov
GIS: https://services.arcgis.com/jBUMuPL1Irp5kPy3/arcgis/rest/services
North Carolina Department of Transportation
Website: https://www.ncdot.gov/
GIS: https://gis11.services.ncdot.gov/arcgis/rest/services
8-9-2023 No tiled data
GIS: https://spatialags.vhb.com/arcgis/rest/services/NCDOT_PADT
8-9-2023 No tiled data

## Page 306

North Carolina Agriculture Multi-Hazard Threat Database
Website: https://www.ncmhtd.com/
GIS: https://www.ncmhtd.com/arcgis/rest/services
Has tiled data.  Do a Google search.  site:server_address   “wmts”
8-9-2023 Tiled data.  Several.  Go to top of this PDF file and search for ‘wmts'.
University of North Carolina at Chapel Hill
Website: https://maps.unc.edu/about
GIS: https://gismaps.unc.edu/arcgis/rest/services
8-9-2023 No tiled data
North Carolina various layers
GIS: https://fris.nc.gov/arcgis/rest/services     Flood risk data
GIS: https://services.gis.nc.gov/secure/rest/services
GIS: https://services1.arcgis.com/YfqBAUM5nWR3yhGP/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/YfqBAUM5nWR3yhGP/arcgis/rest/services
GIS: https://services5.arcgis.com/gRcZqepTaRC6tVZL/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/gRcZqepTaRC6tVZL/arcgis/rest/services
GIS: https://services6.arcgis.com/VLA0ImJ33zhtGEaP/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/VLA0ImJ33zhtGEaP/arcgis/rest/services
North Carolina Regional
Centralina Regional Council
Website: https://centralina.org
GIS: https://services7.arcgis.com/Mt0avId2EsFKSCRW/ArcGIS/rest/services
Durham-Chapel Hill-Carrboro Metropolitan Planning Organization
Website: https://www.dchcmpo.org
GIS: https://services.arcgis.com/eK97im1C4M6mxInu/arcgis/rest/services
High Country Council of Governments
Website: https://hccog.org
GIS: https://services1.arcgis.com/vj28eVZMB2OMIUh5/ArcGIS/rest/services
Piedmont Triad Regional Council
Website: https://www.ptrc.org
GIS: https://maps.ptrc.org/arcgis/rest/services
8-9-2023 No tiled data
/Recreation/Trails/MapServer
Trail.  Supports dynamic layers
North Carolina County GIS Servers
All counties are listed and have been checked for GIS
Website: https://www.lib.ncsu.edu/gis/counties.html
Among other things, the above page is a portal to county portals

## Page 307

Alamance
https://apps.alamance-nc.com/arcgis/rest/services
Alexander
https://maps.alexandercountync.gov/arcgis/rest/services
Alleghany
https://www.webgis.net/arcgis/rest/services/NC/Alleghany/MapSer
ver
Anson
 https://ansoncountygis.com/arcgis/rest/services
Avery
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Avery_AGOL/FeatureServer
Go to the top and search for ‘Avery’
Beaufort
https://services1.arcgis.com/oXsk9nimtmSEU8Ko/arcgis/rest/servi
ces
Ashe
https://gis.ashecountygov.com/arcgis/rest/services
Bertie
           https://services3.arcgis.com/tiupcc8dC1j2CPV5/arcgis/rest/services
Bladen
https://gis.bladenco.org/server/rest/services
Brunswick
https://geo.brunswickcountync.gov/arcgis/rest/services
Buncombe
https://gis.buncombecounty.org/arcgis/rest/services
Burke
https://gis.burkenc.org/arcgis/rest/services
Cabarrus
https://location.cabarruscounty.us/arcgisservices/rest/services
Cabarrus
https://location.cabarruscounty.us/accelaarc/rest/services
Cabarrus
https://services1.arcgis.com/cIoFE3yKRdfF5T0H/ArcGIS/rest/serv
ices
Cabarrus
https://tiles.arcgis.com/tiles/cIoFE3yKRdfF5T0H/arcgis/rest/servic
es
Caldwell
https://gis.caldwellcountync.org/arcgis/rest/services
https://services1.arcgis.com/t75DNILBKGwB5K5z/ArcGIS/rest/se
rvices
Baton Water Corporation
Camden
https://services7.arcgis.com/f8vjF7CsMeTPBIVC/arcgis/rest/servic
es
Carteret
https://arcgisweb.carteretcountync.gov/arcgis/rest/services
Carteret
https://services1.arcgis.com/CsRkg76wVkJL8hZq/arcgis/rest/servi
ces

## Page 308

Carteret
https://tiles.arcgis.com/tiles/CsRkg76wVkJL8hZq/arcgis/rest/servi
ces
Caswell
https://www.webgis.net/arcgis/rest/services/NC/Caswell_BldgNo/
MapServer
Caswell
https://www.webgis.net/arcgis/rest/services/NC/Caswelle911_Web
GIS/MapServer
Caswell
https://www.webgis.net/arcgis/rest/services/NC/Caswell/MapServe
r
Catawba
https://arcgis2.catawbacountync.gov/arcgis/rest/services
Chatham
https://gisservices.chathamcountync.gov/webapps/rest/services
Chatham
https://gisservices.chathamcountync.gov/chathamgis/rest/services
Chatham
https://gisservices.chathamcountync.gov/opendataagol/rest/services
Chatham
https://gisservices.chathamcountync.gov/projects/rest/services
Cherokee
https://maps.cherokeecounty-nc.gov/ccgis/rest/services
Chowan
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Chowan_Feature_Service/FeatureServer
Go to the top and search for ‘Chowan’
Columbus
WMS server
Craven
https://gis.cravencountync.gov/arcgis/rest/services
Cumberland
https://gis.co.cumberland.nc.us/server/rest/services
Cumberland
https://services1.arcgis.com/ssJTvu2LI9qRE1oE/ArcGIS/rest/servi
ces
Currituck
https://maps.currituckcountync.gov/arcgis/rest/services
Dare
WMS server
Davidson
https://webgis.co.davidson.nc.us/arcgis/rest/services
Davie
https://gis.daviecountync.gov/server/rest/services
Duplin
https://gis.duplinnc.gov/server/rest/services
Durham
https://webgis.durhamnc.gov/server/rest/services
Durham
https://services2.arcgis.com/G5vR3cOjh6g2Ed8E/ArcGIS/rest/serv
ices
Durham
https://tiles.arcgis.com/tiles/G5vR3cOjh6g2Ed8E/arcgis/rest/servic
es

## Page 309

Edgecombe
https://gis.edgecombecountync.gov/arcgis/rest/services
Forsyth
https://maps.co.forsyth.nc.us/arcgis/rest/services
Forsyth
https://terraweb.co.forsyth.nc.us/arcgis/rest/services
Forsyth
https://services1.arcgis.com/5Yf8nIJWE7cxpd3N/arcgis/rest/servic
es
Forsyth
https://tiles.arcgis.com/tiles/5Yf8nIJWE7cxpd3N/arcgis/rest/servic
es
Franklin
https://arcgis5.roktech.net/arcgis/rest/services/Franklin
Gaston
_ttps://gis.gastongov.com/publicgis/rest/services
dead link 1
Gaston
https://services6.arcgis.com/qnm8JRPoNeQjgcLi/arcgis/rest/servic
es
Gaston
https://tiles.arcgis.com/tiles/qnm8JRPoNeQjgcLi/arcgis/rest/servic
es
Gates
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/GatesStatic/FeatureServer
Go to the top and search for ‘Gates’
Graham
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/GrahamAGOL/FeatureServer
Go to the top and search for ‘Graham’
Granville
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Granville_Buildings/FeatureServer
Go to the top and search for ‘Granville’
Greene
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/GreeneStatic/FeatureServer
Go to the top and search for ‘Greene’
Guilford
https://gcgis.guilfordcountync.gov/arcgis/rest/services
Guilford
https://services5.arcgis.com/RR1v7NWFfwk98pUn/ArcGIS/rest/se
rvices
Guilford
https://tiles.arcgis.com/tiles/RR1v7NWFfwk98pUn/arcgis/rest/serv
ices
Halifax
Schneider Geospatial - ArcGIS server address is not public
Harnett
https://gis.harnett.org/arcgis/rest/services
Haywood
https://maps.haywoodcountync.gov/arcgis/rest/services
Henderson
https://arcgis4.roktech.net/arcgis/rest/services/Henderson

## Page 310

Hertford
___________
Hoke
https://maps.hokecounty.org/server/rest/services
Hyde
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/arcgis/rest/service
s/Hyde_AGOL/FeatureServer
Go to the top and search for ‘Hyde’
Iredell
https://icgis.co.iredell.nc.us/arcgis/rest/services
Iredell
https://gis1.co.iredell.nc.us/arcgis/rest/services
Jackson
https://gis.jacksonnc.org/jcgis/rest/services
Johnston
WMS server
Jones
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Jones_Bitek/FeatureServer
Go to the top and search for ‘Jones’
Lee
https://lee-arcgis.leecountync.gov/arcgis/rest/services
Lenoir
https://services3.arcgis.com/bDx73HOFAO3oSeDq/arcgis/rest/ser
vices
Lincoln
https://arcgisserver.lincolncounty.org/arcgis/rest/services
SSL problem
Lincoln
https://services8.arcgis.com/TaX0xkzgvxdv4n56/ArcGIS/rest/servi
ces
Lincoln
          https://tiles.arcgis.com/tiles/TaX0xkzgvxdv4n56/arcgis/rest/services
Macon
https://gis2.maconnc.org/arcgis/rest/services
Martin
https://gis.martincountyncgov.com/server/rest/services
Martin
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/MartinNC_Parcels/FeatureServer
Go to the top and search for ‘Martin’
Madison
https://services3.arcgis.com/NwIC4HArqo0JlKGT/arcgis/rest/servi
ces
McDowell
https://www.webgis.net/arcgis/rest/services/NC/McDowell/MapSe
rver
Mecklenburg
https://meckgis.mecklenburgcountync.gov/server/rest/services
Mecklenburg
https://codemap.mecklenburgcountync.gov/server/rest/services
Mecklenburg
https://meckags.mecklenburgcountync.gov/server/rest/services

## Page 311

Mecklenburg
https://services.arcgis.com/BWD3gDuaqc7SQmy7/arcgis/rest/servi
ces
Mecklenburg
https://tiles.arcgis.com/tiles/BWD3gDuaqc7SQmy7/arcgis/rest/ser
vices
Mitchell
_ttps://mapping.mitchellcounty.org/arcgis/rest/services  dead link 1
Montgomery
https://www.webgis.net/arcgis/rest/services/NC/Montgomery/Map
Server
Montgomery
https://services9.arcgis.com/omIyQysyaJipPNFR/arcgis/rest/servic
es
Moore
https://gis.moorecountync.gov/server/rest/services
Nash
They have a GIS but not ArcGIS
New Hanover
https://gis.nhcgov.com/server/rest/services
New Hanover
https://services1.arcgis.com/KHqZAAIdlp1670Ft/ArcGIS/rest/serv
ices
Northampton
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/NorthamptonService/FeatureServer
Go to the top and search for ‘Northampton’
Onslow
https://gismaps.onslowcountync.gov/arcgis/rest/services
Onslow
https://arcgis5.roktech.net/arcgis/rest/services/Onslow
Onslow
https://services7.arcgis.com/RLKshC6KfXm2kCVy/ArcGIS/rest/s
ervices
Onslow
https://tiles.arcgis.com/tiles/RLKshC6KfXm2kCVy/arcgis/rest/ser
vices
Orange
https://gis.orangecountync.gov/arcgis/rest/services
Pamlico
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Pamlico_ParcelService/FeatureServer
Go to the top and search for ‘Pamlico’
Pasquotank
https://services2.arcgis.com/0sC2n3LxYOcxBOg0/arcgis/rest/servi
ces
Pender
https://gis.pendercountync.gov/arcgis/rest/services
Pender
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/PenderDamageAssessment/FeatureServer
Go to the top and search for ‘Pender’

## Page 312

Perquimans
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Perquimans_addresspoints/FeatureServer
Go to the top and search for ‘Perquimans’
Person
https://gis.personcountync.gov/arcgis/rest/services
Pitt
https://gis.pittcountync.gov/gis/rest/services
Pitt
https://services7.arcgis.com/vyLlHMsTQ4c3bKwi/arcgis/rest/servi
ces
Pitt
https://tiles.arcgis.com/tiles/vyLlHMsTQ4c3bKwi/arcgis/rest/servi
ces
Polk
https://services1.arcgis.com/23uf7jKvz6SRPFWJ/ArcGIS/rest/serv
ices
Polk
https://tiles.arcgis.com/tiles/23uf7jKvz6SRPFWJ/arcgis/rest/servic
es
Randolph
https://gis.randolphcountync.gov/arcgis/rest/services
Randolph
https://gis.randolphcountync.gov/image/rest/services
Randolph
https://services3.arcgis.com/P4svYWrn4xHobm3O/arcgis/rest/serv
ices
Richmond
https://gis3.richmondnc.com/arcgis/rest/services
Robeson
https://arcgis4.roktech.net/arcgis/rest/services/robeson
Robeson
https://arcgis5.roktech.net/arcgis/rest/services/robeson
Rockingham
https://www.webgis.net/arcgis/rest/services/NC/Rockingham/Map
Server
Rowan
https://gis.rowancountync.gov/arcgis/rest/services
Rowan
https://services3.arcgis.com/lwqPl6kobtfot3r5/ArcGIS/rest/services
Rowan
https://tiles.arcgis.com/tiles/lwqPl6kobtfot3r5/arcgis/rest/services

Rutherford
https://gis.rutherfordcountync.gov/server/rest/services
Sampson
https://services3.arcgis.com/fM4kjZmPOS4ay2Ff/arcgis/rest/servic
es
Sampson
https://tiles.arcgis.com/tiles/fM4kjZmPOS4ay2Ff/arcgis/rest/servic
es
Scotland
https://services3.arcgis.com/bgKigTDifCMNj8OU/arcgis/rest/servi
ces
Stanly
https://services6.arcgis.com/w1igg0Q14weqYXUh/arcgis/rest/servi
ces

## Page 313

Stanly
https://tiles.arcgis.com/tiles/w1igg0Q14weqYXUh/arcgis/rest/servi
ces
Stokes
https://stokescountygis.com/server/rest/services
Surry
http://gis.surryinfo.net/arcgis/rest/services
not https
Surry
https://gis.surryinfo.net/arcgis/rest/services
SSL problem
Swain
https://arcgis5.roktech.net/arcgis/rest/services/Swain
No data

Transylvania
https://gis.transylvaniacounty.org/server/rest/services
Tyrrell
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/TyrrellService/FeatureServer
Go to the top and search for ‘Tyrrell’
Union
https://atlas.unioncountync.gov/server/rest/services
Vance
https://services6.arcgis.com/pET3krhY1T0smsXf/arcgis/rest/servic
es
Wake
https://maps.wakegov.com/arcgis/rest/services
Wake
https://maps.wake.gov/arcgis/rest/services
Wake
https://services1.arcgis.com/a7CWfuGP5ZnLYE7I/ArcGIS/rest/ser
vices
Wake
https://tiles.arcgis.com/tiles/a7CWfuGP5ZnLYE7I/arcgis/rest/servi
ces
Wake
https://services2.arcgis.com/oqISN6Dt6ax5xklN/ArcGIS/rest/servi
ces
Public schools
Wake
           https://tiles.arcgis.com/tiles/oqISN6Dt6ax5xklN/arcgis/rest/services
Warren
https://arcgis5.roktech.net/arcgis/rest/services/Warren
Washington
https://services6.arcgis.com/hBMRLv0wWV0IhJ8I/arcgis/rest/serv
ices
Watauga
https://gissvr.watgov.org/arcgis/rest/services
Watauga
https://services2.arcgis.com/wdQEqhSQSuYA89VW/arcgis/rest/se
rvices
Watauga
https://tiles.arcgis.com/tiles/wdQEqhSQSuYA89VW/arcgis/rest/se
rvices
Wayne
https://services5.arcgis.com/q2nSlChj7QgGTANO/arcgis/rest/servi
ces

## Page 314

Wilkes
https://gis.wilkescounty.net/arcgis/rest/services
Wilkes
https://services.arcgis.com/F0NVAWW1QWjo230B/arcgis/rest/ser
vices
Wilson
https://gis.wilson-co.com/arcgis/rest/services
Wilson
https://services7.arcgis.com/vnRUSjPdUqxb6IDG/ArcGIS/rest/ser
vices
Wilson
https://tiles.arcgis.com/tiles/vnRUSjPdUqxb6IDG/arcgis/rest/servi
ces
Yadkin
https://gis.yadkincountync.gov/arcgis/rest/services
Yancey
https://gis.yanceycountync.org/server/rest/services
North Carolina City, Town, Village, etc GIS Servers
Alleghany
https://www.webgis.net/arcgis/rest/services/NC/Alleghany/MapSer
ver
Apex
https://services1.arcgis.com/nry3yyvaEfskMEXA/ArcGIS/rest/serv
ices
Apex
https://tiles.arcgis.com/tiles/nry3yyvaEfskMEXA/arcgis/rest/servic
es
Asheboro
See Randolph County
Asheville
https://gis.ashevillenc.gov/server/rest/services
Asheville
https://services.arcgis.com/aJ16ENn1AaqdFlqx/arcgis/rest/services
See also Buncombe County
Asheville
https://tiles.arcgis.com/tiles/aJ16ENn1AaqdFlqx/arcgis/rest/services
Beaufort
See Carteret County
Belmont
See Gaston County
Blowing Rock
https://services5.arcgis.com/qWbsNTne6eidnUv9/ArcGIS/rest/serv
ices
Boone
https://gisviewer.townofboone.net/arcgis/rest/services
Burlington
https://maps.regisnc.org/arcgis/rest/services
Burlington
          https://spatialags.vhb.com/arcgis/rest/services/38912_BurlingtonNC
Butner
See Granville county
Cabarrus
See Cabarrus county

## Page 315

Cambridge
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Cambridge_Service/FeatureServer
Go to the top and search for ‘Cambridge’
Carrboro
https://tocgis.ci.carrboro.nc.us/server/rest/services
Cary
_ttps://maps.townofcary.org/arcgis/rest/services
dead link 1
Cary
_ttps://maps.townofcary.org/arcgis1/rest/services
dead link 1
Cary
https://iot.connectedcary.org/server/rest/services
Cary
https://services2.arcgis.com/l4TwMwwoiuEVRPw9/ArcGIS/rest/s
ervices
Cary
https://tiles.arcgis.com/tiles/l4TwMwwoiuEVRPw9/arcgis/rest/ser
vices
Chapel Hill
https://gisweb.townofchapelhill.org/arcgis/rest/services
Chapel Hill
https://aom-us.nearmap.com/arcgis/rest/services
Chapel Hill
https://services2.arcgis.com/7KRXAKALbBGlCW77/arcgis/rest/se
rvices
Chapel Hill
https://tiles.arcgis.com/tiles/7KRXAKALbBGlCW77/arcgis/rest/se
rvices
Charlotte
https://gis.charlottenc.gov/arcgis/rest/services
Charlotte
https://cltwmaps.ci.charlotte.nc.us/arcgis/rest/services
Charlotte
https://services.arcgis.com/9Nl857LBlQVyzq54/ArcGIS/rest/servic
es
Charlotte
https://tiles.arcgis.com/tiles/9Nl857LBlQVyzq54/arcgis/rest/servic
es
Charlotte
https://services3.arcgis.com/t6ulOHDjzlBrOlof/ArcGIS/rest/servic
es
Fire department
Charlotte
https://services6.arcgis.com/mPOesUQpvBzlaIKQ/arcgis/rest/servi
ces
Charlotte
https://tiles.arcgis.com/tiles/mPOesUQpvBzlaIKQ/arcgis/rest/servi
ces
Chatham Park
See Wake County
Clayton
https://cw2.townofclaytonnc.org/gis/rest/services
Cleveland
https://www.webgis.net/arcgis/rest/services/NC/Cleveland_Topo/I
mageServer
Cleveland
https://www.webgis.net/arcgis/rest/services/NC/Cleveland/MapSer
ver
Clinton
https://services3.arcgis.com/qk51vpz9llUiMFK3/arcgis/rest/servic
es

## Page 316

Concord
https://maps2.concordnc.gov/server/rest/services
Davie
https://gis.daviecountync.gov/server/rest/services
Durham
https://webgis.durhamnc.gov/server/rest/services
See also Durham county
Elon
https://maps.regisnc.org/arcgis/rest/services
Fayetteville
          https://services.arcgis.com/j3zNT485kmwrBtMJ/arcgis/rest/services
Fayetteville
https://tiles.arcgis.com/tiles/j3zNT485kmwrBtMJ/arcgis/rest/servic
es

Forest
___________
Franklin
https://arcgis4.roktech.net/arcgis/rest/services/Franklin
Fuquay-Varina
https://services3.arcgis.com/GrxjHvUy8y7KXoVk/ArcGIS/rest/ser
vices/Existing_Zoning/FeatureServer
Gastonia
_ttps://coggis.cityofgastonia.com/cogwa/rest/services   dead link 1
Gastonia
https://services3.arcgis.com/u6Nvh8zpOQRNNRJi/arcgis/rest/serv
ices
Gastonia
https://tiles.arcgis.com/tiles/u6Nvh8zpOQRNNRJi/arcgis/rest/servi
ces
Goldsboro
https://services1.arcgis.com/OWMFbun3mxdAXbUM/ArcGIS/rest
/services
Graham
https://maps.regisnc.org/arcgis/rest/services
Greensboro
https://gis.greensboro-nc.gov/arcgis/rest/services
Greensboro
https://services1.arcgis.com/A7KFW0gHh8qBaXk3/ArcGIS/rest/s
ervices
Greensboro
https://tiles.arcgis.com/tiles/A7KFW0gHh8qBaXk3/arcgis/rest/ser
vices
Greenville
https://services2.arcgis.com/VSBiNLpPiT129XQl/ArcGIS/rest/ser
vices
Greenville
https://tiles.arcgis.com/tiles/VSBiNLpPiT129XQl/arcgis/rest/servi
ces
Havelock
See Craven County
Hendersonville
https://cw.hendersonvillenc.gov/arcgis/rest/services
Table of contents disabled

## Page 317

Hickory
https://services6.arcgis.com/ypDgb6uhGtJ8MYK9/ArcGIS/rest/ser
vices
Highpoint
https://gisentapp01.highpointnc.gov/server/rest/services
Hillsborough
__________
Holly Springs
https://services1.arcgis.com/b6kciy3dYoQmo0t3/ArcGIS/rest/servi
ces
Holly Springs           https://tiles.arcgis.com/tiles/b6kciy3dYoQmo0t3/arcgis/rest/services
Indian Trail
https://services8.arcgis.com/7YUdLQ8pDBKU1XYI/ArcGIS/rest/s
ervices
Iredell
__________
Jacksonville
https://cjaxgisweb.jacksonvillenc.gov/image/rest/services
Jacksonville
https://services.arcgis.com/p6AtkBQ0z2Evsivu/arcgis/rest/services
Jamestown
They have a GIS based on Google maps
Kernersville
__________
King
https://www.webgis.net/arcgis/rest/services/NC/CityOfKing/MapS
erver
Kings Mountain
__________
Kinston
https://services5.arcgis.com/oHyVM17u2FMyV4oB/arcgis/rest/ser
vices
Kinston
https://tiles.arcgis.com/tiles/oHyVM17u2FMyV4oB/arcgis/rest/ser
vices
Laurinburg
See Scotland County
Leland
https://services8.arcgis.com/BAAWxWvGDwvQaRgQ/arcgis/rest/
services
Brunswick Regional Water and Sewer
Lenoir
_________
Lumberton
Integritygis - ArcGIS server address is not public
McDowell
https://www.webgis.net/arcgis/rest/services/NC/McDowell_aerial1
7/MapServer
McDowell
https://www.webgis.net/arcgis/rest/services/NC/McDowell/MapSe
rver

## Page 318

Mebane
https://services8.arcgis.com/pqfZyBvxpstAt1gO/ArcGIS/rest/servi
ces
Mebane
          https://tiles.arcgis.com/tiles/pqfZyBvxpstAt1gO/arcgis/rest/services
Morganton
https://gis.morgantonnc.gov/server/rest/services
Mooresville
https://gis.mooresvillenc.gov/gisadmin/rest/services
Mooresville
https://services.arcgis.com/ud8kSLNkfBb9WX8U/arcgis/rest/servi
ces
Morrisville
__________
Nags Head
https://arcgis.mobile311.com/arcgis/rest/services/NorthCarolina/N
agsHeadNC/MapServer
Nags Head
https://services1.arcgis.com/ooP6YxNTswasez32/arcgis/rest/servic
es
Nags Head
https://tiles.arcgis.com/tiles/ooP6YxNTswasez32/arcgis/rest/servic
es
New Bern
https://gis.newbernnc.gov/arcgis/rest/services
New Bern
https://services.arcgis.com/dgTfTbo7vv4DUTMz/arcgis/rest/servic
es
New Bern
https://tiles.arcgis.com/tiles/dgTfTbo7vv4DUTMz/arcgis/rest/servi
ces
Oak Island
          https://services1.arcgis.com/bj5mi85xssAepres/ArcGIS/rest/services
Onslow
https://arcgis5.roktech.net/arcgis/rest/services/Onslow
Oxford
See Granville County

Raleigh
https://maps.raleighnc.gov/arcgis/rest/services
Raleigh
https://maps.raleighnc.gov/images/rest/services

Raleigh
          https://services.arcgis.com/v400IkDOw1ad7Yad/arcgis/rest/services
Raleigh
https://tiles.arcgis.com/tiles/v400IkDOw1ad7Yad/arcgis/rest/servic
es
Rocky Mount            https://services.arcgis.com/4MdqIsNzxG7xyTvf/arcgis/rest/services
Salisbury
https://services.arcgis.com/FKrJWv8CWiYT6Rsn/arcgis/rest/servi
ces
Salisbury
https://tiles.arcgis.com/tiles/FKrJWv8CWiYT6Rsn/arcgis/rest/serv
ices
Sampson
_____________

## Page 319

Sanford
See Lee County
Southern Pines
https://services9.arcgis.com/AtyX8cqqHxBiQIog/arcgis/rest/servic
es
Stanly
____________
Statesville
https://services2.arcgis.com/WbGEgSzGTEPg4fr6/ArcGIS/rest/ser
vices
Statesville
https://tiles.arcgis.com/tiles/WbGEgSzGTEPg4fr6/arcgis/rest/servi
ces
Transylvania
https://www.webgis.net/arcgis/rest/services/NC/Transylvania/Map
Server
Troy
https://services7.arcgis.com/BUt1m9lcWX8yDHxX/ArcGIS/rest/s
ervices
Vance
____________
Wake Forest
https://twfgis.wakeforestnc.gov/server/rest/services
Wake Forest
https://services1.arcgis.com/gqTCvanrwF2z2HEu/ArcGIS/rest/serv
ices
Wake Forest
https://tiles.arcgis.com/tiles/gqTCvanrwF2z2HEu/arcgis/rest/servic
es
Walnut Cove
https://services6.arcgis.com/XsdTa0Wx7CWWHG4Z/ArcGIS/rest/
services
Waxhaw
https://services2.arcgis.com/Sa3FPjCP8681JQgz/ArcGIS/rest/servi
ces
Wilkesboro
https://services3.arcgis.com/xb2qUX5xzfQSbb1s/ArcGIS/rest/serv
ices
Wilmington
https://geohub.wilmingtonnc.gov/hosting/rest/services
Wilmington
https://gis.wilmingtonnc.gov/arcgis/rest/services
Wilmington
https://services1.arcgis.com/GwaLJVJq0Y6voqEc/ArcGIS/rest/ser
vices
Wilmington
https://tiles.arcgis.com/tiles/GwaLJVJq0Y6voqEc/arcgis/rest/servi
ces
Wilson
https://services2.arcgis.com/EkGnQVqymucRyoIM/ArcGIS/rest/se
rvices

Winston-Salem
See Forsyth county

## Page 320

North Dakota State GIS Servers
North Dakota Geographic Information Systems
Website: https://www.gis.nd.gov
GIS: https://ndgishub.nd.gov/arcgis/rest/services
Parcels for many counties: NDGISHUB_Parcels/FeatureServer
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/GOcSXpzwBHyk2nog/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/GOcSXpzwBHyk2nog/arcgis/rest/services
North Dakota Department of  Health
Website: https://www.hhs.nd.gov/health
GIS: https://services3.arcgis.com/Fc1HANRtm0NzrqlS/arcgis/rest/services
Table of contents displays but the each layer requires a token
North Dakota Department of Transportation
Website: https://www.dot.nd.gov/
GIS: https://gis.dot.nd.gov/arcgis/rest/services/external
8-9-2023 No tiled data
GIS: https://gis.dot.nd.gov/ArcGIS/rest/services/external
8-9-2023 No tiled data
GIS: https://maps.loadpasspermits.com/arcgis/rest/services
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
North Dakota County GIS Servers
All counties are listed and have been checked for GIS.
Adams
No GIS found
Barnes
No GIS found
Benson
No GIS found
Billings
MapServer GIS
Bottineau
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/BottineauNDFeatures/FeatureServer
Go to the top and search for ‘BottineauND’
Bottineau
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/BottineauNDCadastral/MapServer
Go to the top and search for ‘BottineauND’
Bowman
MapServer GIS

## Page 321

Burke
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/BurkeNDFeatures/FeatureServer
Go to the top and search for ‘BurkeND’
Burke
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/BurkeNDCadastral/MapServer
Go to the top and search for ‘BurkeND’
Burleigh
https://services2.arcgis.com/8r0lsT7QHelkANsD/ArcGIS/rest/servi
ces
Cass
https://gisweb.casscountynd.gov/arcgis/rest/services
Cass
https://services2.arcgis.com/j6jJDjDMig3bSqKL/arcgis/rest/servic
es
Cavalier
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es
Go to the top and search for ‘CavalierND’
Cavalier
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/CavalierNDAerial2017/MapServer
Go to the top and search for ‘CavalierND’
Dickey
No GIS found
Divide
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/DivideNDFeatures/FeatureServer
Go to the top and search for ‘DivideND’
Divide
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/DivideNDCadastral/MapServer
Dunn
https://mapserver01.gworks.com/arcgis/rest/services/Dunn_County
_ND_EM/MapServer
Dunn
https://services9.arcgis.com/4dMIJArpVSm5lXfT/ArcGIS/rest/ser
vices
Eddy
No GIS found
Emmons
https://services3.arcgis.com/zDNWy26tIMyYaGcC/arcgis/rest/serv
ices
Emmons
https://tiles.arcgis.com/tiles/zDNWy26tIMyYaGcC/arcgis/rest/serv
ices
Foster
WMS server
Golden Valley
https://mapserver01.gworks.com/arcgis/rest/services/Golden_Valle
y_County_ND_Assessor/MapServer
Go to the top and search for ‘Golden_Valley’

## Page 322

Grand Forks
https://gfgis1.nd.gov/arcgis/rest/services
Grand Forks
https://www.gfgis.com/arcgis/rest/services
Grand Forks
_ttps://www.gfgis.com/enterprise/rest/services
dead link 1
Grand Forks
https://services5.arcgis.com/tEvkdB384rqq9Ook/ArcGIS/rest/servi
ces
Grand Forks
           https://tiles.arcgis.com/tiles/tEvkdB384rqq9Ook/arcgis/rest/services
Grant
https://mapserver01.gworks.com/arcgis/rest/services/Grant_County
_ND_Assessor/MapServer
Go to the top and search for ‘Grant’
Griggs
No GIS found
Hettinger
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/HettingerNDFeatures/FeatureServer
Go to the top and search for ‘HettingerND’
Hettinger
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/HettingerNDCadastral/MapServer
Kidder
No GIS found
LaMoure
https://mapserver01.gworks.com/arcgis/rest/services/LaMoure_Co
unty_ND_Tax_Director/MapServer
Go to the top and search for ‘LaMoure’
Logan
No GIS found
McHenry
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/McHenryNDFeatures/FeatureServer
Go to the top and search for ‘McHenryND’
McHenry
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/McHenryNDCadastral/MapServer
McIntosh
WMS server
McKenzie
https://mckenziegis.co.mckenzie.nd.us/server/rest/services
McKenzie
https://services8.arcgis.com/RPIW3ufPaKmSTpzr/ArcGIS/rest/ser
vices
McLean
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/McleanNDFeatures/FeatureServer
Go to the top and search for ‘McLeanND’
McLean
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/McleanNDCadastral/MapServer
Go to the top and search for ‘McLeanND’

## Page 323

Mercer
They have a GIS but it is not ArcGIS
Morton
https://services2.arcgis.com/KK9EVAUoqJyQSD0q/ArcGIS/rest/s
ervices
Morton
https://tiles.arcgis.com/tiles/KK9EVAUoqJyQSD0q/arcgis/rest/ser
vices
Mountrail
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/MountrailNDFeatures/FeatureServer
Go to the top and search for ‘MountrailND’
Mountrail
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/MountrailNDCadastral/MapServer
Go to the top and search for ‘MountrailND’
Nelson
MapServer GIS
Oliver
They have GIS staff but server address not found.
Pembina
WMS server
Pierce
No GIS found
Ramsey
https://gis.co.ramsey.nd.us/server/rest/services
Ransom
No GIS found
Renville
https://services5.arcgis.com/jGqB8YbZAHp2DDax/ArcGIS/rest/se
rvices
Renville
https://tiles.arcgis.com/tiles/jGqB8YbZAHp2DDax/arcgis/rest/serv
ices
Richland
https://gis.co.richland.nd.us/arcgis/rest/services
Rolette
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/RoletteNDFeatures/FeatureServer
Go to the top and search for ‘RoletteND’
Rolette
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/RoletteNDTribalTrust/MapServer
Sargent
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/SargentNDFeatures/FeatureServer
Go to the top and search for ‘SargentND’
Sargent
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/SargentNDCadastral/MapServer
Sheridan
MapServer GIS

## Page 324

Sioux
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/SiouxNDFeatures/FeatureServer
Go to the top and search for ‘SiouxND’
Sioux
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/SiouxNDCadastral/MapServer
Slope
MapServer GIS
Stark
________ check for new server
Steele
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/SteeleNDFeatures/FeatureServer
Go to the top and search for ‘SteeleND’
Steele
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/SteeleNDCadastral/MapServer
Stutsman
GIS not found
Towner
GIS not found
Traill
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/TraillNDFeatures/FeatureServer
Go to the top and search for ‘TraillND’
Traill
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/TraillNDCadastral/MapServer
Walsh
No GIS found
Ward
https://services2.arcgis.com/tvgNL3LD8EYwagwG/arcgis/rest/serv
ices
Ward
https://tiles.arcgis.com/tiles/tvgNL3LD8EYwagwG/arcgis/rest/serv
ices
Wells
No GIS found
Williams
https://willgis.co.williams.nd.us/willgis/rest/services
Williams
https://services1.arcgis.com/D85sDZoJyameepNh/ArcGIS/rest/ser
vices
Williams
https://tiles.arcgis.com/tiles/D85sDZoJyameepNh/arcgis/rest/servic
es
North Dakota City, Town, Village, etc GIS Servers
Bismarck
https://bisgis.bismarcknd.gov/server/rest/services
Bismarck
https://services1.arcgis.com/XxHmL09eFqJWI0gE/arcgis/rest/serv
ices

## Page 325

Bismarck
https://tiles.arcgis.com/tiles/XxHmL09eFqJWI0gE/arcgis/rest/servi
ces
Cavalier
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/CavalierNDFeatures/FeatureServer
Go to the top and search for ‘CavalierND'
Cavalier
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/CavalierNDAerial2017/MapServer
Go to the top and search for ‘CavalierND'
Dickinson
https://gis.dickinsongov.com/server/rest/services
Fargo
https://gis.cityoffargo.com/arcgis/rest/services
Fargo
https://acquisition.cityoffargo.com/arcgis/rest/services

Grand Forks
https://www.gfgis.com/arcgis/rest/services
Hazen
See Mercer County
Hettinger
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/HettingerNDFeatures/FeatureServer
Go to the top and search for ‘Hettinger’
McHenry
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/McHenryNDFeatures/FeatureServer
Go to the top and search for ‘McHenryND’
McHenry
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/McHenryNDCadastral/MapServer
Go to the top and search for ‘McHenryND’
Minot
https://services6.arcgis.com/JVhcJQfCdTgGR2OL/ArcGIS/rest/ser
vices
Rolette
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/RoletteNDFeatures/FeatureServer
Go to the top and search for ‘RoletteND’
Steele
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/SteeleNDFeatures/FeatureServer
Go to the top and search for ‘SteeleND’
Steele
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/SteeleNDCadastral/MapServer
Go to the top and search for ‘SteeleND’
West Fargo
https://gis.westfargond.gov/arcgis/rest/services
West Fargo
https://map.westfargond.gov/arcgis/rest/services

## Page 326

Ohio State GIS Servers
Ohio Spatial Information Portal
Website:
https://das.ohio.gov/technology-and-strategy/OGRIP
GIS: https://maps.ohio.gov/arcgis/rest/services
GIS: https://maps.ohio.gov/image/rest/services
Ohio Office of Information Technology
Website: https://das.ohio.gov/about/office-of-information-technology
GIS: https://services2.arcgis.com/MlJ0G8iWUyC7jAmu/ArcGIS/rest/services
Ohio Emergency Management Agency
Website: https://ema.ohio.gov
GIS: https://services6.arcgis.com/zxOMWqh0yAD6mMsJ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/zxOMWqh0yAD6mMsJ/arcgis/rest/services
Ohio Department of Agriculture
Website: https://agri.ohio.gov
GIS: https://services5.arcgis.com/Md3L6VMzW1XYzZds/ArcGIS/rest/services
Ohio Department of Natural Resources
Website: https://ohiodnr.gov
GIS: https://gis.ohiodnr.gov/arcgis/rest/services
8-9-2023 No tiled data
GIS: https://gis.ohiodnr.gov/arcgis_site2/rest/services
8-9-2023 No tiled data
GIS: https://gis2.ohiodnr.gov/arcgis/rest/services
Parcel lines:
OIT_Services/ODNR_Landbase_CNTY_TWP_OLS_PARC/MapS
erver/5-6
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.ohiodnr.gov/image/rest/services
GIS: https://services5.arcgis.com/ajRlmtxbNBjZggOT/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/ajRlmtxbNBjZggOT/arcgis/rest/services
Ohio Department of Transportation
Website: https://www.transportation.ohio.gov/
GIS: https://odotgis.dot.state.oh.us/arcgis/rest/services
8-9-2023 No tiled data
GIS: _ttps://collectornew.dot.state.oh.us/arcgis/rest/services
dead link 1
8-9-2023 No tiled data
GIS: _ttps://collectortstnew.dot.state.oh.us/arcgis/rest/services
dead link 1
8-9-2023 No tiled data
GIS: https://tims.dot.state.oh.us/ags/rest
GIS: https://services1.arcgis.com/1AlElnGrgBM62OSj/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/1AlElnGrgBM62OSj/arcgis/rest/services

## Page 327

Ohio Environmental Protection Agency
Website: https://epa.ohio.gov
GIS: https://geo.epa.ohio.gov/arcgis/rest/services
GIS: https://services2.arcgis.com/dPMsmH8HlhhfDWQu/ArcGIS/rest/services
Public Utilities Commission of Ohio
Website: https://puco.ohio.gov
GIS: https://maps.puco.ohio.gov/arcgis/rest/services
8-9-2023 No tiled data
Ohio various layers
GIS: https://services2.arcgis.com/4XlTp6SwwtAtXgjj/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/4XlTp6SwwtAtXgjj/arcgis/rest/services
Ohio Regional
Ohio-Kentucky-Indiana Regional Council of Governments (OKI)
Website: https://www.oki.org
GIS: https://gis.oki.org/server/rest/services
Metro Parks
Website: https://metroparkstoledo.com
GIS: https://services1.arcgis.com/SvdVZfVAhlYe04Tl/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/SvdVZfVAhlYe04Tl/arcgis/rest/services
Miami Valley Regional Planning Commission
Website: https://www.mvrpc.org/about-mvrpc
GIS: https://services.arcgis.com/3TIUdMHOqnLBrZEH/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/3TIUdMHOqnLBrZEH/arcgis/rest/services
Mid-Ohio Regional Planning Commission
Website: https://www.morpc.org
GIS: https://arcserver.morpc.org/arcgis/rest/services

Metro Sewer District Greater Cincinnati
Website: https://www.msdgc.org
GIS: _ttps://gis.msdgc.org/arcgist/rest/services
dead link 1
8-9-2023 No tiled data
Northeast Ohio Regional Sewer District
Website: https://www.neorsd.org
GIS: https://neogis.neorsd.org/arcgis/rest/services
8-9-2023 No tiled data
GIS: https://services1.arcgis.com/SPFcZzbZkZvJ7Vki/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/SPFcZzbZkZvJ7Vki/arcgis/rest/services
Eastgate Regional Council of Governments

## Page 328

Website: https://eastgatecog.org
GIS: https://services1.arcgis.com/Tp2BiFFnIouuk00r/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Tp2BiFFnIouuk00r/arcgis/rest/services
Northwestern Water & Sewer District
Website: https://www.nwwsd.org
GIS: https://services1.arcgis.com/lAWlC1VwZYAIzeQJ/ArcGIS/rest/services
Ohio Township GIS Servers
Beaver Creek
https://services1.arcgis.com/4aXVop4P5CmtTU19/ArcGIS/rest/ser
vices
Ohio County GIS Servers
Allen
https://gis.allencountyohio.com/arcgis/rest/services
Ashland
https://gis.ashland-ohio.com/arcgis/rest/services
Ashtabula
https://parcelmap.ashtabulacounty.us/arcgis/rest/services
Ashtabula
https://services3.arcgis.com/LbREO35fKGJZptlq/ArcGIS/rest/serv
ices
Ashtabula
https://tiles.arcgis.com/tiles/LbREO35fKGJZptlq/arcgis/rest/servic
es
Athens
https://services2.arcgis.com/2zE4x6y8cTIstSBE/ArcGIS/rest/servi
ces
Athens
           https://tiles.arcgis.com/tiles/2zE4x6y8cTIstSBE/arcgis/rest/services
Auglaize
https://gis.auglaizecounty.org/arcgis/rest/services
Belmont
https://gis.belcogis.com/hosting/rest/services
Belmont
https://services7.arcgis.com/GfbqZj5EAUgRd4ES/arcgis/rest/servi
ces
Butler
https://maps.butlercountyauditor.org/arcgis/rest/services
Carroll
https://services8.arcgis.com/dZSJY7MSQPhysZUz/arcgis/rest/serv
ices
Carroll
https://tiles.arcgis.com/tiles/dZSJY7MSQPhysZUz/arcgis/rest/serv
ices
Champaign
https://services5.arcgis.com/HBIN2hfRscrws7eM/arcgis/rest/servic
es
Champaign
https://tiles.arcgis.com/tiles/HBIN2hfRscrws7eM/arcgis/rest/servic
es

## Page 329

Clark
https://ago.clarkcountyohio.gov/ccoarcgis/rest/services
Clark
https://services3.arcgis.com/VYdZ1CPI3COqRVej/ArcGIS/rest/ser
vices
Clark
https://tiles.arcgis.com/tiles/VYdZ1CPI3COqRVej/arcgis/rest/servi
ces
Clermont
https://maps.clermontauditor.org/arcgis/rest/services
Clermont
_ttps://maps4.clermontauditor.org/arcgis/rest/services   dead link 1
Clermont
https://maps5.clermontcountyohio.gov/arcgis/rest/services
SSL problem
Clermont
_ttps://maps13.clermontauditor.org/arcgis/rest/services  dead link 1
Clinton
https://services1.arcgis.com/tAhcHWpOD9ygNPbJ/arcgis/rest/serv
ices
Columbiana
https://services8.arcgis.com/234WKrCI77bh5yOY/arcgis/rest/servi
ces
Columbiana
https://tiles.arcgis.com/tiles/234WKrCI77bh5yOY/arcgis/rest/servi
ces
Cuyahoga
https://gis.cuyahogacounty.us/server/rest/services
Table of contents disabled
Cuyahoga
https://services7.arcgis.com/GXM8JipKyc0m6HBi/ArcGIS/rest/ser
vices
Cuyahoga
https://tiles.arcgis.com/tiles/GXM8JipKyc0m6HBi/arcgis/rest/servi
ces
Cuyahoga
https://services8.arcgis.com/1cKSe8lh4duMZ8W0/ArcGIS/rest/ser
vices
County Planning Commission
Cuyahoga
https://tiles.arcgis.com/tiles/1cKSe8lh4duMZ8W0/arcgis/rest/servi
ces
Delaware
https://services2.arcgis.com/ziXVKVy3BiopMCCU/ArcGIS/rest/s
ervices
Delaware
https://tiles.arcgis.com/tiles/ziXVKVy3BiopMCCU/arcgis/rest/ser
vices
Drake
https://services8.arcgis.com/7y4HUzu9j7NevHP9/arcgis/rest/servic
es
Drake
https://tiles.arcgis.com/tiles/7y4HUzu9j7NevHP9/arcgis/rest/servic
es
Erie
https://maps.eriecounty.oh.gov/arcgis/rest/services
Erie
https://maps7.eriecounty.oh.gov/arcgis/rest/services
Fairfield
https://gis.co.fairfield.oh.us/arcgis/rest/services

## Page 330

Franklin
https://gis.franklincountyohio.gov/hosting/rest/services
Franklin
https://services1.arcgis.com/7r2Wl09a1Apy459r/ArcGIS/rest/servi
ces
Franklin
          https://tiles.arcgis.com/tiles/7r2Wl09a1Apy459r/arcgis/rest/services
Fulton
https://gis.fultoncountyoh.com/arcgis/rest/services
Geauga
https://geaugarealink.geauga.oh.gov/Geocortex/Essentials/REST/si
tes/GeaugaRL/map/mapservices
The layers on the above server are structured a bit
differently and may or may not display as standard ArcGIS
data.
Geauga
https://services3.arcgis.com/otmFGc3Z1CITN3V3/arcgis/rest/servi
ces
Geauga
https://tiles.arcgis.com/tiles/otmFGc3Z1CITN3V3/arcgis/rest/servi
ces
Greene
https://gis.greenecountyohio.gov/webgis2/rest/services
Greene
https://gis.greenecountyohio.gov/webgis3/rest/services
Greene
https://services8.arcgis.com/pqnSvb0IQVVHEYRu/ArcGIS/rest/se
rvices
Greene
https://tiles.arcgis.com/tiles/pqnSvb0IQVVHEYRu/arcgis/rest/serv
ices
Hamilton
https://cagisonline.hamilton-co.org/arcgis/rest/services
Table of contents disabled
Hardin
Not a public-facing ArcGIS server
Holmes
https://gis.co.holmes.oh.us/server/rest/services
Holmes
           https://services6.arcgis.com/JuJ3otBHQoYlrmJI/arcgis/rest/services
Holmes
           https://tiles.arcgis.com/tiles/JuJ3otBHQoYlrmJI/arcgis/rest/services
Knox
https://services6.arcgis.com/Xar2ihPAmZ2Wc8fe/arcgis/rest/servic
es
Knox
https://tiles.arcgis.com/tiles/Xar2ihPAmZ2Wc8fe/arcgis/rest/servic
es
Lake
https://gis.lakecountyohio.gov/arcgis/rest/services
Licking
https://apps.lickingcounty.gov/arcgis/rest/services
Logan
https://services9.arcgis.com/mFxO7gBbusFBQ5o9/arcgis/rest/servi
ces
Logan
https://tiles.arcgis.com/tiles/mFxO7gBbusFBQ5o9/arcgis/rest/servi
ces

## Page 331

Lorain
https://maps.lcauditor.com/hosting/rest/services
Lorain
https://services1.arcgis.com/vGBb7WYV10mOJRNM/arcgis/rest/s
ervices
Lorain
https://tiles.arcgis.com/tiles/vGBb7WYV10mOJRNM/arcgis/rest/s
ervices
Lucas
https://lcaudgis.co.lucas.oh.us/gisaudimage/rest/services
Lucas
https://lcaudgis.co.lucas.oh.us/gisaudserver/rest/services
Mahoning
https://gisapp.mahoningcountyoh.gov/arcgis/rest/services
Mahoning
https://services3.arcgis.com/ngoyBHXXyqVFvjtM/ArcGIS/rest/ser
vices
Public Health
Marion
https://mcogis.co.marion.oh.us/arcgis/rest/services
Marion
          https://services.arcgis.com/T6eVl85nNm64wxjn/arcgis/rest/services
Marion
https://tiles.arcgis.com/tiles/T6eVl85nNm64wxjn/arcgis/rest/servic
es
Medina
https://services5.arcgis.com/m37BbrYBtVXq1nb8/ArcGIS/rest/ser
vices
Medina
https://tiles.arcgis.com/tiles/m37BbrYBtVXq1nb8/arcgis/rest/servi
ces
Meigs
https://services.arcgis.com/izF1Oz3upCFoiHfD/arcgis/rest/services
Meigs
          https://tiles.arcgis.com/tiles/izF1Oz3upCFoiHfD/arcgis/rest/services
Mercer
https://services5.arcgis.com/Hym5ktUHlHiJ3AfR/arcgis/rest/servic
es
Mercer
https://tiles.arcgis.com/tiles/Hym5ktUHlHiJ3AfR/arcgis/rest/servic
es
Monroe
https://services8.arcgis.com/ToWOUVqNUhbTXzVc/ArcGIS/rest/
services
Monroe
https://tiles.arcgis.com/tiles/ToWOUVqNUhbTXzVc/arcgis/rest/se
rvices
Montgomery
https://engineer01.gomvo.org/arcgis/rest/services
Morgan
https://services8.arcgis.com/cYuOLPdETvKbspkC/arcgis/rest/servi
ces
Morgan
https://tiles.arcgis.com/tiles/cYuOLPdETvKbspkC/arcgis/rest/servi
ces
Muskingum
https://services5.arcgis.com/N1ybEAKiuuUIL8Mz/ArcGIS/rest/ser
vices

## Page 332

Muskingum
https://tiles.arcgis.com/tiles/N1ybEAKiuuUIL8Mz/arcgis/rest/servi
ces
Ottawa
_ttps://gis.co.ottawa.oh.us/arcgis/rest/services
dead link 1
Pickaway
https://services6.arcgis.com/FhJ42byMw3LmPYCN/arcgis/rest/ser
vices
Pickaway
https://tiles.arcgis.com/tiles/FhJ42byMw3LmPYCN/arcgis/rest/ser
vices
Putnam
https://putnamcountygis.com/arcgis/rest/services
Putnam
https://services2.arcgis.com/axfQw4ze2yV2XAgg/arcgis/rest/servi
ces
Sandusky
Schneider Geospatial - ArcGIS server address is not public
Scioto
https://www.sciotocountyengineer.org/arcgis/rest/services
Seneca
https://services.arcgis.com/b8eHPJ5KRnX3dHNa/arcgis/rest/servi
ces
Seneca
https://tiles.arcgis.com/tiles/b8eHPJ5KRnX3dHNa/arcgis/rest/servi
ces
Shelby
https://cama.shelbycountyauditors.com/arcgis/rest/services
Stark
https://scgisa.starkcountyohio.gov/arcgis/rest/services
Stark
https://scgisb.starkcountyohio.gov/arcgis/rest/services
Stark
https://services2.arcgis.com/1JiK2PayqrHvvJhM/arcgis/rest/servic
es
Stark
          https://tiles.arcgis.com/tiles/1JiK2PayqrHvvJhM/arcgis/rest/services
Stark
https://services3.arcgis.com/UrHoExVO3YKMIi6I/arcgis/rest/serv
ices
Summit
https://scgis.summitoh.net/hosted/rest/services
Summit
https://services3.arcgis.com/3Ukh5HzAdI6WZ3KP/arcgis/rest/serv
ices
Summit
https://tiles.arcgis.com/tiles/3Ukh5HzAdI6WZ3KP/arcgis/rest/serv
ices
Union
https://www7.co.union.oh.us/unioncountyohio/rest/services
Warren
https://gisportal.co.warren.oh.us/server/rest/services
Wayne
https://services6.arcgis.com/WiOy9S7NUTWyXUe4/ArcGIS/rest/s
ervices

## Page 333

Wayne
https://tiles.arcgis.com/tiles/WiOy9S7NUTWyXUe4/arcgis/rest/ser
vices
Wood
https://engineergis.co.wood.oh.us/arcgis/rest/services
Wood
https://services.arcgis.com/uCMcDQQnwrXjpTHr/arcgis/rest/servi
ces
Wyandot
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/WyandotOHFeatures/FeatureServer
Go to the top and search for ‘WyandotOH’
Wyandot
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/WyandotOHCadastral/MapServer
Go to the top and search for ‘WyandotOH’
Ohio City, Town, Village, etc GIS Servers
Akron
https://services1.arcgis.com/8roChjXOF0iBhNoB/arcgis/rest/servic
es
Akron
https://tiles.arcgis.com/tiles/8roChjXOF0iBhNoB/arcgis/rest/servic
es
Akron
See also Summit County
Beavercreek
__________
Belpre
https://services6.arcgis.com/7dg74tDVCouCPxRV/ArcGIS/rest/ser
vices
Brookville
__________
Celina
____________
Centerville
https://maps.centervilleohio.gov/arcgis/rest/services
Centerville
https://services.arcgis.com/M5UrDFRz2ZRTplQC/arcgis/rest/servi
ces
Centerville
https://tiles.arcgis.com/tiles/M5UrDFRz2ZRTplQC/arcgis/rest/serv
ices
Cincinnati
https://arcgis.cincinnati-oh.gov/arcgis/rest/services
Table of contents disabled
Cleveland
https://services3.arcgis.com/dty2kHktVXHrqO8i/ArcGIS/rest/servi
ces
Cleveland Heights
https://services8.arcgis.com/5SpPPOsuKB3yehHW/ArcGIS/rest/se
rvices

Columbus
https://maps.columbus.gov/arcgis/rest/services

## Page 334

Columbus
https://maps2.columbus.gov/arcgis/rest/services

Columbus
https://services1.arcgis.com/9yy6msODkIBzkUXU/ArcGIS/rest/se
rvices
Columbus
https://tiles.arcgis.com/tiles/9yy6msODkIBzkUXU/arcgis/rest/servi
ces

Columbus
https://services3.arcgis.com/n1HcYIXT6v5SL7bQ/ArcGIS/rest/ser
vices
Public schools
Coshocton
_ttps://arcgis.mobile311.com/arcgis/rest/services/Ohio/CityOfCosh
octon/MapServer
dead link 1
Covington
__________
Dayton
https://maps.daytonohio.gov/gisservices/rest/services
Dayton
https://services2.arcgis.com/3dDB2Kk6kuA2gIGw/ArcGIS/rest/ser
vices
Dayton
https://tiles.arcgis.com/tiles/3dDB2Kk6kuA2gIGw/arcgis/rest/servi
ces
Defiance
https://arcgis.mobile311.com/arcgis/rest/services/Ohio/DefianceO
H/MapServer
Delaware
https://services.arcgis.com/eDETAHfuRDcwL2kQ/arcgis/rest/servi
ces
Delaware
https://tiles.arcgis.com/tiles/eDETAHfuRDcwL2kQ/arcgis/rest/ser
vices
Dublin
https://mapping.dublin.oh.us/arcgis/rest/services
Dublin
https://services1.arcgis.com/NqY8dnPSEdMJhuRw/ArcGIS/rest/se
rvices
Dublin
https://tiles.arcgis.com/tiles/NqY8dnPSEdMJhuRw/arcgis/rest/serv
ices
Fayette
__________
Gahanna
https://gis.gahanna.gov/server/rest/services
Gahanna
https://maps.gahanna.gov/server/rest/services
Gahanna
https://services.arcgis.com/23PN23oQTHW8Q4Ls/arcgis/rest/servi
ces
Gahanna
https://tiles.arcgis.com/tiles/23PN23oQTHW8Q4Ls/arcgis/rest/ser
vices
Greenville
__________
Grove City
https://arcgisweb.grovecityohio.gov:6443/arcgis/rest/services

## Page 335

Hamilton
https://gis.hamilton-oh.gov/arcgis/rest/services
Hamilton
https://services1.arcgis.com/1pXnFsHirWAc6772/ArcGIS/rest/serv
ices
Hamilton
https://tiles.arcgis.com/tiles/1pXnFsHirWAc6772/arcgis/rest/servic
es
Hudson
_ttps://ags.hudson.oh.us/server/rest/services
dead link 1
Lakewood
https://services5.arcgis.com/tH1j0ErvAo6IVI7r/ArcGIS/rest/servic
es
Lancaster
https://www2.ci.lancaster.oh.us/webgis/rest/services
Lancaster
https://services1.arcgis.com/CRjnKyCe3OfYTMC3/arcgis/rest/ser
vices
Lancaster
https://tiles.arcgis.com/tiles/CRjnKyCe3OfYTMC3/arcgis/rest/serv
ices
Lebanon
https://maps.lebanonohio.gov/legis/rest/services
Lebanon
https://maps3.lebanonohio.gov/legis/rest/services
Marysville
https://services3.arcgis.com/ccRMrVzOSHBUG6X2/arcgis/rest/ser
vices
Marysville
https://tiles.arcgis.com/tiles/ccRMrVzOSHBUG6X2/arcgis/rest/ser
vices
Middlefield
___________
Middleton
http://gis.cityofmiddletown.com:6080/arcgis/rest/services
Monroe
https://services5.arcgis.com/ZpzXpUOckwsAhLFh/ArcGIS/rest/se
rvices
Monroe
https://tiles.arcgis.com/tiles/ZpzXpUOckwsAhLFh/arcgis/rest/servi
ces
Oxford
https://services2.arcgis.com/FS7YxIXpWoaR2sAe/ArcGIS/rest/ser
vices
Oxford
https://tiles.arcgis.com/tiles/FS7YxIXpWoaR2sAe/arcgis/rest/servi
ces
Piqua
https://services8.arcgis.com/kZPPWTIJ6kOFJTWc/ArcGIS/rest/se
rvices
Piqua
https://tiles.arcgis.com/tiles/kZPPWTIJ6kOFJTWc/arcgis/rest/serv
ices
Powell
https://gis.cityofpowell.us/arcgis/rest/services

## Page 336

Solon
http://gis.solonohio.org/arcgis/rest/services
    Not open to public
Toledo
https://gis.toledo.oh.gov/arcgis/rest/services
Toledo
https://services.arcgis.com/2snQ88YUjP9CNEbe/arcgis/rest/servic
es
Troy
https://gis.troyohio.gov/arcgis/rest/services
Troy
https://services2.arcgis.com/x918hwvMFkK14smu/arcgis/rest/serv
ices            This might be for the county and not just Troy
Troy
https://tiles.arcgis.com/tiles/x918hwvMFkK14smu/arcgis/rest/servi
ces
Upper Arlington        https://services5.arcgis.com/ImL8oyfZuCxsvjaT/arcgis/rest/services
Upper Arlington        https://tiles.arcgis.com/tiles/ImL8oyfZuCxsvjaT/arcgis/rest/services
Versailles
__________
Westerville
https://services.arcgis.com/OrM4sGBhxpl5PoQe/arcgis/rest/servic
es
Westerville
https://tiles.arcgis.com/tiles/OrM4sGBhxpl5PoQe/arcgis/rest/servi
ces
Willoughby
__________
Oklahoma State GIS Servers
Parcel lines:  Data is on a WMS server.  https://okmaps.org/geoserver/wms
layer name
ogi_wms:Statewide_Parcels
Oklahoma Open Data
Website: https://okmaps.onenet.net/digital_data.htm
Oklahoma Department of Emergency Management
Website: https://oklahoma.gov/oem.html
GIS: https://services5.arcgis.com/75KlGMUjpNfFMWey/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/75KlGMUjpNfFMWey/arcgis/rest/services
Oklahoma Department of Agriculture, Food and Forestry
Website: https://www.ag.ok.gov/
GIS: _ttp://maps.ag.ok.gov/arcgis/rest/services
dead link 3
Oklahoma Department of Environmental Quality
Website: _ttps://www.deq.state.ok.us
dead link 1
GIS: https://gis.deq.ok.gov/server/rest/services
Mesonet: Weather stations, dynamic layer support
GIS: https://services1.arcgis.com/ITtWh5MaoQucXt9D/ArcGIS/rest/services

## Page 337

GIS: https://tiles.arcgis.com/tiles/ITtWh5MaoQucXt9D/arcgis/rest/services
Oklahoma Department of Health
Website: https://oklahoma.gov/health.html
GIS: https://services9.arcgis.com/QeqGrHRDFO8mPwTf/ArcGIS/rest/services
Oklahoma Department of Transportation
Website: https://ok.gov/odot/
GIS: https://services6.arcgis.com/RBtoEUQ2lmN0K3GY/arcgis/rest/services
Oklahoma Water Resources Board
Website: https://www.owrb.ok.gov/
GIS: https://owrb.csa.ou.edu/server/rest/services
GIS: https://services2.arcgis.com/fI5CUOPa2wdhkCHV/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/fI5CUOPa2wdhkCHV/arcgis/rest/services
Oklahoma Land Office
Website: https://clo.ok.gov
GIS: https://gis.clo.ok.gov/server/rest/services
Oklahoma Corporation Commission
Website: https://oklahoma.gov/occ.html
GIS: https://gis.occ.ok.gov/server/rest/services
University of Oklahoma Center for Spatial Analysis
Website: https://www.ou.edu/ags/csa
GIS: https://services.arcgis.com/3xOwF6p0r7IHIjfn/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/3xOwF6p0r7IHIjfn/arcgis/rest/services
GIS: https://services3.arcgis.com/MUsqg3LXXXYe8gDP/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/MUsqg3LXXXYe8gDP/arcgis/rest/services
Oklahoma various layers
GIS: https://services3.arcgis.com/yrIZ0Nv0mSGTWJsH/arcgis/rest/services
Oklahoma Regional
Association of Central Oklahoma Governments (ACOG)
Website: https://www.acogok.org
GIS: https://arcgis4.roktech.net/arcgis/rest/services/ACOG
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/F3fwU7bP9u9L7CRX/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/F3fwU7bP9u9L7CRX/arcgis/rest/services
Indian Nations Council of Governments (INCOG) (planning for NE Oklahoma)

## Page 338

Website: https://www.incog.org
GIS: https://map11.incog.org/arcgis11wa/rest/services
Oklahoma eCOP
Website: http://www.sdrmaps.com/ecop/Oklahoma.html
not https
GIS:
https://elb.elevatemaps.io/arcgis/rest/services
8-9-2023 No tiled data
Southeastern Regional Transportation Planning
Website: https://www.sertpo.org
GIS: https://services6.arcgis.com/SO99JCHlk9W1iAMm/ArcGIS/rest/services
Oklahoma County GIS Servers
Beaver
https://images3.integritygis.com/arcgis/rest/services/OK/Beaver_P
hotography_2023/ImageServer
Beckham
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Murray_County_Data/FeatureServer
Blaine
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Blaine_Data_Layers/FeatureServer
Caddo
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Caddo_Data_Layers/FeatureServer
Caddo
https://images3.integritygis.com/arcgis/rest/services/OK/Caddo_Ph
otography_2023/ImageServer
Carter
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Carter_County_Data/FeatureServer
Cherokee
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Cherokee_Data_Layers/FeatureServer
Cimarron
https://images3.integritygis.com/arcgis/rest/services/OK/Cimarron
_Photography_2023/ImageServer
Cleveland
https://services1.arcgis.com/kxHJSF07PF5lbQ3z/arcgis/rest/servic
es
Cleveland
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Cleveland_County_Data/FeatureServer
Coal
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Coal_County_Data/FeatureServer
Comanche
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Comanche_County_Data/FeatureServer

## Page 339

Cotton
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Cotton_County_Data/FeatureServer
Craig
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Craig_County_Data/FeatureServer
Custer
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Custer_County_Data/FeatureServer
Delaware
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Delaware_County_Data/FeatureServer
Dewey
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Dewey_County_Data/FeatureServer
Ellis
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Ellis_County_Data/FeatureServer
Garfield
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Garfield_County_Data/FeatureServer
Garvin
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Garvin_County_Data/FeatureServer
Grady
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Grady_County_Data/FeatureServer
Grant
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Grant_County_Data/FeatureServer
Greer
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Greer_County_Data/FeatureServer
Harmon
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Harmon_County_Data/FeatureServer
Harper
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Harper_County_Data/FeatureServer
Haskell
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Haskell_County_Data/FeatureServer
Hughes
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Hughes_County_Data/FeatureServer
Hughes
https://images3.integritygis.com/arcgis/rest/services/OK/Hughes_P
hotography_2023/ImageServer

## Page 340

Jackson
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Jackson_County_Data/FeatureServer
Jefferson
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Jefferson_County_Data/FeatureServer
Johnston
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Johnston_County_Data/FeatureServer
Kay
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Kay_County_Data/FeatureServer
Kay
https://images3.integritygis.com/arcgis/rest/services/OK/Kay_Phot
ography_2023/ImageServer
Kingfisher
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Kingfisher_County_Data/FeatureServer
Kingfisher
https://images3.integritygis.com/arcgis/rest/services/OK/Kingfisher
_Photography_2023/ImageServer
Kiowa
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Kiowa_County_Data/FeatureServer
Latimer
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Latimer_County_Data/FeatureServer
LeFlore
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/LeFlore_County_Data/FeatureServer
Lincoln
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Lincoln_County_Data/FeatureServer
Logan
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Logan_County_Data/FeatureServer
Love
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Love_County_Data/FeatureServer
Marshall
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Marshall_County_Data/FeatureServer
McClain
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Mcclain_County_Data/FeatureServer
McCurtain
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Mccurtain_County_Data/FeatureServer

## Page 341

McIntosh
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Mcintosh_County_Data/FeatureServer
Mayes
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Mayes_County_Data/FeatureServer
Murray
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Murray_County_Data/FeatureServer
Murray
https://images3.integritygis.com/arcgis/rest/services/OK/Murray_P
hotography_2023/ImageServer
Muskogee
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Muskogee_County_Data/FeatureServer
Noble
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Noble_County_Data/FeatureServer
Noble
https://images3.integritygis.com/arcgis/rest/services/OK/Noble_Ph
otography_2023/ImageServer
Nowata
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Nowata_County_Data/FeatureServer
Nowata
https://images3.integritygis.com/arcgis/rest/services/OK/Nowata_P
hotography_2023/ImageServer
Okfuskee
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Okfuskee_County_Data/FeatureServer
Oklahoma
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Oklahoma_County_Data/FeatureServer
Oklahoma
           https://services8.arcgis.com/euhkr1dAJeQBIjV0/arcgis/rest/services
Oklahoma
           https://tiles.arcgis.com/tiles/euhkr1dAJeQBIjV0/arcgis/rest/services
Okmulgee
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Okmulgee_County_Data/FeatureServer
Osage
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Osage_County_Data/FeatureServer
Ottawa
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Ottawa_County_Data/FeatureServer
Pawnee
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Pawnee_County_Data/FeatureServer
Pawnee
https://images3.integritygis.com/arcgis/rest/services/OK/Pawnee_P
hotography_2023/ImageServer

## Page 342

Payne
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Payne_County_Data/FeatureServer
Pittsburg
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Pittsburg_County_Data/FeatureServer
Pontotoc
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Pontotoc_County_Data/FeatureServer
Pottawatomie
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Pottawatomie_County_Data/FeatureServer
Pushmataha
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Pushmataha_County_Data/FeatureServer
Roger Mills
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Roger_Mills_County_Data/FeatureServer
Rogers
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Rogers_County_Data/FeatureServer
Seminole
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Seminole_County_Data/FeatureServer
Sequoyah
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Sequoyah_County_Data/FeatureServer
Stephens
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Stephens_County_Data/FeatureServer
Texas
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Texas_County_Data/FeatureServer
Texas
https://images3.integritygis.com/arcgis/rest/services/OK/Texas_Ph
otography_2023/ImageServer
Tillman
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Tillman_County_Data/FeatureServer
Tulsa
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Tulsa_County_Data/FeatureServer
Tulsa
https://services5.arcgis.com/BXF8h2ocSJQxuW52/arcgis/rest/servi
ces
Tulsa
https://tiles.arcgis.com/tiles/BXF8h2ocSJQxuW52/arcgis/rest/servi
ces
Tulsa
https://services6.arcgis.com/Z8p3hPcWWaaGWw4N/ArcGIS/rest/
services
Tulsa Area Emergency Management Agency

## Page 343

Tulsa
https://tiles.arcgis.com/tiles/Z8p3hPcWWaaGWw4N/arcgis/rest/se
rvices
Wagoner
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Wagoner_County_Data/FeatureServer
Washington
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Washington_County_Data/FeatureServer
Washita
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Washita_County_Data/FeatureServer
Woods
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Woods_County_Data/FeatureServer
Woodward
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Woodward_County_Data/FeatureServer
Oklahoma City, Town, Village, etc GIS Servers
Altus
https://services8.arcgis.com/YCqZ37LEnvwvpiLb/arcgis/rest/servi
ces
Altus
https://tiles.arcgis.com/tiles/YCqZ37LEnvwvpiLb/arcgis/rest/servi
ces
Atoka
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Atoka_Data_Layers/FeatureServer
Beaver
__________
Broken Arrow
https://services5.arcgis.com/rr6hTHIOPEZnXs66/ArcGIS/rest/serv
ices
Bryan
https://services.arcgis.com/3xOwF6p0r7IHIjfn/ArcGIS/rest/service
s/Bryan_Data_Layers/FeatureServer
Chickasha
https://maps.chickasha.org/server/rest/services
Collinsville
https://services7.arcgis.com/T4VS1sBitWBtDLv1/ArcGIS/rest/ser
vices
Collinsville
https://tiles.arcgis.com/tiles/T4VS1sBitWBtDLv1/arcgis/rest/servi
ces
Crescent
___________
Cushing
https://services8.arcgis.com/gPS4jLTZiHJgmgyG/arcgis/rest/servic
es

## Page 344

Del City
https://services6.arcgis.com/MIUuXlEJ4d9x6sYB/ArcGIS/rest/ser
vices
Del City
https://tiles.arcgis.com/tiles/MIUuXlEJ4d9x6sYB/arcgis/rest/servi
ces
Douglas
https://services.arcgis.com/pDAi2YK0L0QxVJHj/arcgis/rest/servic
es
Douglas
https://tiles.arcgis.com/tiles/pDAi2YK0L0QxVJHj/arcgis/rest/servi
ces
Edmond
https://gis.edmondok.gov/arcgis/rest/services
El Reno
https://services3.arcgis.com/9voKBZ2F2TY0HVPc/arcgis/rest/serv
ices
Guthrie
https://arcgis4.roktech.net/arcgis/rest/services/Guthrie
Guthrie
https://arcgis5.roktech.net/arcgis/rest/services/Guthrie
Jenks
https://services6.arcgis.com/4Mu2JOJIDuTmmPXb/arcgis/rest/ser
vices
Jenks
https://tiles.arcgis.com/tiles/4Mu2JOJIDuTmmPXb/arcgis/rest/serv
ices
Kingfisher
https://services9.arcgis.com/vuaQoZM5FY00qVi8/arcgis/rest/servi
ces   Also may have data for other cities
Lawton
https://services2.arcgis.com/baoUryRiOxhCY0yb/ArcGIS/rest/serv
ices
Midwest City
https://maps.midwestcityok.org/arcgis/rest/services
Midwest City
https://services5.arcgis.com/oWb0kRlzCaAiXrg1/ArcGIS/rest/serv
ices
Midwest City
https://tiles.arcgis.com/tiles/oWb0kRlzCaAiXrg1/arcgis/rest/servic
es
Moore
https://gis.cityofmoore.com/arcgis/rest/services
Mustang
          https://services8.arcgis.com/gbzZfTaSTnfRdQPt/arcgis/rest/services
Nowata
____________
Nowata
____________

Oklahoma City
https://gis.okc.gov/arcgis/rest/services

Okmulgee
           _ttps://maps.meshekgis.com/arcgis/rest/services/City_of_Okmulgee

## Page 345

dead link 3
Owasso
They have a GIS but not ArcGIS
Piedmont
https://services7.arcgis.com/OJ8CIjB2a1JPYuG7/arcgis/rest/servic
es
Poteau
_ttps://maps.meshekgis.com/arcgis/rest/services/City_of_Poteau
dead link 3
Norman
https://maps.normanok.gov/arcgis/rest/services
Norman
           https://services.arcgis.com/rt1leD4Hj3sLGHNL/arcgis/rest/services
Norman
https://tiles.arcgis.com/tiles/rt1leD4Hj3sLGHNL/arcgis/rest/servic
es
Stillwater
https://services.arcgis.com/RPfJX2yEEVtopacQ/arcgis/rest/services
Stillwater
https://tiles.arcgis.com/tiles/RPfJX2yEEVtopacQ/arcgis/rest/servic
es
Tahlequah
           _ttps://maps.meshekgis.com/arcgis/rest/services/City_of_Tahlequah
dead link 3

Tulsa
https://services2.arcgis.com/XkZ90iCdbTJ9oNXl/arcgis/rest/servic
es
Tulsa
https://tiles.arcgis.com/tiles/XkZ90iCdbTJ9oNXl/arcgis/rest/servic
es
Woodward
__________
Oregon State GIS Servers
Oregon Open Data Portal
Website: https://data.oregon.gov/
Oregon Department of Agriculture
Website: https://www.oregon.gov/ODA/Pages/default.aspx
GIS: https://maps.oda.state.or.us/arcgis/rest/services
8-9-2023 No tiled data
Oregon Department of Environmental Quality
Website: https://www.oregon.gov/DEQ/Pages/index.aspx
GIS: https://arcgis.deq.state.or.us/arcgis/rest/services
8-9-2023 No tiled data
Oregon Department of Fish and Wildlife
Website: https://www.dfw.state.or.us/

## Page 346

GIS: https://nrimp.dfw.state.or.us/arcgis/rest/services
Oregon Department of Forestry
Website: https://www.oregon.gov/odf/pages/index.aspx
GIS: https://gis.odf.oregon.gov/ags1/rest/services
Parcel lines by county:  WebMercator/TaxlotsDisplay/MapServer
Recreation info: WebMercator/FERNSBasemap
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.odf.oregon.gov/ags3/rest/services
Oregon Department of Geology and Mineral Industries
Website: https://www.oregon.gov/dogami/pages/default.aspx
GIS: https://gis.dogami.oregon.gov/arcgis/rest/services
8-9-2023 No tiled data
Oregon Department of Land Conservation and Development
Website: https://www.oregon.gov/lcd/pages/index.aspx
GIS: https://gis.lcd.state.or.us/server/rest/services
Oregon Department of State Lands
Website: https://www.oregon.gov/dsl/pages/default.aspx
GIS: https://maps.dsl.state.or.us/arcgis/rest/services
Oregon Department of Transportation
Website: https://www.oregon.gov/ODOT/Pages/index.aspx
GIS: https://gis.odot.state.or.us/arcgis1006/rest/services
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Oregon Water Resources Department
Website: https://www.oregon.gov/OWRD/pages/index.aspx
GIS: https://arcgis.wrd.state.or.us/arcgis/rest/services
8-9-2023 No tiled data
Oregon various layers
GIS: https://navigator.state.or.us/arcgis/rest/services
8-9-2023 No tiled data
GIS: https://maps.prd.state.or.us/arcgis/rest/services
8-9-2023 No tiled data
GIS: https://imagery.oregonexplorer.info/arcgis/rest/services
2022 aerials
8-9-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.prd.state.or.us/arcgis/rest/services
GIS: https://services.arcgis.com/uUvqNMGPm7axC2dD/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/uUvqNMGPm7axC2dD/arcgis/rest/services
GIS: https://services8.arcgis.com/8PAo5HGmvRMlF2eU/ArcGIS/rest/services

## Page 347

Oregon Regional
Metro
Website: https://www.oregonmetro.gov/regional-leadership/what-metro
GIS: https://gis.oregonmetro.gov/arcgis/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.oregonmetro.gov/ArcGIS/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services2.arcgis.com/McQ0OlIABe29rJJy/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/McQ0OlIABe29rJJy/arcgis/rest/services
Geospatial Infrastructure Group
Website: https://geo-orgig.hub.arcgis.com/pages/b5f3f78124194eb6b0568c9e139a0eb0
GIS: https://services3.arcgis.com/ArcmNlqX6P5aOaMC/arcgis/rest/services
Mid-Willamette Valley Council of Governments
Website: https://www.mwvcog.org
GIS: https://services2.arcgis.com/89BLPQl3PdPQE7iy/ArcGIS/rest/services
Lane Council of Governments
Website: https://www.lcog.org
GIS: https://services3.arcgis.com/NbWCmkRTtvyr63CT/ArcGIS/rest/services
Lane Geographic Data Consortium
GIS: https://services5.arcgis.com/9s1YtFmLS0YTl10F/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/9s1YtFmLS0YTl10F/arcgis/rest/services
Oregon County GIS Servers
All counties are listed.  Any showing _______ need to be checked for a GIS server.
Baker
__________
Benton
https://gis.co.benton.or.us/arcgis/rest/services
Benton
https://services5.arcgis.com/U7TbEknoCzTtNGz4/ArcGIS/rest/ser
vices
Clackamas
WMS server
Clatsop
https://delta.co.clatsop.or.us/server/rest/services
Clatsop
https://services8.arcgis.com/l89P2qlKPxgrFDLw/ArcGIS/rest/servi
ces
Clatsop
https://tiles.arcgis.com/tiles/l89P2qlKPxgrFDLw/arcgis/rest/servic
es
Columbia
https://gis.columbiacountymaps.com/server/rest/services
Coos
__________

## Page 348

Crook
https://gis.crookcountyor.gov/server/rest/services
Crook
https://services9.arcgis.com/UuDCSelW0J9DF8Nq/arcgis/rest/serv
ices
Curry
https://gateway.maps.rlid.org/maps1/rest/services
Deschutes
https://maps.deschutes.org/arcgis/rest/services
Deschutes
https://services1.arcgis.com/znO8Hz1SuVVohYhZ/arcgis/rest/serv
ices
Deschutes
https://tiles.arcgis.com/tiles/znO8Hz1SuVVohYhZ/arcgis/rest/serv
ices
Douglas
https://gis.co.douglas.or.us/server/rest/services
Gilliam
https://services3.arcgis.com/e3KSI9Py4B7m3xu6/ArcGIS/rest/serv
ices
Might be multiple entries for this county
Grant
https://services3.arcgis.com/e3KSI9Py4B7m3xu6/ArcGIS/rest/serv
ices
Might be multiple entries for this county
Harney
https://services3.arcgis.com/e3KSI9Py4B7m3xu6/ArcGIS/rest/serv
ices
Might be multiple entries for this county
Hood River
https://services7.arcgis.com/xtfQPw7zwSRPkcfN/arcgis/rest/servic
es
Hood River
https://tiles.arcgis.com/tiles/xtfQPw7zwSRPkcfN/arcgis/rest/servic
es
Jackson
https://spatial.jacksoncountyor.gov/arcgis/rest/services
Jackson
https://services1.arcgis.com/DwYBkWQPdaJNWrPG/arcgis/rest/s
ervices
Jackson
https://tiles.arcgis.com/tiles/DwYBkWQPdaJNWrPG/arcgis/rest/se
rvices
Jackson
https://services5.arcgis.com/f9aJvXZvmLstTQ3E/arcgis/rest/servic
es
Jackson
https://tiles.arcgis.com/tiles/f9aJvXZvmLstTQ3E/arcgis/rest/servic
es
Jefferson
WMS server
Josephine
https://gis.co.josephine.or.us/arcgis/rest/services
Klamath
https://services.arcgis.com/H6Mh1bySxR4oHx6x/arcgis/rest/servic
es
Klamath
https://tiles.arcgis.com/tiles/H6Mh1bySxR4oHx6x/arcgis/rest/servi
ces

## Page 349

Lake
https://services3.arcgis.com/e3KSI9Py4B7m3xu6/ArcGIS/rest/serv
ices
Might be multiple entries for this county
Lane
https://lcmaps.lanecounty.org/arcgis/rest/services
Lincoln
WMS server
Linn
https://gis.co.linn.or.us/public/rest/services
Table of contents disabled
Malheur
Their GIS maps seem to just use layers from a state server
Marion
https://services1.arcgis.com/sYGZnQPdJ0azuLyn/arcgis/rest/servic
es
Morrow
__________
Multnomah
https://www3.multco.us/arcgis/rest/services
Multnomah
https://www3.multco.us/arcgispublic/rest/services
Multnomah
https://services5.arcgis.com/x7DNZL1YqNQVNykA/arcgis/rest/se
rvices
Multnomah
https://tiles.arcgis.com/tiles/x7DNZL1YqNQVNykA/arcgis/rest/se
rvices
Polk
https://maps.co.polk.or.us/gis/rest/services
Sherman
__________
Tillamook
https://services3.arcgis.com/JnnlTIrcZLzs7d68/arcgis/rest/services
Umatilla
https://services3.arcgis.com/tNPgIZWOB0Efvm0g/arcgis/rest/servi
ces
Union
__________
Wallowa
https://services1.arcgis.com/CD5mKowwN6nIaqd8/arcgis/rest/serv
ices/Wallowa_County_Tax_Lot_Property_Boundaries/FeatureServ
er
Wallowa
https://tiles.arcgis.com/tiles/CD5mKowwN6nIaqd8/arcgis/rest/serv
ices
Wasco
https://public.co.wasco.or.us/gisserver/rest/services
Washington
https://gispub.co.washington.or.us/server/rest/services
Washington
https://gisweb.co.washington.or.us/agsimage/rest/services
Washington
https://gisweb.co.washington.or.us/arcgispub/rest/services

## Page 350

Washington
https://pappgispub1.co.washington.or.us/server/rest/services
Washington
https://pappgiswa1.co.washington.or.us/arcgispub/rest/services
Wheeler
https://services3.arcgis.com/e3KSI9Py4B7m3xu6/ArcGIS/rest/serv
ices
Might be multiple entries for this county
Yamhill
https://services6.arcgis.com/toubSXwoan3LMhOW/ArcGIS/rest/se
rvices
Oregon City, Town, Village, etc GIS Servers
Albany
https://services1.arcgis.com/rTbYoZX7yR1PY1BP/arcgis/rest/serv
ices
Albany
https://tiles.arcgis.com/tiles/rTbYoZX7yR1PY1BP/arcgis/rest/servi
ces
Ashland
https://gis.ashland.or.us/arcgis/rest/services
Table of contents disabled
Ashland
https://gis.ashland.or.us/imageserver23/rest/services
Ashland
https://services1.arcgis.com/NTWWSjEn5J53Yoh1/ArcGIS/rest/se
rvices
Ashland
https://tiles.arcgis.com/tiles/NTWWSjEn5J53Yoh1/arcgis/rest/serv
ices
Beaverton
_ttps://gis.beavertonoregon.gov/server/rest/services      dead link 1
Bend
https://services5.arcgis.com/JisFYcK2mIVg9ueP/arcgis/rest/servic
es
Bend
https://tiles.arcgis.com/tiles/JisFYcK2mIVg9ueP/arcgis/rest/servic
es
Corvallis
https://gis.corvallisoregon.gov/pub2/rest/services
Eugene
https://gis.eugene-or.gov/arcgis/rest/services
Eugene
https://services3.arcgis.com/F7NiRLGNbA2hh7gE/arcgis/rest/serv
ices
Eugene
https://tiles.arcgis.com/tiles/F7NiRLGNbA2hh7gE/arcgis/rest/servi
ces
Gresham
https://portal.greshamoregon.gov/server/rest/services
Table of contents disabled
Gresham - Rockwood PUD
___________
Hillsboro
https://gis.hillsboro-oregon.gov/public/rest/services
Hillsboro
https://mapsvcs2.hillsboro-oregon.gov/public/rest/services

## Page 351

King City
https://services8.arcgis.com/NsUn9YuPFCjrkDe3/ArcGIS/rest/serv
ices
Klamath Falls
https://maps.cityofkfalls.com/server/rest/services
Lebanon
https://services1.arcgis.com/K1vRaK7vKFsLv6fj/arcgis/rest/servic
es
Lebanon
https://tiles.arcgis.com/tiles/K1vRaK7vKFsLv6fj/arcgis/rest/servic
es
McMinnville
https://macgisworx.ci.mcminnville.or.us/mac_or/rest/services
Medford
https://services.arcgis.com/ogdeCdziRfIzuoFs/arcgis/rest/services
Medford
https://tiles.arcgis.com/tiles/ogdeCdziRfIzuoFs/arcgis/rest/services
Newberg
https://services.arcgis.com/LJLnwUl0uTPWJE9B/arcgis/rest/servic
es
Newberg
https://tiles.arcgis.com/tiles/LJLnwUl0uTPWJE9B/arcgis/rest/servi
ces
Oregon City
https://maps.orcity.org/arcgis/rest/services
Oswego
https://maps.ci.oswego.or.us/server/rest/services
Portland
https://www.portlandmaps.com/arcgis/rest/services
Portland
https://services5.arcgis.com/M4BVfpAFnNvNYNUz/ArcGIS/rest/
services    Replace I-5 bridge over Columbia River
Portland
          https://services.arcgis.com/quVN97tn06YNGj9s/arcgis/rest/services
Portland
https://tiles.arcgis.com/tiles/quVN97tn06YNGj9s/arcgis/rest/servic
es
Redmond
https://services2.arcgis.com/B0h69gkZPiRSTUFu/arcgis/rest/servi
ces
Redmond
https://tiles.arcgis.com/tiles/B0h69gkZPiRSTUFu/arcgis/rest/servi
ces

Salem
https://services.arcgis.com/kIA6yS9KDGqZL7U3/arcgis/rest/servi
ces
Salem
https://tiles.arcgis.com/tiles/kIA6yS9KDGqZL7U3/arcgis/rest/servi
ces
Silverton
____________
Sweet Home
https://services3.arcgis.com/BsoDXITBbyVjvV7L/arcgis/rest/servi
ces

## Page 352

Sweet Home
https://tiles.arcgis.com/tiles/BsoDXITBbyVjvV7L/arcgis/rest/servi
ces
Tigard
https://svr.tigardmaps.com/arcgis/rest/services
Tigard
https://services1.arcgis.com/d9Fl2w84c4Vbf9kI/ArcGIS/rest/servic
es
Tigard
https://tiles.arcgis.com/tiles/d9Fl2w84c4Vbf9kI/arcgis/rest/services
Tualatin
https://tualgis.ci.tualatin.or.us/server/rest/services
Table of contents disabled
Washington
https://services1.arcgis.com/LX1Oq2Zzv8CmxRHo/ArcGIS/rest/se
rvices
Washington
https://tiles.arcgis.com/tiles/LX1Oq2Zzv8CmxRHo/arcgis/rest/ser
vices
Woodburn
https://gis.ci.woodburn.or.us/arcgis/rest/services
Woodburn
https://services6.arcgis.com/SDNCi2XpF9TilQhj/arcgis/rest/servic
es
Pennsylvania State GIS Servers
Pennsylvania Open Data
Website: https://data.pa.gov/
Pennsylvania Spatial Data Access (PASDA)
Website: https://www.pasda.psu.edu
GIS: https://maps.pasda.psu.edu/ArcGIS/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://apps.pasda.psu.edu/ArcGIS/rest/services
Parcel lines by county:  PA_Parcels_2022/MapServer
GIS: https://mapservices.pasda.psu.edu/server/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services9.arcgis.com/4ChUzhvTv2zEJshI/ArcGIS/rest/services
Pennsylvania Emergency Management Agency
Website: https://www.pa.gov/agencies/pema.html
GIS: https://services2.arcgis.com/xtuWQvb2YQnp0z3F/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/xtuWQvb2YQnp0z3F/arcgis/rest/services
Pennsylvania Department of Community and Economic Development
Website: https://dced.pa.gov
GIS: https://services6.arcgis.com/532hEgQVqKXr4LOZ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/532hEgQVqKXr4LOZ/arcgis/rest/services
Pennsylvania Department of Conservation and Natural Resources

## Page 353

Website: https://www.dcnr.pa.gov/Pages/default.aspx
GIS: https://maps.dcnr.pa.gov/agsprod/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://www.gis.dcnr.state.pa.us/agsprod/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS:
https://mapservices.pasda.psu.edu/server/rest/services/pasda/DCNR_OutdoorRecr
eationAccess/MapServer
8-10-2023 No tiled data
GIS: https://mapservices.pasda.psu.edu/server/rest/services/pasda/DCNR/MapServer
8-10-2023 No tiled data
GIS: https://services.arcgis.com/CPq7UDkBXVRqtgLR/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/CPq7UDkBXVRqtgLR/arcgis/rest/services
Pennsylvania Department of Environmental Protection
Website: https://www.dep.pa.gov/Pages/default.aspx
Data portal: https://www.dep.pa.gov/DataandTools/Pages/GIS.aspx
GIS: https://gis.dep.pa.gov/depgisprd/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://mapservices.pasda.psu.edu/server/rest/services/pasda/DEP2/MapServer
8-10-2023 No tiled data
GIS: https://mapservices.pasda.psu.edu/server/rest/services/pasda/DEP/MapServer
8-10-2023 No tiled data
GIS: https://services5.arcgis.com/bykQ7FaL2oSIxFNa/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/bykQ7FaL2oSIxFNa/arcgis/rest/services
Pennsylvania Department of Transportation
Website: https://www.penndot.gov/Pages/default.aspx
GIS: https://gis.penndot.gov/arcgis/rest/services
GIS: https://services1.arcgis.com/jOy9iZUXBy03ojXb/arcgis/rest/services
Includes layers for various counties
GIS: https://tiles.arcgis.com/tiles/jOy9iZUXBy03ojXb/arcgis/rest/services
GIS: https://mapservices.pasda.psu.edu/server/rest/services/pasda/PennDOT/MapServer
8-10-2023 No tiled data
Pennsylvania Fish and Boat Commission
Website: https://www.fishandboat.com/Pages/default.aspx
GIS: https://fbweb.pa.gov/arcgis/rest/services
See the ‘PASDA’ links above
8-10-2023 No tiled data
Pennsylvania Game Commission
Website: https://www.pgc.pa.gov/Pages/default.aspx
GIS: https://pgcmaps.pa.gov/arcgis/rest/services
8-10-2023 No tiled data
GIS: https://services1.arcgis.com/k8yxvICm95iIFicb/arcgis/rest/services

## Page 354

GIS:
https://mapservices.pasda.psu.edu/server/rest/services/pasda/PennsylvaniaGameC
ommission/MapServer
8-10-2023 No tiled data
County Commissioners Association of Pennsylvania
GIS: https://services6.arcgis.com/NI2zGiYg8AZCsScF/arcgis/rest/services
Pennsylvania various layers
GIS: https://services1.arcgis.com/fmL63zawJNFGptQt/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/fmL63zawJNFGptQt/arcgis/rest/services
GIS: https://services3.arcgis.com/dBSpWiMm4bd648G0/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/dBSpWiMm4bd648G0/arcgis/rest/services
GIS: https://services6.arcgis.com/BAJNi3EgCdtQ1BCG/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/BAJNi3EgCdtQ1BCG/arcgis/rest/services
Pennsylvania Regional
Capital Region Water
Website: https://capitalregionwater.com
GIS: https://services7.arcgis.com/ovShRX1QWLiEg5eF/arcgis/rest/services
Centre Regional Planning Agency
Website: https://www.crcog.net/index.asp
GIS: https://services7.arcgis.com/Kr1baS89p5maegub/ArcGIS/rest/services
Delaware Valley Regional Planning Commission
Website: https://www.dvrpc.org
GIS: https://arcgis.dvrpc.org/portal/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Delaware North Central PA Regional Planning & Development
Website: https://www.ncentral.com
GIS: https://services1.arcgis.com/qXvbYftT9ld1YWzi/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/qXvbYftT9ld1YWzi/arcgis/rest/services
Susquehanna Economic Development Association - Council of Governments
Website: https://seda-cog.org
GIS: https://services1.arcgis.com/6NNMHuq8MYlPbI46/ArcGIS/rest/services
Southern Alleghenies Planning & Development Commission
Website: https://sapdcgis.maps.arcgis.com/home/index.html
GIS: https://services.arcgis.com/KTgVkgA4uog8cyEc/arcgis/rest/services
Southeastern Pennsylvania Transportation Authority
Website: https://www.septa.org
GIS: https://services2.arcgis.com/9U43PSoL47wawX5S/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/9U43PSoL47wawX5S/arcgis/rest/services

## Page 355

Southwestern Pennsylvania Commission
Website: https://www.spcregion.org
GIS: https://spcarcgis.org/arcgis/rest/services
GIS: https://services3.arcgis.com/MV5wh5WkCMqlwISp/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/MV5wh5WkCMqlwISp/arcgis/rest/services
Pennsylvania Turnpike Commission
Website: https://www.paturnpike.com
GIS: https://services.arcgis.com/FohZlMMG15EeWv3q/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/FohZlMMG15EeWv3q/arcgis/rest/services
Pennsylvania County GIS Servers

Adams
https://mapping.adamscountypa.gov/arcgis/rest/services
Adams
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Adam
sCounty/MapServer
Adams
https://services3.arcgis.com/6cMZno0DoVgS6q58/arcgis/rest/servi
ces
Adams
https://tiles.arcgis.com/tiles/6cMZno0DoVgS6q58/arcgis/rest/servi
ces
Allegheny
https://gisdata.alleghenycounty.us/arcgis/rest/services
Allegheny
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Alleg
henyCounty/MapServer
Allegheny
https://services1.arcgis.com/vdNDkVykv9vEWFX4/ArcGIS/rest/s
ervices
Allegheny
https://tiles.arcgis.com/tiles/vdNDkVykv9vEWFX4/arcgis/rest/ser
vices
Bedford
https://services2.arcgis.com/tXFMtuwRfEDEFdnG/arcgis/rest/serv
ices
Bedford
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Bedfo
rdCounty/MapServer
Berks
https://gis.co.berks.pa.us/arcgis/rest/services
Berks
https://services3.arcgis.com/dGYe1jDYrTw1wwpc/ArcGIS/rest/se
rvices
Blair
https://mapservices.pasda.psu.edu/server/rest/services/pasda/BlairC
ounty/MapServer
Blair
https://services1.arcgis.com/uRt3JfP8exTIPzvd/ArcGIS/rest/servic
es
Bradford
https://arcgis.vgsi.com/server/rest/services/Bradford_County_PA
Bradford
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Bradf
ordCounty/MapServer

## Page 356

Bucks
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Bucks
County/MapServer
Bucks
https://services3.arcgis.com/SP47Tddf7RK32lBU/ArcGIS/rest/serv
ices
Bucks
https://tiles.arcgis.com/tiles/SP47Tddf7RK32lBU/arcgis/rest/servic
es
Butler
https://geo.co.butler.pa.us/server/rest/services
Butler
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Butler
County/MapServer
Butler
https://services9.arcgis.com/5VOhDgerxIw33LoH/ArcGIS/rest/ser
vices
Cambria
https://services1.arcgis.com/Fw15y9AZK02r2ZNA/arcgis/rest/serv
ices
Carbon
https://gis.carboncounty.com/arcgis/rest/services
Carbon
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Carbo
nCounty/MapServer
Carbon
https://services5.arcgis.com/dbmvQjTMiMGbWCNp/ArcGIS/rest/
services
Centre
https://gissites4.centrecountypa.gov/arcgis/rest/services
Centre
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Centre
County/MapServer
Centre
https://services3.arcgis.com/HDjl48g0Y109Q9wX/arcgis/rest/servi
ces
Centre
https://tiles.arcgis.com/tiles/HDjl48g0Y109Q9wX/arcgis/rest/servi
ces
Chester
https://gisprodops.chesco.org/server/rest/services
Chester
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Chest
erCounty/MapServer
Chester
https://services.arcgis.com/G4S1dGvn7PIgYd6Y/ArcGIS/rest/servi
ces
Chester
https://tiles.arcgis.com/tiles/G4S1dGvn7PIgYd6Y/arcgis/rest/servi
ces
Chester
East Goshen Township
https://services6.arcgis.com/TTOLfTFz2poZabMn/arcgis/re
st/services
Clearfield
https://gis.clearfieldco.org/arcgis/rest/services
SSL problem
Clinton
http://maps.clintoncountypa.com/arcgis/rest/services      not https
Columbia
https://gismaps.columbiapa.org/server/rest/services

## Page 357

Crafton Borough
https://services8.arcgis.com/GgSf1dNLgvOpRB5b/ArcGIS/rest/ser
vices
Crawford
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Crawf
ordCounty/MapServer
Crawford
https://ccgis.crawfordcountypa.net/arcgis/rest/services
Not open to public
Crawford
https://services1.arcgis.com/CcJI8wbz22fo71LO/ArcGIS/rest/servi
ces
Crawford
          https://tiles.arcgis.com/tiles/CcJI8wbz22fo71LO/arcgis/rest/services
Cumberland
https://gis.ccpa.net/arcgiswebadaptor/rest/services
Cumberland
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Cumb
erlandCounty/MapServer
Cumberland
https://services1.arcgis.com/1Cfo0re3un0w6a30/ArcGIS/rest/servi
ces
Cumberland
           https://tiles.arcgis.com/tiles/1Cfo0re3un0w6a30/arcgis/rest/services
Dauphin
https://gis.dauphincounty.org/arcgis/rest/services
Table of contents disabled
Dauphin
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Dauph
inCounty/MapServer
Dauphin
https://services2.arcgis.com/EEtiX55QzkHKYQKY/ArcGIS/rest/s
ervices
Dauphin
https://tiles.arcgis.com/tiles/EEtiX55QzkHKYQKY/arcgis/rest/ser
vices
Delaware
https://gis.delcopa.gov/arcgis/rest/services
Erie
https://mapservices.pasda.psu.edu/server/rest/services/pasda/ErieC
ountyParcels/MapServer
Forest
https://services8.arcgis.com/3SC5aoxCO7AZDldv/arcgis/rest/servi
ces
Franklin
https://services2.arcgis.com/9ITMSQly9V0ER26l/ArcGIS/rest/ser
vices
Franklin
https://tiles.arcgis.com/tiles/9ITMSQly9V0ER26l/arcgis/rest/servic
es
Fulton
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Fulton
County/MapServer
Fulton
https://services6.arcgis.com/pcp4UiBBXQK2kACC/arcgis/rest/ser
vices
Fulton
https://tiles.arcgis.com/tiles/pcp4UiBBXQK2kACC/arcgis/rest/ser
vices

## Page 358

Greene
https://arcgis.vgsi.com/server/rest/services/Greene_County_PA
Huntingdon
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Hunti
ngdonCounty/MapServer
Huntingdon
           https://services3.arcgis.com/liWtJPxLI3mlx8pH/arcgis/rest/services
Indiana
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Indian
aCounty/MapServer
Juniata
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Juniat
aCounty/MapServer
Juniata
https://parcelviewer.geodecisions.com/arcgis/rest/services/Juniata
Lancaster
https://arcgis.lancastercountypa.gov/arcgis/rest/services
Lancaster
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Lanca
sterCounty/MapServer
Lancaster
https://services1.arcgis.com/I6XnrlnguPDoEObn/arcgis/rest/servic
es
Lancaster
          https://tiles.arcgis.com/tiles/I6XnrlnguPDoEObn/arcgis/rest/services
Lancaster
https://services2.arcgis.com/Q7vbMM01kPfXsshv/ArcGIS/rest/ser
vices
Redevelopment Authority
Lawrence
https://gis.leoc.net:6443/arcgis/rest/services
Lebanon
ArcGIS table of contents not available
Lehigh
https://gis.lehighcounty.org/arcgis/rest/services
Lehigh
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Lehig
hCounty/MapServer
Lehigh
https://services1.arcgis.com/XWDNR4PQlDQwrRCL/arcgis/rest/s
ervices
Lehigh
https://tiles.arcgis.com/tiles/XWDNR4PQlDQwrRCL/arcgis/rest/s
ervices
Luzerne
https://gis.luzernecounty.org/server/rest/services
Lycoming
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Lyco
mingCounty/MapServer
Lycoming
http://gismaps.lyco.org/arcgis/rest/services
not https
Mercer
https://gis.mercercountypa.gov/mercserver/rest/services
Table of contents disabled
Mercer
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Merce
rCounty/MapServer
Mifflin
        https://services3.arcgis.com/9PrY5vQAoyxoIswz/arcgis/rest/services

## Page 359

Mifflin
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Miffli
nCounty/MapServer
Monroe
https://www.monroegis.org/webadaptor/rest/services
Monroe
https://services6.arcgis.com/AISpg3PNp6bMI13R/ArcGIS/rest/ser
vices
Montgomery
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Montg
omeryCounty/MapServer
Montgomery
https://services1.arcgis.com/kOChldNuKsox8qZD/arcgis/rest/servi
ces
Montgomery
https://tiles.arcgis.com/tiles/kOChldNuKsox8qZD/arcgis/rest/servi
ces
Northampton
https://gis.northamptoncounty.org/arcgisweb/rest/services
Northumberland
https://gis.norrycopa.net/arcgis/rest/services
Perry
https://services.arcgis.com/b1rOZp0BNgsXJwyv/arcgis/rest/servic
es
Perry
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Perry
County/MapServer
Pike
https://gis.pikepa.org/arcgis/rest/services
Potter
https://services3.arcgis.com/vqFmmrJngO1NzsuX/ArcGIS/rest/ser
vices
Potter
https://tiles.arcgis.com/tiles/vqFmmrJngO1NzsuX/arcgis/rest/servi
ces
Snyder
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Snyde
rCounty/MapServer
Tioga
https://tiogagis.tiogacountypa.us/arcgis2017/rest/services
Tioga
https://arcgis.vgsi.com/server/rest/services/Tioga_County_PA
Union
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Union
County/MapServer
Union
https://services1.arcgis.com/oX0kbxItOpLtURFa/arcgis/rest/servic
es
Union
https://tiles.arcgis.com/tiles/oX0kbxItOpLtURFa/arcgis/rest/servic
es
Venango
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Venan
goCounty/MapServer

## Page 360

Warren
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Warre
nCounty/MapServer
Warren
https://arcgis.vgsi.com/server/rest/services/Warren_County_PA
Washington
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Washi
ngtonCounty/MapServer
Washington
https://services2.arcgis.com/LgK9DpUhNjdU0HLy/arcgis/rest/serv
ices
Washington
https://tiles.arcgis.com/tiles/LgK9DpUhNjdU0HLy/arcgis/rest/serv
ices
Westmoreland
https://gis.westmorelandcountypa.gov/arcgis/rest/services
Wyoming
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Wyo
mingCounty/MapServer
York
https://arcweb1.ycpc.org/server/rest/services/OPEN_DATA
York
https://mapservices.pasda.psu.edu/server/rest/services/pasda/York
County/MapServer
York
https://services1.arcgis.com/bzC4sqfGZJYY5WBz/arcgis/rest/serv
ices
Pennsylvania Township
Ferguson
          https://services5.arcgis.com/zSetpLaT9l7ewm02/arcgis/rest/services
Ferguson
          https://tiles.arcgis.com/tiles/zSetpLaT9l7ewm02/arcgis/rest/services
Montgomery
https://services3.arcgis.com/JIovTcv1KPd5wmrk/ArcGIS/rest/serv
ices
Pennsylvania City, Town, Village, etc GIS Servers
Abington
https://services9.arcgis.com/vVEAzvHld4MaNqmD/ArcGIS/rest/s
ervices
Abington
https://tiles.arcgis.com/tiles/vVEAzvHld4MaNqmD/arcgis/rest/ser
vices
Allentown
https://geoservices1.allentownpa.gov/server/rest/services
Allentown
https://services1.arcgis.com/WUqVDRuvIiIiH2Pl/ArcGIS/rest/serv
ices
Allentown
https://tiles.arcgis.com/tiles/WUqVDRuvIiIiH2Pl/arcgis/rest/servic
es
Bethlehem
https://services2.arcgis.com/NlbUAihbvA50xxJw/ArcGIS/rest/serv
ices
Bethlehem
https://tiles.arcgis.com/tiles/NlbUAihbvA50xxJw/arcgis/rest/servic
es

## Page 361

Carlisle
https://services3.arcgis.com/pHC6TPvZkDtsIbAp/arcgis/rest/servic
es
Hamburg Area School District
https://services4.arcgis.com/7IX23slWd1fwLYlq/Ar
cGIS/rest/services
Hampton
https://services6.arcgis.com/cMgmhwu0L5CeOOoS/arcgis/rest/ser
vices
Hampton
https://tiles.arcgis.com/tiles/cMgmhwu0L5CeOOoS/arcgis/rest/ser
vices
Hanover Township
https://services7.arcgis.com/n33ZkGC2m9SnOfiy/arcgis/rest/servi
ces

Harrisburg
https://services5.arcgis.com/9n3LUAMi3B692MBL/ArcGIS/rest/s
ervices

Harrisburg
https://tiles.arcgis.com/tiles/9n3LUAMi3B692MBL/arcgis/rest/ser
vices
Lansdale Borough
https://gis.lansdale.org/arcgis/rest/services
Lansdale Borough
https://services2.arcgis.com/b1ixAfZlGa0SKuLS/ArcGIS/rest/servi
ces
Lansdale Borough
https://tiles.arcgis.com/tiles/b1ixAfZlGa0SKuLS/arcgis/rest/servic
es
Norristown
https://services7.arcgis.com/XSBhS35I3OBovhy9/arcgis/rest/servi
ces
Penn Hills
https://services5.arcgis.com/DllnbBENKfts6TQD/ArcGIS/rest/serv
ices
Philadelphia
https://services.arcgis.com/fLeGjb7u4uXqeF9q/arcgis/rest/services
Philadelphia
           https://tiles.arcgis.com/tiles/fLeGjb7u4uXqeF9q/arcgis/rest/services
Pittsburgh
See also Allegheny County
Pittsburgh
https://services1.arcgis.com/YZCmUqbcsUpOKfj7/ArcGIS/rest/ser
vices
Pittsburgh
https://tiles.arcgis.com/tiles/YZCmUqbcsUpOKfj7/arcgis/rest/servi
ces
Spring Creek
https://mapservices.pasda.psu.edu/server/rest/services/pasda/Spring
Creek_PA/MapServer
Tredyffrin Township https://services2.arcgis.com/o9a0D2ZwwG8CDFVQ/arcgis/rest/ser
vices

## Page 362

Waren
See Warren County
Rhode Island State GIS Servers
Rhode Island Maps and Data
Website: https://risegis.ri.gov/portal/home
GIS: https://risegis.ri.gov/gpserver/rest/services
8-10-2023 No tiled data
GIS: https://risegis.ri.gov/hosting/rest/services
Parcel lines:  RIDEM/Tax_Parcels/MapServer/0
/RIDEM/Arcadia_Trails_Rev2/MapServer
trail data.  Supports dynamic layers.
8-10-2023 No tiled data
GIS: https://risegis.ri.gov/imgserver/rest/services
GIS: https://services2.arcgis.com/S8zZg9pg23JUEexQ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/S8zZg9pg23JUEexQ/arcgis/rest/services
Rhode Island Department of Health
Website: https://health.ri.gov
GIS: https://services1.arcgis.com/dkWT1XL4nglP5MLP/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/dkWT1XL4nglP5MLP/arcgis/rest/services
Rhode Island Department of Transportation
Website: https://www.dot.ri.gov
GIS: https://vueworks.dot.ri.gov/arcgis/rest/services
8-10-2023 No tiled data
GIS: https://spatialags.vhb.com/arcgis/rest/services/RIMobility
8-10-2023 No tiled data
GIS: https://spatialags.vhb.com/arcgis/rest/services/RITransit
8-10-2023 No tiled data
GIS: https://gisstage.dot.ri.gov/editting/rest/services
GIS: https://services1.arcgis.com/7arM4WYbUOtKu3Zq/ArcGIS/rest/services
Rhode Island Emergency Management Agency
Website: https://riema.ri.gov
GIS: https://services.arcgis.com/NTATf0tiWDCcE3aD/arcgis/rest/services
University of Rhode Island - Environmental Data Center
Website: https://www.edc.uri.edu
GIS: https://maps.edc.uri.edu/arcgis/rest/services
Rhode Island City, Town, Village, etc GIS Servers
Does not have county governments
Burrillville
https://gisserver2.axisgis.com/arcgis/rest/services/BurrillvilleRI

Not open to public

## Page 363

Charlestown
https://dfgdfg.mapxpress.net/arcgis/rest/services/Charlestown
Charlestown
https://sgsdgf.mapxpress.net/arcgis/rest/services/Charlestown
Charlestown
https://server1.mapxpress.net/arcgis/rest/services/Charlestown
Cranston
_ttps://gis.cranstonri.org/arcgis/rest/services
dead link 1
Cranston
https://services5.arcgis.com/bmiwyveTUuaT56jB/ArcGIS/rest/serv
ices
Glocester
https://arcgis.vgsi.com/server/rest/services/Glocester_RI
Hopkinton
https://dfgdfg.mapxpress.net/arcgis/rest/services/Hopkinton
Hopkinton
https://sgsdgf.mapxpress.net/arcgis/rest/services/Hopkinton
Hopkinton
https://arcgis.vgsi.com/server/rest/services/Hopkinton_RI
Hopkinton
https://server1.mapxpress.net/arcgis/rest/services/Hopkinton
Middletown
https://hostingdata3.tighebond.com/arcgis/rest/services/Middletow
nRI
Newport
https://services2.arcgis.com/URasD5e1uL7MfVOn/arcgis/rest/serv
ices
Providence
https://webgis.providenceri.gov/server/rest/services

Providence
https://engineering.provwater.com/arconline/rest/services
Providence
https://services6.arcgis.com/wv9mHoqblhTsnqdG/arcgis/rest/servi
ces
Providence
https://tiles.arcgis.com/tiles/wv9mHoqblhTsnqdG/arcgis/rest/servi
ces
Providence
https://services6.arcgis.com/obJRhrN980HlxKDK/ArcGIS/rest/ser
vices
Providence
https://tiles.arcgis.com/tiles/obJRhrN980HlxKDK/arcgis/rest/servi
ces
Scranton
https://services7.arcgis.com/c8axx5qqzVWAC8iN/ArcGIS/rest/ser
vices
Smithfield
They have a GIS based on Google maps
South Kingstown
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/SouthK
ingstown_Basemap/MapServer
South Kingstown
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/SouthK
ingstown_OperationalMap_Pub/MapServer
South Kingstown
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/SouthK
ingstown_OperationalMap_Tax_Pub/MapServer
South Kingstown
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/SouthK
ingstown_OperationalMap/MapServer

## Page 364

South Kingstown
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/SouthK
ingstown_Overview/MapServer
South Kingstown
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/SouthK
ingstownRI_ViewPermit/MapServer
Westerly
https://dfgdfg.mapxpress.net/arcgis/rest/services/Westerly
Westerly
https://sgsdgf.mapxpress.net/arcgis/rest/services/Westerly
Westerly
https://server1.mapxpress.net/arcgis/rest/services/Westerly
Westerly
https://server1.mapxpress.net/arcgis/rest/services/Westerly
South Carolina State GIS Servers
South Carolina various layers
GIS: https://ags3.scgov.net/agsfed/rest/services
Table of contents disabled
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
South Carolina Department of Health and Environmental Control
Website: https://des.sc.gov
GIS: https://gisweb01vm.dhec.sc.gov/arcgis/rest/services
Table of contents disabled
8-10-2023 No tiled data
GIS: https://gis.dhec.sc.gov/arcgis/rest/services
Table of contents disabled
Parcel lines by county:  Baselayers/Parcels/MapServer
Dams
8-10-2023 No tiled data
GIS: https://services2.arcgis.com/XZg2efAbaieYAXmu/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/XZg2efAbaieYAXmu/arcgis/rest/services
South Carolina Department of Natural Resources
Website: https://www.dnr.sc.gov
GIS: https://services.arcgis.com/acgZYxoN5Oj8pDLa/arcgis/rest/services
GIS: https://arcweb.dnr.sc.gov/server/rest/services
South Carolina Department of Public Safety
Website: https://scdps.sc.gov
GIS: https://services2.arcgis.com/P9hJiO7L6IjDhyvn/ArcGIS/rest/services
State Law Enforcement Division
GIS: https://tiles.arcgis.com/tiles/P9hJiO7L6IjDhyvn/arcgis/rest/services
GIS: https://services7.arcgis.com/TdsEnMqzMcTd7pnb/ArcGIS/rest/services
South Carolina Emergency Management Division
Website: https://www.scemd.org
GIS: https://services1.arcgis.com/TXIoeSnCA2m7KVZj/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/TXIoeSnCA2m7KVZj/arcgis/rest/services
South Carolina Department of Transportation
https://services1.arcgis.com/VaY7cY9pvUYUP1Lf/arcgis/rest/services

## Page 365

https://tiles.arcgis.com/tiles/VaY7cY9pvUYUP1Lf/arcgis/rest/services
South Carolina Army National Guard
GIS: https://scarng-gis.sc.gov/arcgis/rest/services
South Carolina Aeronautics Commission
Website: http://www.scaeronautics.com/commission.asp
not https
GIS: https://services1.arcgis.com/mBK8wqXy5kTsaVZw/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/mBK8wqXy5kTsaVZw/arcgis/rest/services
South Carolina various layers
GIS: https://services.arcgis.com/F7DSX1DSNSiWmOqh/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/F7DSX1DSNSiWmOqh/arcgis/rest/services
South Carolina Regional
Grand Strand Water and Sewer Authority
Website: https://www.gswsa.com
GIS: _ttps://www.gswsa.com/arcgis/rest/services
dead link 3
Berkeley-Charleston-Dorchester Council of Governments
Website: https://bcdcog.com/about-bcdcog
GIS: https://services2.arcgis.com/BTzI2Eau2uhzyzR0/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/BTzI2Eau2uhzyzR0/arcgis/rest/services
South Carolina County GIS Servers
All counties are listed and have been checked for GIS
Abbeville
Schneider Geospatial - ArcGIS server address is not public
Aiken
Schneider Geospatial - ArcGIS server address is not public
Allendale
Schneider Geospatial - ArcGIS server address is not public
Anderson
https://propertyviewer.andersoncountysc.org/arcgis/rest/services
Bamberg
Schneider Geospatial - ArcGIS server address is not public
Barnwell
Schneider Geospatial - ArcGIS server address is not public
Beaufort
https://gis.beaufortcountysc.gov/server/rest/services
Beaufort
https://image.beaufortcountysc.gov/server/rest/services
Beaufort
https://services.arcgis.com/mbPLXL6SDfBjrAmS/arcgis/rest/servi
ces
Beaufort
https://tiles.arcgis.com/tiles/mbPLXL6SDfBjrAmS/arcgis/rest/serv
ices

## Page 366

Berkeley
https://gis.berkeleycountysc.gov/arcgis/rest/services
Calhoun
https://gis.aecomonline.net/arcgis/rest/services/CalhounCO
Charleston
https://gisccapps.charlestoncounty.org/arcgis/rest/services
Charleston
https://gisccimg.charlestoncounty.org/arcgis/rest/services
Charleston
https://services.arcgis.com/jR9eNCjAkxwH2nLe/arcgis/rest/servic
es
Cherokee
Schneider Geospatial - ArcGIS server address is not public
Chester
Schneider Geospatial - ArcGIS server address is not public
Chesterfield
GIS is not ArcGIS
Clarendon
GIS is not ArcGIS
Colleton
https://services1.arcgis.com/m0cnLGKdhwao8WvM/ArcGIS/rest/s
ervices
Colleton
https://tiles.arcgis.com/tiles/m0cnLGKdhwao8WvM/arcgis/rest/ser
vices
Darlington
           https://services5.arcgis.com/8FJikaProY6O3ncx/arcgis/rest/services
Dillon
GIS is not ArcGIS
Dorchester
https://gisportal.dorchestercounty.net/hosting/rest/services

Edgefield
Schneider Geospatial - ArcGIS server address is not public
Fairfield
Schneider Geospatial - ArcGIS server address is not public
Florence
https://arc2000.florenceco.org/arcgis/rest/services
Florence
https://services1.arcgis.com/40L6yX6OtdCifNez/arcgis/rest/servic
es
Georgetown
https://gis1.georgetowncountysc.org/portal/rest/services
Georgetown
https://services6.arcgis.com/nEIrIdcFpdK28ibf/arcgis/rest/services
Greenville
https://services.arcgis.com/s8BzdTejnTIG3ix6/arcgis/rest/services
Greenville
https://tiles.arcgis.com/tiles/s8BzdTejnTIG3ix6/arcgis/rest/services
Greenwood
http://www.greenwoodsc.gov/arcgis/rest/services
not https
Hampton
https://services8.arcgis.com/6eabNhFouHU5vuYk/arcgis/rest/servi
ces

## Page 367

Horry
https://www.horrycounty.org/gisweb/rest/services
Horry
https://services1.arcgis.com/If0JkGr8ABreBTuS/ArcGIS/rest/servi
ces
Horry
           https://tiles.arcgis.com/tiles/If0JkGr8ABreBTuS/arcgis/rest/services
Jasper
https://services3.arcgis.com/oJaBluQKw5aLHpzj/arcgis/rest/servic
es
Jasper
https://tiles.arcgis.com/tiles/oJaBluQKw5aLHpzj/arcgis/rest/servic
es
Kershaw
GIS is not ArcGIS
Lancaster
https://services3.arcgis.com/rJcpRneDUBgTeCT3/arcgis/rest/servi
ces
Lancaster
https://tiles.arcgis.com/tiles/rJcpRneDUBgTeCT3/arcgis/rest/servi
ces
Laurens
https://gis.aecomonline.net/arcgis/rest/services/LCWSC
Lee
Schneider Geospatial - ArcGIS server address is not public
Lexington
https://maps.lex-co.com/agstserver/rest/services
Table of  contents disabled
Marion
GIS is not ArcGIS
Marlboro
GIS is not ArcGIS
McCormick
GIS is not ArcGIS
Newberry
https://map.newberrycounty.net/gis/rest/services
Oconee
https://arcserver2.oconeesc.com/arcgis/rest/services
Oconee
https://services1.arcgis.com/UOvRn2Rvzysthh3i/ArcGIS/rest/servi
ces
Oconee
https://services7.arcgis.com/JBTLpuRiIpQ2vA5Y/ArcGIS/rest/ser
vices
Oconee
https://tiles.arcgis.com/tiles/JBTLpuRiIpQ2vA5Y/arcgis/rest/servic
es
Orangeburg
https://gis2.orangeburgcounty.org/ocgis/rest/services
Pickens
          https://services1.arcgis.com/59960rq18IxUcAVI/arcgis/rest/services
Pickens
           https://tiles.arcgis.com/tiles/59960rq18IxUcAVI/arcgis/rest/services
Richland
GIS is not ArcGIS

## Page 368

Saluda
https://saludacountysc.net/arcgis/rest/services
Spartanburg
https://maps.spartanburgcounty.org/server/rest/services
Spartanburg
https://maps.spartanburgcounty.org/image/rest/services
Sumter
ArcGIS REST services not public
Union
GIS is not ArcGIS
Williamsburg
GIS is not ArcGIS
York
https://maps2.yorkcountygov.com/imagery/rest/services
York
https://maps.yorkcounty.gov/arcgis/rest/services
York
https://services1.arcgis.com/2AGLxyiJoNiVHKwq/arcgis/rest/serv
ices
York
https://tiles.arcgis.com/tiles/2AGLxyiJoNiVHKwq/arcgis/rest/servi
ces
South Carolina City, Town, Village, etc GIS Servers
Aiken
https://gis.cityofaikensc.gov/arcgis/rest/services
Aiken
https://services6.arcgis.com/1j2MGpnNTNYf1YBN/ArcGIS/rest/s
ervices
Aiken
https://tiles.arcgis.com/tiles/1j2MGpnNTNYf1YBN/arcgis/rest/ser
vices
Batesburg-Leesville
__________
Beaufort
https://services9.arcgis.com/NpTdr5u1ft9aY31O/ArcGIS/rest/servi
ces
Bluffton
https://www.townofbluffton.us/s/rest/services
Bluffton
https://services2.arcgis.com/emqdvAOVfTSmahz0/arcgis/rest/serv
ices
Bluffton
https://tiles.arcgis.com/tiles/emqdvAOVfTSmahz0/arcgis/rest/servi
ces
Charleston
https://gis.charleston-sc.gov/arcgis/rest/services
Charleston
https://gis.charleston-sc.gov/arcgis2/rest/services
Clemson
https://services2.arcgis.com/xPCLC1gCi03Ni6Q1/arcgis/rest/servi
ces
Clinton
https://gis.cityofclintonsc.com/arcgis/rest/services

Columbia
https://services1.arcgis.com/Mnt8FoJcogKtoVBs/arcgis/rest/servic
es

## Page 369

Columbia
https://tiles.arcgis.com/tiles/Mnt8FoJcogKtoVBs/arcgis/rest/servic
es
Conway
https://gis.cityofconway.com/arcgis/rest/services
Fort Mill
https://gis.aecomonline.net/arcgis/rest/services/FortMill
Greenville
https://citygis.greenvillesc.gov/arcgis/rest/services
Greenville
https://www.gcgis.org/arcgis/rest/services
Greenville
https://services.arcgis.com/s8BzdTejnTIG3ix6/arcgis/rest/services
Greenville
https://tiles.arcgis.com/tiles/s8BzdTejnTIG3ix6/arcgis/rest/services
Greenwood
See also Greenwood county
Greer
https://gismaps.cityofgreer.org/arcgis/rest/services
 SSL problem
Greer
https://services1.arcgis.com/bskBH6JV42oEWJvZ/arcgis/rest/servi
ces
Hardeeville
https://services6.arcgis.com/UXJOITFCLbn0Ibm0/ArcGIS/rest/ser
vices
Hilton Head Island
https://gis.hiltonheadislandsc.gov/arcgis/rest/services
SSL problem
Hilton Head Island
https://services1.arcgis.com/t1pOARESVtLutuqb/ArcGIS/rest/serv
ices
Hilton Head Island
https://tiles.arcgis.com/tiles/t1pOARESVtLutuqb/arcgis/rest/servic
es
Mount Pleasant
https://maps.tompsc.com/arcgis/rest/services
Myrtle Beach
https://services2.arcgis.com/650sW8BhgpAHhq6u/arcgis/rest/servi
ces
Myrtle Beach
https://tiles.arcgis.com/tiles/650sW8BhgpAHhq6u/arcgis/rest/servi
ces
North Charleston
https://arc.northcharleston.org/arcgis/rest/services
Parker
_ttps://gis.aecomonline.net/arcgis/rest/services/Parker   dead link 3
Rock Hill
https://rockhillgis.cityofrockhill.com/arcgis/rest/services
Summerville
https://services8.arcgis.com/0zSnoqwLCR3i1Yfw/ArcGIS/rest/ser
vices
Summerville
https://tiles.arcgis.com/tiles/0zSnoqwLCR3i1Yfw/arcgis/rest/servi
ces

## Page 370

Sumter
https://services.arcgis.com/4B9WU9185SohZnyi/arcgis/rest/servic
es
Sumter
https://tiles.arcgis.com/tiles/4B9WU9185SohZnyi/arcgis/rest/servi
ces
West Columbia
https://services5.arcgis.com/A56vsmaRYeXpHm01/arcgis/rest/ser
vices
West Columbia
https://tiles.arcgis.com/tiles/A56vsmaRYeXpHm01/arcgis/rest/serv
ices
South Dakota State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
South Dakota Open Data
Website: https://opendata2017-09-18t192802468z-sdbit.opendata.arcgis.com
South Dakota Department of Transportation
Website: https://dot.sd.gov
GIS: https://sdgis.sd.gov/dot/rest/services
South Dakota various layers
GIS: https://arcgis.sd.gov/arcgis/rest/services
8-10-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://sdgis.sd.gov/host/rest/services
8-10-2023 No tiled data
GIS: https://gfpgis.sd.gov/arcgis/rest/services
GIS: https://sdgis.sd.gov/gfp/rest/services
University of South Dakota
Website: https://www.usd.edu
GIS: https://gis.usd.edu/arcgis/rest/services
8-10-2023 No tiled data
South Dakota Regional
Community Planning. and Economic Development (Northeast South Dakota)
Website: https://www.1stdistrict.org/
GIS: https://www.1stdistrict.org/arcgis/rest/services
8-10-2023 No tiled data
Planning and Development DISTRICT III
Website: https://www.districtiii.org
GIS: https://gis.districtiii.org/server/rest/services
First District Association of Local Governments

## Page 371

Website: https://www.1stdistrict.org
GIS: https://services5.arcgis.com/ceZU40cgb1gjKt1n/ArcGIS/rest/services
South Dakota County GIS Servers
Aurora
https://gis.districtiii.org/server/rest/services/AURORA_COUNTY_
WEB_LAYERS/MapServer
Go to the top and search for ‘Aurora’
Beadle
https://www.1stdistrict.org/arcgis/rest/services/Beadle
Bennett
https://gis.districtiii.org/server/rest/services/BENNETT_COUNTY
_WEB_LAYERS/MapServer
Go to the top and search for ‘Bennett’

Bon Homme
_ttps://gis.districtiii.org/server/rest/services/BON_HOMME_COU
NTY_WEB_LAYERS/MapServer
dead link 1
Go to the top and search for ‘Bon Homme’
Brule
https://gis.districtiii.org/server/rest/services/BRULE_COUNTY_W
EB_LAYERS/MapServer
Go to the top and search for ‘Brule’
Buffalo
https://gis.districtiii.org/server/rest/services/BUFFALO_COUNTY
_WEB_LAYERS/MapServer
Go to the top and search for ‘Buffalo’
Burke
______________
Butte
https://gis.districtiii.org/server/rest/services/BUTTE_COUNTY_W
EB_LAYERS2/MapServer
Go to the top and search for ‘Butte’
Campbell
https://gis.districtiii.org/server/rest/services/CAMPBELL_COUNT
Y_WEB_LAYERS/MapServer
Go to the top and search for ‘Campbell’
Charles Mix
_ttps://gis.districtiii.org/server/rest/services/CHARLES_MIX_WE
B_LAYERS/MapServer
dead link 1
Go to the top and search for ‘Charles_Mix’
Clark
https://www.1stdistrict.org/arcgis/rest/services/Clark
Codington
https://www.1stdistrict.org/arcgis/rest/services/Codington
Davison
https://gis.districtiii.org/server/rest/services/DAVISON_COUNTY
_WEB_LAYERS1/MapServer

## Page 372

Go to the top and search for ‘Davison’
Day
https://gis.districtiii.org/server/rest/services/DAY_COUNTY_WE
B_LAYERS/MapServer
Go to the top and search for ‘Day’
Deuel
https://www.1stdistrict.org/arcgis/rest/services/Deuel
Douglas
https://gis.districtiii.org/server/rest/services/DOUGLAS_COUNTY
_WEB_LAYERS/MapServer
Go to the top and search for ‘Douglas’
Edmunds
https://www.1stdistrict.org/arcgis/rest/services/Edmunds
Faulk
https://gis.districtiii.org/server/rest/services/FAULK_COUNTY_W
EB_LAYERS/MapServer
Go to the top and search for ‘Faulk’
Grant
https://www.1stdistrict.org/arcgis/rest/services/Grant
Gregory
https://gis.districtiii.org/server/rest/services/GREGORY_COUNT
Y_WEB_LAYERS/MapServer
Go to the top and search for ‘Gregory’
Hamlin
https://www.1stdistrict.org/arcgis/rest/services/Hamlin
Hanson
https://gis.districtiii.org/server/rest/services/HANSON_COUNTY_
WEB_LAYERS/MapServer
Go to the top and search for ‘Hanson’
Hughes
https://gis.districtiii.org/server/rest/services/HUGHES_COUNTY_
WEB_LAYERS/MapServer
Go to the top and search for ‘Hughes’
Hutchinson
https://gis.districtiii.org/server/rest/services/HUTCHINSON_COU
NTY_WEB_LAYERS2/MapServer
Go to the top and search for ‘Hutchinson’
Jackson
https://gis.districtiii.org/server/rest/services/JACKSON_COUNTY
_WEB_LAYERS2/MapServer
Go to the top and search for ‘Jackson’
Jerauld
https://gis.districtiii.org/server/rest/services/JERAULD_COUNTY
_WEB_LAYERS/MapServer
Go to the top and search for ‘Jerauld’

## Page 373

Jones
https://gis.districtiii.org/server/rest/services/JONES_COUNTY_W
EB_LAYERS/MapServer
Go to the top and search for ‘Jones’
Kingsbury
https://www.1stdistrict.org/arcgis/rest/services/Kingsbury
Lake
https://www.1stdistrict.org/arcgis/rest/services/Lake
Lawrence
___________
Lincoln
https://gis.lincolncountysd.gov/arcgis/rest/services
Lyman
https://gis.districtiii.org/server/rest/services/LYMAN_COUNTY_
WEB_LAYERS/MapServer
Go to the top and search for ‘Lyman’
Marshall
https://gis.districtiii.org/server/rest/services/MARSHALL_COUNT
Y_WEB_LAYERS/MapServer
Go to the top and search for ‘Marshall’
McPherson
https://gis.districtiii.org/server/rest/services/MCPHERSON_COU
NTY_WEB_LAYERS/MapServer
Go to the top and search for ‘McPherson’
Meade
https://wfs.schneidercorp.com/arcgis/rest/services/MeadeCountyS
D_REST/MapServer
Meade
https://wfs.schneidercorp.com/arcgis/rest/services/MeadeCountyS
D_WFS/MapServer
Mellette
https://gis.districtiii.org/server/rest/services/MELLETTE_COUNT
Y_WEB_LAYERS/MapServer
Go to the top and search for ‘Mellette’
Miner
https://www.1stdistrict.org/arcgis/rest/services/Miner
Moody
https://www.1stdistrict.org/arcgis/rest/services/Moody
Minnehaha
https://gis.minnehahacounty.org/minnemap/rest/services
Minnehaha
https://services.arcgis.com/I1RVogOPDepkQmjk/arcgis/rest/servic
es
Pennington
https://services.arcgis.com/NYzD3RdsOTglw6xI/arcgis/rest/servic
es
Pennington
https://tiles.arcgis.com/tiles/NYzD3RdsOTglw6xI/arcgis/rest/servi
ces

## Page 374

Potter
https://gis.districtiii.org/server/rest/services/POTTER_COUNTY_
WEB_LAYERS/MapServer
Roberts
https://www.1stdistrict.org/arcgis/rest/services/Roberts
Sanborn
https://gis.districtiii.org/server/rest/services/SANBORN_COUNT
Y_WEB_LAYERS/MapServer
Go to the top and search for ‘Sanborn’
Stanley
https://gis.districtiii.org/server/rest/services/STANLEY_COUNTY
_WEB_LAYERS/MapServer
Go to the top and search for ‘Stanley’
Sully
https://gis.districtiii.org/server/rest/services/SULLY_COUNTY_W
EB_LAYERS/MapServer
Go to the top and search for ‘Sully’
Tripp
https://gis.districtiii.org/server/rest/services/TRIPP_TODD_WEB_
LAYERS/MapServer
Go to the top and search for ‘Tripp’
Turner
https://gis.districtiii.org/server/rest/services/TURNER_COUNTY_
LAYERS/MapServer
Go to the top and search for ‘Turner’
Yankton
____________
Ziebach
https://gis.districtiii.org/server/rest/services/ZIEBACH_WEB_LA
YERS/MapServer
Go to the top and search for ‘Ziebach’
South Dakota City, Town, Village, etc GIS Servers
Ames
https://gis.cityofames.org/arcgis/rest/services
Table of contents disabled
Belle Fourche
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Belle_F
ourche_SD_MGMT/MapServer
Table of contents disabled
Chamberlain
Cleveland
https://www.efsedge.com/arcgis/rest/services/Cleveland_SD
Fall River
___________
Harrisburg
https://gis3.gisworkshop.com/arcgis/rest/services/City_of_Harrisbu
rg_SD_MGMT/MapServer
Table of contents disabled

## Page 375

Madison
https://wfs.schneidercorp.com/arcgis/rest/services/CityofMadisonS
D_REST/MapServer
Mason City
https://wfs.schneidercorp.com/arcgis/rest/services/CityofMasonCit
yIA_WFS/MapServer
Milbank
https://www.1stdistrict.org/arcgis/rest/services/Milbank
Mitchell
https://gis.districtiii.org/server/rest/services/MITCHELL_CEMET
ERY_WEB_LAYERS/MapServer

Pierre
?
Rapid City
https://permits.rcgov.org/arcgiswebadaptor/rest/services
Rapid City
https://gis.rcgov.org/server/rest/services
Rapid City
See also Pennington County
Sioux Falls
https://gis.siouxfalls.gov/arcgis/rest/services
Sioux Falls
https://services.arcgis.com/YpECgwASS4iMvgsA/arcgis/rest/servi
ces
Sioux Falls
https://tiles.arcgis.com/tiles/YpECgwASS4iMvgsA/arcgis/rest/serv
ices
Tennessee State GIS Servers
Parcel lines:  Public data not found on any state ArcGIS server
Tennessee Open Data Portal
Website: https://tn-tnmap.opendata.arcgis.com/
GIS: https://tnmap.tn.gov/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
CADASTRAL/STATEWIDE_PARCELS_WEB_MERCATOR/MapServer
likely need a token
Tennessee Emergency Management Agency
Website: https://www.tn.gov/tema.html
GIS: https://services1.arcgis.com/kILp9lqGUeOhnDbI/ArcGIS/rest/services
Tennessee Geographic Information Council
Website: https://www.tngic.org
GIS: https://services8.arcgis.com/Pf1Hg2j6tlIyfPPe/arcgis/rest/services
Tennessee Department of Environment and Conservation
Website: https://tdec.tn.gov/
GIS: https://tdeconline.tn.gov/arcgis/rest/services

## Page 376

8-12-2023 No tiled data
GIS: https://services5.arcgis.com/bPacKTm9cauMXVfn/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/bPacKTm9cauMXVfn/arcgis/rest/services
Tennessee Department of Transportation
Website: https://www.tn.gov/tdot.html
GIS: https://spatial.tdot.tn.gov/arcgis/rest/services
8-12-2023 No tiled data
GIS: https://services2.arcgis.com/nf3p7v7Zy4fTOh6M/arcgis/rest/services
Tennessee Wildlife Resources Agency
Website: https://www.tn.gov/twra.html
GIS: https://services3.arcgis.com/PWXNAH2YKmZY7lBq/arcgis/rest/services
Tennessee Comptroller of the Treasury
GIS: https://services2.arcgis.com/63Ka7QbNqm4NLbeo/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/63Ka7QbNqm4NLbeo/arcgis/rest/services
Tennessee various layers
GIS: https://services1.arcgis.com/YuVBSS7Y1of2Qud1/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/YuVBSS7Y1of2Qud1/arcgis/rest/services
Tennessee Regional
Chattanooga-Hamilton County Regional Planning Agency
Website: https://chcrpa.org
GIS: https://services2.arcgis.com/cclAu9OKhOfjeUdr/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/cclAu9OKhOfjeUdr/arcgis/rest/services
North West Utility District
GIS: https://services.arcgis.com/dzhPRiWP0DwuzONX/arcgis/rest/services
Sewanee Utility District
Website: https://www.sewaneeutility.org         server might be slow
GIS: https://services7.arcgis.com/WH3Iir20Swo1MIop/arcgis/rest/services
Tennessee County GIS Servers
Blount
https://com.blountgis.org/server/rest/services
Chester
https://maps.capturecama.com/arcgis/rest/services/Chester
Greene
https://www.gcgis.org/arcgis/rest/services
Hamilton
https://mapsdev.hamiltontn.gov/hcwa03/rest/services
Hickman
https://maps.capturecama.com/arcgis/rest/services/Hickman

## Page 377

Jefferson
https://services7.arcgis.com/in9ruKxwZKI20efQ/arcgis/rest/servic
es
Lincoln
_ttps://lctnecd.com/arcgis/rest/services
dead link 1
Lincoln
https://services7.arcgis.com/6g8EiHg00n6qjpO2/ArcGIS/rest/servi
ces
Lincoln
           https://tiles.arcgis.com/tiles/6g8EiHg00n6qjpO2/arcgis/rest/services
Maury
_ttp://maps.maurycounty-tn.gov/arcgis/rest/services    dead link 3
Montgomery
https://maps.capturecama.com/arcgis/rest/services/MontTN
Putnam
_ttps://services.putnamco.org/arcgis/rest/services
dead link 3
Rutherford
https://imagery.rutherfordcountytn.gov/img/rest/services
Rutherford
https://maps.rutherfordcountytn.gov/ags02/rest/services
Rutherford
https://services.arcgis.com/36I6IHIdr660pAyH/arcgis/rest/services
Rutherford
           https://tiles.arcgis.com/tiles/36I6IHIdr660pAyH/arcgis/rest/services
Sevier
https://services1.arcgis.com/Qu4yM4JJvNoC2GKw/arcgis/rest/ser
vices
Shelby
https://gis.shelbycountytn.gov/arcgis/rest/services
Shelby
https://uasiportal.shelbycountytn.gov/arcgis/rest/services
Shelby
https://services5.arcgis.com/sn9W9R6WNyjF8aWW/ArcGIS/rest/s
ervices
Shelby
https://services6.arcgis.com/FStub7HlCSCdqoXK/ArcGIS/rest/ser
vices
Tipton
https://services3.arcgis.com/dpcWjCfPyDdLMs5n/ArcGIS/rest/ser
vices
Tipton
https://tiles.arcgis.com/tiles/dpcWjCfPyDdLMs5n/arcgis/rest/servi
ces
Williamson
https://arcgis2.williamson-tn.org/arcgis/rest/services
Tennessee City, Town, Village, etc GIS Servers
Arlington
_________
Brentwood
https://maps.brentwoodtn.gov/arcgis/rest/services
Chattanooga
https://pwgis.chattanooga.gov/arcgis/rest/services
Chattanooga
https://services2.arcgis.com/OIAIimblRxPs0xxc/ArcGIS/rest/servi
ces
Chattanooga
           https://tiles.arcgis.com/tiles/OIAIimblRxPs0xxc/arcgis/rest/services

## Page 378

Clarksville
https://services1.arcgis.com/dsBx9Fh6umHq10SL/ArcGIS/rest/ser
vices
Clarksville
https://tiles.arcgis.com/tiles/dsBx9Fh6umHq10SL/arcgis/rest/servi
ces
Cleveland
https://gis.clevelandtn.gov/arcgis/rest/services
Table of contents disabled
Collierville
https://services1.arcgis.com/sRmcNvrTVX9Y0AgX/ArcGIS/rest/s
ervices
Collierville
https://tiles.arcgis.com/tiles/sRmcNvrTVX9Y0AgX/arcgis/rest/ser
vices
Elizabethton
_ttps://arcfm.eesonline.org/arcgis/rest/services
dead link 1
Franklin
https://publicmaps.franklintn.gov/arcgis/rest/services
Gallatin
https://arcweb.gallatin-tn.gov/arcgis/rest/services
Germantown
https://services5.arcgis.com/LnfZzt7NtPrHmp5p/ArcGIS/rest/servi
ces
Greeneville
See Greene county
Henderson
https://arcgis5.roktech.net/arcgis/rest/services/Henderson
Johnson City
https://gis.johnsoncitytn.org/arcgis/rest/services
Johnson City
https://services2.arcgis.com/sFeLdas1ukfB6i8T/ArcGIS/rest/servic
es
Johnson City
https://tiles.arcgis.com/tiles/sFeLdas1ukfB6i8T/arcgis/rest/services
Kingsport
https://services1.arcgis.com/zH77CQArAPDz2Bv4/ArcGIS/rest/se
rvices
Kingsport
https://tiles.arcgis.com/tiles/zH77CQArAPDz2Bv4/arcgis/rest/serv
ices
Knoxville

https://www.kgis.org/arcgis/rest/services           Not open to public
Lebanon
https://maps.lebanontn.org/arcgis/rest/services
Lincoln
https://services7.arcgis.com/2pbkyZtgsuWoNVtB/ArcGIS/rest/serv
ices
Memphis
https://maps.memphistn.gov/hosted/rest/services
Memphis
https://comgis2.memphistn.gov/arcgis/rest/services    SSL problem

## Page 379

Memphis
https://services2.arcgis.com/saWmpKJIUAjyyNVc/ArcGIS/rest/ser
vices
Memphis
https://tiles.arcgis.com/tiles/saWmpKJIUAjyyNVc/arcgis/rest/servi
ces
Montgomery
https://mcggis.mcgtn.org/mcggis/rest/services
Morristown
https://services.mh-gis.com/server/rest/services
Murfreesboro
https://mwrdmaps.murfreesborotn.gov/server/rest/services
Murfreesboro
_ttps://mwsdmaps.murfreesborotn.gov/mwsd/rest/services
dead link 1
Murfreesboro
https://maps.murfreesborotn.gov/image/rest/services
Murfreesboro
https://mpdgisweb.ci.murfreesboro.tn.us/arcgis/rest/services
Murfreesboro
https://services5.arcgis.com/A5C0MR9xfkxVRwat/ArcGIS/rest/se
rvices
Murfreesboro
https://tiles.arcgis.com/tiles/A5C0MR9xfkxVRwat/arcgis/rest/servi
ces

Nashville
https://maps.nashville.gov/arcgis/rest/services
Nashville
https://services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/ser
vices
Nashville
https://tiles.arcgis.com/tiles/HdTo6HJqh92wn4D8/arcgis/rest/servi
ces
Portland
https://services2.arcgis.com/T3IV683iYKk0vYAI/arcgis/rest/servi
ces
Portland
https://tiles.arcgis.com/tiles/T3IV683iYKk0vYAI/arcgis/rest/servic
es
Smyrna
https://maps.townofsmyrna.org/server/rest/services
Spring Hill
https://arcgis4.roktech.net/arcgis/rest/services/SpringHillTN
Spring Hill
https://arcgis5.roktech.net/arcgis/rest/services/SpringHillTN
White House
https://services3.arcgis.com/pFngyvIqq2CUcLpI/ArcGIS/rest/servi
ces
White House            https://tiles.arcgis.com/tiles/pFngyvIqq2CUcLpI/arcgis/rest/services
Texas State GIS Servers
Parcel lines:  Data not found on any state ArcGIS server
Texas Open Data Portal
Website: https://data.texas.gov/

## Page 380

Texas Division of Emergency Management
Website: https://tdem.texas.gov
GIS: https://services5.arcgis.com/Rvw11bGpzJNE7apK/ArcGIS/rest/services
Texas Parks and Wildlife Department
Website: https://tpwd.texas.gov
GIS: https://tpwd.texas.gov/arcgis/rest/services
8-12-2023 No tiled data
GIS: https://tpwd.texas.gov/server/rest/services
GIS: https://services1.arcgis.com/1mtXwieMId59thmg/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/1mtXwieMId59thmg/arcgis/rest/services
Texas Department of Transportation
Website: https://www.txdot.gov/
GIS: https://maps.dot.state.tx.us/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://maps.txdot.gov/arcgis/rest/services
GIS: https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/KTcxiTD9dsQw4r7Z/arcgis/rest/services
Texas Department of State Health Services
Website: https://www.dshs.texas.gov
GIS: https://services3.arcgis.com/vljlarU2635mITsl/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/vljlarU2635mITsl/arcgis/rest/services
Texas Legislative Council
Website: https://tlc.texas.gov
GIS: https://giswebe.tlc.texas.gov/ArcGIS/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
districts for 2026 congressional election: /plan_shaded/MapServer
Texas Commission on Environmental Quality
Website: https://www.tceq.texas.gov
GIS: https://gisweb.tceq.texas.gov/arcgis/rest/services
8-12-2023 No tiled data
GIS: https://services3.arcgis.com/odYmV2LSdMHrxCiE/ArcGIS/rest/services
Railroad Commission of Texas
Website: https://www.rrc.state.tx.us
GIS: https://gis.rrc.texas.gov/server/rest/services
Table of contents disabled
8-12-2023 No tiled data
Texas Natural Resources Information System
Website: https://tnris.org/
GIS: https://feature.tnris.org/arcgis/rest/services
8-12-2023 No tiled data

## Page 381

Texas General Land Office
Website: https://www.glo.texas.gov/land/land-management/gis/index.html
GIS: _ttps://gis.glo.texas.gov/arcgis/rest/services
dead link 1
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services3.arcgis.com/13DnfApjhE0EY9ik/ArcGIS/rest/services
Community Development & Revitalization Division
Texas Boll Weevil Eradication Foundation
Website: https://www.txbollweevil.org
GIS: https://esri.txbollweevil.org/arcgis/rest/services
8-12-2023 No tiled data
Texas Education Agency
Website: https://tea.texas.gov
Data portal: https://schoolsdata2-tea-texas.opendata.arcgis.com
GIS: https://services2.arcgis.com/5MVN2jsqIrNZD4tP/arcgis/rest/services
Texas Bureau of Economic Geology
Website: https://www.beg.utexas.edu/research/programs/coastal
GIS: https://coastal.beg.utexas.edu/arcgis/rest/services
8-12-2023 No tiled data
Texas Comptroller of Public Accounts
GIS: https://services.arcgis.com/8BKVd7DzccTE7TwW/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/8BKVd7DzccTE7TwW/arcgis/rest/services
Texas Historical Commission
Website: https://thc.texas.gov
GIS: https://mappingtexashistory.thc.texas.gov/arcgis/rest/services
SSL problem
Texas University Lands
Website: https://universitylands.utsystem.edu
GIS: https://services3.arcgis.com/8jYUORGmDUL39WkJ/arcgis/rest/services
Texas various layers
GIS: https://feature.geographic.texas.gov/arcgis/rest/services
GIS: https://gisweb.glo.texas.gov/arcgis/rest/services
Table of contents disabled
GIS: https://services5.arcgis.com/6gTxIFMxZdWxCrVQ/arcgis/rest/services
GIS: https://services7.arcgis.com/2hv9bZMrcgZpr7i9/ArcGIS/rest/services
Texas A and M University - Forest Service
Website: https://tfsweb.tamu.edu
GIS: https://tfsgis02.tfs.tamu.edu/arcgis/rest/services
8-12-2023 No tiled data
GIS: https://services5.arcgis.com/ELI1iJkCzTIagHkp/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/ELI1iJkCzTIagHkp/arcgis/rest/services

## Page 382

Texas Regional
Ark-Tex Council of Governments
Website: https://atcog.org
GIS: https://services3.arcgis.com/lrBbpth805k9reJi/ArcGIS/rest/services
Austin Transit Partnership
Website: https://www.atptx.org
GIS: https://services7.arcgis.com/BnWSLs6TLD51iZWF/ArcGIS/rest/services
Capital Area Council of Governments
Website: https://www.capcog.org
GIS: https://services5.arcgis.com/8DjE4f6iFLArDhsU/ArcGIS/rest/services
CapMetro
Website: https://www.capmetro.org
GIS: https://services6.arcgis.com/RXwE6Rr6OxsElADd/ArcGIS/rest/services
Central Texas Council of Governments
Website: https://ctcog.org
GIS: https://maps.ctcog.org/server/rest/services
8-12-2023 No tiled data
Deep East Texas Council of Governments
Website: https://www.detcog.gov
GIS: https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/services
Greater Harris County 911 Emergency Network
Website: https://911.org
GIS: https://services2.arcgis.com/dhHTVZdGyquZwY8I/ArcGIS/rest/services
Guadalupe-Blanco River Authority
Website: https://www.gbra.org
GIS: https://services7.arcgis.com/Q6vsXnxTnYcWB7qg/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Q6vsXnxTnYcWB7qg/arcgis/rest/services
Houson area - Urban Area Security Initiative (UASI)
Website: https://houstonuasi.com/about/houston-uasi
GIS: https://services7.arcgis.com/0oSa25bMTDqXCJYt/ArcGIS/rest/services
Houston-Galveston Area Council
Website: https://www.h-gac.com/Home
GIS: https://gis.h-gac.com/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/Z6SBWLWGRRejblAA/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Z6SBWLWGRRejblAA/arcgis/rest/services

## Page 383

Lower Colorado River Authority
Website: https://www.lcra.org/about
GIS: They now use Google maps
North Central Texas Council of Governments (NCTCOG):
Website: https://www.nctcog.org
GIS: https://geospatial.nctcog.org/server/rest/services
North Texas Tollway Authority
Website: _ttps://www.ntta.org/Pages/default.aspx
dead link 1
GIS: https://maps.ntta.org/waap1/rest/services
Table of contents disabled
8-12-2023 No tiled data
San Antonio River Authority
Website: https://www.sara-tx.org
GIS: https://gis.sara-tx.org/ags1/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Texoma Council of Governments (TCOG)
Website: https://tcog.com
GIS: https://gis.texoma.cog.tx.us/arcgis/rest/services
GIS: https://services1.arcgis.com/AxQ36D0Busi2R792/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/AxQ36D0Busi2R792/arcgis/rest/services
Tri-County Electric Cooperative
Website: https://tcectexas.com
GIS: https://services.arcgis.com/x4shmVIEqEnhHmQA/arcgis/rest/services
Texas County GIS Servers
Abilene
See City of Abilene.
Angelina
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Angelina_County_GIS_Data/FeatureServer
Go to the top and search for ‘Angelina’
Armstrong
https://gisdata.pandai.com/pamaps02/rest/services/Armstrong
Bailey
https://webmap.trueautomation.com/arcgis/rest/services/BaileyMap
SearchNoLabels/MapServer
Bandera
https://webmap.trueautomation.com/arcgis/rest/services/BanderaM
apSearchNoLabels/MapServer
Bastrop
https://services3.arcgis.com/wdTkTU0MdZbNBEZy/arcgis/rest/ser
vices

## Page 384

Bastrop
https://tiles.arcgis.com/tiles/wdTkTU0MdZbNBEZy/arcgis/rest/ser
vices
Bee
https://gisdata.pandai.com/pamaps02/rest/services/Bee
Not open to public
Bexar
See also City of San Antonio
Bexar
https://maps.bexar.org/arcgis/rest/services
Bexar
https://services1.arcgis.com/8onVmslF2KXErTHT/arcgis/rest/servi
ces
Bexar
https://tiles.arcgis.com/tiles/8onVmslF2KXErTHT/arcgis/rest/servi
ces
Blanco
ArcGIS table of contents not available
Borden
https://gisdata.pandai.com/pamaps02/rest/services/Borden
Brazoria
https://maps.brazoriacountytx.gov/arcgis/rest/services
Brazoria
https://arcgis-web.brazoriacountytx.gov/arcgis/rest/services
Brazoria
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/BrazoriaCADWebService/FeatureServer
Brazos
https://services5.arcgis.com/s91b2wxhO15FkWh5/arcgis/rest/servi
ces
Brewster
https://webmap.trueautomation.com/arcgis/rest/services/Brewster
MapSearchNoLabels/MapServer
Briscoe
https://gisdata.pandai.com/pamaps02/rest/services/Briscoe
Brooks
https://webmap.trueautomation.com/arcgis/rest/services/BrooksMa
pSearchNoLabels/MapServer
Brown
ArcGIS table of contents not available
Burleson
__________ check for new server
Burnet
__________ check for new server
Caldwell
https://services.arcgis.com/HTsVSqwKFyBS7CaT/arcgis/rest/servi
ces
Calhoun
https://webmap.trueautomation.com/arcgis/rest/services/CalhounM
apSearchNoLabels/MapServer
Cameron
GIS is based on open street map

## Page 385

Carson
https://gisdata.pandai.com/pamaps02/rest/services/Carson
Cass
__________ check for new server
Castro
https://gisdata.pandai.com/pamaps02/rest/services/Castro
Chambers
https://gisdata.pandai.com/pamaps02/rest/services/Chambers
Cherokee
__________ check for new server
Childress
https://gisdata.pandai.com/pamaps02/rest/services/Childress
Clay
https://gisdata.pandai.com/pamaps02/rest/services/Clay
Cochran
__________ check for new server
Collin
https://map.collincad.org/Arcgis/rest/services
SSL problem
Collin
https://maps.collincountytx.gov/server/rest/services
Collin
https://services2.arcgis.com/uXyoacYrZTPTKD3R/arcgis/rest/serv
ices      Collin Central Appraisal District
Collingsworth
https://gisdata.pandai.com/pamaps02/rest/services/Collingsworth
Colorado
__________ check for new server
Comal
https://cceo.co.comal.tx.us/arcgissrv/rest/services
Table of contents disabled
Comal
https://webmap.trueautomation.com/arcgis/rest/services/ComalAna
lysis/MapServer
Comal
https://webmap.trueautomation.com/arcgis/rest/services/ComalMa
pFloodTaxingDRGs/MapServer
Comal
https://webmap.trueautomation.com/arcgis/rest/services/ComalMa
pSearchNoLabels/MapServer
Comal
https://services5.arcgis.com/73D3IkNQaVeWK0JB/arcgis/rest/serv
ices
Comanche
https://tiles.arcgis.com/tiles/j94FvPaik4etwHFk/arcgis/rest/services
One or more tile sets are for this county
Cooke
https://gis.texoma.cog.tx.us/arcgis/rest/services
Coryell
__________ check for new server
Cottle
https://gisdata.pandai.com/pamaps02/rest/services/Cottle

## Page 386

Crane
https://gisdata.pandai.com/pamaps02/rest/services/Crane
Crockett
https://gisdata.pandai.com/pamaps02/rest/services/Crockett
Crosby
https://gisdata.pandai.com/pamaps02/rest/services/Crosby
Culberson
https://gisdata.pandai.com/pamaps02/rest/services/Culberson
Cullman
__________ check for new server
Dallam
__________ check for new server
Dallas
https://services3.arcgis.com/zqe2kwz79KUqUvxC/ArcGIS/rest/ser
vices
Dallas
https://tiles.arcgis.com/tiles/zqe2kwz79KUqUvxC/arcgis/rest/servi
ces
Dawson
https://gisdata.pandai.com/pamaps02/rest/services/Dawson
Deaf Smith
__________ check for new server
Delta
See Ark-Tex Council of Governments (above)
Denton
https://gis.dentoncounty.gov/arcgis/rest/services
Table of contents disabled
Denton
https://services.arcgis.com/oTsZYNubyv7xK5yP/arcgis/rest/servic
es
Denton
https://tiles.arcgis.com/tiles/oTsZYNubyv7xK5yP/arcgis/rest/servi
ces
Dewitt
https://gisdata.pandai.com/pamaps02/rest/services/Dewitt
Dickens
https://gisdata.pandai.com/pamaps02/rest/services/Dickens
Dimmit
ArcGIS table of contents not available
Duval
ArcGIS table of contents not available
Eastland
https://gisdata.pandai.com/pamaps02/rest/services/Eastland
Ector
https://services2.arcgis.com/8kTyJ7vw4XFlquQK/ArcGIS/rest/ser
vices
Edwards
__________ check for new server
El Paso
https://gis.epcad.org/arcgis/rest/services

## Page 387

Ellis
https://maps.co.ellis.tx.us/arcgis/rest/services
Erath
__________ check for new server
Falls
https://webmap.trueautomation.com/arcgis/rest/services/FallsMapS
earchNoLabels/MapServer
Fannin
https://gis.texoma.cog.tx.us/arcgis/rest/services
Fayette
__________ check for new server
Fisher
https://gisdata.pandai.com/pamaps02/rest/services/Fisher
Foard
https://gisdata.pandai.com/pamaps02/rest/services/Foard
Fort Bend
https://gisweb.fortbendcountytx.gov/arcgis/rest/services
Fort Bend
https://geocode.arcgis.com/arcgis/rest/services
Table of contents disabled
Fort Bend
https://services.arcgis.com/HfQs2ClqmipKpmFK/arcgis/rest/servic
es
Fort Bend
https://tiles.arcgis.com/tiles/HfQs2ClqmipKpmFK/arcgis/rest/servi
ces
Franklin
https://gisdata.pandai.com/pamaps02/rest/services/Franklin
Freestone
https://gisdata.pandai.com/pamaps02/rest/services/Freestone
Frio
https://gisdata.pandai.com/pamaps02/rest/services/Frio
Gaines
__________ check for new server
Galveston
https://services5.arcgis.com/NAnnb4W7JLztFw9i/arcgis/rest/servi
ces
Galveston
https://tiles.arcgis.com/tiles/NAnnb4W7JLztFw9i/arcgis/rest/servic
es
Gillespie
ArcGIS table of contents not available
Glasscock
https://gisdata.pandai.com/pamaps02/rest/services/Glasscock
Goliad
__________ check for new server
Gonzales
https://gisdata.pandai.com/pamaps02/rest/services/Gonzales
Gray
__________ check for new server

## Page 388

Grayson
https://maps.co.grayson.tx.us/arcgis/rest/services
Gregg
__________ check for new server
Grimes
__________ check for new server
Guadalupe
https://webmap.trueautomation.com/arcgis/rest/services/Guadalupe
Analysis/MapServer
Hale
ArcGIS table of contents not available
Hall
https://gisdata.pandai.com/pamaps02/rest/services/Hall
Hamilton
ArcGIS table of contents not available
Hansford
https://gisdata.pandai.com/pamaps02/rest/services/Hansford
Hardeman
https://gisdata.pandai.com/pamaps02/rest/services/Hardeman

Hardin
ArcGIS table of contents not available
Harris
https://www.gis.hctx.net/arcgis/rest/services
Harris
https://www.gis.hctx.net/arcgishcpid/rest/services
Harris
https://arcweb.hcad.org/server/rest/services
Table of contents disabled
Harris
https://services.arcgis.com/su8ic9KbA7PYVxPS/ArcGIS/rest/servi
ces
Harris
https://tiles.arcgis.com/tiles/su8ic9KbA7PYVxPS/arcgis/rest/servic
es
Harris
https://services2.arcgis.com/nLl0k0Mja5hnSeSl/ArcGIS/rest/servic
es
Harris County flood control district
Harris
https://tiles.arcgis.com/tiles/nLl0k0Mja5hnSeSl/arcgis/rest/services
/Brays_Bayou_Mask/MapServer
Flood control district.
Harris
          https://services6.arcgis.com/2Gyt4iASkG50AI6j/arcgis/rest/services
Emergency Services District 7
Harrison
ArcGIS table of contents not available
Hartley
__________ check for new server
Haskell
https://gisdata.pandai.com/pamaps02/rest/services/Haskell
Hays
https://services5.arcgis.com/bVphnK8rPe5MHUSr/ArcGIS/rest/ser
vices

## Page 389

Hays
https://tiles.arcgis.com/tiles/bVphnK8rPe5MHUSr/arcgis/rest/servi
ces
Hemphill
https://gisdata.pandai.com/pamaps02/rest/services/Hemphill
Henderson
__________ check for new server
Hidalgo
https://services9.arcgis.com/dwMDP55HTfoj4n1c/arcgis/rest/servi
ces
Hill
__________ check for new server
Hockley
https://webmap.trueautomation.com/arcgis/rest/services/HockleyM
apSearchNoLabels/MapServer
Hood
https://services5.arcgis.com/ufxkOGGtW27pGICf/arcgis/rest/servi
ces
Houston
https://gisdata.pandai.com/pamaps02/rest/services/Houston
Houston
https://geogimsms.houstontx.gov/arcgis/rest/services
Houston
https://services.arcgis.com/NummVBqZSIJKUeVR/arcgis/rest/serv
ices
Houston
https://tiles.arcgis.com/tiles/NummVBqZSIJKUeVR/arcgis/rest/ser
vices
Houston
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Houston_County_GIS_Data/FeatureServer
Go to the top and search for ‘Houston’
Houston
https://services7.arcgis.com/YNiGsHEfQPYkIqX5/ArcGIS/rest/ser
vices
Independent school district
Howard
__________ check for new server
Hudspeth
__________ check for new server
Hunt
https://webmap.trueautomation.com/arcgis/rest/services/HuntMapS
earchNoLabels/MapServer
Hunt
           https://services3.arcgis.com/GIIiqmeq0npieHV9/arcgis/rest/services
Hutchinson
https://gisdata.pandai.com/pamaps02/rest/services/Hutchinson
Irion
https://gisdata.pandai.com/pamaps02/rest/services/Irion
Jack
https://gisdata.pandai.com/pamaps02/rest/services/Jack
Jackson
__________ check for new server

## Page 390

Jasper
ArcGIS table of contents not available
Jeff Davis
https://gisdata.pandai.com/pamaps02/rest/services/JeffDavis
Jefferson
https://services.arcgis.com/ZXAF35aJr7XcgDMv/ArcGIS/rest/serv
ices/JCADTXFeatures/FeatureServer
Jefferson
https://tiles.arcgis.com/tiles/ZXAF35aJr7XcgDMv/arcgis/rest/servi
ces
Jim Hogg
https://gisdata.pandai.com/pamaps02/rest/services/JimHogg
Jim Wells
___________ check for new server
Johnson
https://services7.arcgis.com/gVohhGAlfFScDJGs/ArcGIS/rest/serv
ices
Jones
https://gisdata.pandai.com/pamaps02/rest/services/Jones
Karnes
https://gisdata.pandai.com/pamaps02/rest/services/Karnes
Kaufman
__________ check for new server
Kendall
https://services2.arcgis.com/KenzhPpScXZWWBrv/arcgis/rest/ser
vices
Kendall
https://tiles.arcgis.com/tiles/KenzhPpScXZWWBrv/arcgis/rest/serv
ices
Kenedy
__________ check for new server
Kent
https://gisdata.pandai.com/pamaps02/rest/services/Kent
Kerr
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/KerrCADWebService/FeatureServer
Kimble
ArcGIS table of contents not available
King
https://gisdata.pandai.com/pamaps02/rest/services/King
Kinney
https://webmap.trueautomation.com/arcgis/rest/services/KinneyMa
pSearchNoLabels/MapServer
Kleberg
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/KlebergCADWebService/FeatureServer
La Salle
ArcGIS table of contents not available

## Page 391

Lamar
__________ check for new server
Lamb
https://webmap.trueautomation.com/arcgis/rest/services/LambMap
SearchNoLabels/MapServer
Laredo
https://services3.arcgis.com/h9QEFLHkUI1SIRs7/ArcGIS/rest/ser
vices
Lavaca
https://webmap.trueautomation.com/arcgis/rest/services/LavacaMa
pSearchNoLabels/MapServer
Lee
ArcGIS table of contents not available
Leon
https://gisdata.pandai.com/pamaps02/rest/services/Leon
Liberty
__________ check for new server
Limestone
ArcGIS table of contents not available
Live Oak
https://gisdata.pandai.com/pamaps02/rest/services/LiveOak
Llano
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/LlanoCounty911WebService/FeatureServer
Loving
https://gisdata.pandai.com/pamaps02/rest/services/Loving
Lubbock
https://pubgis.ci.lubbock.tx.us/server/rest/services
Lubbock
https://services2.arcgis.com/eYXun6c1pgy8Qpta/ArcGIS/rest/servi
ces
Lubbock
          https://tiles.arcgis.com/tiles/eYXun6c1pgy8Qpta/arcgis/rest/services
Lynn
https://gisdata.pandai.com/pamaps02/rest/services/Lynn
Madison
ArcGIS table of contents not available
Martin
https://gisdata.pandai.com/pamaps02/rest/services/Martin
Matagorda
https://webmap.trueautomation.com/arcgis/rest/services/Matagorda
MapSearchNoLabels/MapServer
Maverick
__________ check for new server
McCulloch
https://gisdata.pandai.com/pamaps02/rest/services/McCulloch
McLennan
https://webmap.trueautomation.com/arcgis/rest/services/Mclennan
MapSearchNoLabels/MapServer

## Page 392

McMullen
ArcGIS table of contents not available
Medina
ArcGIS table of contents not available
Menard
https://gisdata.pandai.com/pamaps02/rest/services/Menard
Mitchell
ArcGIS table of contents not available
Montague
https://gisdata.pandai.com/pamaps02/rest/services/Montague
Montgomery
https://services2.arcgis.com/w2TRse9XgbPXdXc6/ArcGIS/rest/ser
vices
Montgomery
https://services1.arcgis.com/PRoAPGnMSUqvTrzq/ArcGIS/rest/se
rvices
Central Appraisal District
Montgomery
https://tiles.arcgis.com/tiles/PRoAPGnMSUqvTrzq/arcgis/rest/serv
ices
Moore
__________ check for new server
Morris
https://gisdata.pandai.com/pamaps02/rest/services/Morris
Nacogdoches
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Nacogdoches_County_GIS_Data/FeatureServer
Go to the top and search for ‘Nacogdoches’
Navarro
ArcGIS table of contents not available
Newton
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/NewtonCADWebService/FeatureServer
Newton
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Newton_County_GIS_Data/FeatureServer
Go to the top and search for ‘Newton’
Nolan
https://gisdata.pandai.com/pamaps02/rest/services/Nolan
Nueces
ArcGIS table of contents not available
Ochiltree
ArcGIS table of contents not available
Orange
__________ check for new server
Panola
https://gisdata.pandai.com/pamaps02/rest/services/Panola
Pecos
https://gisdata.pandai.com/pamaps02/rest/services/Pecos

## Page 393

Polk
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/PolkCADWebService/FeatureServer
Polk
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Polk_County_GIS_Data/FeatureServer
Go to the top and search for ‘Polk’
Potter
__________ check for new server
Presidio
ArcGIS table of contents not available
Rains
https://tiles.arcgis.com/tiles/j94FvPaik4etwHFk/arcgis/rest/services

One or more tile sets are for this county
Randall
See Potter county
Reagan
https://gisdata.pandai.com/pamaps02/rest/services/Reagan
Real
ArcGIS table of contents not available
Reeves
__________ check for new server
Refugio
https://gisdata.pandai.com/pamaps02/rest/services/Refugio
Roberts
__________ check for new server
Robertson
__________ check for new server
Rockwall
They have a GIS but not ArcGIS
Rusk
https://gisdata.pandai.com/pamaps02/rest/services/Rusk
Sabin
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Sabine_County_GIS_Data/FeatureServer
Go to the top and search for ‘Sabin’
San Augustine
https://gisdata.pandai.com/pamaps02/rest/services/SanAugustine
San Augustine
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/San_Augustine__County_GIS_Data/FeatureServer
Go to the top and search for ‘San Augustine’
San Jacinto
https://webmap.trueautomation.com/arcgis/rest/services/SanJacinto
MapSearchNoLabels/MapServer
San Jacinto
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/San_Jacinto_County_GIS_Data/FeatureServer
Go to the top and search for ‘San Jacinto’

## Page 394

San Patricio
_____________
San Saba
https://gisdata.pandai.com/pamaps02/rest/services/SanSaba
Schleicher
ArcGIS table of contents not available
Scurry
ArcGIS table of contents not available
Shelby
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Shelby_County_GIS_Data/FeatureServer
Go to the top and search for ‘Shelby’
Sherman
https://gisdata.pandai.com/pamaps02/rest/services/Sherman
Smith
https://www.smithcountymapsite.org/publicgis/rest/services
Table of contents disabled
Starr
https://webmap.trueautomation.com/arcgis/rest/services/StarrMapS
earchNoLabels/MapServer
Starr
ArcGIS table of contents not available
Stephens
ArcGIS table of contents not available
Sterling
https://gisdata.pandai.com/pamaps02/rest/services/Sterling
Stonewall
https://gisdata.pandai.com/pamaps02/rest/services/Stonewall
Sugar Land
https://interactivemaps.sugarlandtx.gov/512/rest/services
Sugar Land
          https://services1.arcgis.com/SVtsrBXEiBhI5L5n/arcgis/rest/services
Sugar Land
           https://tiles.arcgis.com/tiles/SVtsrBXEiBhI5L5n/arcgis/rest/services
Sutton
ArcGIS table of contents not available
Swisher
ArcGIS table of contents not available
Tarrant
https://mapit.tarrantcounty.com/arcgis/rest/services
Tarrant
https://services1.arcgis.com/KgTkwJ7lfG2eHF3z/arcgis/rest/servic
es
Tarrant
https://tiles.arcgis.com/tiles/KgTkwJ7lfG2eHF3z/arcgis/rest/servic
es
Tarrant
https://services2.arcgis.com/5S5T6XdxjqI5BK2Y/arcgis/rest/servic
es
Appraisal District     Table of contents hidden by javascript
Taylor
See City of Abilene.

## Page 395

Terrell
https://webmap.trueautomation.com/arcgis/rest/services/TerrellMa
pSearchNoLabels/MapServer
Terry
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/TerryTXFeatures/FeatureServer
Go to the top and search for ‘TerryTX’
Terry
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/TerryTXCadastral/MapServer
Go to the top and search for ‘TerryTX’
Throckmorton
https://gisdata.pandai.com/pamaps02/rest/services/Throckmorton
Titus
ArcGIS table of contents not available
Travis
https://gis.traviscountytx.gov/server1/rest/services
Travis
https://taxmaps.traviscountytx.gov/arcgis/rest/services
Travis
https://services1.arcgis.com/HGcSYZ5bvjRswoCb/ArcGIS/rest/ser
vices
Travis
https://tiles.arcgis.com/tiles/HGcSYZ5bvjRswoCb/arcgis/rest/servi
ces
Trinity
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Trinity_County_GIS_Data/FeatureServer
Go to the top and search for ‘Trinity’
Tyler
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/TylerCADWebService/FeatureServer
Tyler
https://services1.arcgis.com/z3DZ2dwxv2tyH8pc/ArcGIS/rest/serv
ices/Tyler_County_GIS_Data/FeatureServer
Go to the top and search for ‘Tyler’
Upshur
ArcGIS table of contents not available
Upton
https://gisdata.pandai.com/pamaps02/rest/services/Upton
Uvalde
ArcGIS table of contents not available
Val Verde
GIS is not ArcGIS
Van Zandt
ArcGIS table of contents not available
Victoria
ArcGIS table of contents not available
Walker
ArcGIS table of contents not available
Walker
https://tiles.arcgis.com/tiles/j94FvPaik4etwHFk/arcgis/rest/services
One or more tile sets are for this county

## Page 396

Waller
ArcGIS table of contents not available
Ward
https://gisdata.pandai.com/pamaps02/rest/services/Ward
Washington
ArcGIS table of contents not available
Webb
_ttps://webmap.trueautomation.com/arcgis/rest/services/WebbMap
Search/MapServer
dead link 3
Wharton
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/WhartonCADWebService/FeatureServer
Wheeler
https://gisdata.pandai.com/pamaps02/rest/services/Wheeler
Willacy
https://webmap.trueautomation.com/arcgis/rest/services/WillacyM
apSearchNoLabels/MapServer
Williamson
https://gis.wilco.org/arcgis/rest/services
Wilson
___________________
Winkler
ArcGIS table of contents not available
Wise
ArcGIS table of contents not available
Wood
__________ check for new server
Yoakum
ArcGIS table of contents not available
Young
ArcGIS table of contents not available
Zapata
__________ check for new server
Zavala
ArcGIS table of contents not available
Texas City, Town, Village, etc GIS Servers
Abilene
https://services6.arcgis.com/iBFmWI3dYPQqS1KF/ArcGIS/rest/se
rvices
Abilene
https://tiles.arcgis.com/tiles/iBFmWI3dYPQqS1KF/arcgis/rest/serv
ices
Addison
https://gis.addisontx.gov/arcgis/rest/services
Addison
https://services2.arcgis.com/M5mzKG9YWYJySP6Q/ArcGIS/rest/
services
Allen
https://gismaps.cityofallen.org/arcgis/rest/services

## Page 397

Allen
https://services2.arcgis.com/EzT1Zn8fMm7PXUEL/ArcGIS/rest/s
ervices
Allen
https://tiles.arcgis.com/tiles/EzT1Zn8fMm7PXUEL/arcgis/rest/ser
vices
Amarillo
https://gisdata.pandai.com/pamaps01/rest/services/PAAmarillo
Not open to public
Amarillo
https://services6.arcgis.com/Vdk8uHgdgYx8ZqS6/ArcGIS/rest/ser
vices
Amarillo
https://tiles.arcgis.com/tiles/Vdk8uHgdgYx8ZqS6/arcgis/rest/servi
ces
Anderson
__________ check for new server
Andrews
https://webmap.trueautomation.com/arcgis/rest/services/Andrews
MapSearchQA/MapServer
Arlington
https://gis2.arlingtontx.gov/agsext2/rest/services
Arlington
https://services.arcgis.com/jXi5GuMZwfCYtZP9/arcgis/rest/servic
es
Arlington
https://tiles.arcgis.com/tiles/jXi5GuMZwfCYtZP9/arcgis/rest/servi
ces
Austin
https://coagiswebadaptor.austintexas.gov/awgisago/rest/services
Austin
https://maps.austintexas.gov/image/rest/services
Austin
https://awgisadaptor.austintexas.gov/awgisago/rest/services
Austin
https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/servic
es
Austin
https://tiles.arcgis.com/tiles/0L95CJ0VTaxqcmED/arcgis/rest/servi
ces
Austin
https://services6.arcgis.com/76EQ66Fn3C7tjkFD/ArcGIS/rest/serv
ices
Austin
https://tiles.arcgis.com/tiles/76EQ66Fn3C7tjkFD/arcgis/rest/servic
es
Bastrop
https://services7.arcgis.com/qOeXJdBtGknaCJC4/ArcGIS/rest/ser
vices
Bastrop
https://tiles.arcgis.com/tiles/qOeXJdBtGknaCJC4/arcgis/rest/servic
es
Baytown
https://mapdata.baytown.org/arcgis/rest/services
Baytown
https://services8.arcgis.com/2iaYWEMdQLPv0ZUw/ArcGIS/rest/s
ervices
Baytown
https://tiles.arcgis.com/tiles/2iaYWEMdQLPv0ZUw/arcgis/rest/ser
vices

## Page 398

Beaumont
https://gis.beaumonttexas.gov/arcgis/rest/services
Beaumont
          https://services.arcgis.com/wyDgaTdYqIafVmj4/arcgis/rest/services
Beaumont
https://tiles.arcgis.com/tiles/wyDgaTdYqIafVmj4/arcgis/rest/servic
es
Beaumont
https://services3.arcgis.com/rUwYlNumaV2hTY7c/arcgis/rest/serv
ices
Beaumont
https://tiles.arcgis.com/tiles/rUwYlNumaV2hTY7c/arcgis/rest/serv
ices
Beeville
Integritygis - ArcGIS server address is not public
Belton
https://services5.arcgis.com/FkDUU6xkZJTbBa9X/ArcGIS/rest/se
rvices
Brenham
https://map.cityofbrenham.org/server/rest/services
Bryan
https://maps.bryantx.gov/server/rest/services
Table of contents disabled
Bryan
https://maps.bryantx.gov/image/rest/services
Bryan
https://services6.arcgis.com/skDYeFloTW88hhip/ArcGIS/rest/serv
ices
Bryan
https://tiles.arcgis.com/tiles/skDYeFloTW88hhip/arcgis/rest/servic
es
Buda
https://services6.arcgis.com/vXZW4vAaPRr14z2s/arcgis/rest/servi
ces
Burleson
https://gis.burlesontx.com/server/rest/services
Carrollton
https://services7.arcgis.com/o731hPfw3YndegMz/ArcGIS/rest/serv
ices
Carrollton
https://tiles.arcgis.com/tiles/o731hPfw3YndegMz/arcgis/rest/servic
es
Cedar Park
https://gisrest.cedarparktexas.gov/cpgis/rest/services
Cedar Park
https://services3.arcgis.com/38ymeJ0buVXLAhvG/ArcGIS/rest/ser
vices
Celina
https://services1.arcgis.com/x4nhme9V33KOzAfr/arcgis/rest/servi
ces
Cibolo
https://services3.arcgis.com/D32JCd9p0r1BYMwd/ArcGIS/rest/ser
vices
Cibolo
https://tiles.arcgis.com/tiles/D32JCd9p0r1BYMwd/arcgis/rest/servi
ces

## Page 399

Clarksville
See Ark-Tex Council of Governments (above)
Coleman
__________ check for new server
College Station
https://gis.cstx.gov/csgis/rest/services
College Station
https://services1.arcgis.com/nbjPLEfhkN30ptDp/ArcGIS/rest/servi
ces
College Station          https://tiles.arcgis.com/tiles/nbjPLEfhkN30ptDp/arcgis/rest/services
Coppell
https://map.coppelltx.gov/gis/rest/services
Corpus Christi           https://services.arcgis.com/0J4ZNc4NaTguvRy0/arcgis/rest/services
Corpus Christi
https://tiles.arcgis.com/tiles/0J4ZNc4NaTguvRy0/arcgis/rest/servic
es
Corsicana
https://services8.arcgis.com/V3MtivrTOPqThQ57/ArcGIS/rest/ser
vices
Corinth
https://services1.arcgis.com/gOHOrKRKo1Ymuaat/ArcGIS/rest/se
rvices
Crandall
https://services6.arcgis.com/j94FvPaik4etwHFk/ArcGIS/rest/servic
es/City_Of_Crandall_Zoning/FeatureServer
Crockett
https://gisdata.pandai.com/pamaps02/rest/services/Crockett
Dalhart
____________
Dallas
https://egis.dallascityhall.com/arcgis/rest/services
Dallas
https://gis.dallascityhall.com/arcgis/rest/services
Dallas
https://services2.arcgis.com/rwnOSbfKSwyTBcwN/arcgis/rest/serv
ices
Dallas - Forth Worth _ttps://gis.dfwmaps.com/arcgis/rest/services
dead link 1
Dawson
https://gisdata.pandai.com/pamaps02/rest/services/Dawson
Dayton
https://services6.arcgis.com/1zuvRnm7tm3WFwVI/ArcGIS/rest/se
rvices
Decatur
https://services1.arcgis.com/PLOR6Lqgjdua9pO5/ArcGIS/rest/serv
ices/DECATURTX_V_GISDATA_VIEWONLY/FeatureServer
Decatur
https://tiles.arcgis.com/tiles/PLOR6Lqgjdua9pO5/arcgis/rest/servic
es
Deer Park
https://gis.deerparktx.gov/arcgis/rest/services

## Page 400

Denison
https://gis.newedgeservices.com/arcgis/rest/services/Denison
Denton
https://gis.cityofdenton.com:9002/arcgis/rest/services
DeSoto
https://services8.arcgis.com/QHqdbIhWBJLlMbGN/ArcGIS/rest/s
ervices
Dimmit
__________ check for new server
Eastland
https://gisdata.pandai.com/pamaps02/rest/services/Eastland
El Campo
https://services2.arcgis.com/HNMIfnmUIg26wHJa/arcgis/rest/serv
ices
El Paso
https://gis.elpasotexas.gov/arcgis/rest/services
El Paso
https://gis.elpasotexas.gov/dev/rest/services
El Paso
https://gis.elpasotexas.gov/arcgis/rest/services
El Paso
https://gis.elpasotexas.gov/imagery/rest/services
Elsa
https://services5.arcgis.com/T6e33bEB8VeNmfaY/ArcGIS/rest/ser
vices
Euless
https://maps3.eulesstx.gov/arcgis/rest/services
Fair Oaks Ranch
https://services6.arcgis.com/Cnwpb7mZuifVHE6A/arcgis/rest/serv
ices
Fair Oaks Ranch
https://tiles.arcgis.com/tiles/Cnwpb7mZuifVHE6A/arcgis/rest/serv
ices
Flower Mound
https://gismaps.flower-mound.com/wafmp/rest/services
Flower Mound
https://services7.arcgis.com/6qFRqt366CpC8ZLF/ArcGIS/rest/serv
ices
Flower Mound
https://tiles.arcgis.com/tiles/6qFRqt366CpC8ZLF/arcgis/rest/servic
es
Fort Worth
https://mapit.fortworthtexas.gov/ags/rest/services
Fort Worth
https://mapitwest.fortworthtexas.gov/ags/rest/services
Fort Worth
https://services5.arcgis.com/3ddLCBXe1bRt7mzj/ArcGIS/rest/serv
ices
Fort Worth
https://tiles.arcgis.com/tiles/3ddLCBXe1bRt7mzj/arcgis/rest/servic
es
Friendswood
https://services6.arcgis.com/ghs8JYGzwZM6Zl6x/ArcGIS/rest/ser
vices
Friendswood
https://tiles.arcgis.com/tiles/ghs8JYGzwZM6Zl6x/arcgis/rest/servi
ces

## Page 401

Frisco
https://services6.arcgis.com/OGXLcOSnuy0GwFwi/ArcGIS/rest/se
rvices
Frisco
https://tiles.arcgis.com/tiles/OGXLcOSnuy0GwFwi/arcgis/rest/ser
vices
Garland
https://maps.garlandtx.gov/arcgis/rest/services
Garland
https://services2.arcgis.com/g3rbttPStUJTjAz2/ArcGIS/rest/servic
es
Garland
https://tiles.arcgis.com/tiles/g3rbttPStUJTjAz2/arcgis/rest/services
Georgetown
https://gis.georgetown.org/arcgis/rest/services
Georgetown
https://services.arcgis.com/5ZjkDcAQQjFnTEkh/arcgis/rest/servic
es
Georgetown
https://tiles.arcgis.com/tiles/5ZjkDcAQQjFnTEkh/arcgis/rest/servi
ces
Graham
          https://services6.arcgis.com/2rhXUtiJJoWJ7Pn4/arcgis/rest/services
Granbury
https://gis.newedgeservices.com/arcgis/rest/services/Granbury
Grand Prairie
https://gis.gptx.org/srv105/rest/services
Grand Prairie
https://services2.arcgis.com/CqeHAxo0ujDIfHnl/ArcGIS/rest/servi
ces
Grand Prairie           https://tiles.arcgis.com/tiles/CqeHAxo0ujDIfHnl/arcgis/rest/services
Grapevine
https://services.arcgis.com/xSPs49inzz3yMpnd/arcgis/rest/services
Grapevine
           https://tiles.arcgis.com/tiles/xSPs49inzz3yMpnd/arcgis/rest/services
Henderson
https://gisdata.pandai.com/pamaps01/rest/services/PAHenderson
Not open to public
Highland
https://maps.highlandvillage.org/arcgis/rest/services

Horseshoe Bay
https://services2.arcgis.com/PGv0SS9sE3M9RybT/arcgis/rest/servi
ces

Horseshoe Bay
https://tiles.arcgis.com/tiles/PGv0SS9sE3M9RybT/arcgis/rest/servi
ces
Houston
https://mycity2.houstontx.gov/pubgis01/rest/services

Houston
https://mycity2.houstontx.gov/pubgis02/rest/services

Houston
https://hpwgeo-ms.houstontx.gov/arcgis/rest/services
Houston
https://services1.arcgis.com/XpTq0H1nJ5DHgofs/ArcGIS/rest/serv
ices

Houston
https://tiles.arcgis.com/tiles/XpTq0H1nJ5DHgofs/arcgis/rest/servic
es

## Page 402

Hutto
https://services.arcgis.com/YZhxlqU7ABWQBGTG/arcgis/rest/ser
vices
Hutto
https://tiles.arcgis.com/tiles/YZhxlqU7ABWQBGTG/arcgis/rest/se
rvices
Irving

https://services2.arcgis.com/3mkVbLdbLBFHrfbK/ArcGIS/rest/ser
vices
Irving

https://tiles.arcgis.com/tiles/3mkVbLdbLBFHrfbK/arcgis/rest/servi
ces
Irving
          https://services3.arcgis.com/OfsJXUlu8pSkbl7B/arcgis/rest/services
Irving
           https://tiles.arcgis.com/tiles/OfsJXUlu8pSkbl7B/arcgis/rest/services
Jersey Village
https://services8.arcgis.com/GvsnkS48XQZ4HAFX/arcgis/rest/ser
vices
Keller
https://gis.cityofkeller.com/arcgis/rest/services
Keller
https://services2.arcgis.com/7YcJOHUBjYCdeo36/ArcGIS/rest/ser
vices
Keller
https://tiles.arcgis.com/tiles/7YcJOHUBjYCdeo36/arcgis/rest/servi
ces
Kerrville
https://services1.arcgis.com/Ijqs2ihddUy84otW/ArcGIS/rest/servic
es
Kerrville
https://tiles.arcgis.com/tiles/Ijqs2ihddUy84otW/arcgis/rest/services
Kilgore
https://services3.arcgis.com/0koxpwY2esNkg9Bz/ArcGIS/rest/serv
ices
Kyle
https://gis.cityofkyle.com/server/rest/services
Kyle
https://services5.arcgis.com/Zhdeglqfvv6JnrnU/ArcGIS/rest/servic
es
Kyle
https://services7.arcgis.com/4gR5hLdTpqRLVwao/arcgis/rest/servi
ces
La Porte
https://services3.arcgis.com/K8W2oZWmBOVHwjhP/arcgis/rest/s
ervices
La Porte
https://tiles.arcgis.com/tiles/K8W2oZWmBOVHwjhP/arcgis/rest/s
ervices
Lago Vista
          https://services3.arcgis.com/kV3JsjhhKc5dLEbb/arcgis/rest/services
Lampasas
ArcGIS table of contents not available
Leander
https://services1.arcgis.com/L0MLvN0Ay0iEjnCT/ArcGIS/rest/ser
vices

## Page 403

Lewisville
https://services2.arcgis.com/kXGqZY4GIOcEYxoF/ArcGIS/rest/se
rvices
Lewisville
https://tiles.arcgis.com/tiles/kXGqZY4GIOcEYxoF/arcgis/rest/serv
ices
Liberty
__________ check for new server
Little Elm
https://gis.littleelm.org/arcgis/rest/services
Longview
https://cloud.longviewtexas.gov/arcgis/rest/services
Longview
https://services2.arcgis.com/L4ywDaHbEfVZyfpl/ArcGIS/rest/serv
ices
Longview
https://tiles.arcgis.com/tiles/L4ywDaHbEfVZyfpl/arcgis/rest/servic
es
Lubbock
https://pubgis.ci.lubbock.tx.us/server/rest/services
Lubbock
http://216.167.160.20/arcgis107/rest/services
not https
Mason
__________ check for new server
McAllen
https://gismap.mcallen.net/publication/rest/services
McKinney
https://maps.mckinneytexas.org/mckinney/rest/services
Mesquite
https://gisservice.cityofmesquite.com/arcgis/rest/services
Midland
https://maps.midlandtexas.gov/img/rest/services
Midland
_ttps://midland.newedgeservices.com/arcgis/rest/services
dead link 1
Midlothian
https://services9.arcgis.com/N8inFJC6S2HoD3HQ/ArcGIS/rest/ser
vices
Midlothian
https://tiles.arcgis.com/tiles/N8inFJC6S2HoD3HQ/arcgis/rest/servi
ces
Milam
ArcGIS table of contents not available
Mission
https://services9.arcgis.com/TFNWZRl8YdOiBZo4/ArcGIS/rest/se
rvices
Missouri City
https://gis.missouricitytx.gov/arcgis/rest/services
Missouri City
https://services2.arcgis.com/6vRbgYSxztFGZwla/ArcGIS/rest/serv
ices
Missouri City
https://tiles.arcgis.com/tiles/6vRbgYSxztFGZwla/arcgis/rest/servic
es

## Page 404

Montague
https://gisdata.pandai.com/pamaps02/rest/services/Montague
Mount Pleasant
See Ark-Tex Council of Governments (above)
Mount Vernon
See Ark-Tex Council of Governments (above)
Murphy
https://services5.arcgis.com/lt8CbgYaNuFrQ7kB/ArcGIS/rest/serv
ices
Murphy
https://tiles.arcgis.com/tiles/lt8CbgYaNuFrQ7kB/arcgis/rest/servic
es
Nacogdoches
https://maps.ci.nacogdoches.tx.us/arcgis_server/rest/services
New Braunfels
https://maps.nbutexas.com/arcgis/rest/services
New Braunfels
https://gismaps.newbraunfels.gov/arcserverwa22/rest/services
New Braunfels
https://services1.arcgis.com/UrQTvZli004mL2h3/arcgis/rest/servic
es
New Braunfels           https://services.arcgis.com/yHSU3Q4NlapEfzn5/arcgis/rest/services
New Braunfels Utilities
Nolan
https://gisdata.pandai.com/pamaps02/rest/services/Nolan
Odessa
https://services6.arcgis.com/96XBo0KviQ3nV6zg/ArcGIS/rest/ser
vices
Odessa
https://tiles.arcgis.com/tiles/96XBo0KviQ3nV6zg/arcgis/rest/servi
ces
Paris
See Ark-Tex Council of Governments (above)
Parker
https://arcgis4.roktech.net/arcgis/rest/services/ParkerTX
Parker
https://arcgis5.roktech.net/arcgis/rest/services/ParkerTX
Pearland
https://gis.pearlandtx.gov/hosting/rest/services
Pearland
https://services5.arcgis.com/iJ6DPCVBtManqbJU/ArcGIS/rest/ser
vices
Pearland
https://tiles.arcgis.com/tiles/iJ6DPCVBtManqbJU/arcgis/rest/servi
ces
Pfluger Village
https://maps.pflugervilletx.gov/arcgis/rest/services
Pflugerville
https://services.arcgis.com/qDOnMQ2aoGtLgVxL/arcgis/rest/servi
ces
Pflugerville
https://tiles.arcgis.com/tiles/qDOnMQ2aoGtLgVxL/arcgis/rest/serv
ices

## Page 405

Pharr
https://services.arcgis.com/Uj8MycSVzMEzm7ey/arcgis/rest/servi
ces
Pharr
https://tiles.arcgis.com/tiles/Uj8MycSVzMEzm7ey/arcgis/rest/serv
ices
Plano
https://maps.planogis.org/arcgiswad/rest/services
Plano
https://services2.arcgis.com/1DyhsVa6rviDKn5t/ArcGIS/rest/servi
ces
Plano
           https://tiles.arcgis.com/tiles/1DyhsVa6rviDKn5t/arcgis/rest/services
Prosper
https://gis.newedgeservices.com/arcgis/rest/services/Prosper
Prosper
https://services8.arcgis.com/8ofMLzOrtxGP9wVQ/ArcGIS/rest/ser
vices
Richardson
https://maps.cor.gov/arcgis/rest/services
Richardson
https://services2.arcgis.com/5aVZxf6eblRfH5Yb/ArcGIS/rest/servi
ces
Richardson
https://tiles.arcgis.com/tiles/5aVZxf6eblRfH5Yb/arcgis/rest/servic
es
Rockwall
https://gis.rockwall.com/arcgis/rest/services
Rockwall
https://services.arcgis.com/OWPOmsDuApLR0ZGD/arcgis/rest/se
rvices
Rockwall
https://tiles.arcgis.com/tiles/OWPOmsDuApLR0ZGD/arcgis/rest/s
ervices
Rosenberg
https://maps.rosenbergtx.gov/server/rest/services
Rosenberg
https://services6.arcgis.com/4OYLeEKEHNjV6qag/arcgis/rest/serv
ices
Round Rock
https://maps.roundrocktexas.gov/arcgis/rest/services
Round Rock
https://services.arcgis.com/KaARkuoKF9vrGr3P/arcgis/rest/servic
es
Round Rock
https://tiles.arcgis.com/tiles/KaARkuoKF9vrGr3P/arcgis/rest/servi
ces
San Angelo
https://gisdata.pandai.com/pamaps01/rest/services/PASanAngelo
Not open to public
San Antonio
https://qagis.sanantonio.gov/arcgis/rest/services
San Antonio
https://qagis1.sanantonio.gov/arcgis/rest/services
San Antonio
           https://services.arcgis.com/g7IVOf0Gf9OkqkzV/arcgis/rest/services
San Antonio
https://services.arcgis.com/g1fRTDLeMgspWrYp/ArcGIS/rest/ser
vices
San Antonio
https://tiles.arcgis.com/tiles/g1fRTDLeMgspWrYp/arcgis/rest/servi
ces

## Page 406

San Marcos
https://smgis.sanmarcostx.gov/arcgis/rest/services
San Marcos
https://services1.arcgis.com/Hug9pbs2TYetbCha/ArcGIS/rest/servi
ces
San Marcos
https://tiles.arcgis.com/tiles/Hug9pbs2TYetbCha/arcgis/rest/servic
es
Sherman
https://maps.cityofsherman.com/arcgis/rest/services
Sherman
https://services7.arcgis.com/iMHDvyzuG2Q2tuit/ArcGIS/rest/servi
ces
Socorro
https://services7.arcgis.com/qFZTU3XIcy565xhg/arcgis/rest/servic
es
Sulphur Springs
See Ark-Tex Council of Governments (above)
Sunset Valley
https://services8.arcgis.com/OgRe4OZB9AeIkKmc/arcgis/rest/serv
ices
Taylor
https://services7.arcgis.com/SQVxkeGOcRYhZqOD/ArcGIS/rest/s
ervices
Taylor
https://tiles.arcgis.com/tiles/SQVxkeGOcRYhZqOD/arcgis/rest/ser
vices
Temple
https://services5.arcgis.com/OXFB1ND8m9x0pu0w/ArcGIS/rest/s
ervices
Temple
https://tiles.arcgis.com/tiles/OXFB1ND8m9x0pu0w/arcgis/rest/ser
vices
Texarkana
See Ark-Tex Council of Governments (above)
Texarkana
https://services1.arcgis.com/1qdvoNGNoopZM1s5/ArcGIS/rest/ser
vices
Texarkana
https://tiles.arcgis.com/tiles/1qdvoNGNoopZM1s5/arcgis/rest/servi
ces
The colony
https://gis.thecolonytx.gov/arcgis/rest/services
Throckmorton
ArcGIS table of contents not available
Vernon
ArcGIS table of contents not available
Waxahachie
https://arcgis.waxahachie.com/arcgis/rest/services
Waxahachie
https://services5.arcgis.com/akgXEW2N2FkwmHEV/ArcGIS/rest/
services
Waxahachie
https://tiles.arcgis.com/tiles/akgXEW2N2FkwmHEV/arcgis/rest/se
rvices

## Page 407

Weatherford
https://gis.weatherfordtx.gov/arcgis/rest/services
Webster
https://www1.cityofwebster.com/arcgis/rest/services
West University Place
https://services2.arcgis.com/i0yOnTx5hca0RSx2/arcgis/rest
/services
West University Place
https://tiles.arcgis.com/tiles/i0yOnTx5hca0RSx2/arcgis/rest
/services
Wichita Falls
https://propaccess.wadtx.com/arcgis/rest/services
Wolfforth
__________
Wylie
https://gisapp.wylietexas.gov/portalserver/rest/services
Utah State GIS Servers
GIS general info
Website: https://gis.utah.gov
Search for data:
Website: https://gis.utah.gov/products/sgid/sgid-index
Website: https://opendata.utah.gov
Website: https://opendata.gis.utah.gov
Utah Division of Emergency Management
Website: https://dem.utah.gov
GIS: https://services6.arcgis.com/KaHXE9OkiB9e63uE/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/KaHXE9OkiB9e63uE/arcgis/rest/services
Utah Department of Public Safety
Website: https://dps.utah.gov
GIS: https://services6.arcgis.com/LdaErpBRbZIJOzrU/arcgis/rest/services
Utah Department of Natural Resources
Website: https://naturalresources.utah.gov
GIS: https://dwrmapserv.utah.gov/dwrarcgis/rest/services
GIS: https://dwrmapserv.utah.gov/arcgis/rest/services
GIS: https://services.arcgis.com/ZzrwjTRez6FJiOq4/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/ZzrwjTRez6FJiOq4/arcgis/rest/services
GIS: https://services6.arcgis.com/rurJpXWFWyhUqIYR/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/rurJpXWFWyhUqIYR/arcgis/rest/services
Utah Department of Transportation
Website: https://www.udot.utah.gov/connect
GIS: https://maps.udot.utah.gov/central/rest/services
GIS: https://maps.udot.utah.gov/arcgis01/rest/services

## Page 408

GIS: https://maps.udot.utah.gov/image/rest/services
GIS: https://maps.udot.utah.gov/maint/rest/services
GIS: https://central.udot.utah.gov/server/rest/services
GIS: https://roads.udot.utah.gov/server/rest/services
GIS: https://services.arcgis.com/pA2nEVnB6tquxgOW/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/pA2nEVnB6tquxgOW/arcgis/rest/services
Utah public lands
Website: https://plpco-data-resources-hub-plpco.hub.arcgis.com
GIS: https://services5.arcgis.com/XRVBrOxuw8qsD3J3/ArcGIS/rest/services
Utah Inland Port Authority
Website: https://inlandportauthority.utah.gov
GIS: https://services6.arcgis.com/1wGe9OtOPvKepFKv/ArcGIS/rest/services
Trust Lands Administration
Website: https://trustlands.utah.gov
GIS: https://gis.trustlands.utah.gov/mapping/rest/services
GIS: https://services1.arcgis.com/gZywvNC8jZaPf8UX/arcgis/rest/services
Utah Geological Survey
Website: https://geology.utah.gov
GIS: https://webmaps.geology.utah.gov/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Basin Recreation
Website: https://basinrecreationutah.gov
GIS: https://services5.arcgis.com/aqkQEfCsz2vNDB73/ArcGIS/rest/services
Utah various layers
GIS: https://fmags.fm.utah.edu/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/99lidPhWCzftIe9K/ArcGIS/rest/services
Includes parcel layers by county
Statewide parcel layer  UtahStatewideParcels/FeatureServer
GIS: https://tiles.arcgis.com/tiles/99lidPhWCzftIe9K/arcgis/rest/services
Utah Regional
Ashley Valley Water & Sewer Improvement District
Website: https://www.ashleywatersewerut.gov
GIS: https://services3.arcgis.com/VhQvFoV6DSgjT2gN/arcgis/rest/services
Greater Salt Lake Municipal Services District
Website: https://msd.utah.gov
GIS: https://gis.msd.utah.gov/server/rest/services
GIS: https://services5.arcgis.com/vAN1UOB7DAkfLV82/ArcGIS/rest/services

## Page 409

GIS: https://tiles.arcgis.com/tiles/vAN1UOB7DAkfLV82/arcgis/rest/services
Mountainland Association of Governments
Website: https://magutah.gov
GIS: https://services2.arcgis.com/EiGeaCDLpVDPqdJ5/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/EiGeaCDLpVDPqdJ5/arcgis/rest/services
Utah Transit Authority
Website: https://www.rideuta.com
GIS: https://services.arcgis.com/5QAphMT1g51Tw2X4/arcgis/rest/services
Wasatch Front Regional Council
Website: https://wfrc.utah.gov
GIS: https://services1.arcgis.com/taguadKoI1XFwivx/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/taguadKoI1XFwivx/arcgis/rest/services
Utah County GIS Servers
Cache
https://gis.cachecounty.gov/arcgis/rest/services
Cache
https://services2.arcgis.com/BGUZsqWI221fvl15/ArcGIS/rest/serv
ices
Grand
_ttps://gis.grandcountyutah.net:6443/arcgis/rest/services
dead link 1
Salt Lake
https://slco.org/slcogis/rest/services Table of contents disabled
Salt Lake
https://slco.org/arcgis/rest/services
Table of contents disabled
Salt Lake
https://slco.org/slcogcs/rest/services
Salt Lake
https://apps.saltlakecounty.gov/arcgis/rest/services
Table of contents disabled
Salt Lake
https://services1.arcgis.com/DJP723NX3ukQ2LtF/arcgis/rest/servi
ces
Salt Lake
https://tiles.arcgis.com/tiles/DJP723NX3ukQ2LtF/arcgis/rest/servi
ces
Salt Lake
https://services2.arcgis.com/EaEIzTgSTIYutToR/ArcGIS/rest/servi
ces       SLCo Emergency Management and Unified Fire Authority
Salt Lake
https://tiles.arcgis.com/tiles/EaEIzTgSTIYutToR/arcgis/rest/servic
es
Summit
https://maps.summitcounty.org/arcgis/rest/services
Tooele
https://tcgisws.tooeleco.org/server/rest/services       SSL problem
Uintah
https://apps.uintah.utah.gov/arcgis/rest/services
Utah
https://maps.utahcounty.gov/arcgis/rest/services
Utah
https://gisaerials.utahcounty.gov/arcgis/rest/services

## Page 410

Utah
https://maps200.utahcounty.gov/arcgis/rest/services
Washington
https://agisprodvm.washco.utah.gov/arcgis/rest/services
Weber
https://maps.webercountyutah.gov/arcgis/rest/services
Utah City, Town, Village, etc GIS Servers
Draper
https://gisdata.draper.ut.us/drapergis/rest/services
Hurricane
https://services3.arcgis.com/YkC4Iaje1llJo8SI/arcgis/rest/services
Hurricane
https://tiles.arcgis.com/tiles/YkC4Iaje1llJo8SI/arcgis/rest/services
Layton
https://www.laytoncity.org/arcgisportal109/rest/services
Layton
https://services1.arcgis.com/XDo7qgWGk2R5khJB/ArcGIS/rest/se
rvices
Layton
https://tiles.arcgis.com/tiles/XDo7qgWGk2R5khJB/arcgis/rest/serv
ices
Midvale
https://services6.arcgis.com/8xmMYBLanDLIUCUt/ArcGIS/rest/s
ervices
Millcreek
https://services9.arcgis.com/XRrSFvEwSsReIxuA/ArcGIS/rest/ser
vices
Millcreek
https://tiles.arcgis.com/tiles/XRrSFvEwSsReIxuA/arcgis/rest/servi
ces
Ogden
https://arcgis.ogdencity.com/arcgis/rest/services
Orem
https://maps.orem.org/arcgis/rest/services
Park City
https://cityworks.parkcity.org/arcgis/rest/services
Provo
https://gispublicweb.provo.org/arcgis/rest/services
Provo
https://gispublicweb.provo.org/imagery/rest/services
Provo
https://services2.arcgis.com/u1JcjHKiYxDeQU3C/ArcGIS/rest/ser
vices
Provo
https://tiles.arcgis.com/tiles/u1JcjHKiYxDeQU3C/arcgis/rest/servi
ces
Richfield
https://services5.arcgis.com/PmhEdhGbiU6Fds6f/ArcGIS/rest/serv
ices
St. George
https://services3.arcgis.com/sSyqU2G01sKVqGZA/ArcGIS/rest/se
rvices
St. George
https://tiles.arcgis.com/tiles/sSyqU2G01sKVqGZA/arcgis/rest/serv
ices

## Page 411

Salem
___________

Salt Lake City           https://services.arcgis.com/mMBpeYj0vPFotzbe/arcgis/rest/services

Salt Lake City
https://tiles.arcgis.com/tiles/mMBpeYj0vPFotzbe/arcgis/rest/servic
es
Sandy City
https://gis.sandy.utah.gov/arcgis/rest/services
Table of contents disabled
Sandy City
          https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services
South Jordan
https://gis2.southjordanutah.gov/server/rest/services
Spanish Fork
https://gis.spanishfork.gov/arcgis/rest/services
Spanish Fork
https://services.arcgis.com/iyYrowJyNiQoaleL/arcgis/rest/services
West Jordan
https://services1.arcgis.com/yznraL2FyB2Sm732/arcgis/rest/servic
es
West Jordan
https://tiles.arcgis.com/tiles/yznraL2FyB2Sm732/arcgis/rest/servic
es
West Valley City
https://gisserver.wvc-ut.gov/server/rest/services
West Valley City
https://services.arcgis.com/VuwCBhloG26S6mpc/arcgis/rest/servic
es
West Valley City
https://tiles.arcgis.com/tiles/VuwCBhloG26S6mpc/arcgis/rest/servi
ces
Vermont State GIS Servers
Vermont Center for Geographic Information
Website: https://geodata.vermont.gov
Website open data portal: https://geodata.vermont.gov
GIS: https://maps.vcgi.vermont.gov/arcgis/rest/services
 EGC_services  aerials
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Vermont Department of Health
Website: https://www.healthvermont.gov
GIS: https://maps.healthvermont.gov/arcgis/rest/services
Table of contents disabled
Vermont Department of Public Safety
Website: https://dps.vermont.gov
GIS: https://services9.arcgis.com/cb6eDXWVgAvVXeIK/ArcGIS/rest/services
Emergency Management
Vermont Agency of Transportation

## Page 412

Website: https://vtrans.vermont.gov
GIS: https://maps.vtrans.vermont.gov/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services1.arcgis.com/NXmBVyW5TaiCXqFs/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/NXmBVyW5TaiCXqFs/arcgis/rest/services
Vermont Agency of Natural Resources
Website: https://anr.vermont.gov
GIS: https://anrmaps.vermont.gov/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Vermont Agency of Human Services
Website: https://humanservices.vermont.gov
GIS: https://services.arcgis.com/YKJ5JtnaPQ2jDbX8/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/YKJ5JtnaPQ2jDbX8/arcgis/rest/services
Vermont various layers
GIS: https://services1.arcgis.com/BkFxaEFNwHqX3tAw/ArcGIS/rest/services
Includes trails
Parcel lines:  FS_VCGI_OPENDATA_Cadastral_VTPARCELS_poly_standardi
zed_parcels_SP_v1/FeatureServer/0
GIS: https://tiles.arcgis.com/tiles/BkFxaEFNwHqX3tAw/arcgis/rest/services
GIS: https://services5.arcgis.com/Uzks6LSde6r23wwG/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Uzks6LSde6r23wwG/arcgis/rest/services
Green Mountain Power
GIS: https://maps.gmpvt.com/arcgis/rest/services
8-12-2023 No tiled data
Slow the spread project   Gypsy moth, now called Spongy Moth
Website: https://www.slowthespread.org
GIS: https://services6.arcgis.com/o4D8eF2Ip4Ht7I17/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/o4D8eF2Ip4Ht7I17/arcgis/rest/services
Vermont Regional
Addison County Regional Planning Commission
Website: https://www.acrpc.org
GIS: https://services8.arcgis.com/Gf7J70KyUdpb0dNE/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Gf7J70KyUdpb0dNE/arcgis/rest/services
Bennington County Regional Commission
Website: http://www.bcrcvt.org
not https
GIS: https://services3.arcgis.com/j4iUeJBDjMxiPkVg/arcgis/rest/services

## Page 413

Central Vermont Regional Planning Commission (CVRPC)
Website: https://centralvtplanning.org
GIS: https://map.ccrpcvt.org/arcgis/rest/services
8-12-2023 No tiled data
Chittenden County Regional Planning Commission (CCRPC)
Website: https://www.ccrpcvt.org
GIS: See also Central Vermont Regional Planning Commission
GIS: http://map.ccrpcvt.org/arcgis/rest/services
GIS: https://services1.arcgis.com/KVHZNprt62ZdIujN/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/KVHZNprt62ZdIujN/arcgis/rest/services
Lamoille County Planning Commission
Website: https://www.lcpcvt.org
GIS: https://services2.arcgis.com/aYpp0a2OASkHuYP7/arcgis/rest/services
Mount Ascutney Regional Commission (MARC), formerly known as the Southern
Windsor County Regional Planning Commission (SWCRPC)
Website: https://www.marcvt.org
GIS: https://services5.arcgis.com/tbnCzQ0iyXeEj5i5/arcgis/rest/services
Northeastern Vermont Development Association
Website: https://www.nvda.net
GIS: https://services7.arcgis.com/FVjZXV3pTUIV7iuO/arcgis/rest/services
Northwest Regional Planning Commission
Website: https://www.nrpcvt.com
GIS: https://services7.arcgis.com/CIdxNzJmLZGoegAM/arcgis/rest/services
Rutland Regional Planning Commission
Website: https://www.rutlandrpc.org
GIS: https://services7.arcgis.com/aYB5mCBbYQrMYLRI/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/aYB5mCBbYQrMYLRI/arcgis/rest/services
Two Rivers-Ottauquechee Regional Commission
Website: https://www.trorc.org
GIS: https://services1.arcgis.com/u6q3LNruiYmDjGX5/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/u6q3LNruiYmDjGX5/arcgis/rest/services
Windham Regional Commission
Website: http://windhamregional.org
not https
GIS: https://services2.arcgis.com/3xVssd0FD416APnB/arcgis/rest/services
Vermont Association of Planning and Development Agencies
Website: https://www.vapda.org
GIS: https://services3.arcgis.com/lwHERaDzBLjVdNnG/ArcGIS/rest/services

## Page 414

Vermont Community Broadband Board
Website: https://publicservice.vermont.gov/vermont-community-broadband-board-vcbb
GIS: https://services3.arcgis.com/dOwqC45gjPkCyafh/ArcGIS/rest/services
Vermont City, Town, Village, etc GIS Servers
Albany
_ttps://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Albany_Service/FeatureServer
dead link 3
Bakersfield
https://services7.arcgis.com/CIdxNzJmLZGoegAM/ArcGIS/rest/se
rvices
Also for Enosburg, Fairfax, Fairfield, Fletcher, Franklin,
Grand Isle, Highgate, Montgomery, North Hero, Richford,
Saint Albans, Sheldon, South Hero, Swanton
Baltimore
_ttps://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Baltimore_Service/FeatureServer
dead link 3
Brandon
https://gisserver2.axisgis.com/arcgis/rest/services/BrandonVT
Not open to public
Brattleboro
https://gisserver2.axisgis.com/arcgis/rest/services/BrattleboroVT
Not open to public
Bridgewater
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Bridgewater_Service/FeatureServer
Go to the top and search for ‘Bridgewater’
Bridport
_ttps://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Bridport_Service/FeatureServer
dead link 3
Brighton
https://gisserver2.axisgis.com/arcgis/rest/services/BrightonVT
Not open to public

Burlington
https://maps.burlingtonvt.gov/arcgis/rest/services
Burlington
https://services1.arcgis.com/1bO0c7PxQdsGidPK/arcgis/rest/servi
ces
Table of contents hidden by javascript
Burlington
https://tiles.arcgis.com/tiles/1bO0c7PxQdsGidPK/arcgis/rest/servic
es
Caledonia
___________
Calais
https://gisserver2.axisgis.com/arcgis/rest/services/CalaisVT
Not open to public
Canaan
___________

## Page 415

Castleton
https://gisserver2.axisgis.com/arcgis/rest/services/CastletonVT
Not open to public
Cavendish
https://gisserver2.axisgis.com/arcgis/rest/services/CavendishVT
Not open to public
Chester
https://gisserver2.axisgis.com/arcgis/rest/services/ChesterVT
Not open to public
Craftsbury
____________
Essex Town
https://gisserver2.axisgis.com/arcgis/rest/services/Essex_TownVT
Not open to public
Fairfield
https://gisserver2.axisgis.com/arcgis/rest/services/FairfieldVT
Not open to public
Hartford
_________
Hartland
https://gisserver2.axisgis.com/arcgis/rest/services/HartlandVT
Not open to public
Huntington
_________
Hyde Park
https://gisserver2.axisgis.com/arcgis/rest/services/Hyde_ParkVT
Not open to public
Manchester
https://gisserver2.axisgis.com/arcgis/rest/services/ManchesterVT
Not open to public
Montpelier
https://services6.arcgis.com/ALaxfASMULIJ1PP6/arcgis/rest/servi
ces
Montpelier
https://tiles.arcgis.com/tiles/ALaxfASMULIJ1PP6/arcgis/rest/servi
ces
Mount Holly
_________
Newport City            https://gisserver2.axisgis.com/arcgis/rest/services/Newport_CityVT
Not open to public
Norton
_________
Orwell
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Orwell_Service/FeatureServer
Go to the top and search for ‘Orwell’

## Page 416

Park City
https://services1.arcgis.com/wmY050uFnMPcgSCc/ArcGIS/rest/se
rvices
Park City
https://tiles.arcgis.com/tiles/wmY050uFnMPcgSCc/arcgis/rest/serv
ices
Pittsford
https://gisserver2.axisgis.com/arcgis/rest/services/PittsfordVT
Not open to public
Plainfield
_________
Plymouth
https://gisserver2.axisgis.com/arcgis/rest/services/PlymouthVT
Not open to public
Poultney
https://gisserver2.axisgis.com/arcgis/rest/services/PoultneyVT
Not open to public
Readsboro
https://gisserver2.axisgis.com/arcgis/rest/services/ReadsboroVT
Not open to public
Rockingham
https://gisserver2.axisgis.com/arcgis/rest/services/RockinghamVT
Not open to public

Royalton
_________
Rutland Town           https://gisserver2.axisgis.com/arcgis/rest/services/Rutland_TownVT
Not open to public
Sharon
_________
Shelburne
https://gisserver2.axisgis.com/arcgis/rest/services/ShelburneVT
Not open to public
Sheldon
_________
South Hero
https://gisserver2.axisgis.com/arcgis/rest/services/South_HeroVT
Not open to public
Stannard
_________
Stockbridge
https://gisserver2.axisgis.com/arcgis/rest/services/StockbridgeVT
Not open to public
Sudbury
_________
Turnbridge
_________

## Page 417

Victory
_________
Walden
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Walden_Service/FeatureServer
Go to the top and search for ‘Walden’
Warren
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/Warren
VT_BaseMap_Topo/MapServer
Warren
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/Warren
VT_BaseMap/MapServer
Warren
https://gishost.cdmsmithgis.com/cdmsmithgis/rest/services/Warren
VT_Operational/MapServer
Winooski
_________
Wolcott
https://gisserver2.axisgis.com/arcgis/rest/services/WolcottVT
Not open to public
Woodford
_________
Worcester
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Worcester_Service/FeatureServer
Go to the top and search for ‘Worcester’
Woodstock
https://gisserver2.axisgis.com/arcgis/rest/services/WoodstockVT
Not open to public
Virginia State GIS Servers
Virginia Open Data
Website: https://data.virginia.gov
Virginia Geographic Information Network
Website: https://vgin.vdem.virginia.gov
GIS: https://services.arcgis.com/WNJF1HhUVAm3jccO/arcgis/rest/services
Virginia Department of Emergency Management
Website: https://www.vaemergency.gov
GIS: https://vginmaps.vdem.virginia.gov/arcgis/rest/services
Parcel lines tiled:  VA_Base_Layers/VA_Parcels/MapServer/0
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services3.arcgis.com/qVupYidwzMKkDQzr/ArcGIS/rest/services
Virginia Department of Conservation and Recreation
Website: https://www.dcr.virginia.gov
GIS: https://casdsis.dcr.virginia.gov/arcgis/rest/services

## Page 418

GIS: https://dsfmportal.dcr.virginia.gov/server/rest/services
GIS: https://services1.arcgis.com/PxUNqSbaWFvFgHnJ/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/PxUNqSbaWFvFgHnJ/arcgis/rest/services
Virginia Department of Environmental Quality
Website: https://www.deq.virginia.gov
GIS: https://apps.deq.virginia.gov/arcgis/rest/services
Virginia Department of Forestry
Website: https://dof.virginia.gov
GIS: https://services1.arcgis.com/zdPnl7ASQIo6PX54/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/zdPnl7ASQIo6PX54/arcgis/rest/services
Virginia Department of Historic Resources
Website: https://www.dhr.virginia.gov
GIS: https://vcris.dhr.virginia.gov/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Virginia Department of Mines, Minerals and Energy
Website: https://www.virginia.gov/agencies/department-of-mines-minerals-and-energy
GIS: https://energy.virginia.gov/gis/rest/services
8-12-2023 No tiled data
Virginia Department of Rail and Public Transportation
Website: https://drpt.virginia.gov
GIS: https://services9.arcgis.com/9oDT7ErWemWCzvY7/ArcGIS/rest/services
Virginia Department of Transportation
Website: https://www.virginiadot.org
GIS: https://services.arcgis.com/p5v98VHDX9Atv3l7/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/p5v98VHDX9Atv3l7/arcgis/rest/services
Virginia Department of Wildlife Resources
Website: https://dwr.virginia.gov
GIS: https://services2.arcgis.com/qsZIVOgnyrsajEtb/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/qsZIVOgnyrsajEtb/arcgis/rest/services
Virginia Information Technologies Agency
Website: https://www.vita.virginia.gov/
GIS: _ttps://gismaps.vita.virginia.gov/arcgis/rest/services
dead link 3
Virginia Economic Development
Website: https://www.vedp.org
GIS: https://maps.vedp.org/arcgis/rest/services
Virginia Tech Enterprise GIS

## Page 419

Website: https://gis.vt.edu
GIS: https://arcgis-central.gis.vt.edu/arcgis/rest/services
8-12-2023 No tiled data
Virginia Regional
Central Shenandoah Planning District Commission
Website: https://www.cspdc.org
GIS: https://services2.arcgis.com/VkOe3q7u7LGe1XcE/arcgis/rest/services
Hampton Roads Planning District Commission
Website: https://hrtpo.org
GIS: https://services3.arcgis.com/IFfZzsUkSirJaEqg/ArcGIS/rest/services
Southside Planning District Commission
Website: https://www.southsidepdc.org
GIS: https://services.arcgis.com/O8ZpeBC0xLM5nL34/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/O8ZpeBC0xLM5nL34/arcgis/rest/services
HRSD - Hampton Roads wastewater treatment
Website: https://www.hrsd.com
GIS: https://geo.hrsd.com/hrgeo/rest/services
8-12-2023 No tiled data
Virginia County GIS Servers
All counties are listed and have been checked for GIS
Accomack
          https://parcelviewer.geodecisions.com/arcgis/rest/services/accomack
Albemarle
https://services2.arcgis.com/khVz7mitcPJHUnlM/arcgis/rest/servic
es
Albemarle
https://tiles.arcgis.com/tiles/khVz7mitcPJHUnlM/arcgis/rest/servic
es
Alleghany
__________
Amelia
https://www.webgis.net/arcgis/rest/services/VA/AmeliaCo_WebGI
S/MapServer
Amherst
https://maps2.timmons.com/arcgis/rest/services/WL_Amherst
Appomattox
https://maps2.timmons.com/arcgis/rest/services/WL_Appomattox
Arlington
https://arlgis.arlingtonva.us/arcgis/rest/services

## Page 420

Arlington
https://services1.arcgis.com/JrtUzVcH8S2wnzVH/arcgis/rest/servi
ces
Arlington
https://tiles.arcgis.com/tiles/JrtUzVcH8S2wnzVH/arcgis/rest/servi
ces
Augusta
https://gis.co.augusta.va.us/arcgis/rest/services
Bath
https://services2.arcgis.com/VkOe3q7u7LGe1XcE/arcgis/rest/servi
ces
Bedford
https://webgis.bedfordcountyva.gov/arcgis/rest/services
Bedford
https://services3.arcgis.com/DXCmCcRcEQ793kMP/arcgis/rest/se
rvices
Bedford
https://tiles.arcgis.com/tiles/DXCmCcRcEQ793kMP/arcgis/rest/ser
vices
Bland
WMS server
Botetourt
https://www.webgis.net/arcgis/rest/services/VA/Botetourt_BB_Res
/FeatureServer
Botetourt
https://www.webgis.net/arcgis/rest/services/VA/Botetourt_BB_Res
/MapServer
Botetourt
https://www.webgis.net/arcgis/rest/services/VA/Botetourt_Planime
tric/MapServer
Botetourt
https://www.webgis.net/arcgis/rest/services/VA/BotetourtCo_Web
GIS/MapServer
Buchanan
https://www.webgis.net/arcgis/rest/services/VA/Buchanan/MapSer
ver
Buckingham
WMS server
Campbell
https://gis.co.campbell.va.us/arcgis/rest/services
Campbell
https://parcelviewer.geodecisions.com/arcgis/rest/services/Campbe
ll
Campbell
https://services1.arcgis.com/d6RVn1EQDwncFtWo/ArcGIS/rest/se
rvices
Caroline
https://parcelviewer.geodecisions.com/arcgis/rest/services/Caroline
Caroline
https://services8.arcgis.com/javH2x6lNvVqxMm3/ArcGIS/rest/ser
vices
Caroline
https://tiles.arcgis.com/tiles/javH2x6lNvVqxMm3/arcgis/rest/servi
ces
Carroll
WMS server

## Page 421

Charles City County
https://services5.arcgis.com/7ELQsoO4nWXrJNri/arcgis/rest/servi
ces
Charlotte
          https://parcelviewer.geodecisions.com/arcgis/rest/services/Charlotte
Chesterfield
https://services3.arcgis.com/TsynfzBSE6sXfoLq/ArcGIS/rest/servi
ces
Chesterfield
           https://tiles.arcgis.com/tiles/TsynfzBSE6sXfoLq/arcgis/rest/services
Clarke
WMS server
Craig
https://www.webgis.net/arcgis/rest/services/VA/Craig_WebGIS/M
apServer
Culpeper
https://www.webgis.net/arcgis/rest/services/VA/CulpeperWebGIS_
Pro/MapServer
Cumberland
______________
Dickenson
https://services8.arcgis.com/5gMtNRFayyAPvHSm/arcgis/rest/serv
ices
Dinwiddie
https://arcgis.vgsi.com/server/rest/services/Dinwiddie_VA
Dinwiddie
https://services.arcgis.com/pXJ1hE8HkwpsRwne/arcgis/rest/servic
es
Essex
https://arcgis.vgsi.com/server/rest/services/Essex_VA
Fairfax county
https://www.fairfaxcounty.gov/mercator/rest/services
Fairfax county
https://www.fairfaxcounty.gov/lambert/rest/services
Fairfax county
https://www.fairfaxcounty.gov/euclid/rest/services
Fairfax county
https://www.fairfaxcounty.gov/gisimagery/rest/services
Fairfax county
https://services1.arcgis.com/ioennV6PpG5Xodq0/arcgis/rest/servic
es
Fairfax county
https://tiles.arcgis.com/tiles/ioennV6PpG5Xodq0/arcgis/rest/servic
es
Fauquier
https://agol.gis.fauquiercounty.gov:6443/arcgis/rest/services
Fauquier
https://services.arcgis.com/oAoeYJ1kqmAwcEC2/arcgis/rest/servi
ces
Fauquier
https://tiles.arcgis.com/tiles/oAoeYJ1kqmAwcEC2/arcgis/rest/serv
ices
Floyd
WMS server

## Page 422

Fluvanna
https://www.webgis.net/arcgis/rest/services/VA/Fluvanna_WebGI
S/MapServer
Franklin
https://gis.franklincountyva.gov/arcgis/rest/services
Franklin
https://parcelviewer.geodecisions.com/arcgis/rest/services/Franklin
Franklin
https://services9.arcgis.com/AzdpqVmJ5GjGWCoI/arcgis/rest/serv
ices
Franklin
https://tiles.arcgis.com/tiles/AzdpqVmJ5GjGWCoI/arcgis/rest/serv
ices
Frederick
https://fredcogis.fcva.us/maps/rest/services
Giles
WMS server
Gloucester
https://services3.arcgis.com/iQ7tKG8cZYyv3N7s/ArcGIS/rest/serv
ices
Gloucester
https://tiles.arcgis.com/tiles/iQ7tKG8cZYyv3N7s/arcgis/rest/servic
es
Goochland
https://gis.co.goochland.va.us/arcgis/rest/services
Grayson
https://www.webgis.net/arcgis/rest/services/VA/GraysonCo_WebG
IS1/MapServer
Greene
https://www.webgis.net/arcgis/rest/services/VA/GreeneCo_Test/M
apServer
Greene
https://www.webgis.net/arcgis/rest/services/VA/GreeneCo_WebGI
S/MapServer
Greensville
https://www.webgis.net/arcgis/rest/services/VA/GreensvilleCo_W
ebGIS/MapServer
Halifax
https://www.webgis.net/arcgis/rest/services/VA/HalifaxCo_WebGI
S/MapServer
Hanover
https://parcelviewer.geodecisions.com/arcgis/rest/services/Hanover
Hanover
https://services2.arcgis.com/sKZWgJlU6SekCzQV/ArcGIS/rest/ser
vices
Hanover
https://tiles.arcgis.com/tiles/sKZWgJlU6SekCzQV/arcgis/rest/servi
ces
Henrico
https://portal.henrico.us/mapping/rest/services

Henrico
https://services.arcgis.com/LxWK4CxNTBBlLshT/arcgis/rest/servi
ces
Henrico
https://tiles.arcgis.com/tiles/LxWK4CxNTBBlLshT/arcgis/rest/ser
vices

## Page 423

Henry
GIS is not ArcGIS
Highland
https://maps2.timmons.com/arcgis/rest/services/WL_Highland
Isle Of Wight
https://services.arcgis.com/Dc6hhMQCpvLlOmSY/arcgis/rest/serv
ices
James City
https://property.jamescitycountyva.gov/arcgis/rest/services
James City
https://services2.arcgis.com/1xpxJqyECZmZIKoc/ArcGIS/rest/ser
vices
King and Queen
https://maps2.timmons.com/arcgis/rest/services/WL_KingAndQue
en
King George
           https://services2.arcgis.com/S8zMJrpz61FbvL5t/arcgis/rest/services
King William
https://maps2.timmons.com/arcgis/rest/services/WL_KingWilliam
Lancaster
GIS is not ArcGIS
Lee
WMS server
Loudoun
https://logis.loudoun.gov/gis/rest/services
Loudoun
https://logis.loudoun.gov/image/rest/services
Loudoun
https://services1.arcgis.com/MxjRokvPm7bjslyR/arcgis/rest/servic
es
Loudoun
https://tiles.arcgis.com/tiles/MxjRokvPm7bjslyR/arcgis/rest/servic
es
Louisa
https://maps2.timmons.com/arcgis/rest/services/WL_Louisa
Lunenburg
https://maps2.timmons.com/arcgis/rest/services/WL_Lunenburg
Loudoun
https://logis.loudoun.gov/gis/rest/services
Loudoun
https://logis.loudoun.gov/image/rest/services
Madison
https://www.webgis.net/arcgis/rest/services/VA/MadisonCo_Web
GIS1/MapServer
Mathews
https://maps2.timmons.com/arcgis/rest/services/WL_Mathews
Mecklenburg
__________
Middlesex
https://services9.arcgis.com/UrElc2PRESEUr5jw/arcgis/rest/servic
es

## Page 424

Montgomery
https://maps.montva.com/server/rest/services
Montgomery
https://maps.montva.com/image/rest/services
Montgomery
https://services5.arcgis.com/IZ8QFYP84iubFqmi/ArcGIS/rest/serv
ices
Montgomery
https://tiles.arcgis.com/tiles/IZ8QFYP84iubFqmi/arcgis/rest/servic
es
Nelson
https://maps2.timmons.com/arcgis/rest/services/WL_Nelson
New Kent
          https://parcelviewer.geodecisions.com/arcgis/rest/services/NewKent
New Kent
https://services2.arcgis.com/wRTEaR3VIVeAhJdr/ArcGIS/rest/ser
vices
New Kent
https://tiles.arcgis.com/tiles/wRTEaR3VIVeAhJdr/arcgis/rest/servi
ces
Northampton
https://parcelviewer.geodecisions.com/arcgis/rest/services/Northam
pton
Northumberland
No GIS found
Nottoway
https://maps2.timmons.com/arcgis/rest/services/WL_Nottoway
Orange
https://gis.orangecountyva.gov/arcgis/rest/services
Orange
https://services8.arcgis.com/QlNjtMU89yOFWrJ8/ArcGIS/rest/ser
vices
Orange
https://tiles.arcgis.com/tiles/QlNjtMU89yOFWrJ8/arcgis/rest/servi
ces
Page
https://parcelviewer.geodecisions.com/arcgis/rest/services/Page
Patrick
WMS server
Pittsylvania
https://services2.arcgis.com/mTpBDvIjv8OhMDVd/ArcGIS/rest/se
rvices
Pittsylvania
https://tiles.arcgis.com/tiles/mTpBDvIjv8OhMDVd/arcgis/rest/serv
ices
Powhatan
https://services5.arcgis.com/nip9boeHfv9Av5yj/arcgis/rest/services
Powhatan
https://tiles.arcgis.com/tiles/nip9boeHfv9Av5yj/arcgis/rest/services
Prince Edward
https://services7.arcgis.com/7uRcISB6fkHAMbyM/arcgis/rest/serv
ices
Prince George
https://gis.pgatlas.com/pgatlas/rest/services
Prince George
https://arcgis.vgsi.com/server/rest/services/Prince_George_VA

## Page 425

Prince George
https://services.arcgis.com/kSZiBgsXsUF788NB/arcgis/rest/servic
es
Prince George
https://tiles.arcgis.com/tiles/kSZiBgsXsUF788NB/arcgis/rest/servi
ces
Prince William
https://gisweb.pwcgov.org/arcgis/rest/services
Prince William
https://gisweb.pwcva.gov/arcgis/rest/services
Prince William
https://services2.arcgis.com/0Q7l03Ls62VG0fy4/ArcGIS/rest/servi
ces
Prince William          https://tiles.arcgis.com/tiles/0Q7l03Ls62VG0fy4/arcgis/rest/services
Pulaski
https://services5.arcgis.com/cnJiyVVCFyUslPPa/arcgis/rest/servic
es
Rappahannock
No GIS found
Richmond
WMS server
Roanoke
https://arcgis.roanokecountyva.gov/arcgiswebssl/rest/services
Roanoke
https://arcgis.roanokecountyva.gov/arcgisweb/rest/services
Roanoke
https://arcgis.roanokecountyva.gov/arcgisimage/rest/services
Roanoke
https://services1.arcgis.com/VlZ73DcE2ya6FnSK/ArcGIS/rest/serv
ices
Roanoke
https://tiles.arcgis.com/tiles/VlZ73DcE2ya6FnSK/arcgis/rest/servic
es
Rockbridge
https://www.webgis.net/arcgis/rest/services/VA/RockbridgeCo_W
ebGIS/MapServer
Rockingham
WMS server
Russell
WMS server
Scott
WMS server
Shenandoah
https://maps2.timmons.com/arcgis/rest/services/WL_Shenandoah
Smyth
https://www.webgis.net/arcgis/rest/services/VA/SmythCo_WebGI
S/MapServer
Southampton
WMS server
Spotsylvania
https://gis.spotsylvania.va.us/arcgis/rest/services
Spotsylvania
https://services1.arcgis.com/Fs0uoy8dWAYsVfXh/ArcGIS/rest/ser
vices

## Page 426

Spotsylvania
https://tiles.arcgis.com/tiles/Fs0uoy8dWAYsVfXh/arcgis/rest/servi
ces
Stafford
https://gismapping.stafford.va.us/arcgis/rest/services
Table of contents disabled
Stafford
https://services1.arcgis.com/qKiA6JuCrE2l72iL/ArcGIS/rest/servic
es
Stafford
           https://tiles.arcgis.com/tiles/qKiA6JuCrE2l72iL/arcgis/rest/services
Surry
https://parcelviewer.geodecisions.com/arcgis/rest/services/Surry
Sussex
_____________
Tazewell
Warren
https://maps2.timmons.com/arcgis/rest/services/WL_Warren
Washington
WMS server
Westmoreland
No GIS found
Wise
WMS server
Wythe
WMS server
York
https://maps.yorkcounty.gov/arcgis/rest/services
York
          https://services5.arcgis.com/r8jw1egVpeek09G6/arcgis/rest/services
York
           https://tiles.arcgis.com/tiles/r8jw1egVpeek09G6/arcgis/rest/services
Virginia City, Town, Village, etc GIS Servers
Alexandria
https://maps.alexandriava.gov/arcgis/rest/services
Alexandria
https://services2.arcgis.com/ChYV69FhfjwkvRmy/ArcGIS/rest/ser
vices
Alexandria
https://tiles.arcgis.com/tiles/ChYV69FhfjwkvRmy/arcgis/rest/servi
ces
Arlington
See Arlington County
Ashland
See Hanover county
Blacksburg
https://tobmaps.blacksburg.gov/server/rest/services
Blacksburg
https://services1.arcgis.com/rAuQoDGA22NtJdmg/ArcGIS/rest/ser
vices
Charlottesville
https://gisweb.charlottesville.org/cvgisweb/rest/services
Charlottesville
https://gisweb.charlottesville.org/arcgis/rest/services

## Page 427

Charlottesville
https://services2.arcgis.com/ZyVP1uFGBJZ59KCA/ArcGIS/rest/se
rvices
Charlottesville
https://tiles.arcgis.com/tiles/ZyVP1uFGBJZ59KCA/arcgis/rest/serv
ices
Chesapeake
https://gis.cityofchesapeake.net/mapping/rest/services
Chesapeake
https://services1.arcgis.com/OAphVRUvJVpBRovs/ArcGIS/rest/se
rvices
Chesapeake
https://tiles.arcgis.com/tiles/OAphVRUvJVpBRovs/arcgis/rest/serv
ices
Christiansburg
https://services.arcgis.com/hK4vGUcrLZsYhZjD/arcgis/rest/servic
es
Christiansburg
https://tiles.arcgis.com/tiles/hK4vGUcrLZsYhZjD/arcgis/rest/servi
ces
Coeburn
https://services7.arcgis.com/CCm90eUiTNUXFTkz/arcgis/rest/ser
vices
Culpeper
https://services1.arcgis.com/umAze4B28rywBpwB/ArcGIS/rest/ser
vices
Culpeper
https://tiles.arcgis.com/tiles/umAze4B28rywBpwB/arcgis/rest/servi
ces
Danville
https://gis.danvilleva.gov/server/rest/services
Danville
https://services3.arcgis.com/b7ay1OgWNo9QMMMz/ArcGIS/rest/
services
Danville
https://tiles.arcgis.com/tiles/b7ay1OgWNo9QMMMz/arcgis/rest/se
rvices
Emporia
https://parcelviewer.geodecisions.com/arcgis/rest/services/Emporia
Fairfax
https://services2.arcgis.com/DANcyjLcCCpGk8Ri/arcgis/rest/servi
ces
Fairfax
https://services9.arcgis.com/kYvfX7YK8OobHItA/ArcGIS/rest/ser
vices
Police
Falls Church
https://services1.arcgis.com/2hmXRAz4ofcdQP6p/ArcGIS/rest/ser
vices
Falls Church
https://tiles.arcgis.com/tiles/2hmXRAz4ofcdQP6p/arcgis/rest/servi
ces
Farmville
https://maps2.timmons.com/arcgis/rest/services/WL_Farmville
Fredericksburg
https://maps.fredericksburgva.gov/arcgis/rest/services

## Page 428

Fredericksburg
https://services2.arcgis.com/Cp5mSUK6iwpkVD8N/ArcGIS/rest/s
ervices
Fredericksburg
https://tiles.arcgis.com/tiles/Cp5mSUK6iwpkVD8N/arcgis/rest/ser
vices
Galax
https://www.webgis.net/arcgis/rest/services/VA/Galax_WebGIS/M
apServer
Hampton
https://webgis2.hampton.gov/server/rest/services
Harrisonburg
https://gis.harrisonburgva.gov/arcgis/rest/services
Harrisonburg
https://arcgis.vgsi.com/server/rest/services/Harrisonburg_VA
Herndon
See Fairfax County
Kingsville
https://maps2.timmons.com/arcgis/rest/services/WL_Kingsville
Leesburg
https://services1.arcgis.com/7owdfh5mgjEgbCSM/ArcGIS/rest/ser
vices
Leesburg
https://tiles.arcgis.com/tiles/7owdfh5mgjEgbCSM/arcgis/rest/servi
ces
Lexington
https://maps2.timmons.com/arcgis/rest/services/WL_Lexington
Lynchburg
https://mapviewer.lynchburgva.gov/arcgis/rest/services
Lynchburg
https://services1.arcgis.com/7UD44zrYCKZqL1ix/ArcGIS/rest/ser
vices
Lynchburg
https://tiles.arcgis.com/tiles/7UD44zrYCKZqL1ix/arcgis/rest/servi
ces
Manassas
https://services1.arcgis.com/3wpOgOChiWXPeFWB/ArcGIS/rest/
services
Manassas
https://tiles.arcgis.com/tiles/3wpOgOChiWXPeFWB/arcgis/rest/se
rvices
Newport News
https://maps.nnva.gov/arcgis/rest/services
Newport News
https://maps.nnva.gov/gis/rest/services
Newport News
https://services6.arcgis.com/SiUAoHzWN11AIADA/ArcGIS/rest/s
ervices
Newport News
https://tiles.arcgis.com/tiles/SiUAoHzWN11AIADA/arcgis/rest/ser
vices
Norfolk
https://gisshare.norfolk.gov/pubserver/rest/services
Norfolk
https://gisshare.norfolk.gov/server/rest/services
Norfolk
https://services2.arcgis.com/fUAsosS8WXl3mXcn/ArcGIS/rest/ser
vices

## Page 429

Norfolk
https://tiles.arcgis.com/tiles/fUAsosS8WXl3mXcn/arcgis/rest/servi
ces
Norton
______________
Purcellville
https://services3.arcgis.com/94nRGVPbO10XOp1M/ArcGIS/rest/s
ervices
Petersburg
https://parcelviewer.geodecisions.com/arcgis/rest/services/Petersbu
rg
Poquoson
          https://parcelviewer.geodecisions.com/arcgis/rest/services/poquoson
Portsmouth
https://services1.arcgis.com/nGsguNiHLn7MU4R4/arcgis/rest/serv
ices
Portsmouth
https://tiles.arcgis.com/tiles/nGsguNiHLn7MU4R4/arcgis/rest/serv
ices
Radford
https://radfordgis3.radford.va.us/arcgiscloud/rest/services
Radford
https://services2.arcgis.com/uBVNRnvxMutOfx4V/arcgis/rest/serv
ices
Radford
https://tiles.arcgis.com/tiles/uBVNRnvxMutOfx4V/arcgis/rest/serv
ices
Richmond
https://services1.arcgis.com/k3vhq11XkBNeeOfM/arcgis/rest/servi
ces
Richmond
https://tiles.arcgis.com/tiles/k3vhq11XkBNeeOfM/arcgis/rest/servi
ces
Roanoke
https://gis03.roanokeva.gov/arcgis/rest/services
Roanoke
          https://services.arcgis.com/KII0S5XRkpE66Ngk/arcgis/rest/services
Roanoke
https://tiles.arcgis.com/tiles/KII0S5XRkpE66Ngk/arcgis/rest/servic
es
Rural Retreat
https://www.webgis.net/arcgis/rest/services/VA/RuralRetreat_Web
GIS/MapServer
Saint Paul
          https://services6.arcgis.com/djTaaNDqPz5g1z4u/arcgis/rest/services
Salem
https://arcgis.vgsi.com/server/rest/services/Salem_VA
Shenandoah
https://maps2.timmons.com/arcgis/rest/services/WL_Shenandoah
Staunton
https://gis.ci.staunton.va.us:8087/stagis/rest/services
Staunton
https://arcgis.vgsi.com/server/rest/services/Staunton_VA

## Page 430

Staunton
https://services.arcgis.com/bp3MWUdz4OBPF6xz/arcgis/rest/servi
ces
Staunton
https://tiles.arcgis.com/tiles/bp3MWUdz4OBPF6xz/arcgis/rest/ser
vices
Virginia Beach
https://geo.vbgov.com/mapservices/rest/services
Virginia Beach
https://services2.arcgis.com/CyVvlIiUfRBmMQuu/arcgis/rest/servi
ces
Virginia Beach
https://tiles.arcgis.com/tiles/CyVvlIiUfRBmMQuu/arcgis/rest/servi
ces
Warrenton
https://services3.arcgis.com/7Q2bdSYWSeUYx2U5/arcgis/rest/ser
vices
Waynesboro
_____________
West Point
https://parcelviewer.geodecisions.com/arcgis/rest/services/WestPoi
nt
Williamsburg
https://services1.arcgis.com/96Dq0JXOtjNW10pz/ArcGIS/rest/ser
vices
Winchester
https://maps2.timmons.com/arcgis/rest/services/WL_Winchester
Winchester
https://arcgis.vgsi.com/server/rest/services/Winchester_VA
Winchester
https://services5.arcgis.com/a7JbuLDxkxnyaAjZ/ArcGIS/rest/servi
ces
Winchester
          https://tiles.arcgis.com/tiles/a7JbuLDxkxnyaAjZ/arcgis/rest/services
Wytheville
https://www.webgis.net/arcgis/rest/services/VA/Wytheville_WebG
IS/MapServer
Washington State GIS Servers
Washington open data portals
Website: https://data.wa.gov/
Website: https://geo.wa.gov
Washington Department of Agriculture
Website: https://agr.wa.gov/
GIS: https://fortress.wa.gov/agr/gis/wsdagis/rest/services
2-27-2023 no tiled data
Washington Department of Archaeology and Historic Preservation
Website: https://dahp.wa.gov
GIS: https://wisaard.dahp.wa.gov/server/rest/services

## Page 431

Washington Department of Ecology
Website: https://ecology.wa.gov/
GIS: https://gis.ecology.wa.gov/hosting/rest/services
GIS: https://gis.ecology.wa.gov/serverext/rest/services
CPR/CPR/MapServer/
electric utility service areas
GIS: https://services.arcgis.com/6lCKYNJLvwTXqrmp/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/6lCKYNJLvwTXqrmp/arcgis/rest/services
Washington Department of Fish and Wildlife
Website: https://wdfw.wa.gov
GIS: https://gispublic.dfw.wa.gov/arcgis/rest/services
GIS: https://geodataservices.wdfw.wa.gov/arcgis/rest/services
MapServices/BaseImages_VI/MapServer has good scans of the USGS 7.5 minute
topo maps.
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services.arcgis.com/rcya3vExsaVBGUDp/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/rcya3vExsaVBGUDp/arcgis/rest/services
Washington Department of Health
Website: https://www.doh.wa.gov
GIS: https://fortress.wa.gov/doh/arcgis/arcgis/rest/services
8-12-2023 no tiled data
Washington Department of Natural Resources
Website: https://www.dnr.wa.gov
GIS: https://gis.dnr.wa.gov/site1/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.dnr.wa.gov/site2/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://gis.dnr.wa.gov/site3/rest/services
2-27-2023 no tiled data
WUI
Public_Wildfire/WADNR_PUBLIC_WD_WUI/MapServer
GIS: https://gis-dev.dnr.wa.gov/site1/rest/services
Lots of data on mines, geology, faults.
GIS: https://gis.dnr.wa.gov/image/rest/services
GIS: https://services.arcgis.com/4x406oNViizbGo13/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/4x406oNViizbGo13/arcgis/rest/services
Washington Department of Transportation
Website: https://www.wsdot.wa.gov
GIS: https://wsdot.wa.gov/arcgis/rest/services
Table of contents disabled
GIS: https://www.wsdot.wa.gov/arcgis/rest/services
Table of contents disabled
Traffic cams:  Production/WSDOTTrafficCameras/MapServer
8-12-2023 no tiled data
GIS: https://data.wsdot.wa.gov/arcgis/rest/services
8-12-2023 no tiled data

## Page 432

GIS: https://services.arcgis.com/IYrj3otxNjPsrTRD/ArcGIS/rest/services
8-12-2023 no tiled data
GIS: https://tiles.arcgis.com/tiles/IYrj3otxNjPsrTRD/arcgis/rest/services
Washington Recreation and Conservation Office
Website: https://rco.wa.gov
GIS: https://gismanager.rco.wa.gov/arcgis/rest/services
Includes layers showing city, county, state. federal public land
Good trail layer
8-12-2023 no tiled data
GIS: https://services2.arcgis.com/TGEC20q86HQAeMS6/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/TGEC20q86HQAeMS6/arcgis/rest/services
Washington Utilities and Transportation Commission
Website: https://www.utc.wa.gov
GIS: https://services2.arcgis.com/lXwA5ckdH5etcXUm/ArcGIS/rest/services
Washington State County Road Administration Board (CRAB)
Website: https://www.crab.wa.gov
GIS: New GIS being developed
Washington Office of Financial Management
Website: https://ofm.wa.gov
GIS: https://services.arcgis.com/bCYnGqM4FMTBSjd1/arcgis/rest/services
Washington State Office of Equity
Website: https://equity.wa.gov
GIS: https://services7.arcgis.com/QE0COxD8ToUT6CQN/ArcGIS/rest/services
Washington State Military Department
Website: https://mil.wa.gov
GIS: https://services7.arcgis.com/vUVXhXafpruJFs3l/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/vUVXhXafpruJFs3l/arcgis/rest/services
Washington Office of Supt. of Public Instruction  (K-12 schools)
GIS: https://services5.arcgis.com/q9Lwq3BC8p2H6RLg/ArcGIS/rest/services
GIS: https://services9.arcgis.com/fWunDXKkvCx1CM4b/arcgis/rest/services
Washington various layers
GIS: https://imagery-public.watech.wa.gov/arcgis/rest/services
GIS: https://services.arcgis.com/jsIt88o09Q0r1j8h/ArcGIS/rest/services
Parcel lines:  Current_Parcels/FeatureServer/0
Trails:  WATrails2017_State/FeatureServer/0
GIS: https://tiles.arcgis.com/tiles/jsIt88o09Q0r1j8h/arcgis/rest/services
GIS: https://services2.arcgis.com/WW3T8U6q5EkZ9U3n/arcgis/rest/services
GIS: https://services5.arcgis.com/4LKAHwqnBooVDUlX/arcgis/rest/services

## Page 433

Lots of recreation layers
GIS: https://tiles.arcgis.com/tiles/4LKAHwqnBooVDUlX/arcgis/rest/services
GIS: https://services6.arcgis.com/yIPFYZqx6a8IC4Hk/ArcGIS/rest/services
GIS: https://services6.arcgis.com/eIF8pWUENRGiMcYy/arcgis/rest/services
GIS: https://services8.arcgis.com/rGGrs6HCnw87OFOT/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/rGGrs6HCnw87OFOT/arcgis/rest/services
University of Washington - School of Environmental and Forest Sciences
Website: https://sefs.uw.edu/about
GIS: https://uwbgmaps.sefs.uw.edu/arcgis/rest/services
8-12-2023 no tiled data
Washington State University
GIS: https://services1.arcgis.com/rCcfuAf877pT4w3i/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/rCcfuAf877pT4w3i/arcgis/rest/services
Washington Regional
Regional Open Space Strategy
Website: https://openspacepugetsound.org
SSL problem
GIS: https://services1.arcgis.com/4ZKi1B1zTblbwgWB/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/4ZKi1B1zTblbwgWB/arcgis/rest/services
Puget Sound Partnership
Website: https://www.psp.wa.gov
GIS: https://services7.arcgis.com/iAd79FjHxHKsLP0y/ArcGIS/rest/services
Puget Sound Regional Council
Website: https://www.psrc.org
GIS: https://services6.arcgis.com/GWxg6t7KXELn1thE/ArcGIS/rest/services
Sound Transit
Website: https://www.soundtransit.org
GIS: https://rtamaps2.soundtransit.org/arcgis/rest/services
8-12-2023 no tiled data
GIS: https://rtamaps3.soundtransit.org/arcgis/rest/services
8-12-2023 no tiled data
Spokane Regional Transportation Council
Website: https://srtc.org
GIS: https://services1.arcgis.com/Ub7Rr4y0UspW2NcJ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Ub7Rr4y0UspW2NcJ/arcgis/rest/services
Yakima Valley Council of Governments
Website: https://www.yvcog.us
GIS: __________

## Page 434

Washington County GIS Servers
All counties are listed and have been checked for GIS
Asotin
https://services6.arcgis.com/VsJGTl1jmCYBc0EX/arcgis/rest/servi
ces
Benton
https://services7.arcgis.com/NURlY7V8UHl6XumF/ArcGIS/rest/s
ervices
Benton
https://tiles.arcgis.com/tiles/NURlY7V8UHl6XumF/arcgis/rest/ser
vices
Chelan
https://atlas.co.chelan.wa.us/arcgis/rest/services
Chelan
https://services6.arcgis.com/kL9uP9rflLEjUDsy/arcgis/rest/services
Evacuation areas
/Emergency_Management_Layers_View/FeatureServer/2
Chelan
           https://tiles.arcgis.com/tiles/kL9uP9rflLEjUDsy/arcgis/rest/services
Chelan PUD
https://services1.arcgis.com/3ymEnGydxeYILJzI/arcgis/rest/servic
es
Clallam
https://websrv31.clallamcountywa.gov/server/rest/services
Clallam
https://services8.arcgis.com/noCZ2SM2C0rVag8y/ArcGIS/rest/ser
vices
Clallam
https://tiles.arcgis.com/tiles/noCZ2SM2C0rVag8y/arcgis/rest/servi
ces
Clark
https://www.apps.crab.wa.gov/serverstaging/rest/services
Clark
https://services2.arcgis.com/ylxwjFBdCPBzP16d/arcgis/rest/servic
es
Clark
https://tiles.arcgis.com/tiles/ylxwjFBdCPBzP16d/arcgis/rest/servic
es
Columbia
https://services9.arcgis.com/zq1Ay6bxXC1T1CBk/arcgis/rest/servi
ces
Columbia
https://tiles.arcgis.com/tiles/zq1Ay6bxXC1T1CBk/arcgis/rest/servi
ces
Cowlitz
https://cowlitzgis.net/ccserver/rest/services
Douglas
_ttps://gis.douglascountywa.net/server/rest/services       dead link 1
Douglas
https://services2.arcgis.com/fjst9C4kBtvXuiLQ/ArcGIS/rest/servic
es
Douglas
https://tiles.arcgis.com/tiles/fjst9C4kBtvXuiLQ/arcgis/rest/services
Ferry
https://services8.arcgis.com/BBejpmYP0j5q6NLc/arcgis/rest/servi
ces

## Page 435

Franklin
_ttps://gisportal.franklin.co.franklin.wa.us/arcgis/rest/services
dead link 1
Garfield
https://services5.arcgis.com/1UmAlNNRc6UDVQ4y/arcgis/rest/se
rvices
Grant
https://services2.arcgis.com/hQZvdtFxRzJpMtdS/arcgis/rest/servic
es
Grant
https://tiles.arcgis.com/tiles/hQZvdtFxRzJpMtdS/arcgis/rest/servic
es
Grays Harbor
GIS is not ArcGIS
Island
https://maps.islandcountywa.gov/arcgis/rest/services
Island
https://services6.arcgis.com/Q2crTJYujvn27IJC/ArcGIS/rest/servic
es
Island
           https://tiles.arcgis.com/tiles/Q2crTJYujvn27IJC/arcgis/rest/services
Jefferson
https://gisweb.jeffcowa.us/server/rest/services
Jefferson
https://services3.arcgis.com/RPU019D0wA2T8GMO/ArcGIS/rest/
services
Jefferson
https://tiles.arcgis.com/tiles/RPU019D0wA2T8GMO/arcgis/rest/se
rvices
King
https://gismaps.kingcounty.gov/arcgis/rest/services
aerial    BaseMaps/KingCo_Aerial_Overlay
parcels  Property/KingCo_Parcels/MapServer
Tiled traffic cameras.
RoadAlerts/KingCo_Traffic_Cameras/MapServer
Contour lines: Topo/KingCo_Contours/MapServer
8-14-2023 Has tiled data.  Do a Google search.
site:server_address   “wmts”
King
https://gisdata.kingcounty.gov/arcgis/rest/services
2-27-2023 no tiled data
King
https://gismaps.kingcounty.gov/imagery/rest/services
snow priority roads.   PSAP/PSAP/MapServer/  17, 18
King
https://services.arcgis.com/Ej0PsM5Aw677QF1W/ArcGIS/rest/ser
vices
King
https://tiles.arcgis.com/tiles/Ej0PsM5Aw677QF1W/arcgis/rest/serv
ices
Kitsap
https://ags.kitsapgov.com/arcgis/rest/services
Kitsap
https://secure.kitsappublichealth.org/agsserver/rest/services
Kitsap
https://services6.arcgis.com/qt3UCV9x5kB4CwRA/ArcGIS/rest/se
rvices

## Page 436

Kittitas
https://gis.co.kittitas.wa.us/kcgis/rest/services
Kittitas
https://services.arcgis.com/eSnyVpqwqWBADfzp/arcgis/rest/servi
ces
Kittitas
https://tiles.arcgis.com/tiles/eSnyVpqwqWBADfzp/arcgis/rest/serv
ices
Klickitat
https://geo.gartrellgroup.com/server/rest/services/Klickitat
Lewis
https://arcgis.lewiscountywa.gov/arcgispublic/rest/services
Lincoln
https://services3.arcgis.com/caAn57sZq4ktyly4/arcgis/rest/services
Mason
https://gis.masoncountywa.gov/arcgis/rest/services
Okanogan
GIS is not public
Pacific
GIS is not ArcGIS
Pend Oreille
https://gis.pendoreilleco.org/arcgis/rest/services
Pend Oreille
https://services1.arcgis.com/o3wuEYcU5N00WpI1/ArcGIS/rest/se
rvices
Pend Oreille
https://tiles.arcgis.com/tiles/o3wuEYcU5N00WpI1/arcgis/rest/serv
ices
Pierce
https://services2.arcgis.com/1UvBaQ5y1ubjUPmd/arcgis/rest/servi
ces
Pierce
https://services2.arcgis.com/fBDXdj7Zh91YF2mv/ArcGIS/rest/ser
vices
Transit
Pierce
https://tiles.arcgis.com/tiles/1UvBaQ5y1ubjUPmd/arcgis/rest/servi
ces
San Juan
https://gis.sanjuancountywa.gov/arcgis/rest/services
San Juan
          https://services.arcgis.com/PNkCg7xWnaf90qde/arcgis/rest/services
Skagit
https://gis.skagitcountywa.gov/arcgis/rest/services
Skagit
https://services1.arcgis.com/ipyDbwUQfysOAPQq/ArcGIS/rest/ser
vices
Skagit
https://services3.arcgis.com/egpVHNrUBK5fSrmx/arcgis/rest/servi
ces
Skagit PUD
https://services9.arcgis.com/c4BqPQbwsEpxjyX4/ArcGIS/rest/serv
ices
Skamania
https://services3.arcgis.com/uKh72TYBlxpm42Cm/arcgis/rest/serv
ices
Snohomish
https://gis.snoco.org/scd/rest/services

## Page 437

Snohomish
https://gis.snoco.org/spw/rest/services
Snohomish
https://gis.snoco.org/img/rest/services
aerials
Snohomish
https://services6.arcgis.com/z6WYi9VRHfgwgtyW/ArcGIS/rest/se
rvices
Snohomish
https://tiles.arcgis.com/tiles/z6WYi9VRHfgwgtyW/arcgis/rest/serv
ices
Spokane
https://gismo.spokanecounty.org/arcgis/rest/services
   trails:   Other/MtSpokane_SearchandRescue/MapServer
Spokane
          https://services1.arcgis.com/ozNll27nt9ZtPWOn/arcgis/rest/services
Spokane
          https://tiles.arcgis.com/tiles/ozNll27nt9ZtPWOn/arcgis/rest/services
Spokane
https://services3.arcgis.com/9UdSzuxhN4jGcI9p/ArcGIS/rest/servi
ces
Spokane
          https://tiles.arcgis.com/tiles/9UdSzuxhN4jGcI9p/arcgis/rest/services
Stevens
https://gis.stevenscountywa.gov/server/rest/services
Stevens
           https://services.arcgis.com/6E99CuinVlFZ3R03/arcgis/rest/services
Stevens
https://tiles.arcgis.com/tiles/6E99CuinVlFZ3R03/arcgis/rest/servic
es
Thurston
https://map.co.thurston.wa.us/arcgis/rest/services
Table of contents disabled
Thurston
https://map.co.thurston.wa.us/arcgisimage/rest/services
Thurston
https://services1.arcgis.com/jcAMaQSrhOYmQZ89/ArcGIS/rest/se
rvices
Thurston
https://services7.arcgis.com/hU4WZkHiDpy9rKuq/ArcGIS/rest/ser
vices
Intercity Transit
Wahkiakum
https://services5.arcgis.com/SQaKrZ90pTH1GKNW/arcgis/rest/ser
vices
Wahkiakum
https://tiles.arcgis.com/tiles/SQaKrZ90pTH1GKNW/arcgis/rest/ser
vices
Walla Walla
https://webmap.trueautomation.com/arcgis/rest/services/WallaMap
Search/MapServer
Whatcom
https://gis.whatcomcounty.us/arcgis/rest/services
https://services9.arcgis.com/gV1t8qrYM9zDKq3h/arcgis/rest/servi
ces
Birch Bay Water and Sewer District
Whitman
https://services3.arcgis.com/eoLFybJXLOtInQXJ/arcgis/rest/servic
es
Yakima
https://maps.yakimacounty.us/server/rest/services

## Page 438

Yakima
https://services3.arcgis.com/9Qz94N8Zml9hnG84/arcgis/rest/servi
ces
Also has data for various cities
Yakima
https://tiles.arcgis.com/tiles/9Qz94N8Zml9hnG84/arcgis/rest/servi
ces
Washington City, Town, Village, etc GIS Servers
Airway Heights
https://arcgis.mobile311.com/arcgis/rest/services/Washington/Airw
ayHeightsWA/MapServer
Airway Heights
https://services6.arcgis.com/yrsL3gWPR8ZySnTr/ArcGIS/rest/serv
ices
Anacortes
https://arcgiscoa.cityofanacortes.org/arcgiscoa/rest/services
Arlington
https://gis.arlingtonwa.gov/arcgisserver/rest/services
Arlington
https://services3.arcgis.com/nPsPH23NWoWmXQgb/ArcGIS/rest/
services
Auburn
https://gis.auburnwa.gov/mapping/rest/services
Auburn
           https://services1.arcgis.com/Talr0y9yrNfatLSI/ArcGIS/rest/services
Auburn
https://tiles.arcgis.com/tiles/Talr0y9yrNfatLSI/arcgis/rest/services
Bainbridge Island
https://services5.arcgis.com/0Q6HuHqqcg7Zo8zH/arcgis/rest/servi
ces
Bainbridge Island
https://tiles.arcgis.com/tiles/0Q6HuHqqcg7Zo8zH/arcgis/rest/servi
ces
Bellevue
https://portal-web.bellevuewa.gov/gisext/rest/services
Bellevue
https://gis-web.bellevuewa.gov/gisext/rest/services
Bellevue
https://services1.arcgis.com/EYzEZbDhXZjURPbP/arcgis/rest/serv
ices
Bellevue
https://tiles.arcgis.com/tiles/EYzEZbDhXZjURPbP/arcgis/rest/serv
ices
Bellingham
https://maps.cob.org/arcgis2/rest/services
Bellingham
https://maps.cob.org/arcgis3/rest/services
Bellingham
https://maps.cob.org/arcgis4/rest/services
Blaine
https://services6.arcgis.com/ZGYHIuOAkxkv8laH/arcgis/rest/servi
ces
Bothell
https://gisweb.bothellwa.gov/server/rest/services
Bothell
https://services1.arcgis.com/yWC3RwGqrp7oLKhO/ArcGIS/rest/s
ervices
Bothell
https://tiles.arcgis.com/tiles/yWC3RwGqrp7oLKhO/arcgis/rest/ser
vices

## Page 439

Bremerton
https://imagegis.bremertonwa.gov/arcgis/rest/services
Burien
https://gisdev.burienwa.gov/serverdev/rest/services
Burien
https://services6.arcgis.com/pZ4CUxkTrr0NFJXS/ArcGIS/rest/ser
vices
Burien
https://tiles.arcgis.com/tiles/pZ4CUxkTrr0NFJXS/arcgis/rest/servi
ces
Centralia
__________
Chelan
https://services1.arcgis.com/cQqftPrF7IjnPbra/arcgis/rest/services
Chelan
https://tiles.arcgis.com/tiles/cQqftPrF7IjnPbra/arcgis/rest/services
Cheney
https://services.arcgis.com/yP5WvH3YqutU0LDh/arcgis/rest/servi
ces
Clark
https://gis.clark.wa.gov/arcgisfed/rest/services
Clyde Hill
___________
Collage Place
https://services8.arcgis.com/1PhDbUrDTOM4lipn/arcgis/rest/servi
ces
Collage Place
https://tiles.arcgis.com/tiles/1PhDbUrDTOM4lipn/arcgis/rest/servi
ces
Covington
https://maps.covingtonwa.gov/arcgis/rest/services
Des Moines
https://maps.desmoineswa.gov/dmgis/rest/services
Table of contents disabled
Edgewood
           https://services.arcgis.com/Vf718JZV3goJ8GJT/arcgis/rest/services
Edgewood
https://tiles.arcgis.com/tiles/Vf718JZV3goJ8GJT/arcgis/rest/servic
es
Edmonds
https://maps.edmondswa.gov/gis/rest/services
Everett
https://gismaps.everettwa.gov/manarcgis/rest/services
Federal Way
https://services7.arcgis.com/nNFRPD700OKIXF3J/ArcGIS/rest/se
rvices
Ferndale
https://arcgis.cityofferndale.org/server/rest/services
Fife
https://services6.arcgis.com/TFkOPx3Uro4KZkmF/arcgis/rest/serv
ices

## Page 440

Issaquah
https://apps.issaquahwa.gov/server/rest/services
Issaquah
https://services6.arcgis.com/emvaTQRwXeOg8U36/ArcGIS/rest/s
ervices
Kelso
See Cowlitz County
Kenmore
https://gwa.kenmorewa.gov/arcgis/rest/services
Kenmore
           https://services7.arcgis.com/Yj2o7NF3597r0ar6/arcgis/rest/services
Kennewick
https://maps.ci.kennewick.wa.us/server/rest/services
Kennewick
          https://services5.arcgis.com/Pj4k0Gr9T183FLSI/arcgis/rest/services
Kennewick
           https://tiles.arcgis.com/tiles/Pj4k0Gr9T183FLSI/arcgis/rest/services
Kent
https://services3.arcgis.com/AME2ELqJ7UG0JjrU/ArcGIS/rest/ser
vices
Kent
https://tiles.arcgis.com/tiles/AME2ELqJ7UG0JjrU/arcgis/rest/servi
ces
Kennewick
https://maps.ci.kennewick.wa.us/server/rest/services
Kirkland
https://maps.kirklandwa.gov/host/rest/services
Kirkland
https://maps.kirklandwa.gov/appx/rest/services
Table of contents disabled
Kirkland
https://services2.arcgis.com/loGMwowmR0OPlOQb/ArcGIS/rest/s
ervices
Kirkland
https://tiles.arcgis.com/tiles/loGMwowmR0OPlOQb/arcgis/rest/ser
vices
Lake Stevens
https://services.arcgis.com/gr7sYYW0YAciUIIG/arcgis/rest/servic
es
Lake Stevens
https://tiles.arcgis.com/tiles/gr7sYYW0YAciUIIG/arcgis/rest/servi
ces
Lakewood
https://services3.arcgis.com/DP7cu0aLwEbmib3H/arcgis/rest/servi
ces
Lakewood
https://services7.arcgis.com/SQ8ST1rqgNxTciZJ/ArcGIS/rest/servi
ces         Water district
Lynnwood
https://gis.lynnwoodwa.gov/gis_server/rest/services
Lynnwood
https://services2.arcgis.com/W2b0jYHWnOivta60/arcgis/rest/servi
ces
Lynnwood
https://tiles.arcgis.com/tiles/W2b0jYHWnOivta60/arcgis/rest/servi
ces
Mercer Island
https://chgis1.mercergov.org/arcgis/rest/services

## Page 441

Mercer Island
https://services3.arcgis.com/bJ3kuL5CJAvqKrUn/ArcGIS/rest/serv
ices
Moses Lake
https://arcgis.cityofml.com/server/rest/services
Moses Lake
https://services3.arcgis.com/EhVTEJ0Ki1rmDSHF/ArcGIS/rest/ser
vices
Moses Lake
https://tiles.arcgis.com/tiles/EhVTEJ0Ki1rmDSHF/arcgis/rest/servi
ces
Mount Vernon
https://services7.arcgis.com/6P1T5eIC5rmIemSw/arcgis/rest/servic
es
Mukilteo
https://gis.mukilteowa.gov/arcgis/rest/services
Mukilteo
http://gis.ci.mukilteo.wa.us/arcgis/rest/services
not https
Mukilteo
https://services2.arcgis.com/csauTsCJzwR6Erxa/ArcGIS/rest/servi
ces
Mukilteo
           https://tiles.arcgis.com/tiles/csauTsCJzwR6Erxa/arcgis/rest/services
Newcastle
https://services6.arcgis.com/kvG4x0h4KLP0c8nr/arcgis/rest/servic
es
Newcastle
https://tiles.arcgis.com/tiles/kvG4x0h4KLP0c8nr/arcgis/rest/servic
es

Oak Harbor
https://services9.arcgis.com/SVlf413Qqlzv09Uo/ArcGIS/rest/servi
ces

Oak Harbor
           https://tiles.arcgis.com/tiles/SVlf413Qqlzv09Uo/arcgis/rest/services
Olympia
https://gis.olympiawa.gov/arcgis/rest/services
Pacific
https://arcgis.mobile311.com/arcgis/rest/services/Washington/City
OfPacificWA/MapServer
Pasco
https://services5.arcgis.com/Mrjxd32WJFxUIHrM/arcgis/rest/servi
ces
Pasco
https://tiles.arcgis.com/tiles/Mrjxd32WJFxUIHrM/arcgis/rest/servi
ces
Port Angeles
https://gis.cityofpa.us/legacy/rest/services
Port Angeles
https://services6.arcgis.com/4A9OnENzvPN6Lx02/ArcGIS/rest/ser
vices
Prosser
https://services9.arcgis.com/XsJlQdGk2nRJazuv/ArcGIS/rest/servi
ces
Pullman
https://gis.pullman-wa.gov/arcgis/rest/services

## Page 442

Pullman
https://services7.arcgis.com/Tg1NKl9jSAarBGJc/ArcGIS/rest/serv
ices
Pullman
https://tiles.arcgis.com/tiles/Tg1NKl9jSAarBGJc/arcgis/rest/servic
es
Puyallup
https://gis.puyallupwa.gov/arcgis/rest/services
Puyallup
https://services8.arcgis.com/5K6vnOH0GkPyJs6A/arcgis/rest/servi
ces
Redmond
https://gis.redmond.gov/arcgis/rest/services
Redmond
https://maps.redmond.gov/server/rest/services
Renton
https://gismaps.rentonwa.gov/as03/rest/services
Renton
https://services1.arcgis.com/slSNGMtvwLJi21om/arcgis/rest/servi
ces
Renton
https://tiles.arcgis.com/tiles/slSNGMtvwLJi21om/arcgis/rest/servic
es
Richland
https://imaps.ci.richland.wa.us/arcgis1081/rest/services
Richland
https://services3.arcgis.com/5g4JcCVJwbhPOszb/ArcGIS/rest/serv
ices
Richland
https://tiles.arcgis.com/tiles/5g4JcCVJwbhPOszb/arcgis/rest/servic
es
Sammamish
https://maps.sammamishwa.gov/arcgis/rest/services
Seatac
https://data.seatacwa.gov/arcgis/rest/services
Table of contents disabled
Seatac
https://services3.arcgis.com/DLryYCwhA8W7Jq7Q/arcgis/rest/ser
vices
Seattle
https://gisdata.seattle.gov/server/rest/services
2-27-2023 no tiled data
Seattle
https://gis.seattle.gov/image/rest/services
Seattle
https://services.arcgis.com/ZOyb2t4B0UYuYNYH/arcgis/rest/serv
ices
Seattle
https://tiles.arcgis.com/tiles/ZOyb2t4B0UYuYNYH/arcgis/rest/ser
vices
Shelton
See Mason County
Shoreline
https://gis.shorelinewa.gov/server/rest/services
Spokane
https://services.spokanegis.org/arcgis/rest/services
Spokane
https://services.arcgis.com/3PDwyTturHqnGCu0/arcgis/rest/servic
es

## Page 443

Spokane
https://tiles.arcgis.com/tiles/3PDwyTturHqnGCu0/arcgis/rest/servi
ces
Spokane Valley
https://arcgis.spokanevalley.org/arcgis/rest/services
Sumner
https://services5.arcgis.com/i22ctDcYlAxooCJX/arcgis/rest/servic
es
Sumner
https://arcgis.mobile311.com/arcgis/rest/services/Washington/Sum
nerWAM311/MapServer
Sumner
https://arcgis.mobile311.com/arcgis/rest/services/Washington/Sum
nerWA/MapServer
Tacoma
_ttps://gis.cityoftacoma.org/arcgis/rest/services
     dead link 1
_ttps://imagery.cityoftacoma.org/arcgis/rest/services     dead link 1
Tacoma
https://services1.arcgis.com/WGzzp37bqYMLyzDR/ArcGIS/rest/s
ervices
Tacoma
https://tiles.arcgis.com/tiles/WGzzp37bqYMLyzDR/arcgis/rest/ser
vices
Tacoma
https://services3.arcgis.com/SCwJH1pD8WSn5T5y/ArcGIS/rest/se
rvices
Tukwila
https://services7.arcgis.com/ttErFEyWkCDr9b67/arcgis/rest/servic
es
Tukwila
https://tiles.arcgis.com/tiles/ttErFEyWkCDr9b67/arcgis/rest/servic
es
Tumwater
https://services6.arcgis.com/ovypB8ighP2NPfFE/arcgis/rest/servic
es
Tumwater
          https://tiles.arcgis.com/tiles/ovypB8ighP2NPfFE/arcgis/rest/services
Vancouver
https://gis.cityofvancouver.us/arcgis/rest/services
Vancouver
https://services.arcgis.com/oNvpY90qsPDizwkN/arcgis/rest/servic
es
Vancouver
https://tiles.arcgis.com/tiles/oNvpY90qsPDizwkN/arcgis/rest/servi
ces
Walla Walla
https://gis2.ci.walla-walla.wa.us/arcgis/rest/services
Wenatchee
https://maps.wenatcheewa.gov/server/rest/services
Woodinville
https://services8.arcgis.com/OQPRCxZXJewOd2xW/ArcGIS/rest/
services
Woodinville
https://tiles.arcgis.com/tiles/OQPRCxZXJewOd2xW/arcgis/rest/ser
vices

## Page 444

Yakima
https://gis.yakimawa.gov/arcgis/rest/services
Table of contents disabled
Yakima
https://gis.yakimawa.gov/geoevent/rest/services
Yakima
https://services5.arcgis.com/drBwGNA3YMS2QPJd/ArcGIS/rest/s
ervices
West Virginia State GIS Servers
West Virginia GIS Data Clearinghouse
Website: https://wvgis.wvu.edu/data/data.php
West Virginia Department of Environmental Protection
Website: https://dep.wv.gov/Pages/default.aspx
GIS: https://tagis.dep.wv.gov/arcgis/rest/services
8-12-2023 No tiled data
GIS: https://tagis.dep.wv.gov/image/rest/services
GIS: https://services6.arcgis.com/3iZGO9lgMHNG1V3R/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/3iZGO9lgMHNG1V3R/arcgis/rest/services
West Virginia Department of Transportation
Website: https://transportation.wv.gov/Pages/default.aspx
GIS: https://gis.transportation.wv.gov/arcgis/rest/services
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://services2.arcgis.com/xLpB90lOmCXYDAWo/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/xLpB90lOmCXYDAWo/arcgis/rest/services
West Virginia Office of Environmental Health Services
Website: https://www.wvdhhr.org/oehs
GIS: https://oehsportal.wvdhhr.org/arcgis/rest/services
8-12-2023 No tiled data
West Virginia Statewide Addressing
Website: https://emd.wv.gov/Operations/pages/statewide-addressing-and-mapping.aspx
GIS: https://wvsams.mapwv.org/arcgis/rest/services
8-12-2023 No tiled data
West Virginia University GIS Technical Center
Website: https://wvgis.wvu.edu
GIS: https://services.wvgis.wvu.edu/ArcGIS/rest/services
Parcel lines:  Planning_Cadastre/WV_Parcels/MapServer/0
8-12-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
WV Geological and Economic Survey
Website: https://www.wvgs.wvnet.edu
GIS: https://atlas.wvgs.wvnet.edu/arcgis/rest/services
8-12-2023 No tiled data

## Page 445

West Virginia Broadband Enhancement Council
Website: https://broadband.wv.gov
GIS: https://services8.arcgis.com/qs2IqinxpjidSPO1/ArcGIS/rest/services
West Virginia various layers
https://services7.arcgis.com/IRwObajcV9nxQIrC/arcgis/rest/services
Parcel data for various counties
https://tiles.arcgis.com/tiles/IRwObajcV9nxQIrC/arcgis/rest/services
West Virginia Regional
Region 2 Planning & Development Council
Website: https://region2pdc.org
GIS: https://services9.arcgis.com/HnL2SUtoTunnQDmX/ArcGIS/rest/services
Region 3 Planning & Development Council
Website: https://wvregion3.org
GIS: https://services9.arcgis.com/fVcw4GvGXZ2a5g3r/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/fVcw4GvGXZ2a5g3r/arcgis/rest/services
Region 4 Planning & Development Council
Website: https://reg4wv.org
GIS: https://services8.arcgis.com/aPNo3KjV6fgrbzfN/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/aPNo3KjV6fgrbzfN/arcgis/rest/services
West Virginia County GIS Servers
Barbour
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/BarbourService_/FeatureServer
Go to the top and search for ‘Barbour’
Berkeley
https://maps.berkeleywv.org/bclive/rest/services
Cabell
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/CabellWV_Service/FeatureServer
Go to the top and search for ‘Cabell’
Doddridge
http://www.landmarkgeospatial.com/ArcGIS/rest/services/Doddrid
ge
not https
Fayette
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Fayette_Service/FeatureServer
Go to the top and search for ‘Fayette’
Gilmer
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/GilmerVoting/FeatureServer
Go to the top and search for ‘Gilmer’

## Page 446

Grant
WMS server
Greenbrier
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Greenbrier_Addressing_Service/FeatureServer
Go to the top and search for ‘Greenbrier’
Harrison
https://gismaps.harrisoncountywv.com/server/rest/services
Hampshire
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/HampshireMapService/FeatureServer
Go to the top and search for ‘Hampshire’
Hancock
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/HancockWV_Service/FeatureServer
Go to the top and search for ‘Hancock’
Hardy
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/HardyMapService/FeatureServer
Go to the top and search for ‘Hardy’
Jefferson
https://jcarcgis.wvassessor.com:6443/arcgis/rest/services
Kanawha
https://kanawhacountyassessorgis.com/server/rest/services
Lewis
See ‘West Virginia various layers’ (above)
Lincoln
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Lincoln_WV_Service/FeatureServer
Go to the top and search for ‘Lincoln’
Marshall
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/MarshallWV_Service/FeatureServer
Go to the top and search for ‘Marshall’
Mercer
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Mercer_AGOL/FeatureServer
Go to the top and search for ‘Mercer’
Mineral
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Mineral_Service/FeatureServer
Go to the top and search for ‘Mineral’
Monongalia
https://ags.agdmaps.com/arcgis/rest/services/MonongaliaWV/Map
Server
Monongalia
https://services3.arcgis.com/MGBEQZtkTlJin8UB/ArcGIS/rest/ser
vices

## Page 447

Monroe
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/MonroeFieldService/FeatureServer
Go to the top and search for ‘Monroe’
Morgan
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/MorganService/FeatureServer
Go to the top and search for ‘Morgan’
Ohio
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/OhioService/FeatureServer
Go to the top and search for ‘Ohio’
Pendleton
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/PendletonService2019/FeatureServer
Go to the top and search for ‘Pendleton’
Preston
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/PrestonWV_Service_NEW/FeatureServer
Go to the top and search for ‘Preston’
Putnam
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/re
st/services/PutnamPrecintsFInal/FeatureServer
Go to the top and search for ‘Putnam’
Also a WMS server
Raleigh
https://services.arcgis.com/7qDWTH3pTiLOFaZS/arcgis/rest/servi
ces
Randolph
See ‘West Virginia various layers’ (above)
Summers
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/SummersWV_Service/FeatureServer
Go to the top and search for ‘Summers’
Taylor
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Taylor_TabletService/FeatureServer
Go to the top and search for ‘Taylor’
Tyler
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Tyler_911/FeatureServer
Go to the top and search for ‘Tyler’
Upshur
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Upshur_Web_Service/FeatureServer
Go to the top and search for ‘Upshur’

## Page 448

Wayne
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/WayneWV_Service/FeatureServer
Go to the top and search for ‘Wayne’
Webster
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/WebsterWV_Service/FeatureServer
Go to the top and search for ‘Webster’
Wetzel
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/Wetzel911_Service/FeatureServer
Go to the top and search for ‘Wetzel’
Wirt
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/WirtService/FeatureServer
Go to the top and search for ‘Wirt’
Wood
https://services3.arcgis.com/nJbIFHiSnaX0z0hS/ArcGIS/rest/servi
ces/WoodWV/FeatureServer
Go to the top and search for ‘Wood’
Wyoming
        See ‘West Virginia various layers’ (above)
West Virginia City, Town, Village, etc GIS Servers
Berkeley
https://maps.berkeleywv.org/bclive/rest/services
Martinsburg
https://services6.arcgis.com/deAS8KeQ1ASFd1S2/ArcGIS/rest/ser
vices
Martinsburg
https://tiles.arcgis.com/tiles/deAS8KeQ1ASFd1S2/arcgis/rest/servi
ces
Morgantown
https://morgantownwv.maps.arcgis.com
Morgantown
          https://services7.arcgis.com/lE5mQkgxehcTjzKf/arcgis/rest/services
Morgantown
          https://tiles.arcgis.com/tiles/lE5mQkgxehcTjzKf/arcgis/rest/services
Oak Hill
https://cityoh.maps.arcgis.com
Oak Hill
https://services5.arcgis.com/BDFOlyqRRLqzSDEj/ArcGIS/rest/ser
vices
Oak Hill
https://tiles.arcgis.com/tiles/BDFOlyqRRLqzSDEj/arcgis/rest/servi
ces
Wisconsin State GIS Servers
Wisconsin Emergency Management
Website: https://wem.wi.gov

## Page 449

GIS: https://services2.arcgis.com/m4ifbfJVkN6lFRO3/ArcGIS/rest/services
GIS: https://services3.arcgis.com/GoOAGCoqFEhZEh7f/ArcGIS/rest/services
Office of Emergency Communications
Wisconsin Department of Agriculture, Trade and Consumer Protection
Website: https://datcp.wi.gov/Pages/Homepage.aspx
GIS: https://datcpgis.wi.gov/arcgis/rest/services
Wisconsin Department of Health Services
Website: https://www.dhs.wisconsin.gov
GIS: https://dhsgis.wi.gov/server/rest/services
GIS: https://services1.arcgis.com/ISZ89Z51ft1G16OK/ArcGIS/rest/services
Wisconsin Department of Military Affairs
Website: https://dma.wi.gov
GIS: https://widmamaps.us/arcgisimage/rest/services
8-13-2023 No tiled data
Wisconsin Department of Natural Resources
Website: https://dnr.wisconsin.gov
Website: https://data-wi-dnr.opendata.arcgis.com
Open data
Data portal: https://data-wi-dnr.opendata.arcgis.com
GIS: https://dnrmaps.wi.gov/arcgis/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
GIS: https://dnrmaps.wi.gov/arcgis2/rest/services
GIS: https://dnrmaps.wi.gov/arcgis_image/rest/services
8-13-2023 No tiled data
GIS: https://dnrmaps.wi.gov/arcgis_image/rest/services
8-13-2023 No tiled data
GIS: https://uadnrmaps.wi.gov/arcgis/rest/services
GIS: https://uadnrmaps.wi.gov/arcgis2/rest/services
Wisconsin Office of Outdoor Recreation
Website: https://outdoorrecreation.wi.gov/Pages/home.aspx
GIS: https://services5.arcgis.com/83GPubpIPhmSrWRQ/ArcGIS/rest/services
Wisconsin Department of Transportation
Website: https://wisconsindot.gov/Pages/home.aspx
GIS: https://services5.arcgis.com/0pgGLzT0Nh7FVjon/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/0pgGLzT0Nh7FVjon/arcgis/rest/services
GIS: https://services8.arcgis.com/o4NJgD3NfeHnWy06/ArcGIS/rest/services
Wisconsin State Legislature
Website: https://legis.wisconsin.gov
GIS: https://mapservices.legis.wisconsin.gov/arcgis/rest/services
Parcel lines:  WLIP_V7/V7_Parcels/MapServer/0

## Page 450

8-13-2023 No tiled data
GIS: https://services1.arcgis.com/FDsAtKBk8Hy4cAH0/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/FDsAtKBk8Hy4cAH0/arcgis/rest/services
Public Service Commission of Wisconsin
Website: https://psc.wi.gov/Pages/Home.aspx
GIS: https://maps.psc.wi.gov/server/rest/services
Wisconsin Geological and Natural History Survey
Website: https://home.wgnhs.wisc.edu
GIS: https://services5.arcgis.com/hYFYGk4BynrIaicK/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/hYFYGk4BynrIaicK/arcgis/rest/services
Wisconsin Historical Society
Website: https://www.wisconsinhistory.org
GIS: _ttps://gis.wisconsinhistory.org:6443/arcgis/rest/services
dead link 3
8-13-2023 No tiled data
University of Wisconsin
Website: https://uwm.edu/cgis
GIS: https://webgis.uwm.edu/arcgisuwm/rest/services
8-13-2023 Has tiled data.  Do a Google search.  site:server_address   “wmts”
Wisconsin various layers
GIS: https://services5.arcgis.com/Ul9AyFFeFTjf08DW/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Ul9AyFFeFTjf08DW/arcgis/rest/services
Wisconsin Regional
Fox-Wolf Watershed Alliance
GIS: https://services6.arcgis.com/HOfcuGaO8g9pAEYZ/ArcGIS/rest/services
Bay-Lake Regional Planning Commission
Website: https://baylakerpc.org
GIS: https://services6.arcgis.com/LERb7fGqsOTCtM9z/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/LERb7fGqsOTCtM9z/arcgis/rest/services
Northwest Regional Planning Commission
Website: https://www.nwrpc.com
GIS: _ttp://nwrpcmaps.nwrpc.com/wahost/rest/services
dead link 3
8-13-2023 No tiled data
East Central Regional Planning Commission
Website: https://www.ecwrpc.org
GIS: https://services1.arcgis.com/Osi6nedbad6tbPn5/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Osi6nedbad6tbPn5/arcgis/rest/services

## Page 451

Capital Area Regional Planning Commission
Website: https://www.capitalarearpc.org
GIS: https://services1.arcgis.com/4NZ4Ghri2AQmNOuO/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/4NZ4Ghri2AQmNOuO/arcgis/rest/services
Wisconsin County GIS Servers
As of 12-30-2019 all Wisconsin counties have been checked for a public-facing GIS server.  All
counties not listed below fall into one of the following categories.
1.
County ArcGIS server is not public-facing.  Login credentials are required.
2.
County GIS is hosted on some other kind of GIS server (not ArcGIS and not WMS) that
cannot be accessed directly by GISsurfer.
3.
County has no GIS.
Some counties that do not have an ArcGIS server do have a WMS server.  However, usually
those WMS servers just have a few data layers and most of those layers are aerial photos.
Adams
https://services5.arcgis.com/cmcEK45KcVMmaCd7/arcgis/rest/ser
vices
Adams
https://tiles.arcgis.com/tiles/cmcEK45KcVMmaCd7/arcgis/rest/ser
vices
Ashland
https://gis.ashlandcountywi.gov/arcgis/rest/services
Ashland
https://services8.arcgis.com/QlEvoqmtm2DnG9gw/ArcGIS/rest/ser
vices
Ashland
https://tiles.arcgis.com/tiles/QlEvoqmtm2DnG9gw/arcgis/rest/servi
ces
Barron
Schneider Geospatial - ArcGIS server address is not public
Bayfield
https://maps.bayfieldcounty.wi.gov/arcgis/rest/services
Brown
https://gis.browncountywi.gov/arcgis/rest/services
Buffalo
https://services2.arcgis.com/4fskj6X2QqYEBVyr/ArcGIS/rest/serv
ices
Burnett
Schneider Geospatial - ArcGIS server address is not public
Calumet
https://calmaps.co.calumet.wi.us/server/rest/services
Calumet
https://services6.arcgis.com/gI7hlABYSIIozaRg/ArcGIS/rest/servi
ces
Calumet
           https://tiles.arcgis.com/tiles/gI7hlABYSIIozaRg/arcgis/rest/services
Chippewa
WMS server.

## Page 452

Clark
WMS server.
Columbia
https://lrs.co.columbia.wi.us/server/rest/services
Columbia
https://services3.arcgis.com/MKZTaVIv7NykZYTn/arcgis/rest/ser
vices
Table of contents hidden by javascript
Crawford
WMS server.
Dane
https://elb.ags.ruekert-mielke.com/arcgis/rest/services/DaneCo
Dane
https://services6.arcgis.com/Tu5JcmtrRRLVaRlf/ArcGIS/rest/servi
ces
Dane
https://dcimapapps.countyofdane.com/arcgissrv/rest/services
Dodge
https://geo2.co.dodge.wi.us/arcgis/rest/services
Dodge
https://services5.arcgis.com/WoH0haFujOX8jVNs/ArcGIS/rest/ser
vices
Door
https://elb.ags.ruekert-mielke.com/arcgis/rest/services/DoorCounty
Douglas
WMS server.
Dunn
WMS server.
Eau Claire
https://gis.co.eau-claire.wi.us/agsserver/rest/services
Table of contents disabled
Fond du Lac
https://gisweb.fdlco.wi.gov/server/rest/services
Fond du Lac
https://services3.arcgis.com/7YXkvZxnb69oxbTb/ArcGIS/rest/ser
vices
Fond du Lac
https://services5.arcgis.com/PwbtiIod8IBSgKGS/ArcGIS/rest/servi
ces
Forest
WMS server.
Grant
https://gcarcgis.co.grant.wi.gov/server/rest/services
Green
https://services5.arcgis.com/pkUtXVHrGelPAY8k/arcgis/rest/servi
ces
Green Lake
https://services2.arcgis.com/rOcU2BSg8NccU249/ArcGIS/rest/ser
vices
Green Lake
https://tiles.arcgis.com/tiles/rOcU2BSg8NccU249/arcgis/rest/servi
ces
Hudson
https://services5.arcgis.com/BHiA4BaB0lvyaF6R/arcgis/rest/servic
es

## Page 453

Hudson
https://tiles.arcgis.com/tiles/BHiA4BaB0lvyaF6R/arcgis/rest/servic
es
Iron
https://services1.arcgis.com/XNW34unDaz7i1bfP/arcgis/rest/servi
ces
Jackson
WMS server.
Jefferson
https://jeffarcgis.jeffersoncountywi.gov/arcgis/rest/services
Juneau
https://gismap.co.juneau.wi.us/server/rest/services
Kenosha
https://mapping.kenoshacountywi.gov/server/rest/services
Kenosha
https://mapping.kenoshacountywi.gov/image/rest/services
Kenosha
https://services1.arcgis.com/G9PTZYkfeC1onwUV/ArcGIS/rest/se
rvices
Kenosha
https://tiles.arcgis.com/tiles/G9PTZYkfeC1onwUV/arcgis/rest/serv
ices
Kewaunee
https://services6.arcgis.com/OVykjebCTL9ZTdn8/ArcGIS/rest/ser
vices
Kewaunee
https://tiles.arcgis.com/tiles/OVykjebCTL9ZTdn8/arcgis/rest/servi
ces
La Crosse
https://gis.lacrossecounty.org/gisserver/rest/services
La Crosse
https://gis1.cityoflacrosse.org/laxgis1/rest/services
La Crosse
https://services.arcgis.com/YTojcvpJ9GpgYxjF/arcgis/rest/services
La Crosse
          https://tiles.arcgis.com/tiles/YTojcvpJ9GpgYxjF/arcgis/rest/services
La Crosse
https://services5.arcgis.com/vwNkSCPYyA8kVRT7/arcgis/rest/ser
vices
Lafayette
https://gis.lafayettecountywi.org/arcgis/rest/services
Langlade
WMS server.
Lincoln
https://maps.co.lincoln.wi.us/arcgis/rest/services
Manitowoc
https://manitowocmaps.info/arcgis/rest/services
Marathon
https://gis2.co.marathon.wi.us/arcgis/rest/services
Marquette
https://webportal.co.marquette.wi.us/publicags/rest/services
Milwaukee
https://lio.milwaukeecountywi.gov/arcgis/rest/services
Milwaukee
https://lio.milwaukeecountywi.gov/imagery/rest/services
Milwaukee
https://milwaukeemaps.milwaukee.gov/arcgis/rest/services

## Page 454

Milwaukee
https://services1.arcgis.com/5ly0cVV70qsN8Soc/ArcGIS/rest/servi
ces
Milwaukee
          https://tiles.arcgis.com/tiles/5ly0cVV70qsN8Soc/arcgis/rest/services
Milwaukee
https://services1.arcgis.com/SuEt4jqH31FZKNYY/arcgis/rest/servi
ces
Metropolitan Sewerage District
Milwaukee
https://tiles.arcgis.com/tiles/SuEt4jqH31FZKNYY/arcgis/rest/servi
ces
Milwaukee
https://services2.arcgis.com/s1wgJQKbKJihhhaT/arcgis/rest/servic
es
Milwaukee
https://tiles.arcgis.com/tiles/s1wgJQKbKJihhhaT/arcgis/rest/servic
es
Monroe
WMS server.
Oconto
https://oc17maps.co.oconto.wi.us/arcgis/rest/services
Oneida
https://gis.co.oneida.wi.us/arcgis/rest/services
Outagamie
https://gis.outagamie.org/arcgis/rest/services
Outagamie
https://services.arcgis.com/VJeP6MUQzbTKwSpv/arcgis/rest/servi
ces
Outagamie
https://tiles.arcgis.com/tiles/VJeP6MUQzbTKwSpv/arcgis/rest/ser
vices
Ozaukee
https://gis2.co.ozaukee.wi.us/arcgis/rest/services
Pepin
https://gis.co.pepin.wi.us/arcgis/rest/services
Pepin
https://services3.arcgis.com/MQWdWjYsCvF5w01v/ArcGIS/rest/s
ervices
Pepin
https://tiles.arcgis.com/tiles/MQWdWjYsCvF5w01v/arcgis/rest/ser
vices
Pierce
https://gis.co.pierce.wi.us/arcgis/rest/services
Pierce
https://services3.arcgis.com/dSlsxEMSX5MkNRyf/ArcGIS/rest/ser
vices
Polk
https://services8.arcgis.com/2RIFco0Rk0YlWKga/arcgis/rest/servi
ces
Portage
https://gisinfo.co.portage.wi.gov/server/rest/services
Portage
https://services6.arcgis.com/xvAbcCjMMQaESVE2/ArcGIS/rest/s
ervices
Price
WMS server.
Racine
https://gis.cityofracine.org/arcgis/rest/services

## Page 455

Racine
https://arcgis.racinecounty.com/arcgis/rest/services
Racine
https://services1.arcgis.com/z1oAk3W6cWVD8swZ/ArcGIS/rest/s
ervices
Racine
https://tiles.arcgis.com/tiles/z1oAk3W6cWVD8swZ/arcgis/rest/ser
vices
Racine
https://services3.arcgis.com/wPrvwb4qM5Yocx5m/ArcGIS/rest/se
rvices
water utility
Racine
https://services5.arcgis.com/WgCOhpTBP3tb7eDk/arcgis/rest/serv
ices
Racine
https://tiles.arcgis.com/tiles/WgCOhpTBP3tb7eDk/arcgis/rest/servi
ces
Richland
https://gis.co.richland.wi.us/arcgis/rest/services
Rock
https://rockgis.co.rock.wi.us:8443/rockpub/rest/services
Rock
https://services3.arcgis.com/iP3EkckmBHOMrtt5/ArcGIS/rest/serv
ices
Rock
https://tiles.arcgis.com/tiles/iP3EkckmBHOMrtt5/arcgis/rest/servic
es
Rusk
WMS server.
Sauk
https://gis.co.sauk.wi.us/arcgis/rest/services
Sauk
https://services.arcgis.com/iwDlR6c2PKIpwnf7/arcgis/rest/services
Sauk
https://services3.arcgis.com/uPJ8ipjmRGTGfF02/ArcGIS/rest/serv
ices    Lake Delton area Public Works & Water Utility
Sauk
https://tiles.arcgis.com/tiles/uPJ8ipjmRGTGfF02/arcgis/rest/servic
es
Sawyer
https://services7.arcgis.com/q3CBvv2nu27WiO0o/arcgis/rest/servi
ces
Sawyer
Also a WMS server
Shawano
https://maps.co.shawano.wi.us/server/rest/services
Sheboygan
https://services3.arcgis.com/lZtNcxj8HI3jnkkl/arcgis/rest/services
Sheboygan
https://tiles.arcgis.com/tiles/lZtNcxj8HI3jnkkl/arcgis/rest/services
St Croix
https://services1.arcgis.com/HuQMFGE1RTLjFtYd/ArcGIS/rest/se
rvices
St Croix
https://tiles.arcgis.com/tiles/HuQMFGE1RTLjFtYd/arcgis/rest/serv
ices
Taylor
WMS server.
Trempealeau
Schneider Geospatial - ArcGIS server address is not public

## Page 456

Vernon
_ttps://apps.vernoncounty.org/server/rest/services
dead link 1
Vilas
https://maps.vilascountywi.gov/vilasgis/rest/services
Vilas
https://services1.arcgis.com/EpBsZtekrgiFz19U/ArcGIS/rest/servic
es
Walworth
https://gisinfo.co.walworth.wi.us/arcgis/rest/services
Walworth
https://services1.arcgis.com/k7zLk7Ef9KUrRdlo/arcgis/rest/servic
es
Walworth
          https://tiles.arcgis.com/tiles/k7zLk7Ef9KUrRdlo/arcgis/rest/services
Washburn
WMS server.
Washington
https://maps.washcowisco.gov/server/rest/services
Washington
https://services.arcgis.com/GyNseLhoRPXwnhWP/arcgis/rest/servi
ces
Washington
https://tiles.arcgis.com/tiles/GyNseLhoRPXwnhWP/arcgis/rest/ser
vices
Waukesha
https://gis.waukeshacounty.gov/host/rest/services
Waukesha
https://is.waukesha-wi.gov/server/rest/services
Waukesha
https://gis.waukeshacounty.gov/host/rest/services
Waukesha
https://services.arcgis.com/5mNcDbMaBDRgBsIc/arcgis/rest/servi
ces
Waukesha
https://tiles.arcgis.com/tiles/5mNcDbMaBDRgBsIc/arcgis/rest/serv
ices
Waupaca
https://public1.co.waupaca.wi.us/arcgis/rest/services
Waupaca
https://services3.arcgis.com/7eEEBGPmOQcC1gAa/ArcGIS/rest/s
ervices
Waupaca
https://tiles.arcgis.com/tiles/7eEEBGPmOQcC1gAa/arcgis/rest/ser
vices
Waushara
https://gis.co.waushara.wi.us/arcgis/rest/services
Waushara
https://services.arcgis.com/VHAfuDfA8BDwzLtL/arcgis/rest/servi
ces
Winnebago
https://wcgis3.co.winnebago.wi.us/wings/rest/services
Wood
https://gis.co.wood.wi.us/gis/rest/services   Not open to public
Wood
https://gis.woodcountywi.gov/gis/rest/services
Wood
https://services2.arcgis.com/kTzzDJBaecBOZCjk/ArcGIS/rest/serv
ices
Wood
https://tiles.arcgis.com/tiles/kTzzDJBaecBOZCjk/arcgis/rest/servic
es

## Page 457

Wisconsin City, Town, Village, etc GIS Servers
Abbotsford
https://services5.arcgis.com/N6XQ8qY4vomGrduj/ArcGIS/rest/ser
vices
Antigo
https://services3.arcgis.com/BsJtox87gtRLeAxl/arcgis/rest/services
Appleton
https://gis.appleton.org/pubserver/rest/services
Appleton
https://services1.arcgis.com/KowZ0VFM04w7hjgW/ArcGIS/rest/s
ervices
Appleton
https://tiles.arcgis.com/tiles/KowZ0VFM04w7hjgW/arcgis/rest/ser
vices
Arena
See Iowa county
Ashland
https://gis.coawi.org/arcgis/rest/services
Barneveld
https://services5.arcgis.com/RdkPF6RyvQRLjoru/ArcGIS/rest/serv
ices
Barron
https://services3.arcgis.com/3Kf2DMwaWP7HTsew/arcgis/rest/ser
vices
Beaver Dam
See Dodge County
Bellevue
https://esriweb.villageofbellevuewi.gov/arcgis/rest/services
Bellevue
https://services5.arcgis.com/rjgzgiSlP549zUdy/arcgis/rest/services
Beloit
https://services.arcgis.com/4YineAQdtmx0tv46/ArcGIS/rest/servic
es/CityofBeloitWIFeatures/FeatureServer
Go to the top and search for ‘BeloitWI’
Beloit
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/service
s/CityofBeloitWICadastral/MapServer
Go to the top and search for ‘BeloitWI’
Brodhead
______________
Brookfield
_ttps://webgis.ci.brookfield.wi.us/gis/rest/services    dead link 1
Carlton
______________
Eagle River
______________
Elm Grove
https://services3.arcgis.com/FXCMr1cDm8oL228X/ArcGIS/rest/se
rvices

## Page 458

Fitchburg
https://services1.arcgis.com/1VeK15F7oaitDair/ArcGIS/rest/servic
es
Fond du Lac
https://maps.fdl.wi.gov/server/rest/services
Fox Crossing
https://services8.arcgis.com/QRGgMFUUVpQjjfGd/ArcGIS/rest/s
ervices
Fox Crossing
https://tiles.arcgis.com/tiles/QRGgMFUUVpQjjfGd/arcgis/rest/ser
vices
Fox Point
https://services5.arcgis.com/IGF93xm2PgMbYJEP/arcgis/rest/serv
ices
Franklin
https://services2.arcgis.com/iVgAL45PIFPKIKKT/arcgis/rest/servi
ces
Franklin
https://tiles.arcgis.com/tiles/iVgAL45PIFPKIKKT/arcgis/rest/servi
ces
Frederic
https://services.arcgis.com/XzOgqjXGmvnuPSRG/arcgis/rest/servi
ces
Frederic
https://tiles.arcgis.com/tiles/XzOgqjXGmvnuPSRG/arcgis/rest/serv
ices
Grafton
https://services5.arcgis.com/C63lHqWdVDd6GUJY/arcgis/rest/ser
vices
Grand Chute
https://services8.arcgis.com/deR2GmCznCnyAVvu/ArcGIS/rest/se
rvices
Grand Chute
https://tiles.arcgis.com/tiles/deR2GmCznCnyAVvu/arcgis/rest/serv
ices
Green Bay
https://map.greenbaywi.gov/server/rest/services
Green Bay
https://services1.arcgis.com/rR5gshOOu0KM2c4P/arcgis/rest/servi
ces
Green Lake
___________
Greenville
https://arcgis.townofgreenville.com/server/rest/services
Greenville
https://services1.arcgis.com/AK12XGOfzttnFFY1/arcgis/rest/servi
ces
Hartland
          https://services.arcgis.com/LMg9EBZsadvfYa82/arcgis/rest/services
Janesville
https://services2.arcgis.com/i52vmcFqzIWK9plW/ArcGIS/rest/ser
vices

## Page 459

Kenosha
See Kenosha County
Kewaunee
           https://services3.arcgis.com/IZu8JiqSTXTykolP/arcgis/rest/services
Table of contents hidden by javascript
La Crosse
https://gis1.cityoflacrosse.org/laxgis1/rest/services
Lodi
____________

Madison
https://maps.cityofmadison.com/arcgis/rest/services

Madison
https://services.arcgis.com/lx96Ahunbwmk5g5p/ArcGIS/rest/servi
ces
Manitowoc
https://citygis.manitowoc.org/arcgis/rest/services
Middleton
https://services.arcgis.com/dril3ypTviG7LeUO/arcgis/rest/services
Middleton
           https://tiles.arcgis.com/tiles/dril3ypTviG7LeUO/arcgis/rest/services
Milwaukee
https://milwaukeemaps.milwaukee.gov/arcgis/rest/services
Mineral Point
https://services8.arcgis.com/H7t3NN1b8XE156Ts/ArcGIS/rest/ser
vices
Minong
https://services6.arcgis.com/34oZAi6uNhCJGam8/arcgis/rest/servi
ces
Mukwonago
https://services6.arcgis.com/3u5nlx5f2iT1o0oh/ArcGIS/rest/servic
es
Mukwonago
https://tiles.arcgis.com/tiles/3u5nlx5f2iT1o0oh/arcgis/rest/services
Muskego
https://www.mapmuskego.com/arcgis/rest/services
Necedah
https://services9.arcgis.com/kkYT6TgK0b9w6M5K/ArcGIS/rest/s
ervices
Neenah
https://gis.ci.neenah.wi.us/maps/rest/services
Nekoosa
https://services7.arcgis.com/0MF1TckfXBgRFtzu/arcgis/rest/servi
ces
Nekoosa
https://tiles.arcgis.com/tiles/0MF1TckfXBgRFtzu/arcgis/rest/servic
es
Oshkosh
https://www.ci.oshkosh.wi.us/arcgis/rest/services
Oshkosh
https://services1.arcgis.com/FxsZDd9jOLijkyzz/ArcGIS/rest/servic
es
Oshkosh
https://tiles.arcgis.com/tiles/FxsZDd9jOLijkyzz/arcgis/rest/services

## Page 460

Pardeeville
https://services8.arcgis.com/VaS4IZ7Ts2EoDxiC/arcgis/rest/servic
es
Plover
https://services8.arcgis.com/EzLR0vC4DOzvTZYk/ArcGIS/rest/se
rvices
Princeton
____________
Racine
https://gis.cityofracine.org/arcgis/rest/services
Reedsburg
https://services5.arcgis.com/beOfeHoZl96ztTxG/ArcGIS/rest/servi
ces
Rothschild
https://services6.arcgis.com/U8aLV7JhWlzvq2FB/ArcGIS/rest/ser
vices
Sheboygan
https://gis.sheboyganwi.gov/server/rest/services
Table of contents disabled
Shell Lake
____________
Sparta
https://services7.arcgis.com/ob3iBq0CA0JS6eE3/ArcGIS/rest/serv
ices
Sparta
https://tiles.arcgis.com/tiles/ob3iBq0CA0JS6eE3/arcgis/rest/servic
es
Spooner
https://services3.arcgis.com/Xnd2fKNA0yBORhwl/ArcGIS/rest/se
rvices
Spooner
https://tiles.arcgis.com/tiles/Xnd2fKNA0yBORhwl/arcgis/rest/serv
ices
Sun Prairie
https://services3.arcgis.com/EgnL1bB7VxL4zhx7/ArcGIS/rest/ser
vices
Sun Prairie
https://tiles.arcgis.com/tiles/EgnL1bB7VxL4zhx7/arcgis/rest/servic
es
Thiensville
https://services2.arcgis.com/ZPVVPZnrNWpkxoDU/ArcGIS/rest/s
ervices
Thiensville
https://tiles.arcgis.com/tiles/ZPVVPZnrNWpkxoDU/arcgis/rest/ser
vices
Tomahawk
____________
Two Rivers
https://services7.arcgis.com/ZNYU9ysVgADcg8Pt/arcgis/rest/servi
ces

## Page 461

Two Rivers
https://tiles.arcgis.com/tiles/ZNYU9ysVgADcg8Pt/arcgis/rest/servi
ces
Watertown
https://gis.watertownwi.gov/arcgis/rest/services
Waukesha
https://gis.waukesha-wi.gov/server/rest/services
Waukesha
https://services6.arcgis.com/QbV7DVTtrU1HrF5i/ArcGIS/rest/ser
vices
Wausau
https://gis.ci.wausau.wi.us/server/rest/services
Wautoma
https://services5.arcgis.com/8VuR6esDVgNf6mbn/arcgis/rest/servi
ces
Wauwatosa
https://services5.arcgis.com/gyXZ0hXCxDXxFxHi/ArcGIS/rest/se
rvices
West Allis
https://gis.westalliswi.gov/server/rest/services
West Allis
https://services2.arcgis.com/BL3BaPwSW83Cd89R/ArcGIS/rest/s
ervices
West Baraboo
https://services8.arcgis.com/XgY4bePgJSXNuVDC/ArcGIS/rest/se
rvices
West Bend
https://gis.ci.west-bend.wi.us/arcgis/rest/services
Westport
https://services6.arcgis.com/562VkASKWkZY7Bxu/ArcGIS/rest/s
ervices
Weston
https://gis.westonwi.gov/arcgis/rest/services
Whitewater
https://services2.arcgis.com/1BOMy3PNdECswnJ5/ArcGIS/rest/se
rvices
Whitewater
https://tiles.arcgis.com/tiles/1BOMy3PNdECswnJ5/arcgis/rest/serv
ices
Wisconsin Rapids
https://gis.wirapids.org/arcgis/rest/services
Wyoming State GIS Servers
Wyoming Geospatial Hub
Website: https://data.geospatialhub.org
Wyoming Department of Environmental Quality
Website: https://deq.wyoming.gov
GIS: https://gis.deq.wyo.gov/arcgis/rest/services

## Page 462

8-13-2023 No tiled data
Wyoming Department of Transportation
Website: https://www.dot.state.wy.us/home.html
GIS: https://map.wyoroad.info/ags/rest/services
8-13-2023 No tiled data
Wyoming Oil and Gas Conservation Commission
Website: https://wogcc.wyo.gov/
GIS: https://portal.wsgs.wyo.gov/ags/rest/services
GIS: Also WMS server
Wyoming State Geological Survey
Website: https://www.wsgs.wyo.gov
GIS: https://portal.wsgs.wyo.gov/ags/rest/services
Wyoming Office of State Lands and Investments
Website: https://lands.wyo.gov
GIS: https://gis.statelands.wyo.gov/arcgis/rest/services
SSL problem
University of Wyoming Geographic Information Science Center
Website: https://www.uwyo.edu/wygisc
GIS: https://services.wygisc.org/hostgis/rest/services
8-13-2023 No tiled data
GIS: https://services3.arcgis.com/vldsFscHxBjhK9SI/ArcGIS/rest/services
Wyoming various layers
https://services3.arcgis.com/r0iJ85SKZ4zAzz3P/ArcGIS/rest/services
Parcel lines:  Wyoming_Parcels_2023/FeatureServer/0
Parcel address likely changes each year
Central Wyoming College
GIS: https://services.arcgis.com/Mst6sJ6aFGwWU3UM/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/Mst6sJ6aFGwWU3UM/arcgis/rest/services
Wyoming Regional
Cheyenne and Laramie County GIS Cooperative
Website: https://hub.clcgisc.com
GIS: https://services1.arcgis.com/e5t4ywWgRBNUuDeU/ArcGIS/rest/services
Wyoming County GIS Servers
Albany
https://services1.arcgis.com/EmwrhKkmuQhTATzU/arcgis/rest/ser
vices
Campbell
https://gis.campbellcountywy.gov/arcgis/rest/services

## Page 463

Campbell
http://cecilmaps.ccgov.org/arcgis/rest/services
   not https
Campbell
https://services3.arcgis.com/4bXlKnUVV4OdWWbc/ArcGIS/rest/
services
Carbon
WMS server
Crook
https://crookela.centralus.cloudapp.azure.com/server/rest/services/
Crook
Goshen
https://services1.arcgis.com/HGQgPu4V7Rwvw86U/arcgis/rest/ser
vices
Laramie
https://maps.laramiecounty.com/arcgis/rest/services
Lincoln
https://maps.lcwy.org/arcgis/rest/services
Lincoln
https://services1.arcgis.com/mAJPyaZkZWzjRIy7/ArcGIS/rest/ser
vices
Lincoln
https://tiles.arcgis.com/tiles/mAJPyaZkZWzjRIy7/arcgis/rest/servi
ces
Niobrara
https://crookela.centralus.cloudapp.azure.com/server/rest/services/
Niobrara
Wyoming City, Town, Village, etc GIS Servers
Casper
hhttps://maps.casperwy.gov/nrgisc/rest/services
Table of contents disabled
Cheyenne
See Laramie County
Gillette
https://gisportal.gillettewy.gov/arcgisserver/rest/services
Gillette
https://services5.arcgis.com/ZI2myA5m7MRarLFN/arcgis/rest/ser
vices
Gillette
https://tiles.arcgis.com/tiles/ZI2myA5m7MRarLFN/arcgis/rest/serv
ices
Green River
https://services7.arcgis.com/KuLOZPy3lKDA07LB/ArcGIS/rest/se
rvices
Green River
https://tiles.arcgis.com/tiles/KuLOZPy3lKDA07LB/arcgis/rest/serv
ices
Jackson
WMS
Lander
https://services8.arcgis.com/DaaN11r1KfwdApEp/ArcGIS/rest/ser
vices
Laramie
See Albany County

## Page 464

Sheridan
https://gismaps.sheridanwy.net/arcgis/rest/services
Teton
https://services9.arcgis.com/6ukHJ1QHS9lvQoRO/ArcGIS/rest/ser
vices
8.
Washington D.C. Servers
Washington D.C. servers
Website: https://octo.dc.gov/service/dc-gis-services
Website: https://opendata.dc.gov
GIS: https://maps2.dcgis.dc.gov/dcgis/rest/services
GIS: https://imagery.dcgis.dc.gov/dcgis/rest/services
GIS: https://rh.dcgis.dc.gov/dcgis/rest/services
GIS: https://em.dcgis.dc.gov/dcgis/rest/services
GIS: https://services.arcgis.com/neT9SoYxizqTHZPH/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/neT9SoYxizqTHZPH/arcgis/rest/services
GIS: https://services9.arcgis.com/UmGCPY8AKRzyOzJX/ArcGIS/rest/services
Washington D.C. Regional
Metropolitan Washington Council of Governments
Website: https://www.mwcog.org
GIS: https://services.arcgis.com/n8kgWFr4EwFGg3zA/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/n8kgWFr4EwFGg3zA/arcgis/rest/services
9.
Native American Tribes
Cherokee Tribe
Website: https://cherokee.org
GIS: http://geodata.cherokee.org/arcgis/rest/services
not https
Coeur d'Alene Tribe
Website: https://www.cdatribe-nsn.gov
GIS: https://gis.cdatribe-nsn.gov/arcgisdatastore/rest/services
GIS: https://gis.cdatribe-nsn.gov/arcgisimage/rest/services
GIS: https://gis.cdatribe-nsn.gov/arcgis/rest/services
Navaho Nation
Black Mesa United
Website: https://www.navajo-nsn.gov
GIS: https://services1.arcgis.com/jj1iIK6we0wGtl1K/arcgis/rest/services
Navajo Safe Water
Website: https://navajo-safe-water-2-navajosafewater.hub.arcgis.com

## Page 465

GIS: https://services6.arcgis.com/1sSbDd9ooAdT8xO8/ArcGIS/rest/services
Saint Regis Mohawk Tribe
Website: https://www.srmt-nsn.gov
GIS: https://services6.arcgis.com/xo0Sli3SaYPY0VRz/arcgis/rest/services
Snoqualmie Tribe
Website: https://snoqualmietribe.us
GIS: https://gis.snoqualmietribe.us/arcgis/rest/services
GIS: https://image.snoqualmietribe.us/arcgis/rest/services       Table of contents disabled
GIS: https://services6.arcgis.com/Xtfy79A56GMM2RrJ/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/Xtfy79A56GMM2RrJ/arcgis/rest/services
Tanana Chiefs Conference
Website: https://www.tananachiefs.org
GIS: https://gis.tananachiefs.org/arcgisserver/rest/services
Tulalip Tribe
Website: https://www.tulaliptribes-nsn.gov
GIS: https://gismaps2.tulaliptribes-nsn.gov/arcgis/rest/services
Indian Nations Council of Governments (INCOG)
Website: https://www.incog.org
GIS: https://map11.incog.org/arcgis11wa/rest/services
Muscogee Creek Nation
Website: https://www.muscogeenation.com
GIS:
https://services3.arcgis.com/yBwJ5BxqvbumespK/ArcGIS/rest/services/Hanna_F
arm2_Trust_Land_Parcel_View/FeatureServer
GIS: https://tiles.arcgis.com/tiles/yBwJ5BxqvbumespK/arcgis/rest/services
Seneca Nation
Website: https://sni.org
GIS: https://services8.arcgis.com/OX5r7ewGgTojKuuK/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/OX5r7ewGgTojKuuK/arcgis/rest/services
Nez Perce
Website: https://nezperce.org
GIS: https://services7.arcgis.com/iICsLMZKYMImM2LL/arcgis/rest/services
10.
U.S. Territories
American Samoa
GIS: https://services5.arcgis.com/ugcD1wqDyNIfJ9ce/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/ugcD1wqDyNIfJ9ce/arcgis/rest/services
Guam

## Page 466

GIS: https://gis.epa.guam.gov/arcgis/rest/services
GIS: https://services2.arcgis.com/FPJlJZYRsD8OhCWA/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/FPJlJZYRsD8OhCWA/arcgis/rest/services
Northern Mariana Islands
GIS: https://www.oc.nps.edu/CMSP/CNMI/index.html
GIS: https://services.arcgis.com/qchgHH9IIeiivY5M/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/qchgHH9IIeiivY5M/arcgis/rest/services
Puerto Rico
Whole Community Resilience Planning (WCRP)
Website: https://foundationforpuertorico.org/en/wcrp-faq-fpr
GIS: https://www.sigela.pr.gov/arcgis/rest/services
GIS: https://sigejp.pr.gov/server/rest/services
GIS: https://sige.pr.gov/server/rest/services
GIS: https://services6.arcgis.com/MUhnqxO71cMj5hRO/ArcGIS/rest/services
Virgin Islands
GIS Division https://gisdivision-usvi.maps.arcgis.com/home/group.html?id=a979add560
73462a94d17528dfb76a7b#overview
GIS: https://maps.capturecama.com/arcgis/rest/services/USVI
GIS: https://services3.arcgis.com/UfiM23HwAqZRk1vw/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/UfiM23HwAqZRk1vw/arcgis/rest/services
11.
Multi-state planning
Flood Science Center
Website: https://floodsciencecenter.org
GIS: https://services3.arcgis.com/PwSEIra0zgvwmApz/ArcGIS/rest/services
Ohio-Kentucky-Indiana Regional Council of Governments (OKI)
Website: https://www.oki.org
GIS: https://gis.oki.org/server/rest/services
Mid-America Regional Council's (MARC) 9-county region
(Kansas and Missouri)
Website: https://www.marc.org
GIS: https://gis2.marc2.org/arcgis/rest/services
/Recreation  lots of trail data.  Supports dynamic layers.
Susquehanna River Basin Commission
(New York State, Pennsylvania, and Maryland)
Website: https://www.srbc.net/index.html
GIS: https://gis.srbc.gov/arcgis/rest/services
Appalachian Regional Commission

## Page 467

Website: https://www.arc.gov
Region 1 GIS: https://services9.arcgis.com/KpMczgynHDNPRX7w/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/KpMczgynHDNPRX7w/arcgis/rest/services
Pacific States Marine Fisheries Commission
Website: https://www.psmfc.org
GIS: https://services.arcgis.com/kpMKjjLr8H1rZ4XO/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/kpMKjjLr8H1rZ4XO/arcgis/rest/services
Central U.S. Earthquake Consortium
Website: https://cusec.org
GIS: https://services1.arcgis.com/utFj6xjAHT9GdIit/ArcGIS/rest/services
Gulf of Mexico Alliance
Website: https://gulfofamericaalliance.org
GIS: https://services6.arcgis.com/doedjwXkt41ndzZQ/arcgis/rest/services
Western Association of Fish & Wildlife Agencies
Website: https://wafwa.org
GIS: https://services.arcgis.com/w3IoZRfDCEvXzZYb/arcgis/rest/services
GIS: _ttps://cloud.wafwachat.org/arcgis/rest/services
dead link 1
South Atlantic Coastal Study
Website: https://www.sad.usace.army.mil/SACS
GIS: https://services9.arcgis.com/AU2Ll3RnmTTOkkZq/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/AU2Ll3RnmTTOkkZq/arcgis/rest/services
Bi-State Regional Commission    Covers part of Iowa and Illinois\
Website: https://bistateonline.org
GIS: https://services6.arcgis.com/nNJLeOqxAgP4H4UY/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/nNJLeOqxAgP4H4UY/arcgis/rest/services
Delaware River Basin Commission
Website: https://www.nj.gov/drbc
GIS: https://services1.arcgis.com/HERT3Lrqxe0YUfxz/arcgis/rest/services
12.
Miscellaneous Regional Data
Northeast Regional Ocean Council
Website: https://www.northeastoceancouncil.org
GIS: https://services.northeastoceandata.org/arcgis1/rest/services
GIS: http://50.19.218.171/arcgis1/rest/services
not https
Northeast Ocean Data Portal
Website: https://www.northeastoceandata.org
GIS: http://ec2-50-19-218-171.compute-1.amazonaws.com/arcgis1/rest/services not https

## Page 468

GIS: https://devservices.northeastoceandata.org/neoddev/rest/services
Mid-Atlantic Regional Ocean Council
Website: https://midatlanticocean.org
GIS: https://services.northeastoceandata.org/arcgis1/rest/services
Pacific Disaster Center - University of Hawaii
Website: https://www.pdc.org
GIS: https://arcgis.pdc.org/arcgis/rest/services
Multi-Resolution Land Cover Characteristics (MRLC) Consortium
Website: https://www.mrlc.gov
GIS:  WMS server
Gulf of Mexico Coastal Ocean Observing System
Website: https://gcoos.org
GIS: https://services1.arcgis.com/qr14biwnHA6Vis6l/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/qr14biwnHA6Vis6l/arcgis/rest/services
Data Basin
Website: https://databasin.org
GIS: https://padags.databasin.org/arcgis/rest/services
SSL problem
13.
USA Miscellaneous Servers
This section has been reorganized.  All of this data is hosted on ESRI’s servers as part of ArcGIS
Online.  Usually the unique identifier (i.e. string of gibberish) leads to both a server with
FeatureServer data and a server with tile data.  That is the reason the addresses shown below will
appear in pairs.  As more ArcGIS addresses are found for tile servers those addressesd will be
added here.
https://services.arcgis.com/0ZRg6WRC7mxSLyKX/ArcGIS/rest/services
Includes ‘crowdsourced’ photos complied by NAPSG
https://tiles.arcgis.com/tiles/0ZRg6WRC7mxSLyKX/arcgis/rest/services
https://services.arcgis.com/4YineAQdtmx0tv46/arcgis/rest/services
https://tiles.arcgis.com/tiles/4YineAQdtmx0tv46/arcgis/rest/services
Lots of aerials and other data for counties and maybe cities.  Links to related
FeatureServer data appear in various places in this curated list.
https://services.arcgis.com/B7X7NCOKKXditlwZ/ArcGIS/rest/services
Includes data on cell towers, wireless, etc
https://tiles.arcgis.com/tiles/B7X7NCOKKXditlwZ/arcgis/rest/services
https://services.arcgis.com/cJ9YHowT8TU7DUyn/ArcGIS/rest/services

## Page 469

Lots of climate, air quality and environment data
/FRS_PowerPlants/FeatureServer
https://tiles.arcgis.com/tiles/cJ9YHowT8TU7DUyn/arcgis/rest/services
https://services.arcgis.com/dlFJXQQtlWFB4qUk/arcgis/rest/services
https://services.arcgis.com/DO4gTjwJVIJ7O9Ca/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/DO4gTjwJVIJ7O9Ca/arcgis/rest/services
Lots of layers after disasters of various kinds
https://services.arcgis.com/jIL9msH9OI208GCb/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/jIL9msH9OI208GCb/arcgis/rest/services
https://services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/P3ePLMYs2RVChkJx/arcgis/rest/services
https://services.arcgis.com/p3UBboyC0NH1uCie/arcgis/rest/services
https://tiles.arcgis.com/tiles/p3UBboyC0NH1uCie/arcgis/rest/services
https://services.arcgis.com/pGfbNJoYypmNq86F/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/pGfbNJoYypmNq86F/arcgis/rest/services
https://services.arcgis.com/q3Zg9ERurv23iysr/arcgis/rest/services
https://tiles.arcgis.com/tiles/q3Zg9ERurv23iysr/arcgis/rest/services
https://services.arcgis.com/rOo16HdIMeOBI4Mb/ArcGIS/rest/services
https://services.arcgis.com/uCXeTVveQzP4IIcx/arcgis/rest/services
https://tiles.arcgis.com/tiles/uCXeTVveQzP4IIcx/arcgis/rest/services
https://services.arcgis.com/umnz0Hyr6owZYHTd/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/umnz0Hyr6owZYHTd/arcgis/rest/services
https://services.arcgis.com/VTyQ9soqVukalItT/ArcGIS/rest/services
https://services1.arcgis.com/4yjifSiIG17X0gW4/arcgis/rest/services
https://tiles.arcgis.com/tiles/4yjifSiIG17X0gW4/arcgis/rest/services
https://services1.arcgis.com/CD5mKowwN6nIaqd8/arcgis/rest/services
If this link opens but the screen is mostly blank then click the word “Home”.
https://tiles.arcgis.com/tiles/CD5mKowwN6nIaqd8/arcgis/rest/services
https://services1.arcgis.com/E5n4f1VY84i0xSjy/arcgis/rest/services
https://tiles.arcgis.com/tiles/E5n4f1VY84i0xSjy/arcgis/rest/services
https://services1.arcgis.com/fcrLbZIfZI20fNqr/arcgis/rest/services

## Page 470

https://tiles.arcgis.com/tiles/fcrLbZIfZI20fNqr/arcgis/rest/services
https://services1.arcgis.com/Hp6G80Pky0om7QvQ/ArcGIS/rest/services
Lots of federal data that used to be on HILFD is here
https://tiles.arcgis.com/tiles/Hp6G80Pky0om7QvQ/arcgis/rest/services
https://services1.arcgis.com/RLQu0rK7h4kbsBq5/ArcGIS/rest/services
https://services1.arcgis.com/Ug5xGQbHsD8zuZzM/arcgis/rest/services
https://tiles.arcgis.com/tiles/Ug5xGQbHsD8zuZzM/arcgis/rest/services
https://services2.arcgis.com/cPVqgcKAQtE6xCja/arcgis/rest/services
https://tiles.arcgis.com/tiles/cPVqgcKAQtE6xCja/arcgis/rest/services
https://services2.arcgis.com/djh8oO0rYU7YdX5J/arcgis/rest/services
https://tiles.arcgis.com/tiles/djh8oO0rYU7YdX5J/arcgis/rest/services
https://services2.arcgis.com/FiaPA4ga0iQKduv3/arcgis/rest/services
USA_Structures_View
Building footprints
USNG grid lines.  No labels.  Clicking a box displays USNG coordinates
https://tiles.arcgis.com/tiles/FiaPA4ga0iQKduv3/arcgis/rest/services
https://services2.arcgis.com/fJJEXNgxjn0dpNsi/arcgis/rest/services
https://services2.arcgis.com/HXuDXoXgsUiaeXTG/arcgis/rest/services
https://tiles.arcgis.com/tiles/HXuDXoXgsUiaeXTG/arcgis/rest/services
https://services2.arcgis.com/JHQPLKbcY2kneu4b/arcgis/rest/services
https://services2.arcgis.com/mI7DQu3pwg8FcliY/ArcGIS/rest/services
https://services2.arcgis.com/nln0k0iBNk3Anmkc/arcgis/rest/services
https://tiles.arcgis.com/tiles/nln0k0iBNk3Anmkc/arcgis/rest/services
https://services2.arcgis.com/RPhrOu9XQzI31xTa/arcgis/rest/services
https://tiles.arcgis.com/tiles/RPhrOu9XQzI31xTa/arcgis/rest/services
https://services2.arcgis.com/ZktcQDbWRlii7YHf/arcgis/rest/services
https://tiles.arcgis.com/tiles/ZktcQDbWRlii7YHf/arcgis/rest/services
https://services2.arcgis.com/6Miy5NqQWjMYTGFY/ArcGIS/rest/services
Active_SNOTEL_Stations
https://services3.arcgis.com/0Fs3HcaFfvzXvm7w/ArcGIS/rest/services
National Climate Resilience
https://tiles.arcgis.com/tiles/0Fs3HcaFfvzXvm7w/arcgis/rest/services

## Page 471

https://services3.arcgis.com/0i8WvfNdfTbWrPkh/arcgis/rest/services
https://tiles.arcgis.com/tiles/0i8WvfNdfTbWrPkh/arcgis/rest/services
https://services3.arcgis.com/1pxU2hJU9ZszJDcX/ArcGIS/rest/services
Data on opioid epidemic
https://tiles.arcgis.com/tiles/1pxU2hJU9ZszJDcX/arcgis/rest/services
https://services3.arcgis.com/6CawrotsIAWp4yUX/ArcGIS/rest/services
https://services3.arcgis.com/GVgbJbqm8hXASVYi/arcgis/rest/services
https://services3.arcgis.com/hb51ynJDNOT9ybXe/arcgis/rest/services
The Emergency Transport Healthcare Operations and Safety (ETHOS) database is a
real-time resource for air medical asset tracking across the U.S.
https://services3.arcgis.com/LNTe09Xft4ymdHYS/arcgis/rest/services
https://tiles.arcgis.com/tiles/LNTe09Xft4ymdHYS/arcgis/rest/services
https://services3.arcgis.com/N2cjIoVJvUn451AH/arcgis/rest/services
https://tiles.arcgis.com/tiles/N2cjIoVJvUn451AH/arcgis/rest/services
https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services
Above server has lots of wildland fire data.  Also folder ArcGIS
NIFC posts data here.
Current fires /WFIGS_Incident_Locations_Current/FeatureServer/0
Red dot. Name does not display.
2-29-2024 inciweb using for perimeter:
WFIGS_Interagency_Perimeters_YearToDate/FeatureServer/0
https://tiles.arcgis.com/tiles/T4QMspbfLg3qTGWY/arcgis/rest/services
https://services3.arcgis.com/ZvidGQkLaDJxRSJ2/arcgis/rest/services
https://services4.arcgis.com/QdHwhlbx61LR3TWb/arcgis/rest/services
https://tiles.arcgis.com/tiles/QdHwhlbx61LR3TWb/arcgis/rest/services
https://services4.arcgis.com/raoQw2g6KLgutJjp/arcgis/rest/services
https://tiles.arcgis.com/tiles/raoQw2g6KLgutJjp/arcgis/rest/services
https://services5.arcgis.com/fmKivMCp6fwbWbeE/ArcGIS/rest/services
National States Geographic Information Council
https://services6.arcgis.com/2DGR1sZBUvcPcd8Z/ArcGIS/rest/services
Gulf of America Coastal Ocean Observing System Regional Association
https://services7.arcgis.com/L95Wwv9OjRQ0tjAs/ArcGIS/rest/services

## Page 472

https://services7.arcgis.com/Vzo8VQfynhdJwtUh/ArcGIS/rest/services
National Association of State Fire Marshals
https://services9.arcgis.com/RHVPKKiFTONKtxq3/ArcGIS/rest/services
For information about the above link see:
https://www.esri.com/arcgis-blog/products/public-safety/public-safety/new-live-feeds-we
ather-data-goes-live          weather data
https://services9.arcgis.com/U0vgiXgwLpyQDfbW/ArcGIS/rest/services
Civil Air Patrol
https://tiles.arcgis.com/tiles/U0vgiXgwLpyQDfbW/arcgis/rest/services
14.
World Miscellaneous Servers With Some USA Data
https://gisserver.ibwc.gov/agsserver/rest/services/USIBWCPublic/US_MexicoIB/FeatureServer
USA section of International Boundary and Water Commission (USIBWC)
https://services.arcgisonline.com/arcgis/rest/services
Lots of tiled data
https://services.arcgis.com/V6ZHFr6zdgNZuVG0/arcgis/rest/services
https://tiles.arcgis.com/tiles/V6ZHFr6zdgNZuVG0/arcgis/rest/services
https://services.arcgis.com/VgnIzOwU2FBU6E7K/ArcGIS/rest/services
NATO countries
https://tiles.arcgis.com/tiles/VgnIzOwU2FBU6E7K/arcgis/rest/services
https://services1.arcgis.com/4TXrdeWh0RyCqPgB/arcgis/rest/services
https://tiles.arcgis.com/tiles/4TXrdeWh0RyCqPgB/arcgis/rest/services
https://services1.arcgis.com/blRg5afpxSe1ecGt/arcgis/rest/services
https://tiles.arcgis.com/tiles/blRg5afpxSe1ecGt/arcgis/rest/services
https://services1.arcgis.com/g2TonOxuRkIqSOFx/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/g2TonOxuRkIqSOFx/arcgis/rest/services
https://services1.arcgis.com/hLJbHVT9ZrDIzK0I/arcgis/rest/services
https://tiles.arcgis.com/tiles/hLJbHVT9ZrDIzK0I/arcgis/rest/services
https://services1.arcgis.com/VA8qSG2eGMxXGKnw/arcgis/rest/services
https://tiles.arcgis.com/tiles/VA8qSG2eGMxXGKnw/arcgis/rest/services
https://services2.arcgis.com/cFEFS0EWrhfDeVw9/ArcGIS/rest/services
https://tiles.arcgis.com/tiles/cFEFS0EWrhfDeVw9/arcgis/rest/services
https://services4.arcgis.com/nFXg5SbskEHIHraQ/arcgis/rest/services

## Page 473

https://services4.arcgis.com/pKwhgSeu8oDudbDZ/arcgis/rest/services
https://services5.arcgis.com/U8xJBTiAx2RGR2e2/arcgis/rest/services
https://tiles.arcgis.com/tiles/U8xJBTiAx2RGR2e2/arcgis/rest/services
https://services7.arcgis.com/oF9CDB4lUYF7Um9q/arcgis/rest/services
https://tiles.arcgis.com/tiles/oF9CDB4lUYF7Um9q/arcgis/rest/services
15.
Environmental groups
Alaska Trails
Website: https://www.alaska-trails.org
GIS: https://services.arcgis.com/E4aLbdRuC2azR6Sw/arcgis/rest/services
Allegheny-Blue Ridge Alliance
Website: https://www.abralliance.org
GIS: https://services6.arcgis.com/cGI8zn9Oo7U9dF6z/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/cGI8zn9Oo7U9dF6z/arcgis/rest/services
Carmel River Watershed Conservancy (California)
Website: https://www.carmelriverwatershed.org
GIS: https://services.arcgis.com/U6Yf5wUw3JQs22Xn/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/U6Yf5wUw3JQs22Xn/arcgis/rest/services
CEDR Digital Corps (Crowd sourced disaster data)
Website: https://cedrdigitalcorps.org
GIS: https://services8.arcgis.com/X1w9TNdH7ukf6Awg/arcgis/rest/services
Center for Biological Diversity
Website: https://www.biologicaldiversity.org
GIS: https://services.arcgis.com/HoKuy8MaByQZ1OQ9/arcgis/rest/services
Center for Climate Equity and Resilience
Website: https://climatecenter.sdsu.edu
GIS: https://services5.arcgis.com/rquOuNGYVRyOnUdO/arcgis/rest/services
Chesapeake Bay Foundation
GIS: https://gis.cbf.org/arcgis/rest/services
GIS: https://services5.arcgis.com/pGIpkO9l9XlmojjG/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/pGIpkO9l9XlmojjG/arcgis/rest/services
Chesapeake Conservancy
Website: https://www.chesapeakeconservancy.org
GIS: https://cicgis.org/arcgis/rest/services
GIS: https://services.arcgis.com/dqnSpuoMiocEiFNg/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/dqnSpuoMiocEiFNg/arcgis/rest/services

## Page 474

Chesapeake Geoplatform.  Looks like federal data.  Owner unknown.
GIS: https://services1.arcgis.com/r1R8Ngr5TIxz8w0M/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/r1R8Ngr5TIxz8w0M/arcgis/rest/services
Clackamas River Water Providers
Website: https://www.clackamasproviders.org
GIS: https://services7.arcgis.com/INLhOe4g2EkCnz7H/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/INLhOe4g2EkCnz7H/arcgis/rest/services
Continental Divide Trail Coalition
Website: https://cdtcoalition.org
GIS: https://services8.arcgis.com/WyuHwdftppQLa5KO/ArcGIS/rest/services
Ducks Unlimited
Website: https://www.ducks.org
GIS: https://services2.arcgis.com/5I7u4SJE1vUr79JC/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/5I7u4SJE1vUr79JC/arcgis/rest/services
Grand Canyon Trust
Website: https://www.grandcanyontrust.org
GIS: https://services.arcgis.com/sYBjPLGLPQvUC9uV/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/sYBjPLGLPQvUC9uV/arcgis/rest/services
Great Basin Bird Observatory
Website: https://www.gbbo.org
GIS: https://services.arcgis.com/6BT4RkNpUeVq1TOz/arcgis/rest/services
Housatonic Valley Association
Website: https://hvatoday.org
GIS: https://services.arcgis.com/0ahKkMERRbqrhR00/ArcGIS/rest/services
Klamath River Restoration Project
Website: https://klamathrenewal.org
GIS: https://services8.arcgis.com/F2C54G6dv3T0LAEz/arcgis/rest/services
Lower Boise Watershed Council
Website: https://www.lowerboisewatershedcouncil.org
GIS: https://www.lowerboisewatershedcouncil.org
Madison Land Trust trails (Connecticut)
Website: https://www.madisonlandtrust.org
GIS: https://sgsdgf.mapxpress.net/arcgis/rest/services/MLCT
8-1-2023 No tiled data
National Audubon Society
Website: https://www.audubon.org

## Page 475

GIS: https://gis.audubon.org/arcgisweb/rest/services
GIS: https://services1.arcgis.com/lDFzr3JyGEn5Eymu/arcgis/rest/services
If this link opens but the screen is mostly blank then click the word “Home”.
GIS: https://tiles.arcgis.com/tiles/lDFzr3JyGEn5Eymu/arcgis/rest/services
National Parks Conservation Association
Website: https://www.npca.org
GIS: https://services3.arcgis.com/17F7m6SrhCakwCcI/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/17F7m6SrhCakwCcI/arcgis/rest/services
National Trust for Historic Preservation
Website: https://savingplaces.org
GIS: https://services3.arcgis.com/8mRVhBBtAu5eqZUu/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/8mRVhBBtAu5eqZUu/arcgis/rest/services
NatureServe
Website: https://www.natureserve.org
GIS: https://services.arcgis.com/EVsTT4nNRCwmHNyb/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/EVsTT4nNRCwmHNyb/arcgis/rest/services
Savannah Riverkeeper
Website: https://www.savannahriverkeeper.org
GIS: https://services3.arcgis.com/kTHh5mF5pghzqQ3m/ArcGIS/rest/services
The Nature Conservancy
Website: https://www.nature.org/en-us
GIS: https://cirrus.tnc.org/arcgis/rest/services
GIS: https://services.arcgis.com/F7DSX1DSNSiWmOqh/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/F7DSX1DSNSiWmOqh/arcgis/rest/services
The Piedmont Environmental Council
Website: https://www.pecva.org
GIS: https://services3.arcgis.com/mTaShYKffyWc5uRb/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/mTaShYKffyWc5uRb/arcgis/rest/services
The Trust for Public Land
Website: https://www.tpl.org
GIS: https://server5.tplgis.org/arcgis5/rest/services
GIS: https://server6.tplgis.org/arcgis6/rest/services
GIS: https://server7.tplgis.org/arcgis7/rest/services
GIS: https://services.arcgis.com/BvefdV6XvRo2Jt72/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/BvefdV6XvRo2Jt72/arcgis/rest/services
The Wildlife Society
GIS: https://services1.arcgis.com/IAQQkLXctKHrf8Av/arcgis/rest/services
GIS: https://tiles.arcgis.com/tiles/IAQQkLXctKHrf8Av/arcgis/rest/services

## Page 476

Trout Unlimited  (ArcGIS servers shared with Wilderness Society)
Website: https://www.tu.org
GIS: https://services1.arcgis.com/754BERmVIq3RqSf8/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/754BERmVIq3RqSf8/arcgis/rest/services
Virginia Outdoors Foundation
Website: https://www.vof.org
GIS: https://services.arcgis.com/9G4sdQoLZS9CCa9R/arcgis/rest/services
Western Pennsylvania Conservancy
Website: https://waterlandlife.org
GIS:
https://mapservices.pasda.psu.edu/server/rest/services/pasda/WesternPennsylvania
Conservancy/MapServer
8-10-2023 No tiled data
Wilderness Society (ArcGIS servers shared with Trout Unlimited)
Website: https://www.wilderness.org
GIS: https://services1.arcgis.com/IAQQkLXctKHrf8Av/ArcGIS/rest/services
GIS: https://tiles.arcgis.com/tiles/754BERmVIq3RqSf8/arcgis/rest/services
World Wildlife Fund
Website: https://www.worldwildlife.org
GIS: _ttps://maps.wwfus.org/server/rest/services
dead link 3
16.
Canada GIS servers
The following link will take you to a somewhat similar list of GIS servers across Canada.
https://www.nrcan.gc.ca/science-and-data/science-and-research/geomatics/canadas-spatial-data-i
nfrastructure/geospatial-web-services/19359

