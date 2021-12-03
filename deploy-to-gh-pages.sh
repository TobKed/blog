#!/bin/bash
# based on: https://github.com/nolanbconaway/pelican-deploy-gh-actions/blob/master/deploy-to-gh-pages.sh

set -euo pipefail


if [ -z "$ACCESS_TOKEN" ]
then
  echo "No access token!"
  exit 1
fi

FOLDER='output'
BASE_BRANCH='master'
BRANCH='gh-pages'
COMMIT_EMAIL="${GITHUB_ACTOR}@users.noreply.github.com"
REPOSITORY_PATH="https://${ACCESS_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"


echo '----- Deploy Settings -----'

echo "* REPO: ${GITHUB_REPOSITORY}"
echo "* ACTOR: ${GITHUB_ACTOR}"
echo "* BRANCH: ${BRANCH}"
echo "* BASE_BRANCH: ${BASE_BRANCH}"
echo "* COMMIT_EMAIL: ${COMMIT_EMAIL}"
echo "* GITHUB_REPOSITORY: ${GITHUB_REPOSITORY}"
echo "* FOLDER: ${FOLDER}"


echo '----- Configuring git -----'
git init && \
git config --global user.email "${COMMIT_EMAIL}" && \
git config --global user.name "${GITHUB_ACTOR}"


echo "----- Checking on $BRANCH branch -----"
if [ "$(git ls-remote --heads "$REPOSITORY_PATH" "$BRANCH" | wc -l)" -eq 0 ];
then
  echo "Creating remote branch ${BRANCH} as it doesn't exist..."
  git checkout "$BASE_BRANCH" && \
  git checkout --orphan $BRANCH && \
  git rm -rf . && \
  echo 'just creating the branch...' > README.md && \
  git add README.md && \
  git commit -m "Initial ${BRANCH} commit" && \
  git push "${REPOSITORY_PATH}" "${BRANCH}"
fi

git checkout "$BASE_BRANCH"


echo '----- Making HTML -----'
publish=$(make publish 2>&1)
echo -e "${publish}"
echo "${publish}" | grep -vzq "ERROR" || exit 1


echo '----- Deploying -----'
git add -f $FOLDER && \
git commit -m "Deploy to ${BRANCH} - $(date +"%T")" && \
git push "${REPOSITORY_PATH}" "$(git subtree split --prefix ${FOLDER} ${BASE_BRANCH})":"${BRANCH}" --force


echo "Deployment successful!"
