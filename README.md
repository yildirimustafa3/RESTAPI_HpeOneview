# RESTAPI_HpeOneview
With this repo, I aimed to automate some of Oneview operations that I need to do in my job.

what is oneview? 
--> https://buy.hpe.com/emea_europe/en/software/converged-infrastructure-management-software/converged-infrastructure-management/oneview-management-software/hpe-oneview/p/5410258

--> https://support.hpe.com/connect/s/product?language=en_US&tab=manualsAndGuides&kmpmoid=5410259&manualsAndGuidesFilter=66000003%2C66000033%2C66000006%2C66000002%2C66000008&manualsAndGuidesQuery=OneView+Release+Notes

documentatin for Oneview Rest API --> https://techlibrary.hpe.com/docs/enterprise/servers/oneview5.4/cicf-api/en/#about
#This looks outdated since last version shows 5.40 but currently last version is 6.50 https://myenterpriselicense.hpe.com/cwp-ui/free-software/Z7550-63180 as of Jan 2022.

#When you deploy Oneview and login to it On the right side upper corner there is a "?" button where you can find "Rest API Reference" it opens https://{ONEVIEW_IP}/api-docs/current/ link, from here you can see documentation for Oneview Rest APIs.

Prerequisites:
- Python3 (my version:Python 3.8.9)
- urllib3 library
- request library
- Oneview (my version: 6.20 and 6.30)


Script Purposes:
- getAuthtoken.py-->creates Auth Token by supplying Oneview username and password, this auth token is needed for remaining scripts.
- addServerHardware.py--> adds HPE Servers to Oneview.
- getAvailableTargets.py--> retrieves server hardwares that don't have any Server profile assigned to them(called available target)
- serverProfileTemplate_create.py--> creates Server Profile Template with specified settings.
- serverProfileCreateAndAssignHW.py--> creates Server Profile(depending on specified Server Profile Template) and assign to available targets it finds.


More details can be found on each script.
If you have any question, don't hesitate to contact me via yildirimustafa3@gmail.com


  
