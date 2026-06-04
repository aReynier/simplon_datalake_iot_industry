#!/bin/bash

# Attendre de démarrage e MinIO
sleep 15

# Renter dans le conteneur docker
# docker exec -it minio bash

# Mise en place de l'alias local et connexion en admin
mc alias set local http://minio:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD}

# Créer les buckets
mc mb local/raw --ignore-existing
mc mb local/staging --ignore-existing
mc mb local/curated --ignore-existing
mc mb local/archive --ignore-existing

# Créer des utilisateurs
mc admin user add local ${MINIO_LOCAL_ANALYST_USER} ${MINIO_LOCAL_ANALYST_PASSWORD} 
mc admin user add local ${MINIO_LOCAL_ENGINEER_USER} ${MINIO_LOCAL_ENGINEER_PASSWORD}
mc admin user add local ${MINIO_LOCAL_ADMIN_USER} ${MINIO_LOCAL_ADMIN_PASSWORD}

# Associer les utilisateurs précédemment créés à chaque groupe
mc admin group add local data-analyst ${MINIO_LOCAL_ANALYST_USER}
mc admin group add local data-engineer ${MINIO_LOCAL_ENGINEER_USER}
mc admin group add local admin ${MINIO_LOCAL_ADMIN_USER}

# Enregister la policy pour les analystes tant que policy pour l'alias local
mc admin policy create local readonly-curated /tmp/policies/analyst-policy.json

# Attacher aux analyst la policy qui vient d'être créée
mc admin policy attach local readonly-curated --group data-analyst

# Attacher aux groupes data-engineer et admin une policy readwrite dans l'alias local
mc admin policy attach local readwrite --group data-engineer
mc admin policy attach local readwrite --group admin

# Vérification
mc admin policy entities local