---
id: 2990
title: "פרדוקס האוטובוס הצפוף"
date: 2013-12-13 16:35:09
layout: post
categories: 
  - הסתברות
  - משחקים וחידות מתמטיות
tags: 
  - התפלגות בינומית
  - התפלגות מולטינומית
  - מתמטיקה היא מדע אמפירי
  - תוצאות לא אינטואיטיביות
---


<p>אהוד אהרוני (שבנוסף למעלליו בפוסט הזה גם <a href="http://www.youtube.com/user/udiprod?feature=watch">יוצר סרטוני וידאו</a> די פנטסטיים למראה) פנה אלי עם סיפור שאותו המציא: ישנה עיירה ובה מפעל, ובכל יום הפועלים נוסעים למפעל באוטובוס. יש 30 פועלים ועומדים לרשותם 3 אוטובוסים שממתינים בחניה, וכל פועל בוחר באקראי לאיזה אוטובוס לעלות (כלומר, לכל אוטובוס יש את אותה הסתברות להיבחר על ידי כל פועל). עבור מתבונן מבחוץ שעוקב אחרי מה שקורה יום אחרי יום, נראה שבתוחלת (כלומר, בממוצע לאורך זמן) כל אוטובוס מכיל 10 אנשים. לעומת זאת, הפועל בוב טוען שחד משמעית, תוחלת מספר האנשים על האוטובוס <strong>שלו</strong> היא גדולה יותר מ-10, כלומר האוטובוס של בוב יותר צפוף ממה שהיה צפוי. ואז באה הפועלת אליס ואומרת שגם אצלה זה ככה!</p>

<p>איך זה ייתכן?</p>

<p>ובכן, אני במבט ראשון לא האמנתי שזה ייתכן ושיערתי שיש כאן בעיה כלשהי בניסוח הסיפור. אז מה עושים במקרים כאלו? כשזה מגיע לשאלות הסתברותיות פשוטות, מתמטיקה יכולה להיות מדע אמפירי לגמרי - אפשר לערוך ניסויים ולראות מה התוצאות שלהן. את הניסויים שלנו אנחנו עורכים בדרך כלל בסימולציית מחשב, אז כתבתי חיש קל סימולציה שכזו שבה פועלים באמת עולים לאוטובוס ואני מודד מה קורה. מדדתי שלושה דברים - את כמות הפעמים שבהן האוטובוס של בוב היה הצפוף ביותר (דהיינו, היו בו ממש יותר אנשים מאשר באוטובוסים האחרים; אם מספר האנשים באוטובוס של בוב היה שווה למספרם באוטובוס אחר, זה לא נחשב), את מספר האנשים הכולל באוטובוס הראשון לאורך כל הימים, ואת מספר האנשים הכולל באוטובוס שבוב היה בו לאורך כל הימים, ואת שלושת המספרים הללו חילקתי במספר הימים של הסימולציה - 100,000. התוצאה: ההסתברות לכך שהאוטובוס של בוב יהיה הצפוף ביותר היא {% equation %}0.3812{% endequation %}; תוחלת מספר האנשים באוטובוס הראשון הייתה {% equation %}10.0076{% endequation %}, ואילו תוחלת מספר האנשים באוטובוס של בוב הייתה {% equation %}10.65412{% endequation %}. במילים אחרות, יש לנו סוג של חוק מרפי הסתברותי: "האוטובוס שאליו אתה עולה יהיה תמיד האוטובוס הצפוף ביותר" (רק לא תמיד אלא בהסתברות כלשהי ש<strong>גדולה</strong> מההסתברות של התפלגות אקראית אחידה).</p>

<p>אוקיי, זה מפתיע.</p>

<p>במבט ראשון היינו מצפים שהמספר הראשון יהיה {% equation %}0.333\dots{% endequation %} - הרי בוב עולה באקראי לאחד מבין שלושת האוטובוסים, אז יש לו הסתברות של שליש לעלות לאוטובוס הצפוף ביותר. אבל כמובן, האינטואיציה הזו שגויה, כי לפעמים בוב <strong>משפיע</strong> על השאלה מהו האוטובוס הצפוף ביותר. זה קורה כאשר יש שני אוטובוסים שמספר האנשים שאינם בוב שעלו אליהם הוא זהה ולאוטובוס השלישי עלו פחות אנשים מאשר לכל אחד משניהם; במקרה הזה, לא משנה איזה משני האוטובוסים בוב יבחר, ההסתברות שלו לבחור את "האוטובוס הצפוף ביותר" תהיה {% equation %}\frac{2}{3}{% endequation %}. בשאר המקרים ההסתברות שלו תהיה תמיד {% equation %}\frac{1}{3}{% endequation %}, כי אם יש רק אוטובוס יחיד עם מספר אנשים גדול ביותר, רק אם בוב יבחר אותו הוא יגיע לאוטובוס הצפוף ביותר.</p>

<p>אם כן, הסיכוי של בוב בכל אחת מהסיטואציות הוא <strong>לפחות</strong> שליש, ובחלק מהסיטואציות הוא <strong>יותר</strong> משליש, ולכן לא מפתיע שהסיכוי שלו בסך הכל להגיע לאוטובוס הצפוף ביותר הוא יותר משליש; אבל לי זה כן נראה מפתיע, ממבט ראשון.</p>

<p>בואו נעבור לדבר קצת על המתמטיקה שמאחורי זה. איך ממדלים מתמטית סיטואציה הסתברותית כמו זו? אני מניח שאתם כבר מכירים את הפורמליזם הסטנדרטי שהמתמטיקאים משתמשים בו כדי לדבר על הסתברות באופן כללי, ואם לא - <a href="http://www.gadial.net/2010/07/29/probability_intro/">יש לי פוסטים על זה</a>. כאן הסיטואציה היא שיש לנו "ניסוי" שמתבצע מספר רב של פעמים בלתי תלויות אחת בשניה. בכל פעם יש לניסוי הזה כמה תוצאות אפשריות, כל אחת עם ההסתברות שלה, ואנחנו מתעניינים בסופו של דבר רק בשאלה כמה תוצאות מכל סוג התקבלו - אין עבורנו חשיבות ל<strong>סדר</strong> שבו הן התקבלו.</p>

<p>בואו נחשוב על מקרה פשוט שבו יש רק שתי תוצאות אפשריות - "הצלחה" או "כשלון". למשל, אנחנו מנסים לקלוע לסל. יש לנו 30 זריקות וההסתברות שלנו לקלוע היא {% equation %}\frac{1}{3}{% endequation %}. עכשיו אפשר לשאול שאלות כמו "מה ההסתברות שנקלע לסל בדיוק 12 פעמים"?</p>

<p>את הסיטואציה הזו מתאר מה שנקרא <strong>משתנה מקרי בינומי</strong>. נהוג לסמן זאת <strong>{% equation %}X\sim\mbox{Bin}\left(n,p\right){% endequation %} </strong>כאשר {% equation %}n,p{% endequation %} הם הפרמטרים שמאפיינים את המשתנה הבינומי הספציפי הזה: {% equation %}n{% endequation %} הוא מספר הניסויים הכולל שמתקיים (זריקות לסל) ו-{% equation %}p{% endequation %} היא ההסתברות שניסוי "יצליח" (קלענו לסל).</p>

<p>עכשיו, נניח שאנחנו לא שואלים "מה ההסתברות שנקלע לסל בדיוק 12 פעמים" אלא שאלה קצת יותר פשוטה: "מה ההסתברות שנקלע לסל בדיוק ב-12 הזריקות הראשונות ואת היתר נחטיא?". התשובה לזה פשוטה ונובעת מעקרון הכפל בהסתברות, שאומר שאם יש לנו סדרה של ניסויים בלתי תלויים ותוצאות ספציפיות לכל אחד מהניסויים הללו, ההסתברות לקבלת סדרת התוצאות הזו היא בדיוק המכפלה של ההסתברות לכל את התוצאה בכל שלב. במקרה שלנו ההסתברות של קליעה היא {% equation %}\frac{1}{3}{% endequation %} וההסתברות של החטאה היא {% equation %}\frac{2}{3}{% endequation %} ולכן ההסתברות הכוללת היא {% equation %}\frac{1}{3}\cdots\frac{1}{3}\cdot\frac{2}{3}\cdots\frac{2}{3}=\left(\frac{1}{3}\right)^{12}\left(\frac{2}{3}\right)^{18}{% endequation %} .</p>

<p>עכשיו, שימו לב שלא הייתה חשיבות ל<strong>סדר</strong> כאן - כלומר, ההסתברות שקיבלנו לא התעניינה בשאלה אם אנחנו קולעים את 12 הסלים בהתחלה או לא. אפשר באותה מידה היה להסתכל על סדרת קליעות אחרת שכוללת בדיוק 12 קליעות מוצלחות, והיינו מקבלים שההסתברות של אותה סדרת קליעות היא עדיין {% equation %}\left(\frac{1}{3}\right)^{12}\left(\frac{2}{3}\right)^{18}{% endequation %}. לכן אפשר להסיק מכך שההסתברות לקלוע 12 סלים לסל <strong>בסדר כלשהו</strong> שווה ל-{% equation %}\left(\frac{1}{3}\right)^{12}\left(\frac{2}{3}\right)^{18}{% endequation %} כפול מספר הסדרות מאורך 30 של אפסים ואחדים שיש בהן בדיוק 12 פעמים 1 ויתר הפעמים 0 (1 מייצג קליעה מוצלחת). מציאת מספר הסדרות הללו היא בעיה קומבינטורית קלה: <a href="http://www.gadial.net/2010/06/20/combinatorics_intro/">כבר ראינו בבלוג</a> שהתשובה היא {% equation %}\frac{30!}{12!18!}{% endequation %}, ולצורך פשטות מסמנים את המספר הזה בסימון {% equation %}{30 \choose 12}{% endequation %} (שנקרא "מקדם הבינום" מסיבות ש<a href="http://www.gadial.net/2010/06/22/newton_binom/">הסברתי פעם בבלוג</a>, ולכן קוראים להתפלגות הזו "בינומית"). לכן ההסתברות לקלוע בדיוק 12 פעמים לסל היא {% equation %}{30 \choose 12}\left(\frac{1}{3}\right)^{12}\left(\frac{2}{3}\right)^{18}{% endequation %}.</p>

<p>מכאן אני מקווה שההכללה ברורה: אם יש לנו משתנה מקרי שמתפלג בינומית עם פרמטרים {% equation %}n,p{% endequation %}, {% equation %}X\sim\mbox{Bin}\left(n,p\right){% endequation %}, אז {% equation %}\mbox{Pr}\left[X=k\right]={n \choose k}p^{k}\left(1-p\right)^{n-k}{% endequation %}. נסו להוכיח לעצמכם את הנוסחה הזו אם אתם לא בטוחים שהיא נכונה!</p>

<p>הבנו איך מחשבים את ההסתברות לערך קונקרטי של משתנה בינומי, עכשיו בואו נדבר על ה<strong>תוחלת</strong> שלו. התוחלת היא במובן מסויים הערך ה"ממוצע" של המשתנה: פורמלית, היא מוגדרת בתור {% equation %}\mbox{E}\left[X\right]=\sum k\cdot\mbox{Pr}\left[X=k\right]{% endequation %} כאשר המשתנה {% equation %}k{% endequation %} רץ על כל הערכים ש-{% equation %}X{% endequation %} יכול לקבל (כאן אני מניח שיש מספר סופי שלהם ולכן לא צריך להטריד את עצמי עם שאלות כמו מה זה סכום של מספר לא סופי של מחוברים). את התוחלת של משתנה בינומי גם כן <a href="http://www.gadial.net/2010/08/14/random_variables/">חישבתי כבר בעבר</a> ולא אחזור על זה כרגע: היא יוצאת ממש פשוטה - {% equation %}np{% endequation %}. דהיינו, קחו את מספר הניסויים שמבצעים וכפלו אותו בהסתברות שניסוי יצליח.</p>

<p>זה מספיק כדי למצוא שניים משלושת המספרים שהסימולציה שלי החזירה. ראשית, כמה אנשים יהיו בממוצע על אוטובוס מס' 1? ובכן, {% equation %}X{% endequation %} שלנו יספור כמה אנשים עלו לאוטובוס הזה. {% equation %}n=30{% endequation %} במקרה שלנו כי יש 30 אנשים שעולים לאוטובוסים, וכל אחד עולה באופן בלתי תלוי בשני כך שזה אכן מתאים לסיטואציה של משתנה בינומי. ההסתברות שמישהו יעלה לאוטובוס מס' 1 דווקא היא {% equation %}p=\frac{1}{3}{% endequation %}. לכן התוחלת יוצאת 10 - אכן, קרוב מאוד למספר שקיבלנו בפועל.</p>

<p>עכשיו לשאלה השניה - מה תוחלת מספר האנשים ב"אוטובוס של בוב"? כאן החישוב צריך להיות קצת שונה. באוטובוס של בוב תמיד יש לפחות את בוב, והשאלה היא מה קורה עם שאר 29 האנשים. כל אחד מהם עולה לאוטובוס של בוב בהסתברות {% equation %}\frac{1}{3}{% endequation %} כמו קודם, כך שהפעם יש לנו 29 ניסויים, ולכן אנחנו מקבלים שלאוטובוס של בוב עולים בתוחלת {% equation %}\frac{29}{3}{% endequation %} אנשים מלבדו. אם רוצים להיות פורמליים, צריך להגדיר משתנה מקרי {% equation %}Y=1+X{% endequation %} כאשר {% equation %}X\sim\mbox{Bin}\left(29,\frac{1}{3}\right){% endequation %} - המשתנה המקרי {% equation %}Y{% endequation %} הזה מתאר את מספר האנשים באוטובוס של בוב. התוחלת שלו שווה ל-</p>

<p>{% equation %}\mbox{E}\left[1+X\right]=1+\mbox{E}\left[X\right]=1+\frac{29}{3}=\frac{32}{3}=10.666\dots{% endequation %}</p>

<p>כאשר כאן השתמשתי בלי הוכחה בכמה עובדות בסיסיות על תוחלת (מה שנקרא <strong>לינאריות התוחלת</strong>). אכן, גם כאן אנחנו רואים שתוצאת הניסוי בפועל הייתה קרובה למספר הצפוי. ושהמספר הצפוי גדול מ-10. חישוב דומה יעבוד, כמובן, גם במקרה הכללי: אם יש לנו {% equation %}N{% endequation %} פועלים ו-{% equation %}k{% endequation %} אוטובוסים אז תוחלת מספר הפועלים באוטובוס מס' 1 היא {% equation %}\frac{N}{k}{% endequation %} אבל תוחלת מספר הפועלים באוטובוס של בוב היא {% equation %}\frac{N+k-1}{k}{% endequation %}.</p>

<p>נותר עדיין להסביר מתמטית את המספר השלישי מבין התוצאות האמפיריות שלי - ההסתברות של 0.38 בערך לכך שבוב יהיה באוטובוס העמוס ביותר. לרוע המזל, אני לא מכיר דרך פשוטה לחשב את ההסתברות הזו שנותנת נוסחה קצרה ויפה (אולי מישהו כן מכיר?), אבל זה כן נותן לי תירוץ להציג את ההכללה של ההתפלגות הבינומית - <strong>התפלגות מולטינומית</strong>.</p>

<p>הרעיון הוא זה: נניח שלניסוי שלנו יש יותר תוצאות מאשר רק "הצלחה/כשלון", ואנחנו רוצים למצוא את ההסתברות עבור כך-וכך תוצאות מכל סוג - שוב, בלי חשיבות לסדר. למשל, נניח שאני זורק כדור לסל ורוצה לספור כמה פעמים קלעתי (בהסתברות {% equation %}\frac{1}{3}{% endequation %}), כמה פעמים הכדור הגיע אל הסל אבל לא נכנס (הסתברות {% equation %}\frac{1}{6}{% endequation %}) וכמה פעמים כל הסיפור הסתיים בצורה מבישה כשהכדור בכלל לא הגיע אל הסל (הסתברות {% equation %}\frac{1}{2}{% endequation %}). לא אלאה אתכם בפרטים אלא אקפוץ להדגמה של מספר סופי: אם אני רוצה לדעת את ההסתברות ל-8 קליעות, 3 החטאות-עם-הגעה-לסל ו-19 החטאות מבישות (שימו לב שהכל מסתכם ל-30), ההסתברות תהיה {% equation %}\frac{30!}{8!3!19!}\left(\frac{1}{3}\right)^{8}\left(\frac{1}{6}\right)^{3}\left(\frac{1}{2}\right)^{19}{% endequation %}. זה נראה כמו הכללה טבעית של הנוסחה שנתתי קודם, רק שהפעם יש לנו שלושה איברים במקום שניים.</p>

<p>כך גם באופן כללי: נניח שיש לנו {% equation %}t{% endequation %} תוצאות אפשריות עם הסתברויות {% equation %}p_{1},\dots,p_{t}{% endequation %} (שמסתכמות ל-1) ואנחנו רוצים לדעת מה ההסתברות לקבל בדיוק {% equation %}k_{1}{% endequation %} תוצאות מסוג מס' 1, {% equation %}k_{2}{% endequation %} תוצאות מסוג מס' 2 וכן הלאה עד {% equation %}k_{t}{% endequation %} תוצאות מסוג מס' {% equation %}t{% endequation %}. נסמן {% equation %}n=\sum_{i=1}^{n}k_{i}{% endequation %} ואז ההסתברות נתונה על ידי הנוסחה {% equation %}\frac{n!}{k_{1}!\cdots k_{t}!}p_{1}^{k_{1}}\cdots p_{t}^{k_{t}}{% endequation %}. בכתיב מקוצר זה יוצא {% equation %}{n \choose k_{1}\dots k_{t}}\prod p_{i}^{_{k}}{% endequation %}.</p>

<p>איך זה קשור לבוב והאוטובוסים? חשבו על מה שאמרתי קודם - ההסתברות שבוב יעלה לאוטובוס העמוס ביותר היא {% equation %}\frac{2}{3}{% endequation %} אם יש שני אוטובוסים בעלי אותו מספר אנשים (חוץ מבוב) והשלישי מכיל פחות אנשים, והיא {% equation %}\frac{1}{3}{% endequation %} בסיטואציות אחרות. לכן, אם {% equation %}q{% endequation %} היא ההסתברות לסיטואציה הראשונה, אז ההסתברות הכוללת שבוב יעלה לאוטובוס העמוס ביותר היא {% equation %}\frac{2}{3}q+\frac{1}{3}\left(1-q\right){% endequation %}. רק צריך לחשב את {% equation %}q{% endequation %}. וכדי לחשב את {% equation %}q{% endequation %} אני משתמש בהתפלגות מולטינומית.</p>

<p>השאלה שאני שואל עכשיו היא זו: איך צריכים 29 אנשים להתחלק לאוטובוסים כך ששני האוטובוסים הראשונים יכילו את אותו מספר אנשים והשלישי יכיל פחות? ובכן, למשל, הם יכולים להתחלק 14 לאוטובוס הראשון, 14 לשני ו-1 לשלישי. נסמן את זה {% equation %}\left(14,14,1\right){% endequation %}. באופן דומה גם {% equation %}\left(13,13,3\right),\left(12,12,5\right),\left(11,11,7\right),\left(10,10,9\right){% endequation %} הן אפשרויות חוקיות, אבל {% equation %}\left(9,9,11\right){% endequation %} כבר לא (כי עכשיו האוטובוס השלישי מכיל את מספר האנשים הגבוה ביותר). עכשיו משתמשים בהתפלגות מולטינומית כדי לדעת מה ההסתברות של כל סיטואציה כזו, ומקבלים את הזוועה הבאה:</p>

<p>{% equation %}\left(\frac{30!}{14!14!1!}\frac{30!}{13!13!3!}+\frac{30!}{12!12!5!}+\frac{30!}{11!11!7!}+\frac{30!}{10!10!9!}\right)\left(\frac{1}{3}\right)^{30}{% endequation %}</p>

<p>(ה-{% equation %}\left(\frac{1}{3}\right)^{30}{% endequation %} נובע מכך שההסתברות של כל אחד מהאוטובוסים להיבחר היא {% equation %}\frac{1}{3}{% endequation %}, כלומר כל ה-{% equation %}p_{i}{% endequation %}-ים שווים במקרה הזה).</p>

<p>שימו לב שההסתברות הזו עדיין <strong>אינה</strong> {% equation %}q{% endequation %} המדובר; זו ההסתברות שבאוטובוסים 1 ו-2 יהיה מספר אנשים שווה ובאוטובוס מס' 3 יהיה את מספר האנשים הקטן ביותר. באותו האופן יכלנו לבחור שדווקא באוטובוס 2 יהיה מספר האנשים הקטן ביותר, או באוטובוס 1. דהיינו, צריך להכפיל את המספר ההוא ב-3 כדי לקבל את {% equation %}q{% endequation %}.</p>

<p>החישוב הזה אולי נראה מזעזע, אבל במחשב הוא כמובן טריוויאלי לחלוטין - אפילו לא צריך להקליד את כל המספרים אם משתמשים בשפת סקריפטינג נוחה עבור החישובים. התוצאה המספרית הסופית? אני קיבלתי {% equation %}0.38159\dots{% endequation %}, קרוב מאוד לתוצאות האמפיריות. הבעיה היחידה היא שלהכליל את החישוב הזה עבור מספר גדול יותר של אוטובוסים יהיה כאב ראש (עבור מספר גדול יותר של אנשים רק צריך לשנות מספר אחד בשורת הקוד שמבצעת את החישוב) - אולי לכם יהיה פתרון טוב יותר שמוצא את ההסתברות עבור {% equation %}N,k{% endequation %} כלליים? </p>