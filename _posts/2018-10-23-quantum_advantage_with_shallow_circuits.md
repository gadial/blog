---
id: 3671
title: "”הוכחה ראשונה לעליונות מחשב קוונטי“ - מה לא (וקצת מה כן)"
date: 2018-10-23 11:56:25
layout: post
categories: 
  - תורת הסיבוכיות
tags: 
  - חישוב קוונטי
  - סיבוכיות
---
השבוע קרה דבר שהוא תמיד משמח - עולם המתמטיקה עלה לכותרות בזכות תוצאה שקשורה לחישוב קוונטי - תחום שהופך לפופולרי יותר ויותר לאחרונה בעיתונות. "פריצת דרך: הוכחה ראשונה לעליונות מחשוב קוונטי" נאמר בכותרת <a href="https://www.themarker.com/wallstreet/1.6574243">בדה-מרקר</a>, ובלועזית ראיתי כותרות אפילו מתלהבות יותר בסגנון "צוות מיבמ הוכיח שמחשבים קוונטיים יכולים לעשות דברים בלתי אפשריים". ובכן, אני רוצה לעשות קצת סדר. ראשית, להסביר על מה בערך מדובר ומה בערך הוכיחו (התקציר: הוכיחו תוצאה מאוד יפה שהיא אכן פורצת דרך, אבל בואו לא נגזים עם הכותרות שנותנים לה), ושנית (ואת זה אעשה בפוסט נפרד) - להיכנס יותר לפרטים המתמטיים לטובת אלו שמעוניינים בכך (טוקבק זועם אצל דה-מרקר התלונן שלא סיפרו לו "איזו בעיה? גם השם מספיק" - ובכן חבר, להגיד 2D Hidden Linear Function Problem עוזר במשהו?)
<h2>מה זה חישוב קוונטי בכלל?</h2>
נתחיל מהשאלה המתבקשת - מה זה חישוב קוונטי בכלל? יש לי על כך סדרת פוסטים שלמה ש<a href="https://gadial.net/2014/07/17/quantum_computing_intro/">מתחילה כאן</a>, אבל הנה התקציר: חישוב קוונטי הוא תחום במדעי המחשב שמתבסס על היכולת שלנו <strong>לייצג אינפורמציה</strong> בצורה יותר מורכבת מאשר מחשבים מייצגים אותה כיום. הייצוג היותר מורכב הזה מתבסס על האופן שבו מתנהל העולם ברמה התת-אטומית כפי שאנחנו מצליחים להבין את זה; התחום בפיזיקה שעוסק ב"כפי שאנחנו מצליחים להבין את זה" הזה נקרא <strong>תורת הקוונטים</strong>. בנפנוף ידיים הפרוע המתבקש, חישוב "רגיל" מתבסס על כך שיחידת מידע בסיסית היא <strong>ביט</strong>: משהו שיכול להיות או 0 או 1 (ברמת הפרקטיקה, מה שקורה במחשב בפועל הוא שיש רכיב שמיועד לייצג ביט שכזה, והוא יכול לתחזק שתי רמות שונות של מתח חשמלי שאחת מהן מייצגת 0 ואחת מהן מייצגת 1). בחישוב קוונטי לעומת זאת יחידת המידע הבסיסית היא <strong>קיוביט</strong>: משהו שיכול להיות לא רק 0 או 1 אלא גם <strong>תערובת</strong> של השניים עם משקלים שונים ומשונים לכל אחד מהערכים הללו; לתערובת הזו קוראים <strong>סופרפוזיציה</strong> בפיזיקאית.

בואו נכניס <strong>טיפה</strong> סימון מתמטי לסיפור כי לדעתי זה יכול לעזור גם להדיוטות. פיזיקאים אוהבים להשתמש בסימון {% equation %}\left|0\right\rangle {% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %} כדי לתאר את הערכים הבסיסיים שקיוביט יכול להחזיק בהם; יש הגיון מאחורי הסימון המוזר הזה עם המשולש והכל, אבל נעזוב אותו כרגע. "תערובת" של שני המצבים הבסיסיים הללו היא משהו מהצורה {% equation %}a\left|0\right\rangle +b\left|1\right\rangle {% endequation %} כאשר {% equation %}a,b{% endequation %} הם מספרים. מה זה "מספרים" כאן? אני מרשה שברים כמו {% equation %}\frac{1}{2}{% endequation %} וגם מספרים כמו {% equation %}\frac{\sqrt{2}}{2}{% endequation %} ואפילו <strong>מספרים מרוכבים</strong> כמו {% equation %}i{% endequation %} (מה זה {% equation %}i{% endequation %}? זה מספר שמקיים {% equation %}i^{2}=-1{% endequation %}, משהו שלא קורה במספרים שאנחנו מכירים מחיי היום יום). יש רק מגבלה אחת שאני דורש במפורש: שיתקיים {% equation %}\left|a\right|^{2}+\left|b\right|^{2}=1{% endequation %}.

בחישוב קלאסי, לעומת זאת, עדיין אפשר לחשוב על כל מצב בתור משהו מהצורה {% equation %}a\left|0\right\rangle +b\left|1\right\rangle {% endequation %}, אבל עם מגבלה הרסנית הרבה יותר: הדרישה היא ש-{% equation %}a=1{% endequation %} ו-{% equation %}b=0{% endequation %} או ש-{% equation %}a=0{% endequation %} ו-{% equation %}b=1{% endequation %} וזהו. כלומר, ייצוג מידע קוונטי פותח לנו פתח לייצוג מורכב בצורה דרסטית יותר מאשר בייצוג מידע קלאסי. אבל זה אפילו לא סוף הסיפור, כי לא דיברנו (עדיין) על מה קורה במערכות שכוללות יותר מקיוביט בודד.

עכשיו, משהבנו מה זה בערך חישוב קוונטי, אפשר לתהות ממתי הדבר הזה קיים ולמה אנחנו שומעים עליו רק עכשיו. ובכן, תורת הקוונטים עצמה קיימת עוד מתחילת המאה ה-20, ומחשבים "קלאסיים" קיימים מאמצע המאה ה-20, אבל את ההצעה לבצע משהו כמו החישוב הקוונטי שמדברים עליו כיום הציע הפיזיקאי ריצ'ארד פיינמן רק ב-1982, מתוך כוונה להציע בניית מחשבים שיוכלו להתמודד יותר טוב עם בעיות של סימולציה של מערכות פיזיקליות "אמיתיות" (למה לעבוד קשה כדי לסמלץ מצבים קווונטיים בעזרת חישוב קלאסי כשאפשר לרתום את הטבע לעשות את העבודה בשבילנו). באופן די מרתק, עם הזמן התגלה שחישוב קוונטי יכול לסייע גם בכיוון "ההפוך" - לעזור לנו לפתור בעיות "קלאסיות" שמחשב קלאסי מתקשה להתמודד איתן. הדוגמא הידועה ביותר היא בעיית <strong>הפירוק לגורמים</strong> של מספרים; אנחנו לא מכירים כיום אלגוריתם קלאסי יעיל מספיק לפירוק לגורמים, למרות שהאלגוריתמים הקיימיים הם מתוחכמים בצורה יוצאת מן הכלל ומתבססים על מתמטיקה עמוקה למדי. התחושה הכללית היא שפירוק לגורמים היא בעיה "קשה מדי" ושכל אלגוריתם שפותר אותה ייקח כמות גדולה של זמן ("אקספוננציאלית" למי שזה אומר לו משהו).

אבל ב-1994 בא פיטר שור והציע אלגוריתם יעיל לפירוק לגורמים, שמתבסס על חישוב קוונטי. במילים אחרות - בנו מחשב קוונטי שתומך במספיק קיוביטים, והופס - אתם מסוגלים לפרק לגורמים בזמן יעיל, ולעשות צרות גדולות למערכת הצפנה כמו RSA שמסתמכת על כך שפירוק לגורמים זה עניין קשה. מאז התוצאה הסנסציונית הזו העניין התיאורטי בחישוב קוונטי הלך וגדל והתחום נחקר יפה בעשורים האחרונים.

רק מה, הייתה פה רק בעיה קטנה אחת - אין מחשבים קוונטיים שיכולים להריץ בפועל את האלגוריתם של שור. לבנות מחשב קוונטי - זה סיפור רציני ביותר. לא בגלל שלא יודעים איך לייצר רכיב שיתאר קיוביט - יש כבר כמה וכמה גישות שונות לעניין הזה - אלא כי בטכנולוגיות שיש לנו כרגע, המחשבים הקוונטיים רגישים מאוד ל<strong>רעשים</strong>, כש"רעש" יכול להיות גם פוטון בודד שנקלע בטעות למקום הלא נכון, פוגע ברכיב שמייצג קיוביט ומקלקל את הסופרפוזיציה שלו. רעשים קיימים גם במחשבים קלאסיים, כמובן, אבל אנחנו יודעים לבנות רכיבים שיהיו עמידים יחסית לרעש, ואנחנו גם יודעים לבנות רכיבים שמסוגלים לזהות שגיאות ולתקן אותן. במחשבים קוונטיים כל העסק פשוט יותר קשה. למשל, אתגר מרכזי בבניית מחשבים קוונטים בימינו הוא פשוט <strong>לקרר</strong> מספיק את הרכיבים שמייצגים קיוביטים (עד לרמה של כמה מיקרו-קלווין מעל האפס המוחלט) כדי לצמצם למינימום את הרעש שהם יסבלו ממנו.

התוצאה? יש כיום מחשבים קוונטיים, חלקם אפילו נגישים לציבור הרחב דרך שירות ענן, אבל הם על מספר <strong>קטן ביותר</strong> של קיוביטים והזמן המקסימלי של חישוב בהם לפני שהחישוב מתחיל לסבול מרעשים והולך לאיבוד הוא לא גדול. לא צפוי מחשב קוונטי שיוכל להריץ את האלגוריתם של שור בשנים הקרובות (ואולי גם בעשורים הקרובים) אבל התחושה היא שאנחנו הולכים ומתקרבים אל היום שבו מחשב קוונטי יוכל לעשות <strong>משהו</strong> פרקטי שמחשב רגיל לא מסוגל.

האם המאמר הנוכחי שעלה לכותרות עושה את זה?

ובכן, לא.

אבל הוא כן עושה משהו מספיק חשוב כדי להצדיק פרסום במגזין Science. אז מה הוא עושה.
<h2>מה המאמר אומר?</h2>
אפשר לראות <a href="https://arxiv.org/abs/1704.00690">כאן</a> את המאמר. התוצאה שיש במאמר היא <strong>תיאורטית</strong> לגמרי, אם כי ייתכן שבעתיד היא תתורגם גם לניסוי פרקטי. אני מדגיש את הנקודה הזו כי דה-מרקר, למשל, כותב לו בקלילות
<blockquote>בניסוי הוכיחו המדענים בפעם הראשונה, באמצעות דוגמה מוחשית, כי מחשב קוונטי יכול לעשות משימות שמחשב רגיל אינו מסוגל לבצע. עד פרסום תוצאות הניסוי, שבו הצליח המחשב לפתור בעיה מתמטית מורכבת, יתרונות המחשב הקוונטי על פני מחשב רגיל תוארו במונחים תיאורטיים בלבד.</blockquote>
וזה פשוט לא מה שקרה. לא הייתה בעיה מתמטית מורכבת קונקטית שלא הצלחנו לפתור עד כה, ואז כתבו איזו תוכנית למחשב קוונטי, הריצו את המחשב הקוונטי וקיבלו תוצאה שלא הייתה בהישג ידינו עד היום. שוב, אולי זה יקרה בעתיד הקרוב ואולי אפילו אפשר יהיה לעשות את זה בעתיד הקרוב עם הבעיה הספציפית שהמאמר דיבר עליה, אבל זה לא מה שקרה. מה שהמאמר עשה הוא לקחת <strong>מחלקה</strong> של בעיות מסוג מסויים ולהראות שאת כולן אפשר לפתור בעזרת חישוב קוונטי "רדוד" (ועוד אסביר מה זה "רדוד") אבל אי אפשר לפתור באמצעות חישוב קלאסי "רדוד". זה נותן לנו תוצאה תיאורטית חשובה - הוכחה מתמטית שחישוב קוונטי "רדוד" הוא <strong>חזק יותר מבחינה חישובית</strong> מאשר חישוב קלאסי "רדוד". זה בוודאי <strong>לא אומר</strong> שיש משהו שמחשב רגיל לא מסוגל לעשות ומחשב קוונטי יכול; גם מחשב רגיל יוכל לעשות את זה, זה פשוט ייקח לו יותר משאבי חישוב.

כדי לחדד את העניין הזה אני רוצה להתייחס לשתי תוצאות דומות מהעבר: האלגוריתם של שור שכבר הזכרתי, והאלגוריתם של גרובר.

נתחיל מהאלגוריתם של שור. כאמור, הוא פותר <strong>ביעילות</strong> בעיה שאנחנו <strong>לא יודעים</strong> איך לפתור <strong>ביעילות </strong>במחשב קלאסי. כלומר יש כאן שני סייגים:
<ol>
 	<li>הבעיה <strong>ניתנת לפתרון</strong> במחשב קלאסי, זה פשוט לוקח יותר זמן.</li>
 	<li><strong>ייתכן</strong> שקיים פתרון קלאסי יעיל ופשוט טרם מצאנו אותו.</li>
</ol>
סייג 1 הוא לא ייחודי לבעיה הזו - מחשב קלאסי <strong>יכול לסמלץ מחשב קוונטי</strong>, כך שאין דבר שמחשב קוונטי יכול לעשות ומחשב קלאסי לא יוכל לעשות, בהינתן שיש לו יותר זמן חישוב. <strong>אין בעיות שהן בלתי אפשריות למחשב רגיל ואפשריות למחשב קוונטי</strong>. כל הדיון הוא על התחרות של "מי יותר מהיר" (וזה דיון חשוב ביותר; רוב מדעי המחשב עוסקים בשאלות כאלו ולא בשאלות של מה בלתי אפשרי בכלל).

סייג 2 הוא יותר מהותי. בלשון של תורת הסיבוכיות, שהיא הענף המתמטי שעוסק בנושאים הללו, מה שפיטר שור הראה הוא שפירוק לגורמים היא בעיה ששייכת למחלקת הסיבוכיות BQP שבאה לתאר חישובים קוונטיים יעילים. אנחנו <strong>מאמינים</strong> שפירוק לגורמים לא שייכת למחלקה BPP שבאה לתאר חישובים קלאסיים יעילים (שיכולים להשתמש בנוסף לכך בהגרלות; גם חישוב קוונטי הוא כזה). כלומר, אנחנו <strong>מאמינים</strong> שפיטר שור הוכיח ש-BQP <strong>שונה</strong> מ-BPP, אבל אין לנו הוכחה לכך. ייתכן שמחר בבוקר נגלה ש-BPP=BQP וזו תהיה סנסציה אדירה, גדולה אפילו יותר מהאלגוריתם של שור.

המאמר הנוכחי לוקח שני מחלקות סיבוכיות אחרות: אחת "קלאסית" שנקראת {% equation %}\text{NC}^{0}{% endequation %} והשניה קוונטית שנקראת {% equation %}\text{SQC}{% endequation %} (השם הזה הוא לדעתי חידוש של המאמר הנוכחי ולא תמצאו אותו בגוגל) ומראה שהן <strong>כן שונות</strong>, כלומר שיש בעיה ששייכת ל-SQC אבל <strong>לא שייכת</strong> ל-{% equation %}\text{NC}^{0}{% endequation %}. ההוכחה שהבעיה שייכת ל-SQC היא החלק הפשוט יותר של המאמר; עיקר העבודה היא בלהוכיח ש-{% equation %}\text{NC}^{0}{% endequation %} לא כוללת את הבעיה - כלומר, עיקר המאמר הוא תוצאה "קלאסית" בתורת הסיבוכיות שאפשר היה לדבר עליה גם בלי לדבר על חישוב קוונטי.

התוצאה הזו, של הפרדה בין שתי מחלקות סיבוכיות מקבילות שאחת מהן קלאסית ואחת מהן קוונטית, היא באמת משהו חדש (לפחות למיטב ידיעתי). אבל לומר שזו "הוכחה ראשונה לעליונות מחשב קוונטי" זה לא באמת נכון, וכדי להסביר למה אני רוצה להכניס לתמונה את <strong>האלגוריתם של גרובר</strong>. יש לי <a href="https://gadial.net/2014/08/16/grover_algorithm/">פוסט עליו</a>, אבל הנה התקציר: האלגוריתם של גרובר מטפל בבעיה של <strong>חיפוש. </strong>תחשבו שאתם בספריה ועל המדף יש {% equation %}N{% endequation %} ספרים, ואתם מחפשים ספר אחד ספציפי. והמדף לא ממוין בשום צורה - או ליתר דיוק, גם אם הוא ממוין, אתם לא יודעים את זה ואתם לא יודעים על פי איזו שיטת מיון. איך תמצאו את הספר? תצטרכו <strong>לדגום</strong>: לקחת ספר מהמדף, לבדוק אם הוא הספר שלכם, ואם לא אז להחזיר אותו ולעבור לספר אחר. אפשר להוכיח מתמטית שבחישוב רגיל, תצטרכו במקרה הגרוע לדגום את כל {% equation %}N{% endequation %} הספרים לפני שתמצאו את הספר שלכם.

והנה, בחישוב קוונטי קורה קסם מדהים ואתם יכולים למצוא את הספר שלכם ב-{% equation %}\sqrt{N}{% endequation %} דגימות. זה אפשרי בגלל שבחישוב קוונטי, גם "דגימה" היא קוונטית - במקום לדגום את {% equation %}\left|0\right\rangle {% endequation %} או את {% equation %}\left|1\right\rangle {% endequation %} אתם מסוגלים לדגום את {% equation %}a\left|0\right\rangle +b\left|1\right\rangle {% endequation %} "בבת אחת". התיאור הפשטני הזה יוצר תחושה שהרעיון בחישוב קוונטי הוא המקביליות הזו - היכולת לפעול בו זמנית על {% equation %}\left|0\right\rangle {% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %} ולקבל עליהם אינפורמציה ביחד. זה אמנם מה שקורה אבל זה לא סוף הסיפור, ויש לחישוב קוונטי גם קשיים (אין לנו דרך פשוט "לקרוא" את התשובה לדגימה שביצענו; בסוף החישוב הקוונטי כל מה שנקבל הוא את הכתובת של ספר בודד שמוגרל איכשהו מבין כל הספרים, וצריך לעבוד קשה כדי לוודא שההסתברות של הספר "שלנו" תהיה גבוהה).

מה שמעניין באלגוריתם גרובר הוא שמדובר על הוכחה חד משמעית לכך שמחשב קוונטי מסוגל להשיג "קיצורי דרך" שמחשב קלאסי לא מסוגל להן - {% equation %}\sqrt{N}{% endequation %} דגימות מול {% equation %}N{% endequation %} דגימות. יש עוד דוגמאות ל"שיפור במספר הדגימות" והמאמר הנוכחי מאזכר אחת מהן ומתבסס עליה חלקית, אבל הדיבור על "מספר דגימות" הוא שונה מהדיבור על "זמן ריצה" שהזכרנו קודם. גרובר בהחלט משפר את זמן הריצה של אלגוריתמים מסויימים, אבל לא ברמה שמספיקה כדי לטעון ששתי מחלקות סיבוכיות כמו BQP ו-BPP הן שונות זו מזו. מה שהמאמר הנוכחי עושה, ועושה בצורה יפה מאוד, הוא להיפטר מכל הנושא הזה של <strong>דגימה</strong> ובמקום זה לדבר על בעיה שנתונה בצורה מפורשת לחלוטין; אני אסביר את זה בפוסט הבא.

אז נו, למה לשמור אותנו במתח, מה הבעיה? אז זהו, שזו בעיה שמנוסחת בלשון מתמטית למדי והיא לא כל כך מעניינת אלא בתור אמצעי להפריד בין שתי מחלקות סיבוכיות. יש פונקציה שמיוצגת בדרך מסובכת כלשהי ואפשר להסיק מהייצוג המסובך הזה ייצוג יותר פשוט שלה, והאתגר הוא למצוא את הייצוג היותר פשוט הזה (לבקיאים - הייצוג המסובך הוא של <strong>תבנית ריבועית</strong> והייצוג הפשוט הוא של <strong>פונקציה לינארית</strong> על תת-מרחב של הקלטים של התבנית הריבועית). אני לגמרי מסכים עם דה-מרקר שלא פירטו מה בדיוק הבעיה; העובדה שהיא מרגישה מלאכותית שכזו תהיה עוד גורם שיקלקל את תחושת הסנסציה כי רובנו לא מתלהבים כל כך מהפרדות בין שתי מחלקות סיבוכיות.

ולפני שאסיים, האם בכל זאת יש סיכוי שנראה את הבעיה הזו מורצת על מחשבים קוונטיים אמיתיים ונפתרת למרות שאף מחשב קלאסי לא מצליח? אולי. לדיבור על "חישוב רדוד" יש יתרון משמעותי בהקשר הנוכחי של חישוב קוונטי. כבר אמרתי שחישוב קוונטי בימינו סובל מהבעיה המהותית שאחרי זמן חישוב כלשהו הסיכוי שלא ייגרם רעש שיקלקל את כל החישוב הוא נמוך מאוד. כלומר, חישובים קוונטיים צריכים להיות "קצרים" (זה בערך המובן של "רדוד" אבל לא לגמרי). לכן, אם אנחנו רוצים בעיה ספציפית שמחשב קוונטי אמיתי מאלו שנבנים כיום יוכל להתמודד איתה בכבוד, בעיות מסוג זו שבהן המאמר עוסק הן בדיוק מה שכדאי לחפש. מצד שני, יהיה הרבה יותר נחמד אם העליונות של חישוב קוונטי תוכח לבסוף בזכות זה שאלגוריתם קוונטי לסינתזה של מולקולות יצליח לאפשר לחוקרים לייצר תרופה למחלה שעד היום לא עלה בידם לייצר כי חישוב קלאסי היה מסוגל להגיע לאותן תוצאות (גם זה כיוון שעובדים עליו...), ואז הכותרות בעיתון כבר לא יצטרכו להיות לא מדויקות כדי להבהיר את גודל הסנסציה.