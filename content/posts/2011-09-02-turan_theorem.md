---
id: 1313
title: "משפט טורן והולדת תורת הגרפים האקסטרמלית"
date: 2011-09-02 21:00:59
layout: post
categories: 
  - קומבינטוריקה
  - תורת הגרפים
tags: 
  - גרפים
  - משפט טורן
  - תורת הגרפים האקסטרמלית
  - תורת רמזי
---
<a href="http://www.gadial.net/2011/08/03/ramsey_theorem/">לא מזמן</a> כתבתי פוסט על משפט רמזי שעסק בשאלה כמה גדולה צריכה להיות קבוצת ילדים על מנת שתיווצר בה קבוצה מגודל מסויים שכולם בה חברים או כולם בה לא חברים. זה היה מקרה פרטי של השאלה שבה עוסקים בתורת רמזי - כמה גדול צריך להיות אובייקט מתמטי כלשהו לפני שתצוץ בו תכונה מסויימת.

הפעם אני רוצה לעסוק בתחום דומה בקומבינטוריקה (תת-תחום של תורת רמזי? המעמד הרשמי לא ממש חשוב) - תורת הגרפים האקסטרמלית. כפי שניתן לנחש, האובייקטים שלנו כאן הם <a href="http://www.gadial.net/2008/05/06/eulerian_graphs/">גרפים</a> (אבל נו באמת - איזה אובייקט ביקום לא ניתן לתיאור על ידי גרף?) ואנחנו רוצים להבין את תכונותיהם של הגרפים הקיצוניים ביותר שמקיימים (או שלא מקיימים) תכונה כלשהי. באופן קצת יותר קונקרטי, עבור תכונה {% equation %}\Phi{% endequation %} כלשהי של גרפים, שאלה מרכזית היא זו: מה המספר המקסימלי של קשתות שגרף עם {% equation %}n{% endequation %} צמתים יכול להכיל ועדיין לקיים את התכונה {% equation %}\Phi{% endequation %}? המספר הזה מסומן לרוב כ-{% equation %}\mbox{ex}\left(n,\Phi\right){% endequation %} (אפשר לחשוב עליו כפונקציה של {% equation %}n{% endequation %} עם פרמטר {% equation %}\Phi{% endequation %}). לא תמיד אפשר לדעת במדויק את {% equation %}\mbox{ex}\left(n,\Phi\right){% endequation %}, כמובן, ולרוב מסתפקים בהערכה.

המקרה המעניין הראשון הוא זה שבו {% equation %}\Phi{% endequation %} היא התכונה "להכיל תת-גרף מסויים". אז אנחנו שואלים את השאלה הקלאסית של תורת רמזי - מתי אובייקט הוא גדול דיו כדי שמבנה מסויים יצוץ בתוכו לבטח? ומשפט טורן מטפל בתת גרף פשוט במיוחד: קליק. קליק מגודל {% equation %}t{% endequation %}, שאותו אסמן ב-{% equation %}K_{t}{% endequation %}, הוא פשוט קבוצה של {% equation %}t{% endequation %} צמתים שכולם מחוברים אלה לאלה בקשתות. שימו לב להבדל בין זה ומשפט רמזי, שמדבר על מספר ה<strong>צמתים</strong> שצריך להיות בגרף לפני שיצוץ בו קליק מגודל מסויים או קבוצה בלתי תלויה מגודל מסויים; כאן מספר הצמתים {% equation %}n{% endequation %} קבוע ונתון מראש ואנחנו רוצים לדעת מה מספר הקשתות; ולהבדיל ממשפט רמזי, כאן אנחנו יודעים את {% equation %}\mbox{ex}\left(n,K_{t}\right){% endequation %} במדויק וגם יודעים בדיוק איך הגרפים הקיצוניים (בעלי המספר המקסימלי של קשתות ש<strong>אינם</strong> מכילים את {% equation %}K_{t}{% endequation %}) נראים.

בואו נתחיל עם מקרה פרטי שהיה ידוע בימיו של טורן - {% equation %}K_{3}{% endequation %}, משולש. השאלה הראשונה, שעליה אתם יכולים לחשוב בעצמכם, היא איך אפשר לבנות גרף "גדול" (כלומר, עם הרבה קשתות - {% equation %}n{% endequation %} קבוע, זוכרים?) שעדיין לא יכיל משולש. אספיילר אותה כעת מייד אז מי שרוצה לחשוב בעצמו, שיפסיק לקרוא.

התעלול הוא להשתמש במה שנקרא "גרף דו צדדי". גרף דו צדדי הוא כזה שניתן לחלק את צמתיו לשתי קבוצות - הטובים והרעים - כך שכל צומת שייך לאחת מהקבוצות, וכל קשת בהכרח מחברת בין טוב ורע; אין קשת בין שני טובים, או קשת בין שני רעים. בגרף כזה לא יכול להיות משולש, כי בקבוצה של שלושה קודקודים יש שני טובים (שאינם מחוברים בקשת) או שני רעים (שאינם מחוברים בקשת). מצד שני, בגלל שאנחנו יודעים שבגרף דו צדדי מובטח לנו שלא יהיה משולש אנחנו יכולים להתפרע ולהוסיף כמה קשתות שבא לנו כל עוד הן לא מחברות שני טובים או שני רעים. באופן כללי אם יש {% equation %}a{% endequation %} טובים ו-{% equation %}b{% endequation %} רעים וכל טוב מחובר לרע בקשת יהיו לנו {% equation %}ab{% endequation %} קשתות בגרף. מכיוון ש-{% equation %}n=a+b{% endequation %}, זה אומר שיהיו לנו {% equation %}a\left(n-a\right)=na-a^{2}{% endequation %} קשתות בגרף, והשאלה היא איזה ערך של {% equation %}a{% endequation %} ייתן לנו את המקסימום. <a href="http://www.gadial.net/2011/01/16/derivative_and_extremal_problems_1-2/">קצת חשבון דיפרנציאלי</a> (אני לא אומר שאין דרכים אחרות, ועוד נראה כאלו) נותן בקלות את התשובה הלא מפתיעה - {% equation %}a=\frac{n}{2}{% endequation %} (אם {% equation %}n{% endequation %} אי זוגי מעגלים כלפי מטה או מעלה, זה לא משנה). כלומר המספר המקסימלי של קשתות מתקבל כאשר מחלקים את הגרף לשתי קבוצות שוות של צמתים, ואז יהיו {% equation %}\frac{n^{2}}{4}{% endequation %} קשתות. כלומר, {% equation %}\mbox{ex}\left(n,K_{3}\right)=\frac{n^{2}}{4}{% endequation %}. כל זה היה ידוע בימיו של טורן; המשפט שלו הוא פשוט הכללה רדיקלית שנותנת את {% equation %}\mbox{ex}\left(n,K_{t}\right){% endequation %}לכל {% equation %}t{% endequation %}.

כדי לפשט טיפה את הסימונים מכאן ואילך אניח שאנחנו מנסים למצוא את {% equation %}\mbox{ex}\left(n,K_{t+1}\right){% endequation %}; עוד שניה יהיה ברור לכולם למה עדיף לדבר על {% equation %}t+1{% endequation %} כאן.

הצעד הראשון הוא לנסות ולבנות גרפים גדולים ככל האפשר שאינם מכילים קליק מגודל {% equation %}t+1{% endequation %}. ממש מתבקש להכליל כאן את הרעיון שכבר הצגתי - במקום גרף דו-צדדי, לקחת גרף {% equation %}t{% endequation %} צדדי, כלומר כזה שבו הצמתים מחולקים ל-{% equation %}t{% endequation %} קבוצות ואין קשת בין שני חברי אותה קבוצה (אבל כל צומת מקבוצה מסויימת יכול להיות מחובר לכל צומת מכל קבוצה אחרת). ההוכחה שאין בגרף כזה קליק מגודל {% equation %}t+1{% endequation %} זהה: אם יש {% equation %}t+1{% endequation %} צמתים יש לפחות שני צמתים מאותה קבוצה (זהו עקרון שובך היונים בפעולה) ולכן זוג צמתים בלי קשת ביניהם).

כמקודם, די ברור שכדאי לבחור את כל הקבוצות מאותו הגודל בדיוק, ככל שזה אפשרי. למי שזה בכל זאת לא ברור לו, הנה הוכחה בנפנוף ידיים: אם בקבוצה של הטובים יש יותר צמתים מבקבוצה של הרעים, ו-{% equation %}v{% endequation %} הוא צומת בקבוצה של הרעים, רק נאבד קשתות אם נעביר אותו לקבוצה של הטובים: מספר הקשתות שנאבד הוא כמספר הקשתות שבהן {% equation %}v{% endequation %} חובר לטובים (עכשיו הוא לא יהיה מסוגל להיות מחובר אליהן), כלומר כמספר הטובים; ומספר הקשתות שנרוויח הוא כמספר הרעים <strong>פחות אחד</strong> כי הם איבדו את {% equation %}v{% endequation %}. כלומר, הפסדנו יותר משהרווחנו. כעת, אם {% equation %}v{% endequation %} שייך לטובים דווקא אז כשנעביר אותו נאבד קשתות כמספר הרעים, ונרוויח קשתות כמספר הטובים פחות אחד. במקרה הגרוע ביותר לא הרווחנו כלום (אם ההפרש בין הקבוצות הוא בדיוק אחד) ואחרת הרווחנו.

לצורך פשטות נניח מכאן ואילך ש-{% equation %}t{% endequation %} מחלק את {% equation %}n{% endequation %}, אחרת סתם הסימונים שלנו יהיו מסורבלים בהרבה. במקרה הזה, כל הקבוצות יהיו מאותו גודל - {% equation %}\frac{n}{t}{% endequation %}. כמה קשתות יהיו? כמו שראינו קודם, בין כל שתי קבוצות של צמתים מחברות {% equation %}\frac{n^{2}}{t^{2}}{% endequation %} קשתות; ויש לנו {% equation %}{t \choose 2}=\frac{t\left(t-1\right)}{2}{% endequation %} זוגות (למי שלא מכיר את הסימון הזה - <a href="http://www.gadial.net/2010/06/22/newton_binom/">נעים להכיר</a>). לכן יש בסך הכל {% equation %}\frac{t\left(t-1\right)}{2}\cdot\frac{n^{2}}{t^{2}}=\frac{t-1}{t}\frac{n^{2}}{2}=\left(1-\frac{1}{t}\right)\frac{n^{2}}{2}{% endequation %} קשתות.

כעת אפשר לנסח את משפט טורן. פורמלית, הוא אומר ש-{% equation %}\mbox{ex}\left(n,K_{t+1}\right)=\left(1-\frac{1}{t}\right)\frac{n^{2}}{2}{% endequation %}, אבל ניסוחים כאלו הם אחד מהדברים השנואים עלי במתמטיקה. לא כי הוא לא נכון או לא מדויק או כל דבר אחר, אלא כי אם זה מה שתראו למישהו מבחוץ הוא לא יבין את הקטע. אוקיי, אז יש לנו איזו נוסחה לא יפה במיוחד עבור {% equation %}\mbox{ex}\left(n,K_{t+1}\right){% endequation %}, אז מה? הפואנטה כאן לטעמי היא שמשפט טורן אומר שהגרפים האקסטרמליים במקרה הזה הם אכן הגרפים ה-{% equation %}t{% endequation %} צדדיים שבנינו - דרך הרבה יותר ציורית ויפה להבין את המספר {% equation %}\left(1-\frac{1}{t}\right)\frac{n^{2}}{2}{% endequation %} (כמובן, לערך המספרי יש חשיבות ביישומים של המשפט). כך זה תמיד במתמטיקה - המטרה היא לא איזו נוסחה סגורה מפוצצת, אלא ה<strong>הבנה של התופעה</strong> שמאחורי הנוסחה (הבנה שלא תהיה שלמה עד שההוכחות לא יסייעו לנו להבין <strong>למה</strong> הגרפים ה-{% equation %}t{% endequation %} צדדיים הם אכן אקסטרמליים).

אני רוצה להציג שלוש הוכחות למשפט. הראשונה של טורן עצמו שהיא פשוטה ויפה וברורה. השניה של אלון וספנסר שהיא קסם וודו מוחלט, אבל ממחישה יפה את כוחה של השיטה ההסתברותית (שאלון וספנסר כתבו את הספר עליה, תרתי משמע). והשלישית היא אלמנטרית לחלוטין, מבהירה מיידית ובצורה מוחלטת למה הגרפים ה-{% equation %}t{% endequation %} צדדיים הם האקסטרימליים, ולא ברור מי המציא אותה. כל ההוכחות מגיעות מהספר <a href="http://en.wikipedia.org/wiki/Proofs_from_THE_BOOK">Proofs from THE BOOK</a> שכולל גם שתי הוכחות שלא אראה כאן.

ראשית, ניסוח מדויק של המשפט שכוחו יפה גם ל-{% equation %}n{% endequation %} שלא מתחלק על ידי {% equation %}t{% endequation %}: אם {% equation %}G{% endequation %} הוא גרף בעל {% equation %}n{% endequation %} צמתים ואין בו קליק מגודל {% equation %}t+1{% endequation %} (כאשר {% equation %}t\ge2{% endequation %}), אז מספר הקשתות ב-{% equation %}G{% endequation %} הוא לא יותר מ-{% equation %}\left(1-\frac{1}{t}\right)\frac{n^{2}}{2}{% endequation %}.

נתחיל עם טורן. טורן מוכיח את המשפט באינדוקציה על {% equation %}n{% endequation %}, כש-{% equation %}t{% endequation %} קבוע. כל עוד {% equation %}n\le t{% endequation %} אז לא משנה אילו קשתות יהיו בגרף, לא יוכל להיות בו קליק מגודל {% equation %}t+1{% endequation %} כי אין מספיק צמתים; לכן צריך לוודא שמספר הקשתות הכולל בגרף לא יכול לעלות על החסם. מספר הקשתות המקסימלי האפשרי בגרף עם {% equation %}n{% endequation %} צמתים הוא {% equation %}\frac{n\left(n-1\right)}{2}{% endequation %}, ובעזרת אי השוויון {% equation %}n\le t{% endequation %} מקבלים:

{% equation %}\frac{n\left(n-1\right)}{2}\le\left(t-1\right)\frac{n}{2}\le\frac{t-1}{t}\cdot\frac{n^{2}}{2}=\left(1-\frac{1}{t}\right)\frac{n^{2}}{2}{% endequation %}

כך שעם זה סיימנו. החלק המעניין הוא לטפל במקרה שבו {% equation %}n&gt;t{% endequation %}. מספיק להראות שבגרף עם מספר קשתות מקסימלי (ביחס לתכונה "לא מכיל את {% equation %}K_{t+1}{% endequation %}) מתקיים החסם הנדרש, כי לכל גרף אחר אפשר להוסיף קשתות עד שמגיעים לגרף מקסימלי שכזה. גרף מקסימלי שכזה בהכרח יכיל את {% equation %}K_{t}{% endequation %} (כי אם לא, הוא לא היה מקסימלי; הוספה של קשת לא הייתה יכול ליצור את {% equation %}K_{t+1}{% endequation %} כי מ-{% equation %}K_{t+1}{% endequation %} אפשר לקבל את {% equation %}K_{t}{% endequation %} על ידי הסרה של קשת אחת וסילוק אחד הצמתים שמחוברים אליה). הרעיון הוא כעת לחלק את הגרף לשני חלקים: {% equation %}A{% endequation %} תהיה קבוצת הצמתים של הקליק מגודל {% equation %}t{% endequation %} הזה, ו-{% equation %}B{% endequation %} תהיה קבוצת שאר הצמתים.

ב-{% equation %}A{% endequation %} יש בדיוק {% equation %}{t \choose 2}{% endequation %} קשתות שהרי בין כל זוג צמתים שם יש קשת. על {% equation %}B{% endequation %} אנחנו יכולים להשתמש בהנחת האינדוקציה כי מספר הצמתים בה קטן מ-{% equation %}n{% endequation %}, כך שאנחנו יודעים שיש בה לכל היותר {% equation %}\left(1-\frac{1}{t}\right)\frac{\left(n-t\right)^{2}}{2}{% endequation %} קשתות. אילו עוד קשתות יכולות להתקיים בגרף? כאלו שמחברות את {% equation %}A{% endequation %} עם {% equation %}B{% endequation %}. כל צומת ב-{% equation %}B{% endequation %} יכולה להתחבר כמעט לכל הצמתים של {% equation %}A{% endequation %}, אבל רק כמעט; אם היא תתחבר לכל הצמתים של {% equation %}A{% endequation %}, אז היא יחד עם {% equation %}A{% endequation %} יהוו קליק מגודל {% equation %}t+1{% endequation %}. לכן כל צומת מ-{% equation %}B{% endequation %} מחוברת בקשת לכל היותר ל-{% equation %}t-1{% endequation %} צמתים מ-{% equation %}A{% endequation %}. אלו כל האבחנות שצריך, והיתר הוא חשבון מכולת. אנחנו מקבלים שמספר הקשתות הכולל בגרף חסום על ידי:

{% equation %}{t \choose 2}+\left(1-\frac{1}{t}\right)\frac{\left(n-t\right)^{2}}{2}+\left(n-t\right)\left(t-1\right){% endequation %}

אחרי סידור מחדש קטן מקבלים שזה שווה ל:

{% equation %}\left(t-1\right)\left[\frac{t}{2}+\frac{\left(n-t\right)^{2}}{2t}+\left(n-t\right)\right]=\left(t-1\right)\left[\frac{t}{2}+\frac{\left(n-t\right)\left(n+t\right)}{2t}\right]{% endequation %}

{% equation %}=\left(t-1\right)\left[\frac{t^{2}+n^{2}-t^{2}}{2t}\right]=\left(1-\frac{1}{t}\right)\frac{n^{2}}{2}{% endequation %}

כמו קסם, קיבלנו לבסוף בדיוק את החסם שרצינו.

כמובן, אין כאן שום קסם אמיתי, זה היופי בהוכחה הזו - התוצאה חייבת להתקבל, אין מנוס מכך. יש לנו כאן דוגמה קלאסית להוכחה באינדוקציה: ראשית, טורן מזהה מרכיב כלשהו ש<strong>חייב</strong> להופיע בגרף אקסטרימלי כלשהו ({% equation %}K_{t}{% endequation %}). האבחנה הזו היא המפתח לנצחון, ומאותו רגע ההמשך מתבקש: לפרק את הגרף, למתוח כמה קשתות שרק אפשר בין הרכיבים, ולהשתמש בהנחת האינדוקציה על מה שנשאר. בעצם טורן מראה כאן ש-{% equation %}\mbox{ex}\left(n,K_{t+1}\right){% endequation %} מקיים את נוסחת הנסיגה {% equation %}\mbox{ex}\left(n,K_{t+1}\right)=\mbox{ex}\left(n-t,K_{t+1}\right)+{t \choose 2}+\left(n-t\right)\left(t-1\right){% endequation %} עבור {% equation %}n&gt;t{% endequation %}, רק שכאן אין לנו צורך לפתור את הנוסחה הזו כי כבר היה לנו ניחוש מוצלח לגבי הערך של {% equation %}\mbox{ex}\left(n,K_{t+1}\right){% endequation %} מלכתחילה (בסיטואציות קומבינטוריות אחרות לא יהיה לנו כזה ואז נוסחת נסיגה שכזו תעזור גם להבין מה בדיוק הערך שאנחנו מחפשים).

נעבור כעת להוכחה השניה, של אלון וספנסר. הם לוקחים גרף כלשהו {% equation %}G{% endequation %} בעל {% equation %}n{% endequation %} צמתים שמסומנים לצורך נוחות ב-{% equation %}v_{1},\dots,v_{n}{% endequation %}, מסמנים ב-{% equation %}d_{i}{% endequation %} את הדרגה של הצומת {% equation %}v_{i}{% endequation %}, כלומר מספר הקשתות שמחוברות אליו. כעת, אם נסמן ב-{% equation %}\omega\left(G\right){% endequation %} את גודל הקליק הגדול ביותר ב-{% equation %}G{% endequation %}, אלון וספנסר טוענים שמתקיים:

{% equation %}\omega\left(G\right)\ge\sum_{i=1}^{n}\frac{1}{n-d_{i}}{% endequation %}

זו טענה דטרמיניסטית למהדרין, ומרגע שיש לנו אותה המשך ההוכחה נובע באופן טבעי. קודם נראה איך הטענה הזו מסיימת את ההוכחה, ואז נעבור להוכיח אותה עצמה - ההוכחה של הטענה תהיה מבוססת על השיטה ההסתברותית.

אז איך הטענה מסיימת את ההוכחה? כאן שולפים כלי מתמטי סטנדרטי מהשרוול - אי שוויון קושי-שוורץ. לאי השוויון הזה מספר ניסוחים ואבחר את הניסוח הפשוט יחסית שרלוונטי עבורנו: אם {% equation %}a_{1},\dots,a_{n}{% endequation %} ו-{% equation %}b_{1},\dots,b_{n}{% endequation %} הן סדרות מספרים אז:

{% equation %}\left(\sum_{i=1}^{n}a_{i}b_{i}\right)^{2}\le\left(\sum_{i=1}^{n}a_{i}^{2}\right)\left(\sum_{i=1}^{n}b_{i}^{2}\right){% endequation %}

ובמילים: ריבוע סכום המכפלות של אברי הסדרות קטן או שווה למכפלת סכום הריבועים של אברי הסדרות. לטעמי זה עוד אחד מהמקרים שבהם הנוסחה הרבה יותר קלה לקריאה מהניסוח המילולי.

השימוש כאן בקושי-שוורץ הוא פשוט יחסית. נבחר {% equation %}a_{i}=\sqrt{n-d_{i}}{% endequation %} ו-{% equation %}b_{i}=\left(\sqrt{n-d_{i}}\right)^{-1}{% endequation %}, נציב בנוסחה ונקבל:

{% equation %}n^{2}\le\left(\sum_{i=1}^{n}\left(n-d_{i}\right)\right)\left(\sum_{i=1}^{n}\frac{1}{n-d_{i}}\right)\le\omega\left(G\right)\sum_{i=1}^{n}\left(n-d_{i}\right){% endequation %}

עכשיו יש לנו עוד שני תעלולים לשלוף מהשרוול: ראשית, אנחנו מניחים ש-{% equation %}\omega\left(G\right)\le t{% endequation %} - זו ההנחה הבסיסית שלנו, לפיה הגרף לא מכיל את הקליק {% equation %}K_{t+1}{% endequation %}. שנית, יש לנו דרך לקשר בין הדרגות של כל הצמתים בגרף ובין מספר הקשתות בו. אם מספר הקשתות הוא {% equation %}e{% endequation %}, אז בכל גרף (סופי) שהוא מתקיים השוויון {% equation %}2e=\sum_{i=1}^{n}d_{i}{% endequation %}, שכן כל קשת בגרף תורמת 1 לדרגות של שני הצמתים שהיא מחוברת אליהם. מכל אלה אפשר להסיק כעת:

{% equation %}n^{2}\le t\cdot\left(n^{2}-2e\right){% endequation %}

וכל שנשאר הוא ללהטט קצת כדי לחלץ את {% equation %}e{% endequation %}. פתיחת סוגריים, העברת אגפים, ונקבל:

{% equation %}2et\le n^{2}\left(t-1\right){% endequation %}

חלוקה ונקבל:

{% equation %}e\le\left(1-\frac{1}{t}\right)\frac{n^{2}}{2}{% endequation %}

בדיוק מה שרצינו.

בינתיים זה היה טכני ולא הכי מעניין, אני חייב להודות; לב ההוכחה הוא בטענה {% equation %}\omega\left(G\right)\ge\sum_{i=1}^{n}\frac{1}{n-d_{i}}{% endequation %} וההוכחה ההסתברותית שלה שאציג כעת.

במבט ראשון לא ברור איך הסתברות יכולה להשתחל לכאן. הגרף {% equation %}G{% endequation %} נתון וקבוע; מה בדיוק נגריל ואיך? הרעיון של אלון וספנסר הוא להגריל <strong>סדר</strong> על הצמתים - פורמלית, פרמוטציה {% equation %}\pi{% endequation %} כלשהי שלהם, כשכל פרמוטציה נבחרת בהסתברות שווה, {% equation %}\frac{1}{n!}{% endequation %}. נניח שהצמתים {% equation %}v_{1},\dots,v_{n}{% endequation %} כבר מסודרים על פי הפרמוטציה הזו, ונגדיר קבוצת צמתים {% equation %}C_{\pi}{% endequation %} שמכילה את כל הצמתים {% equation %}v_{i}{% endequation %} שמחוברים בקשת לכל הצמתים שבאים לפניהם בפרמוטציה, כלומר לכל {% equation %}v_{j}{% endequation %} כך ש-{% equation %}j&lt;i{% endequation %}.

הנקודה המהותית כאן היא ש-{% equation %}C_{\pi}{% endequation %} היא <strong>קליק</strong>. למה? ובכן, קחו ב-{% equation %}C_{\pi}{% endequation %} את הצומת עם האינדקס המקסימלי; על פי הגדרה, הוא מחובר לכל הצמתים עם אינדקס קטן יותר ובפרט לכל צמתי {% equation %}C_{\pi}{% endequation %}. כעת קחו את הצומת המקסימלי הבא בתור... הבנתם את הרעיון.

יפה, אז הצלחנו להגדיר איכשהו מרחב הסתברות שמערב קליקים. אנחנו מעוניינים בחסם כלשהו על גדלי הקליקים, אז נגדיר <strong>משתנה מקרי</strong> {% equation %}X=\left|C_{\pi}\right|{% endequation %} - גודל {% equation %}C_{\pi}{% endequation %}. בגלל האופן שבה {% equation %}C_{\pi}{% endequation %} נבנתה, קל לפרק את {% equation %}X{% endequation %} לסכום של אינדיקטורים (משתנים מקריים שמקבלים 0 או 1 בלבד): {% equation %}X=\sum_{i=1}^{n}X_{i}{% endequation %} כאשר {% equation %}X_{i}{% endequation %} מקבל 1 אם {% equation %}v_{i}{% endequation %} מחובר בקשת לכל הצמתים שקדמו לו.

כעת השאלה הפשוטה היא - מה ההסתברות ש-{% equation %}X_{i}=1{% endequation %}? מכיוון שכל הקשתות כבר נקבעו, זה תלוי בדרגה של {% equation %}v_{i}{% endequation %}: אם {% equation %}v_{i}{% endequation %} מחובר ל-{% equation %}d_{i}{% endequation %} צמתים, ההסתברות לכך שכל הצמתים שיהיו לפני {% equation %}v_{i}{% endequation %} בפרמוטציה יהיו מתוך {% equation %}d_{i}{% endequation %} הצמתים שהוא מחובר אליהם היא בעצם ההסתברות שמבין כל {% equation %}n-d_{i}{% endequation %} הצמתים שאינם מחוברים אל {% equation %}v_{i}{% endequation %}, כולל {% equation %}v_{i}{% endequation %} עצמו, יהיה זה {% equation %}v_{i}{% endequation %} שמופיע ראשון. מכיוון שיש סימטריה בין כל {% equation %}n-d_{i}{% endequation %} הצמתים הללו, ההסתברות לכך היא {% equation %}\frac{1}{n-d_{i}}{% endequation %} (אתם מוזמנים לעשות חישוב פורמלי אם לא שוכנעתם).

זה מסיים את העניין אם זוכרים מה קורה בדרך כלל בשלב הזה בשיטה ההסתברותית. תוחלת של אינדיקטור היא ההסתברות שהוא יקבל 1, כלומר {% equation %}\mbox{E}\left[X_{i}\right]=\frac{1}{n-d_{i}}{% endequation %}. לינאריות התוחלת נותנת לנו כעת

{% equation %}\mbox{E}\left[X\right]=\mbox{E}\left[\sum_{i=1}^{n}X_{i}\right]=\sum_{i=1}^{n}\mbox{E}\left[X_{i}\right]=\sum_{i=1}^{n}\frac{1}{n-d_{i}}{% endequation %}

ואנחנו מסיימים כי במרחב ההסתברות שלנו חייב להיות איבר שנותן ל-{% equation %}X{% endequation %} לפחות את ערך התוחלת שלו, כלומר קליק שגודלו לפחות {% equation %}\sum_{i=1}^{n}\frac{1}{n-d_{i}}{% endequation %}.

שלא יהיה לכם ספק; אני לא מקבל שום אינטואיציה ל"מה הולך פה" מההוכחה הזו. היא פשוט מגניבה.

נעבור כעת להוכחה השלישית, שכנראה מבהירה הכי טוב "מה הולך פה". מה שההוכחה מראה הוא שהגרף האקסטרמלי חייב להיות גרף {% equation %}k{% endequation %}-צדדי <strong>כלשהו</strong>. כבר הגענו קודם למסקנה שמבין הגרפים ה-{% equation %}k{% endequation %} צדדיים, הכי טוב הוא גרף {% equation %}t{% endequation %} צדדי שבו כל הצדדים כמעט מאותו גודל (הפרש 1 לכל היותר בין כל שני צדדים), כי אם זה לא כך ניתן להזיז צמתים ולהגדיל את מספר הקשתות (וגרף {% equation %}t+1{% endequation %} צדדי כבר יכיל קליק מגודל {% equation %}t+1{% endequation %}).

גרף {% equation %}k{% endequation %}-צדדי כלשהו מאופיין בדרך כלל על ידי ההגדרה ה"גלובלית" שלפיה "יש חלוקה של צמתי הגרף ל-{% equation %}k{% endequation %} קבוצות, כך ש...". אך למעשה, קיימת גם הגדרה "לוקלית" פשוטה במקרה שבו הגרף מכיל את כל הקשתות האפשריות: גרף הוא {% equation %}k{% endequation %}-צדדי מלא, עבור {% equation %}k{% endequation %} כלשהו, אם לכל זוג צמתים {% equation %}u,v{% endequation %} שמחובר בקשת, וצומת נוסף {% equation %}w{% endequation %}, {% equation %}w{% endequation %} חייב להיות מחובר ל-{% equation %}u{% endequation %} או ל-{% equation %}v{% endequation %}.

הטענה בבירור מתקיימת בגרף {% equation %}k{% endequation %} צדדי מלא - אם {% equation %}u,v{% endequation %} מחוברים בקשת זה אומר שהם לא באותו צד, ולכן לא ייתכן ש-{% equation %}w{% endequation %} יהיה גם בצד של {% equation %}u{% endequation %} וגם בצד של {% equation %}v{% endequation %} בו זמנית, ולכן הוא יהיה מחובר לאחד מהם (הרי הגרף מכיל כל קשת חוקית).

למה אם הטענה נכונה הגרף הוא {% equation %}k{% endequation %} צדדי מלא? ובכן, למי שמכיר את המושג: כי היחס "{% equation %}u,v{% endequation %} לא מחוברים בקשת" הוא יחס שקילות; ולמי שלא מכיר, אפשר לבנות את הצדדים כך - ניקח צומת תמים {% equation %}u{% endequation %}, ונגדיר את "הצד של {% equation %}u{% endequation %}" בתור אוסף כל הצמתים ש-{% equation %}u{% endequation %} לא מחובר אליהם. לא ייתכן שבקבוצה הזו יהיו שני צמתים {% equation %}v,w{% endequation %} שמחוברים בקשת (כי אז העובדה ש-{% equation %}u{% endequation %} לא מחובר לאף אחד מהם סותרת את הטענה שלנו), לכן זה אכן צד חוקי של גרף {% equation %}k{% endequation %} צדדי. בנוסף, אם ניקח צומת {% equation %}v{% endequation %} כלשהו בצד הזה, הוא יהיה חייב להיות מחובר לכל צומת שאינה באותו צד איתו; כי אם יש צומת {% equation %}w{% endequation %} שאינה באותו צד איתו אז על פי הגדרת הצד, {% equation %}w{% endequation %} מחובר ל-{% equation %}u{% endequation %}, ולא ייתכן ש-{% equation %}v{% endequation %} לא יהיה מחובר לא ל-{% equation %}u{% endequation %} ולא ל-{% equation %}w{% endequation %}.

יפה, אז יש לנו אפיון לוקלי פשוט, וכל שצריך להראות הוא שהאפיון מתקיים בגרף האקסטרמלי. נניח בשלילה שהוא לא, אז יש לנו שלושה צמתים בגרף: {% equation %}u,v,w{% endequation %}, כך ש-{% equation %}u,v{% endequation %} מחוברים בקשת ואילו {% equation %}w{% endequation %} לא מחובר לאף אחד מהם. הרעיון הוא לבנות עכשיו מהגרף הקיים גרף חדש שבו יש <strong>יותר</strong> קשתות ואותו מספר צמתים ועדיין אין בו את {% equation %}K_{t+1}{% endequation %}, בסתירה לאקסטרימליות של הגרף שלנו.

איך עושים את זה? פשוט: מעיפים מהגרף את אחד מהצמתים {% equation %}u,v,w{% endequation %} שיש לו מעט קשתות ושמים במקומו עותק של אחד מהצמתים האחרים. אם למשל מתקיים ש-{% equation %}d\left(u\right)&gt;d\left(w\right){% endequation %}, אז נעיף מהגרף את {% equation %}w{% endequation %}; בכך איבדנו {% equation %}d\left(w\right){% endequation %} קשתות. כפיצוי, נוסף לגרף צומת {% equation %}u^{\prime}{% endequation %} שמחובר בדיוק לאותם צמתים ש-{% equation %}u{% endequation %} מחובר אליהם; זה ייתן לנו עוד {% equation %}d\left(u\right){% endequation %} קשתות, כלומר הרווחנו. לא קשה לראות שהוספת {% equation %}u^{\prime}{% endequation %} לגרף לא יכולה ליצור קליק מגודל {% equation %}t+1{% endequation %}: אם יש קליק כזה, אז היה קליק כזה גם בגרף המקורי, רק עם {% equation %}u{% endequation %} במקום {% equation %}u^{\prime}{% endequation %} (לא ייתכן שיש קליק שמערב הן את {% equation %}u{% endequation %} והן את {% equation %}u^{\prime}{% endequation %} יחד, שכן אין קשת ביניהם).

באופן דומה מטפלים במקרה שבו {% equation %}d\left(v\right)&gt;d\left(w\right){% endequation %}. המקרה היחיד שנותר לנו הוא זה שבו {% equation %}d\left(w\right)\ge d\left(u\right),d\left(v\right){% endequation %}. כאן נעיף מהגרף את {% equation %}u,v{% endequation %} שניהם גם יחד ונשים שני עותקים של {% equation %}w{% endequation %}; הסיבה שבגללה נרוויח כך קשת היא שכשמסירים את {% equation %}u,v{% endequation %} לא מאבדים {% equation %}d\left(u\right)+d\left(v\right){% endequation %} קשתות אלא רק {% equation %}d\left(u\right)+d\left(v\right)-1{% endequation %} קשתות, שכן הקשת המשותפת של {% equation %}u,v{% endequation %} מוסרת רק פעם אחת. זה מסיים את ההוכחה הזו.

למשפט יש עוד מספר הוכחות, יפות לא פחות, אבל אני חושב שכבר הבאתי מספיק להפעם; אני מקווה שעכשיו ברור לכל הקוראים "מה הולך שם" וגם למה זה מעניין.
