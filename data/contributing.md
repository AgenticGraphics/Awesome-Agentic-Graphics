# Suggest a correction

Click **Suggest a correction** on a paper. Choose a field, enter the proposed value, and cite the paper section or page. Review the before/after preview, then submit the prefilled issue on GitHub. No code or JSON editing is needed.

**Suggestion → automatic PR → human review → merge.**

Once the repository workflow is enabled, the bot validates a structured correction, creates a branch containing only the feed-data change, opens a PR targeting **page**, and replies to the issue with its link. The team reviews the evidence and merges manually. Nothing is automatically approved or merged.

A correction applies to the selected search date unless you choose the other saved dates too. For a long suggestion, copy the prepared text and paste it into the GitHub draft. **Share feedback** handles general ideas and missing papers; these do not automatically become code changes.

A GitHub account and repository access are required. If the repository is private, only people with access can submit issues there.

## Maintainer setup — once

1. Push the website code, bot scripts, taxonomy labels, and validation workflow to **page**.
2. Copy `.github/workflows/correction-pr.yml` to the same path on the default **main** branch. Only this workflow file is needed on `main`; it explicitly checks out the maintained `page` code. Issue events do not run from `page` alone.
3. In **Settings → Actions → General**, an administrator must confirm that Actions is enabled and **Allow GitHub Actions to create and approve pull requests** is enabled. The bot never calls an approval or merge endpoint. It uses the built-in workflow token; no personal token or browser secret is required.
4. Protect `page` with required PRs, human approval, and the **Validate daily feed** check. If GitHub asks for **Approve workflows to run** on a bot PR, approve the check run and wait for it to pass before merging.
5. Test with a real, evidence-backed correction after installation. Inspect the resulting PR before merging.

This local implementation does not change repository settings, install the workflow on `main`, publish the site, or submit a test issue by itself.

## Review behavior

- Only a structured correction submitted through the form can generate a PR. General feedback stays an issue.
- The bot validates labels, dates, evidence format, and the saved before-value. Scientific claims still require human review.
- A changed value or changed evidence makes an old suggestion stale; the bot reports the error instead of overwriting the record.
- One issue creates at most one PR. Editing the issue after PR creation does not silently modify a PR under review. Continue the discussion on the PR; submit a new correction if it was closed.
- Interrupted attempts can resume an exact bot-generated commit. Other branch content is never overwritten.
- Only `data/daily-results.json` is written. Archived search reports stay unchanged.

If automation is unavailable, maintainers can still preview a saved issue body with `node scripts/apply-correction.cjs review.md`, then explicitly use `--write` after review and open a PR manually.

## After merge

The website reads the JSON directly on page load. When the hosting service publishes the merged `page` branch, refreshing shows the change; there is no generated feed file to update. Configure the host to deploy `page` if it does not already do so. For local preview, sync the branch and refresh.

[Issue workflow requirements](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#issues) · [Actions repository permissions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) · [Checks on bot-created PRs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#triggering-a-workflow-from-a-workflow)
