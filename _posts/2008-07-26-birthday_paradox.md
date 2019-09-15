---
id: 147
title: "כיצד פרדוקס יום ההולדת מוליד חוב בבנק"
date: 2008-07-26 16:57:16
layout: post
categories: 
  - הסתברות
  - משחקים וחידות מתמטיות
  - קומבינטוריקה
  - קריפטולוגיה
---
<a href="http://www.gadial.net/?p=136">לא מזמן</a> נתתי כאן חידה ואחזור עליה שוב: כמה אנשים צריכים להיות במסיבה כדי שבהסתברות טובה, לשניים יהיה אותו יום הולדת - כלומר, אותו יום בשנה, לא בהכרח אותה שנה?

כמובן שהשאלה בניסוח הזה מאוד לא מוגדרת היטב. הבה ונבהיר כמה נקודות עדינות. ראשית, אנו מניחים שימי ההולדת מתפלגים באופן אחיד, כלומר לכל יום בשנה אותה הסתברות (למיטב ידיעתי זה לא נכון בעולם האמיתי). שנית, לא מתייחסים לשנים מעוברות, כלומר ל-<a href="http://he.wikipedia.org/wiki/29_%D7%91%D7%A4%D7%91%D7%A8%D7%95%D7%90%D7%A8">29 בפברואר</a>. שלישית, ב"הסתברות טובה" הכוונה היא להסתברות גבוהה מחצי - אבל אראה בהמשך ניסוח עוד יותר מסודר וכללי.

קל לדעת מה כמות האנשים המינימלית שמבטיחה שיהיו שניים עם אותו יום הולדת - 366, תוצאה שנובעת מייד מ<a href="http://he.wikipedia.org/wiki/%D7%A2%D7%A7%D7%A8%D7%95%D7%9F_%D7%A9%D7%95%D7%91%D7%9A_%D7%94%D7%99%D7%95%D7%A0%D7%99%D7%9D">עיקרון שובך היונים</a>. מה שמפתיע הוא שצריך הרבה פחות אנשים כדי להבטיח הסתברות של חצי לפחות - רק 23. לכן התוצאה הזו מכונה "פרדוקס", אבל כמובן שאין כאן סתירה של ממש, והמתמטיקה אינה מסובכת. ב"אינה מסובכת" אני מתכוון, בכל זאת, ל"דורשת ידע כלשהו ב<a href="http://he.wikipedia.org/wiki/%D7%A7%D7%95%D7%9E%D7%91%D7%99%D7%A0%D7%98%D7%95%D7%A8%D7%99%D7%A7%D7%94">קומבינטוריקה</a> ואולי גם טיפה בהסתברות", ולכן מי שאין לו את הידע הזה עשוי לאבד אותי, ומוזמן לקפוץ אל החלק שאחרי הניתוח המתמטי.

איך ניגשים לשאלה שכזו? ראשית, יותר פשוט לבצע אבסטרקציה שלה ולהפסיק לדבר על 365 ימים ועל 23 אנשים. נניח שיש לנו {% equation %}n{% endequation %} אנשים במסיבה, ויש {% equation %}k{% endequation %} ימי הולדת פוטנציאליים. בעצם, עזבו: נניח שאחנו זורקים {% equation %}n{% endequation %} כדורים ל-{% equation %}k{% endequation %} תאים, כך שלכל כדור אנחנו בוחרים תא באקראי - מה ההסתברות ששני כדורים ינחתו באותו התא?

זו תופעה נפוצה במתמטיקה בכלל, ובקומבינטוריקה בפרט - לעבור מהבעיה הקונקרטית והספציפית שלנו לבעיה אחרת, שאולי קל לנו יותר לחשוב עליה, ששקולה לה. כאן אין יתרון מחשבתי רציני לדיבור על כדורים, ובכל זאת זה קצת יותר מסבר את הדעת מאשר ימי הולדת אם {% equation %}k=10,000{% endequation %}, למשל. בהמשך נראה כיצד מתקשר לכל העסק הזה, באופן קונקרטי לגמרי, משהו שאינו קשור לא לכדורים ולא לימי הולדת.

במקום לבדוק את ההסתברות ששני כדורים ייפלו באותו תא (יש המון אפשרויות שונות לכך - אילו שני כדורים? ואולי אפשר שלושה באותו תא? וכו') יותר נוח לדבר על ההסתברות ה"משלימה" - ההסתברות שלא יהיה זוג כדורים באותו תא, דהיינו שכל כדור נמצא בתא נפרד. מכיוון שמדובר במספר סופי של צירופים אפשריים של כדורים ותאים, יש לנו כאן בעיה קומבינטורית עם קשר ישיר להסתברות - ההסתברות המבוקשת היא מספר החלוקות האפשריות של כדורים לתאים כך שאין שני כדורים באותו תא, חלקי כל החלוקות האפשריות בכלל של כדורים לתאים. המספר הכולל הוא קל לחישוב: {% equation %}k^n{% endequation %}. הסיבה לכך היא שלכל אחד מ-{% equation %}n{% endequation %} הכדורים יש לנו {% equation %}k{% endequation %} בחירות לגיטימיות, ולכן מספר האפשרויות הכולל הוא מכפלה של {% equation %}n{% endequation %} פעמים {% equation %}k{% endequation %} (נסו להבין מדוע מכפלה דווקא; דרך נוחה היא לחשוב על מספר הגלידות האפשריות כשלוקחים שני כדורים מתוך קבוצה כלשהי של טעמים, ויש חשיבות לשאלה מי הכדור שלמעלה ומי הכדור שלמטה).

כמה אפשרויות יש לחלוקת {% equation %}n{% endequation %} כדורים ל-{% equation %}k{% endequation %} תאים כך שאין שני כדורים באותו התא? ראשית צריך לבחור {% equation %}n{% endequation %} תאים מתוך כלל ה-{% equation %}k{% endequation %} כדי לחלק להם את הכדורים - יש {% equation %}{k\choose n}{% endequation %} אפשרויות לעשות כן. אחר כך צריך להחליט באיזה סדר יוכנסו {% equation %}n{% endequation %} הכדורים לתאים שבחרנו - יש כאן {% equation %}n!{% endequation %} אפשרויות. בסה"כ נקבל שההסתברות היא {% equation %}{k\choose n}\frac{n!}{k^n}{% endequation %}.

ידוע כי {% equation %}{k\choose n}=\frac{k!}{n!(k-n)!}{% endequation %}, כך שבעצם קיבלנו הסתברות של {% equation %}\frac{k!}{(k-n)!}\cdot\frac{1}{k^n}{% endequation %}. את היצור הזה אפשר להציג בתור מכפלה של {% equation %}n{% endequation %} איברים:

{% equation %}\left(\frac{k}{k}\right)\left(\frac{k-1}{k}\right)\cdots\left(\frac{k-\left(n-1\right)}{k}\right){% endequation %}

ואחרי צמצום קל נקבל:

{% equation %}1\cdot\left(1-\frac{1}{k}\right)\cdots\left(1-\frac{\left(n-1\right)}{k}\right){% endequation %}

ובסימון פשוט קצת יותר:

{% equation %}\prod_{i=0}^{n-1}\left(1-\frac{i}{k}\right){% endequation %}
וזו התוצאה המעניינת כאן מבחינה מתמטית. אפשר היה להגיע אליה גם בצורה קצת יותר פשוטה: ה-1 שבהתחלה הוא ההסתברות שאחרי שזרקנו את הכדור הראשון לא קיבלנו התנגשות. ה-{% equation %}\left(1-\frac{1}{k}\right){% endequation %} שאחר כך זו ההסתברות שאין התנגשות בכדור השני, וכן הלאה - כשבכל פעם אנו בודקים מה ההסתברות שכרגע לא תהיה לנו התנגשות, <strong>בהינתן</strong> שעד עכשיו לא הייתה כזו (ולכן כל הכדורים בתאים שונים, ולכן כדי שלא תהיה התנגשות צריך להגריל אחד מהתאים הנותרים). העדפתי בכל זאת להציג את הדרך הקומבינטורית כי היא דורשת פחות מושגים (כמו הסתברות מותנה) כדי להבין ולהשתכנע.

אם מציבים {% equation %}k=365, n=23{% endequation %} רואים מייד שהערך שמתקבל קטן מחצי - וכזכור, הערך הזה הוא ההסתברות ש<strong>לא</strong> תהיה התנגשות; כלומר, ההסתברות להתנגשות גדולה מחצי. עבור {% equation %}n=22{% endequation %} זה דווקא לא יקרה, ולכן 23 הוא המספר המינימלי של אנשים שצריך.

עד כאן לקוריוז החידתי, אבל את הנוסחה הכללית שקיבלנו למעלה אפשר לנתח בצורה יותר כללית מאשר סתם להציב בה ערכים - אפשר לשאול את עצמנו באופן כללי מה צריך להיות סדר הגודל של {% equation %}n{% endequation %} (מספר הכדורים) ביחס ל-{% equation %}k{% endequation %} (מספר התאים) כדי לקבל סיכוי גבוה להתנגשות. לשם כך אפשר להשתמש בקירוב שחוסם את המכפלה הזו, קירוב שמבוסס על פונקצית ה<a href="http://he.wikipedia.org/wiki/%D7%90%D7%A7%D7%A1%D7%A4%D7%95%D7%A0%D7%A0%D7%98">אקספוננט</a> {% equation %}\exp(x)=e^x{% endequation %} (אלו מכם שמכירים אותה, ייתכן שכבר כשראיתם את המכפלה היא צצה לכם לראש - המכפלה מאוד מזכירה את הגבול שמגדיר את פונקצית האקספוננט).

אי השוויון שמעניין אותנו הוא {% equation %}1+x\le e^x{% endequation %}. הוא לא מסובך להוכחה (לא אעשה זאת) והוא מאפשר לנו לחסום כל איבר במכפלה בצורה נוחה: {% equation %}\left(1-\frac{i}{k}\right)\le e^{-i/k}){% endequation %} באמצעות החסם הזה אפשר להפוך את המכפלה שלעיל למכפלה של אקספוננטים - והיתרון בכך הוא שאז מקבלים אקספוננט שהמעריך שלו הוא <strong>סכום</strong>, דהיינו הפכנו את המכפלה לסכום - וסכום חשבוני, שבו אנו יודעים לטפל. מקבלים (אני משתמש ב-exp במקום ב-e בחזקת משהו כי בגישה השנייה מקבלים משהו שנראה מזעזע טיפוגרפית):

{% equation %}\prod_{i=0}^{n-1}\left(1-\frac{i}{k}\right)\le\prod_{i=0}^{n-1}\exp\left(-i/k\right)=\exp\left(\frac{1}{k}\sum_{i=0}^{n-1}i\right)=\exp\left(-\frac{n\left(n-1\right)}{2k}\right){% endequation %}

אפשר אם כן להתמקד בביטוי {% equation %}\frac{n(n-1)}{2k}{% endequation %}. כאשר הוא שואף לאינסוף, האקספוננט שואף לאפס - ושאיפה מהירה למדי. כדי שהוא ישאף לאינסוף צריך ש-{% equation %}n(n-1){% endequation %} יהיה גדול ביחס ל-{% equation %}2k{% endequation %}, או בניסוח קצת יותר מרושל אבל עדיין מדוייק: צריך ש-{% equation %}n^2{% endequation %} יהיה מסדר גודל גדול מ-{% equation %}k{% endequation %}. ב<a href="http://he.wikipedia.org/wiki/%D7%A1%D7%99%D7%9E%D7%95%D7%9F_%D7%90%D7%A1%D7%99%D7%9E%D7%A4%D7%98%D7%95%D7%98%D7%99">סימון מדוייק</a>: צריך שיתקיים {% equation %}n=\omega(\sqrt{k}){% endequation %} כדי שההסתברות לאי-התנגשות תהיה {% equation %}o(1){% endequation %} (סימון מקובל לכך שההסתברות לאי התנגשות שואפת לאפס). כלומר, אם מספר האנשים הוא גדול יותר מאשר שורש מספר ימי ההולדת הפוטנציאליים, אז ההסתברות להתנגשות תהיה גדולה, ותגדל מהר מאוד עם כל אדם שמוסיפים.

זה מסביר מאיפה צץ המספר הזה, 23: הוא אמנם לא שורש 365 אבל הוא גדול ממנו רק בקצת (וזה בעצם הרעיון - בשורש עצמו בדיוק ההסתברות עדיין לא מצופה להיות ממש גבוהה). אבל זה אומר בעצם הרבה יותר מכך, וזה מה שמקשר אותנו לשימושים שאני רוצה לדבר עליהם - אם יש לנו מרחב גדול מאוד של איברים, ואנחנו דוגמים ממנו איברים באקראי, אז כבר אחרי פרק זמן שהוא שורש מגודל המרחב יש לנו סיכוי סביר להתנגשות. זו תוצאה חשובה שלא ניתן לזלזל בה - ומקום אחד שבו היא באה לידי ביטוי מהותי הוא בקריפטוגרפיה, ובפרט בתחום החתימות הדיגיטליות.

פעם, לפני שנים רבות, דיברתי <a href="http://www.gadial.net/?p=91">כאן</a> על <a href="http://he.wikipedia.org/wiki/%D7%97%D7%AA%D7%99%D7%9E%D7%94_%D7%93%D7%99%D7%92%D7%99%D7%98%D7%9C%D7%99%D7%AA">חתימות דיגיטליות</a>. בבסיסן, חתימות דיגטליות הן פונקציות שבאופן קסום קשה לחשב אלא אם יש לך פרט מידע סודי כלשהו, אבל קל להפוך, כלומר למצוא את המקור בהינתן הפלט; כתוצאה מכך רק מי שיש לו את המידע הסודי יודע לחתום על הודעות (לחשב עליהן את הפונקציה) אבל כל אחד יכול לבדוק, בהינתן הודעה וחתימה, שהחתימה חוקית (ולכן הוא יודע בדיוק ממי ההודעה הגיעה וההוא לא יכול להכחיש זאת).

בפוסט ההוא תיארתי מקצת מהבעיות שבהפעלת פונקצית החתימה ישר על הטקסט שעליו חותמים; ואמרתי שהדרך שבה פותרים את הבעיות הן על ידי שימוש בתמצות - פונקציה (שכל אחד יכול לחשב) ש"מכווצת" את הטקסט הארוך שעליו חותמים לקטע קצר מאוד. תמצות שכזה בהכרח יכיל "התנגשויות" - דהיינו, טקסטים שמתומצתים לאותו הערך -  אבל מכיוון שרוב הטקסטים בעולם הם ג'יבריש (למשל, הטקסט "גכדגכדג" הוא ג'יבריש) התקווה היא שמרביתן המוחצת של ההתנגשויות יהיו בין טקסט לגיטימי לבין ג'יבריש; בפרט, שלא יהיו שתי הודעות בעלות משמעויות "מנוגדות" שיתומצתו לאותו הערך. התקווה הזו היא הבל מוחלט ותכף אפרט.

לפני כן אסביר מה הבעיה הבסיסית שבהתנגשויות. נניח שאני איש רע. נניח גם שאתם פונים לחברה שלי כדי לקבל שירות מסוג זה או אחר. אני שולח לכם חוזה התחייבות סטנדרטי (בן אלף סעיפים שאיש לא קורא) שבסופו גם התחייבות כספית שלכם תמורת השירות שלי - בטקסט יהיה כתוב "מאה דולר". אתם ממהרים לחתום על הטקסט הזה על ידי כך שאתם מתמצתים אותו (עם פונקציה ידועה לכולם) וחותמים על התמצית. כעבור חודש אני בא לבית המשפט, מנופף בחוזה החתום (השופט מוודא את החתימה ורואה שהיא תקפה) ומראה לכם, לזוועתכם, שלא כתוב בחוזה "מאה דולר" אלא "מיליון דולר". איך זה קרה?

זה קרה על ידי כך שהצלחתי איכשהו למצוא התנגשות בפונקצית התמצות. החוזה של מיליון הדולר תומצת <strong>בדיוק לאותה תמצית</strong> כמו חוזה מאה הדולרים, ולכן חתימה על התמצית הזו שקולה לחתימה על כל אחד משני הטקסטים; אין לכם שום דרך להוכיח שחתמתם דווקא על חוזה מאה הדולרים ולא על החוזה השני (כי "הוכחות" קריפטוגרפיות שכאלו מתבססות על החתימה, לא על תכתובות מייל לא חתומות שאפשר אולי לזייף).

כדי למנוע מדבר כזה להתרחש, חייבים לדרוש דרישות מסויימות מפונקצית התמצות - שתי הדרישות העיקריות הן שבהינתן תמצות של הודעה א', יהיה קשה למצוא הודעה ב' שמתומצתת לאותו ערך; ושיהיה קשה באופן כללי למצוא שתי הודעות שמתומצתות לאותו ערך (כשאין דרישה ספציפית על מה יהיה הערך הזה, רק ששתי ההודעות "יתנגשו"). השאלה המהותית היא "מה זה קשה", שהרי תמיד אפשר פשוט לעבור על הרבה הודעות, לתמצת את כולן, ואז לבדוק התנגשויות; אם, למשל, גודל התמצית הוא 80 ביטים, אז יש רק {% equation %}2^{80}{% endequation %} ערכי תמצות אפשריים, ולכן אחרי שנתמצת {% equation %}2^{80}{% endequation %} הודעות בוודאי נמצא התנגשות. כאן נכנס לתמונה פרדוקס יום ההולדת. אם פונקצית התמצות שלנו נראית "אקראית" (ותמיד מניחים שזה כך, כי לפונקציות שלא נראות אקראיות חסרונות משלהן), אין צורך לתמצת {% equation %}2^{80}{% endequation %} הודעות; מספיק לתמצת רק שורש ממספר זה של הודעות, ונקבל התנגשות בסבירות גבוהה - כלומר, מספיק לתמצת {% equation %}2^{40}{% endequation %} הודעות.

אי אפשר לזלזל בתוצאה הזו; היא מראה  שלכל פונקציות התמצות יש חולשה בסיסית שלא ניתן להתגבר עליה. בשל כך, חייבים לבחור מראש את גודל התמציות כך שאפילו השורש שלו יהיה גדול מדי בשביל פריצה פרימיטיבית כמו שהצגתי. {% equation %}2^{80}{% endequation %} זמן זה הרבה מאוד, יותר ממה שמחשבים בימינו מסוגלים לו; {% equation %}2^{40}{% endequation %} זה אפשרי בהחלט. לכן גודל התמצית של פונקצית התמצות <a href="http://he.wikipedia.org/wiki/SHA">SHA-1</a>, אולי הפונקציה הכי פופולרית בתחום זה (שכבר התגלו בה חולשות מהותיות) הוא 160 ביטים ולא משהו נמוך באופן משמעותי. לצורך השוואה - שיטת ההצפנה הסימטרית המקובלת כיום כתקן, <a href="http://he.wikipedia.org/wiki/AES">AES</a>, מתבססת על מפתח בגודל 128 ביטים (גם כאן החשש הוא מהתקפה שהיא פשוט ניסוי סדרתי של כל המפתחות האפשריים), והשיטה שקדמה לה, <a href="http://he.wikipedia.org/wiki/DES">DES</a>, השתמשה במפתחות של 56 ביטים.

עם זאת, עדיין לא הסברתי איך הצלחתי למצוא שתי הודעות <strong>בעלות משמעות</strong> שאומרות בדיוק את מה שאני רוצה שיאמרו ומתומצתות לאותה תמצית. הנה תעלול פשוט שיעבוד לכל קובץ ASCII תמים: לא סתם כך אמרתי שבחוזה ההתחייבות יש אלף סעיפים שאיש לא קורא. כמובן, אני לא מתכוון להכניס לשם ג'יבריש; אני פשוט מתכוון לשחק טיפה בניסוחים. למשל, קחו את הקטע הבא, שמופיע בחוזה דיור סטנדרטי:

"<!--[if gte mso 9]&amp;gt;     Normal   0                             MicrosoftInternetExplorer4   --><em><span dir="rtl">במשך כל תקופת השכירות או תקופת האופציה, לפי העניין, ישלם השוכר, במועד הקבוע לכך על פי דין, בנוסף לכל התשלומים האחרים החלים עליו על פי הסכם זה, את כל התשלומים, האגרות, ההיטלים, הארנונות, המסים ותשלומי החובה מכל סוג שהוא</span></em>".

אוי, כמה שאפשר לחגוג כאן. מה קורה, למשל, אם נחליף את "במשך" ל"במהלך"? מישהו ירגיש בהבדל? ואם במקום "תקופת השכירות או תקופת האופציה" נכתוב "תקופת האופציה או תקופת השכירות"? ובמקום זה "תקופת האופציה או השכירות"? ואם נשמיט את הפסיק אחרי "השוכר ישלם"? ומה קורה בחלק של ה"אגרות-היטלים-ארנונות-מסים-תשלומי חובה"? גם שם אפשר לעשות חוכא ואיטלולא מהסדר שבו מופיעים דברים. וב"לכל התשלומים האחרים", מה מונע מאתנו לכתוב "לכל יתר התשלומים האחרים"? וכן הלאה.

כל אחד מהשינויים הללו הוא בלתי מורגש ולא משנה את משמעות המסמך. עם זאת, כל <strong>צירוף</strong> של שינויים נותן לי מסמך חדש. למשל, אם נשחק רק בשני הפרמטרים של "במשך/במהלך" ושל "לכל התשלומים/לכל יתר התשלומים" כבר נקבל <strong>ארבעה</strong> מסמכים שונים: אחד עם "במשך" ו-"לכל התשלומים"; אחד עם "במהלך" ו-"לכל התשלומים"; אחד עם "במשך" ו-"לכל יתר התשלומים", והאחרון עם "במהלך" ו-"לכל יתר התשלומים". כלומר - משני זוגות אפשריים קיבלתי 4 מסמכים; מ-{% equation %}k{% endequation %} זוגות שכאלו אקבל {% equation %}2^k{% endequation %} מסמכים. מכאן שאני רק צריך לכתוב את החוזה שלי כך שיהיו בו 80 נקודות שאפשר לבחור בכל אחת מהן בין זוג מילים, והצלחתי לייצר {% equation %}2^{80}{% endequation %} מסמכים שונים, שכולם אומרים את אותו הדבר בדיוק, ועל פי פרדוקס יום ההולדת כנראה שתהיה התנגשות בין התמציות שלהם. בבית המשפט אולי אפשר יהיה להתלונן שהניסוח של החוזה שאני מציג לא זהה ב-100% לחוזים אחרים שנתתי לאנשים אחרים, אבל זה משהו שאפשר לתרץ באלף ואחת סיבות אנושיות ("המחשב קרס", "החוזה הזה נכתב על ידי עובד אחר" וכו'), ולא זה מה שיערער על הסמכות שמציעה חתימה דיגיטלית.

עדיין לא הסברתי איך הצלחתי לשנות את ה"מאה דולר" שכתוב למטה ב"מיליון דולר". מה שאני עושה הוא לייצר שתי קבוצות מגודל {% equation %}2^{80}{% endequation %}; אחת שמורכבת כולה מחוזים שבהם כתוב למטה "מאה דולר" ולמעלה אני משחק עם הפרמטרים; והשנייה שמורכבת כולה מחוזים שבהם כתוב למטה "מיליון דולר" ולמעלה אני משחק עם הפרמטרים. מפרדוקס יום ההולדת נובע (לא מייד) שיש הסתברות טובה מאוד שתהיה התנגשות בין התמצית של איבר מהקבוצה הראשונה, ואיבר מהקבוצה השנייה. הבעיה היחידה? {% equation %}2^{80}{% endequation %} הודעות זה הרבה. אין לי מספיק זמן חישוב כדי לתמצת את כולן; אבל מבחינת כמות ההודעות שאפשר לייצר, {% equation %}2^{80}{% endequation %} הודעות בעלות משמעות זהה זה כלום. כמובן שכל זה לא קשור רק לקריפטוגרפיה: בהערת אגב אציין שאותה טכניקה משמשת גם סופרים ומוזיקאים מסויימים.