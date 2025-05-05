SELECT 
    date_trunc('week', incident_date) AS week,
    battalion,
    COUNT(*) AS total_incidents
FROM {{ ref('fire_incidents_stage') }}
GROUP BY 1, 2
ORDER BY 1 DESC