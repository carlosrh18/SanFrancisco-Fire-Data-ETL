SELECT 
    "Incident Number" AS incident_number,
    "Incident Date"::DATE AS incident_date,
    "Battalion" AS battalion,
    "Supervisor District" AS district
FROM {{ source('public', 'fire_incidents') }}