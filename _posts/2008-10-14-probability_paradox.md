---
id: 167
title: "מסתבר שלא"
date: 2008-10-14 08:38:26
layout: post
categories: 
  - הסתברות
social_media_share: true
---
במקרה נתקלתי בחוברות של עיתון מתמטי שיצא לפני כעשור בפקולטה למתמטיקה בטכניון - "אתגר". בנוסף לחידות ולדיווחים על אולימפיאדות למתמטיקה, הן כוללות גם מאמרים פשוטים וקריאים על נושאים מתמטיים בסיסיים. מאמר מעניין אחד דן בהבדל שבין <a href="http://he.wikipedia.org/wiki/%D7%9E%D7%9E%D7%95%D7%A6%D7%A2">הממוצע</a> ו<a href="http://he.wikipedia.org/wiki/%D7%97%D7%A6%D7%99%D7%95%D7%9F">החציון</a>, והמובנים השונים (והסותרים) שביחס אליהם הם אופטימליים - ייתכן שארחיב על כך בעתיד. הפעם אני רוצה לעסוק בפרדוקס <a href="http://he.wikipedia.org/wiki/%D7%AA%D7%95%D7%A8%D7%AA_%D7%94%D7%94%D7%A1%D7%AA%D7%91%D7%A8%D7%95%D7%AA">הסתברותי</a> שהציג <a href="http://ootips.org/dedel/">עודד לבנה</a> במכתב שכתב למערכת, בתגובה למאמר על פרדוקסים הסתברותיים שלצערי נמצא בחוברת שאינה ברשותי. אני מנחש ניחוש פרוע ש<a href="http://www.gadial.net/2008/02/23/monty_hall/">ה"פרדוקס" של מונטי הול</a> ו<a href="http://www.gadial.net/2008/07/25/envelope_paradox/">פרדוקס המעטפות</a> הם בעלי הסתברות גבוהה להשתייך למאמר המקורי.

הפרדוקס דורש ידע בסיסי כלשהו בהסתברות, אך לא למעלה מכך. הוא הולך כך: נניח שיש לנו כד ובו שלושה כדורים, שכל אחד יכול להיות שחור או לבן, ואנו שולפים כדור באקראי. מה ההסתברות שנשלוף כדור לבן? אם שלושת הכדורים בכד הם לבנים, ההסתברות היא 1; אבל יותר מכך, אם ידוע לנו שההסתברות היא 1, אנחנו יכולים להסיק מכך שכל הכדורים בכד לבנים (הרי אם היה שם כדור שחור, ההסתברות כבר לא הייתה 1).

באופן דומה אפשר להסיק את הטענות המקבילות במקרים האחרים - הסתברות של 2/3 לשליפת כדור לבן מתקיימת אם ורק אם יש בדיוק שני כדורים לבנים בכד; והסתברות של 1/3 - אם ורק אם יש בדיוק כדור לבן אחד בכד. עד כאן הכל טוב ויפה, ואני מבטיח שעדיין לא רימיתי. הרעיון של שימוש במשהו הסתברותי כדי ללמוד מידע "ודאי" על העולם (במקרה הזה אנחנו לומדים מההסתברות לשליפת כדור לבן על המספר האמיתי של הכדורים הלבנים) הוא בסיסי וחשוב במתמטיקה; בפרט, כל השיטה ההסתברותית בקומבינטוריקה מבוססת עליו.

כעת מגיע הטוויסט. אנחנו מבצעים את הניסוי המשונה הבא: מגרילים שני כדורים (שחורים בהסתברות 1/2, לבנים בהסתברות 1/2) וזורקים אותם לכד בלי להביט בהם - בפועל אפשר לעשות זאת על ידי כך שמכינים בצד שני כדים, כל אחד עם כדור לבן וכדור שחור אחד, שולפים באקראי כדור מכל כד ומעבירים אותו מבלי להביט בו. כעת אנחנו מוסיפים כדור לבן לכד עם שני הכדורים האקראיים. יש שלוש אפשרויות שונות להתפלגות הכדורים בכד הזה:
<ol>
	<li>שלושה כדורים לבנים, בהסתברות 1/4 (רק אם שני הכדורים שהוגרלו היו לבנים).</li>
	<li>שני כדורים לבנים ואחד שחור, בהסתברות 1/2 (אם אחד משני הכדורים שהוגרלו היה לבן והשני שחור; יש שתי אפשרויות כאן - או שהגרלנו את השחור מהכד הימני, או שהגרלנו אותו דווקא מהכד השמאלי)</li>
	<li>כדור לבן אחד ושני שחורים, בהסתברות 1/4 (בדומה למקרה 1).</li>
</ol>
אחלה. כעת, מה ההסתברות שנשלוף מהכד הזה כדור לבן? זה תרגיל פשוט בהסתברות מותנה: אם אנחנו במקרה 1, אז בהסתברות 1 נשלוף לבן, ולכן ההסתברות של "אנחנו במקרה 1 וגם שלפנו לבן" היא 1/4. בדומה, ההסתברות של "אנחנו במקרה 2 וגם שלפנו לבן" היא חצי כפול שני שליש (שני שליש היא ההסתברות שנשלוף לבן בהינתן שיש שני לבנים ושחור אחד), כלומר שליש. ההסתברות של "אנחנו במקרה 3 וגם שלפנו לבן" היא 1/12, מאותם שיקולים שכבר ראינו. סכום כל ההסתברויות הללו הוא בדיוק ההסתברות של "שלפנו לבן" - וחישוב קצר יראה שהסכום הזה הוא 2/3. כלומר, על פי האבחנה שראינו בהתחלה, נובע מכך שבכד שלנו יש בדיוק שני כדורים לבנים - אבל מי מבטיח את זה? הרי גם אפשרויות 1 ו-3 הן סבירות! מה הולך כאן?

זה השלב שבו כדאי לעצור ולחשוב, ואני מביא קומיקס של <a href="http://xkcd.com/">xkcd</a> כאתנחתא.

<img src="http://imgs.xkcd.com/comics/how_it_works.png" width="410" height="211" />

כמו כל פרדוקס, הבעיה כאן היא שנפלה טעות כלשהי בהנחות שלנו אך אשלייה אופטית כלשהי מונעת מאיתנו להבחין בה. וכמו בפרדוקסים הסתברותיים אחרים, הבעיה היא בדיוק בשלב שבו אנו מנסים למצוא משמעות "אמיתית" לתכונות המתמטיות של האובייקטים שאנו עוסקים בהם. בפרדוקס המעטפות ניסינו להסיק מתוחלת משהו על "האם כדאי להחליף"; כאן אנחנו מנסים להסיק משהו על "כמה כדורים לבנים יש בתיבה", וזו ההסקה הבעייתית. העניין הוא שצריך להבדיל בין שני מקרים שונים מהותית:
<ol>
	<li>נתונה תיבה שבה כדורים לבנים ושחורים, שלושה במספר בסה"כ. ידוע שאם שולפים כדור באקראי מהתיבה, ההסתברות לשלוף כדור לבן היא 2/3. נובע מכך שיש בתיבה בדיוק שני כדורים לבנים.</li>
	<li>נתון תהליך אקראי שמייצר תיבה. זה שידוע שיש הסתברות של 2/3 לשלוף כדור לבן ממנה לא מבטיח כלום לגבי הרכב הכדורים שלה.</li>
</ol>
הרמאות שלי הייתה ששכנעתי אתכם (נניח...) בנכונות טענה 1 (שהיא נכונה לגמרי) אבל אחר כך השתמשתי בה כדי לכסות מקרה מסוג 2, שבו לא עוסקים בתיבה אחת, קונקרטית, שהיא הבסיס למרחב ההסתברות שלנו, אלא בתיבה "אקראית", שהיא פועל יוצא של הגרלות שהן-הן הבסיס למרחב ההסתברות שלנו. אם ננסה לכתוב פורמלית את ההוכחה שמאחורי מקרה 1, נראה די מהר שאנחנו נתקעים כאשר מרחב ההסתברות והתיבה לא חד הם; אבל, וזו הנקודה המהותית ביותר - כשעוסקים בהסתברות, לפעמים מסתפקים רק בתיאור ה"מילולי" של דברים ולא נכנסים לפרטים המדוייקים. וזה, כפי שהפרדוקס בא להדגים, מסוכן מאוד מאוד.

למי שטרם נחה דעתו מהסבר ה"תהליך", עודד לבנה מביא דוגמה נוספת שמבהירה את העניין עוד יותר. נניח שבמקום תהליך יצירת הכד המורכב שהצגנו קודם, עושים משהו פשוט יותר: יש שני כדים מלאים כדורים לבנים, וכד אחד מלא כדורים שחורים. בוחרים אחד מהכדים באקראי. עכשיו שולפים כדור. מה ההסתברות שנשלוף כדור לבן? כמובן, היא 2/3; אבל ברור שהכד שיש לנו לעולם לא יהיה "שני כדורים לבנים וכדור שחור אחד" - ייתכן שכל הכדים מכילים מיליארד כדורים (בשניים מהם לבנים, ובאחד מהם שחורים).

אם כן, לסיכום: ניתן בהסתברות להסיק מידע דטרמיניסטי על מרחב ההסתברות שלנו מכך שאנו יודעים את ההסתברות של מאורע מסויים. עם זאת, כאשר הבעיה שלנו היא מילולית, צריך להיזהר שלא לבחור רק חלק אחד ממרחב ההסתברות ולהתייחס אליו כאילו הוא הכל. הצגתי דבר דומה גם בפוסט שעסק בבעיה המורחבת של מונטי הול, עם השומר והאסירים, שבה ה"הגרלה" שמבצע השומר (ובכלל לא שמים אליה לב בניסוח הפשוט של השאלה) היא חלק חשוב מאוד ממרחב ההסתברות.
