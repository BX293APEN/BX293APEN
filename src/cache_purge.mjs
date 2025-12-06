import fetch from "node-fetch";
import { Octokit } from "@octokit/rest";

const octokit = new Octokit({
    auth: process.env.GITHUB_TOKEN, // GitHub Actionsのsecretsに設定
});

async function purgeCamoCache(owner, repo) {
    const readme = await octokit.repos.getReadme({ owner, repo });
    const downloadUrl = readme.data.download_url;

    const res = await fetch(downloadUrl);
    const text = await res.text();

    const regex = /https:\/\/camo\.githubusercontent\.com\/[^\s)]+/g;
    const urls = text.match(regex) || [];

    for (const url of urls) {
        console.log(`Purging ${url}`);
        try {
            const purgeRes = await fetch(url, { method: "PURGE" });
            console.log(`Status: ${purgeRes.status}`);
        } 
        catch (err) {
            console.error(`Failed to purge ${url}:`, err);
        }
    }
}

// 実行例
purgeCamoCache("BX293APEN", "BX293APEN");
