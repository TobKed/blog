Title: Notion packing lists
Date: 2022-10-25
Category: productivity
Tags: productivity, tools, notion
Slug: notion-packing-lists
Summary: Make packing easier
Header_Cover: /images/posts/2020/2020_summary.png
Status: published

# Packing - what is the problem here?

From time to time I travel.
Usually not very often, usually not very far.
And I always struggle with the same major problem: packing.
Should I take these things, maybe I took too many other things.
I try to recall what I took last time when I went on a similar trip, and what I had forgotten to take.
Even if I consolidate all necessary stuff there is always the same area for improvement.
A pair of sunglasses during sunny festival morning or lightweight sitting mat during hiking
are not necessary but nice to have.
Nice to have, but easy to forget during last minute packing when the vast cognitive resources are spent on remembering the
more necessary stuff to take.

I started preparing paper lists some time ago, and it worked very well.
I had some additional time to think about it before.
I offloaded my brain by storing it on the paper. Additionally, crossing out items from it brings some joy.

But I had to prepare this list again and again every time, so it became obvious that I have to reuse the same lists and improve them through iterations.
I am experimenting with different note-taking systems and currently I am testing [Notion](https://www.notion.so/) so it was an obvious choice.
I came up with a way to solve it as presented below.

## Solution

All lists are stored in a database with different views and visible columns.

Columns:

- **name** (type: _title_): self-described. Name of item. Common for every view.
- **tag** (type: _multi-select_): for categorizing items.
- **packed** (type: _checkbox_): packed or not (that is the question).
- **individual_list_name** (type: _checkbox_): does the item belong on this list.
- **individual_list_name_quantity** (type: _number_): quantity of items for individual list if more than 1.

Views:

- **main**: consists of every column. Used for general management across all lists and bulk unchecking  of the 'packed' column.
- **individual_list_name**: filtered by individual_list_name column so only items belonging on this list are visible.

Below are some screenshots with basic demo lists.

#### Main view

<img src="{static}/images/posts/2022/notion_packing_list_screenshot_01.png" alt="Notion Packing List Screenshot 1" style="display: block; margin-left: auto; margin-right: auto;">

#### Individual lists

<img src="{static}/images/posts/2022/notion_packing_list_screenshot_02.png" alt="Notion Packing List Screenshot 2" style="display: block; margin-left: auto; margin-right: auto;">
<br>
<br>
<img src="{static}/images/posts/2022/notion_packing_list_screenshot_03.png" alt="Notion Packing List Screenshot 3" style="display: block; margin-left: auto; margin-right: auto;">

Every time I travel somewhere I open a corresponding view, or create a new one and follow the list by checking checkboxes in the  ‘packed’ column.
With minimal effort I made some adjustments here and there. Especially after the trips where I forgot something or overpacked. Perfect packing list is on the horizon.

## Summary

It may be not the best way of doing packing lists but it works for me.
If someone has another way I am happy to learn about it.
Take it and enjoy it as I do. Your future self will thank you hopefully :).

Cheers.
