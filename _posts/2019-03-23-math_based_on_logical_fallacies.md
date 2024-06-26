---
id: 3754
title: "האם כל המתמטיקה בעצם מבוססת על כשלים לוגיים?"
date: 2019-03-23 06:41:47
layout: post
categories: 
  - אלגברה מופשטת
  - הבלים פסאודו-מתמטיים
tags: 
  - חוגי פולינומים
  - סתירות לוגיות במתמטיקה
---
להיט עכשיו בפייסבוק העברי הוא צילום המסך הזה של פוסט שלא חשוב על ידי מי נכתב, כי הוא מופץ במטרה ללעוג לכותב:

<img class="alignnone size-full wp-image-3755" src="{{site.baseurl}}{{site.post_images}}/2019/03/DivideByZero.png" alt="" width="738" height="753" />

אותי פחות מעניין ללעוג לכותב ויותר לשאול שאלות ולנסות לענות להן. למשל:
<ol>
 	<li>למה אין כאן סתירה? (התקציר: כי מחלקים באפס)</li>
 	<li>מאיפה בעצם ה"תרגיל" הזה הגיע ומאיפה בא הסיפור על ניוטון? (התקציר: אין לי מושג)</li>
 	<li>האם אפשר לומר משהו מעניין מתמטית על התרגיל הזה? (קצת)</li>
 	<li>האם כל המתמטיקה בעצם מבוססת על כשלים לוגיים? (ובכן... הישארו עמנו?)</li>
</ol>
וכעת לתשובה קצת יותר מפורטת. ראשית, התרגיל. אם נעקוב אחרי השלבים שלו בקפידה נראה שכולם תקינים במובן זה שכל שורה נובעת לוגית מהשורה שמעליה, למעט שורה אחת: המעבר מ-

{% equation %}\left(x-3\right)\left(x+5\right)=\left(x-3\right)\left(x+4\right){% endequation %}

אל

{% equation %}x+5=x+4{% endequation %}

מעבר כזה נקרא <strong>צמצום</strong>, וכדי לבצע אותו צריך לוודא שמה שמצמצמים בו לא שווה לאפס. למה? ובכן, כי לכאורה מה שעושים בצמצום הוא לחלק באפס, וכידוע אסור לחלק באפס. אבל אני אפילו לא זקוק לטענה הזו. צמצום באופן כללי הוא המעבר ממשוואה מהצורה

{% equation %}a\cdot x=a\cdot y{% endequation %}

אל המשוואה

{% equation %}x=y{% endequation %}

"מעבר" ממשוואה אחת לשניה פירושו: אם קיים פתרון למשוואה <strong>הראשונה</strong>, אז הוא יהיה פתרון גם למשוואה <strong>השניה</strong>. זה האופן שבו אנחנו פותרים משוואות: לוקחים משוואה מסובכת ומפעילים עליה שורה של מניפולציות ש<strong>משמרות</strong> את הפתרונות של המשוואה המקורית. המקרה של כפל באפס מקלקל לנו את זה, כי אפס כפול כל דבר שווה לאפס. לכן אם {% equation %}a=0{% endequation %} נקבל ש-{% equation %}a\cdot x=0{% endequation %} תמיד, לא משנה מהו {% equation %}x{% endequation %}, ולכן גם {% equation %}a\cdot x=a\cdot y{% endequation %} מתקיים תמיד בלי תלות בטיב הקשר בין {% equation %}x,y{% endequation %}.

עוד נקודה שאני רוצה לחדד טיפה היא שזה לא אסון אם מקבלים {% equation %}1=0{% endequation %}. זה לא <strong>בהכרח</strong> אומר שהגענו לסתירה במתמטיקה, אלא שהגענו למשהו שנראה כמו סתירה להנחות שלנו ולכן קרוב לודאי שאחת מהן לא נכונה. הרי את ה"תרגיל" למעלה היה אפשר להתחיל מהשורה הלפני אחרונה:

{% equation %}x+5=x+4{% endequation %}

שממנה אכן ניתן להסיק, על ידי חיסור {% equation %}x+4{% endequation %} משני האגפים (פעולה שמשמרת פתרונות), ש-{% equation %}1=0{% endequation %}. עכשיו, את {% equation %}1=0{% endequation %} לא צריך לקרוא בתור "סתירה במתמטיקה!!!!! אההההה!!!!!" אלא בתור "משוואה שלא קיים לה פתרון" - כלומר, זו "משוואה" שבה לא משנה אילו ערכים נציב ב"נעלמים", הם לא יהפכו את המשוואה לנכונה (מכיוון שפשוט <strong>אין בה נעלמים</strong>). המסקנה היא שגם למשוואה הקודמת, {% equation %}x+5=x+4{% endequation %} לא היה פתרון, בגלל תכונת "שימור הפתרונות" שהזכרתי; ש<strong>אם </strong>המשוואה {% equation %}x+5=x+4{% endequation %} הייתה פתירה, אז גם {% equation %}1=0{% endequation %} הייתה פתירה.

במקרה של סדרת המשוואות למעלה, ה"סתירה" מתקבלת מכך שהתחלנו ממשהו שנראה לגיטימי ופתיר - {% equation %}x=3{% endequation %} - ואיכשהו "איבדנו" את הפתרון הזה בדרך; וזה התרחש בגלל המעבר הלא חוקי שתיארתי, כי אם {% equation %}x=3{% endequation %} אז {% equation %}x-3=0{% endequation %} ולכן הצמצום בשורה

{% equation %}\left(x-3\right)\left(x+5\right)=\left(x-3\right)\left(x+4\right){% endequation %}

הוא בדיוק צמצום של אפס-כפול-משהו.

כשפותרים משוואות בעולם האמיתי, כשמבצעים צמצום כזה מתבצעת <strong>חלוקה למקרים</strong>. מוסיפים את ההנחה שמה שמצמצמים בו שונה מאפס וממשיכים לפתור עם זה, ומטפלים במקרה שבו הוא שווה אפס בנפרד. כלומר, פתרון תקין לתרגיל היה מגיע אל "<strong>או</strong> ש-{% equation %}x=3{% endequation %} והוא פתרון של המשוואה, <strong>או</strong> ש-{% equation %}x\ne3{% endequation %} ובמקרה זה אין פתרון למשוואה" שהוא כמובן תקין. בקיצור, קשה מאוד למצוא סתירה כלשהי במתמטיקה עם התרגיל הזה (מפתיע!)

בדיון שבו פורסם הטקסט הזה, האם לא העירו שיש חלוקה באפס? כמובן שהעירו. התשובה הייתה מעניינת: שאין פה חלוקה ב-0 אלא "חלוקה בפולינום {% equation %}x-3{% endequation %}", שזה... נכון? זה באמת מה שקורה פה, אם כי כמובן שזה לא משפיע על הבעיה בתרגיל. אני רוצה לחדד את הנקודה הזו כי היא מעניינת.

כשאנחנו פותרים משוואות עם נעלמים אנחנו בדרך כלל משחקים משחק "נדמה לי". אנחנו אומרים "נניח ש-{% equation %}x{% endequation %} הוא מספר קונקרטי שפותר את המשוואה, אנחנו פשוט עדיין לא יודעים מה הוא אז אנחנו כותבים אות במקומו. אבל כל המניפולציות שאנחנו עושים הן מניפולציות שעושים עם מספרים". כל זה נכון ותקין לחלוטין, אבל בשלב כלשהו בהיסטוריה של האלגברה, המתמטיקאים החליטו שיהיה מעניין גם לאמץ נקודת מבט <strong>נוספת</strong> על זה, ולחשוב על יצורים כמו {% equation %}x^{2}+2x-15{% endequation %} - מה שנקרא <strong>פולינומים</strong> - בתור אובייקטים אלגבריים בפני עצמם (<a href="https://gadial.net/2018/03/29/polynomial_rings/">הנה פוסט שלם</a> בנושא למי שלא רוצים להסתפק במה שאכתוב כאן). מה זה "אובייקט אלגברי"? זה משהו שאפשר להגדיר עליו כללי חשבון עם כפל וחיבור וכדומה שמקיימים תכונות נחמדות כמו חוקי החילוף והפילוג וכדומה. בדרך ההתבוננות הזו, {% equation %}x^{2}+2x-15{% endequation %} הוא פשוט דרך כתיבה "מעניינת" לסדרת המספרים {% equation %}\left(1,2,-15\right){% endequation %} (סדרת <strong>המקדמים</strong> של הפולינום). זו חשיבה קצת שונה מהחשיבה שפולינום הוא בסך הכל כתיב מקוצר לתרגיל כלשהו ("לוקחים מספר, מעלים אותו בריבוע, מוסיפים לו את עצמו פעמיים ומחסרים 15 מהתוצאה").

חיבור של פולינומים הוא פשוט חיבור של שתי סדרות המספרים שמגדירות אותם, "איבר איבר". הנה דוגמא: לפולינום {% equation %}x^{2}+2x-15{% endequation %} אני אחבר את הפולינום {% equation %}x+5{% endequation %}. כדי לעשות את זה, אני יכול לכתוב את שני הפולינומים הללו בתור סדרות מקדמים: {% equation %}\left(1,2,-15\right){% endequation %} ו-{% equation %}\left(0,1,5\right){% endequation %}. עכשיו אני יכול לחבר את שתי הסדרות:

{% equation %}\left(1,2,-15\right)+\left(0,1,5\right)=\left(1+0,2+1,-15+5\right)=\left(1,3,-10\right){% endequation %}

קיבלתי את הפולינום {% equation %}x^{2}+3x-10{% endequation %}. עכשיו, בשביל מה כל זה היה טוב? למה לא פשוט חיברתי "כרגיל" תוך שימוש בזה ש-{% equation %}2x+x=3x{% endequation %} וכדומה? כי כך הדגמתי שאפשר לדבר על הפולינומים הללו בלי להזדקק בכלל לדיבורים על {% equation %}x{% endequation %}, שהוא לכאורה מה שלשמו נתכנסנו פה - ה"נעלם" שלנו. אולי עכשיו מתעוררת בכם שאלה אחרת - אם אפשר פשוט לדבר על סדרות של מספרים, למה לא מדברים עליהן וזהו ובמקום זה משתמשים בכתיב עם {% equation %}x{% endequation %}? אה, טוב ששאלתם - כי <strong>הכפל</strong> הוא פעולה מעניינת יותר מאשר "איבר איבר", ויותר קל להבין אותה כשיש איקס מול העיניים.

בואו נראה דוגמא פשוטה: הפולינומים {% equation %}x-3{% endequation %} ו-{% equation %}x+5{% endequation %}. אני רוצה לכפול אותם; בתור סדרות הם {% equation %}\left(1,5\right){% endequation %} ו-{% equation %}\left(1,-3\right){% endequation %} וכפל "איבר איבר" של הסדרות הללו נותן {% equation %}\left(1,-15\right){% endequation %} כלומר את {% equation %}x-15{% endequation %}, אבל זה לא מתאים למה שאנחנו חושבים עליו כשכופלים פולינומים:

{% equation %}\left(x+5\right)\left(x-3\right)=x^{2}+5x-3x-15=x^{2}+2x-15{% endequation %}

מה קרה פה? קיבלנו פולינום <strong>ממעלה גבוהה יותר</strong> מזו של אלו שהכפלנו - יצרנו סדרת מקדמים <strong>ארוכה יותר</strong>, וזה משהו שכפל "איבר איבר" לא יכול לבצע בכלל. ומאיפה הגיע ה-{% equation %}2x{% endequation %} הזה, הרי בסדרת המקדמים המקורית אין שום דבר שמזכיר את 2? הוא הגיע מהחישוב היחסית מסובך {% equation %}1\cdot5+\left(-3\right)\cdot1{% endequation %} שבו כפלנו את המקדם <strong>השני</strong> באחד הפולינומים במקדם <strong>הראשון</strong> בפולינום השני, ואת הסמטוחה הזו חיברנו אל המקדם <strong>הראשון</strong> בפולינום הראשון שמוכפל במקדם <strong>השני</strong> בפולינום השני... יש כאן פעולה שנקראת <strong>קונבולוציה</strong> של סדרות, שהיא פעולה הרבה יותר מתוחכמת מאשר "כפל איבר איבר". נשמע מפחיד? לא הבנתם איך זה עובד? לא נורא! אתם כמו האדם שדיבר פרוזה כל ימיו ולא ידע זאת; אם אתם יודעים לכפול פולינומים אתם יודעים לחשב קונבולוציות (אם אתם מכירים מטריצות, הסיפור פה די דומה: אובייקט אלגברי "חדש" שבו פעולת החיבור היא "איבר-איבר" משעממת אבל פעולת הכפל היא מחוכמת ומכניסה אותנו לעולם חדש לגמרי).

אם כן, פולינומים הם יצורים מתמטיים עצמאיים, עם פעולות חיבור וכפל משלהם, וגם סוג של פעולת חילוק - חלוקה עם שארית, כמו שיש במספרים שלמים (הדמיון לא מקרי; שלמים ופולינומים הם דוגמאות מרכזיות למשהו שנקרא <strong>תחומים אוקלידיים</strong> ו<a href="https://gadial.net/2018/03/01/euclidean_domains_and_pids/">כתבתי עליו פעם פוסט</a>). בגישה הזו, אם יש לי את המשוואה

{% equation %}\left(x-3\right)p\left(x\right)=\left(x-3\right)q\left(x\right){% endequation %}

שמתארת שוויון בין שני פולינומים, אז בהחלט <strong>אפשר</strong> לחלק ב-{% equation %}x-3{% endequation %}, וזו בהחלט <strong>לא</strong> חלוקה באפס, ולכן בהחלט <strong>כן</strong> מקבלים {% equation %}p\left(x\right)=q\left(x\right){% endequation %}. אז למה {% equation %}x+5=x+4{% endequation %} עדיין לא מתקיים?

ובכן, כי בפולינומים השוויון {% equation %}x=3{% endequation %} שפתח את כל הסיפור הזה <strong>לא מתקיים</strong>. בתור פולינומים, יש לנו בשני האגפים יצורים שונים: באגף שמאל הפולינום {% equation %}\left(1,0\right){% endequation %} ובאגף ימין הפולינום {% equation %}\left(3\right){% endequation %}. אלו סדרות מקדמים מאורכים שונים, עם ערכים שונים בתוכן. ברור שאין קשר. המשמעות <strong>האינטואיטיבית</strong> שיש לנו, של "{% equation %}x{% endequation %} הוא נעלם שאנחנו מציבים בו 3" לא קיימת אוטומטית כשמדברים על פולינומים. לכן התשובה "לא חילקתי באפס, חילקתי ב-{% equation %}x-3{% endequation %}" רק מקלקלת את הטיעון עוד יותר, כי היא מצביעה על הונאה <strong>כבר בשורה הראשונה</strong> של התרגיל.

אפשר לחפור אפילו יותר עמוק כאן אם רוצים. האמת היא שמתמטיקאים בהחלט <strong>רוצים</strong> לפעמים לבצע חשבון של פולינומים תחת ההנחה הנוספת ש-{% equation %}x=3{% endequation %}. בשביל זה הם עוברים לדבר על משהו שנקרא <strong>חוג מנה</strong> של פולינומים. בלי להיכנס יותר מדי להגדרות (<a href="https://gadial.net/2017/12/26/ideals_of_rings/">הנה פוסט בנושא</a> אם כן רוצים הגדרות), הרעיון בחוג מנה שבו {% equation %}x=3{% endequation %} הוא פשוט: פעולות החיבור והכפל של הפולינומים יהיו זהות לאלו שהצגתי קודם, למעט זה שאחרי שמבצעים אותם, מחלקים את התוצאה בפולינום {% equation %}x-3{% endequation %} ולוקחים רק את השארית. בחוג מנה כזה, הפולינום {% equation %}x-3{% endequation %} הוא <strong>שקול לאפס</strong> (כלומר, ביצוע חשבון איתו נותן את אותה תוצאה כמו ביצוע חשבון עם אפס) ולכן כמו קודם, אי אפשר לצמצם בו ואנחנו חוזרים לטיעון שהתחלנו איתו. אי אפשר להתחמק מזה - גם כשהולכים למתמטיקה גבוהה יותר מהתיכונית, אנחנו עדיין רואים שהמתמטיקאים נזהרו מאוד <strong>לא</strong> ליצור סתירות שעליהן הם מתבססים.

אגב, אם כבר הגעתי לכאן, אני רוצה להזכיר חוג מנה חביב במיוחד של פולינומים: זה שמתקבל על ידי חלוקה ב-{% equation %}x^{2}+1{% endequation %}. אפשר לחשוב על איבר כללי בחוג הזה בתור פולינום מהצורה {% equation %}a+bx{% endequation %}. בואו נכפול בשביל הכיף את {% equation %}x{% endequation %} עם עצמו: נקבל {% equation %}x^{2}{% endequation %}, שאם מחלקים אותו ב-{% equation %}x^{2}+1{% endequation %} עם שארית מקבלים את השארית {% equation %}-1{% endequation %}. כלומר בחוג הפולינומים הזה מתקיימת המשוואה {% equation %}x^{2}=-1{% endequation %}. עכשיו בואו נשתמש בסימון קצת שונה: במקום {% equation %}x{% endequation %} נכתוב {% equation %}i{% endequation %}. קיבלנו חוג פולינומים שכל איבר בו הוא מהצורה {% equation %}a+bi{% endequation %} כאשר {% equation %}i{% endequation %} מקיים {% equation %}i^{2}=-1{% endequation %}; החוג הזה נקרא <strong>המספרים המרוכבים</strong> והוא אחת מקבוצות המספרים המעניינות והחשובות במתמטיקה. וזו הדרך הפורמלית הטובה ביותר להגדיר אותה שאני מכיר (<a href="https://gadial.net/2018/04/03/field_extensions_intro/">הנה פוסט</a> שמרחיב על זה).

ועוד הערה אם אני כבר כאן - אפשר לדבר על חוגי מנה גם בהקשרים אחרים, למשל של שלמים, ואתם כבר מכירים חוגי מנה שכאלו - המפורסם שבהם הוא מה שקורה בשעון. אנחנו חושבים על השעות בשעון בתור המספרים מ-0 עד 23, כאשר 24 זה כבר "שוב פעם 0". אם השעה היא 18 ואנחנו שואלים מה תהיה השעה עוד עשר שעות, אנחנו מחשבים {% equation %}18+10=28{% endequation %} ואז מחסרים 24 מהתוצאה - כלומר, מחלקים ב-24 ולוקחים את השארית, 4. זה נקרא <strong>חשבון מודולו </strong><strong>24</strong> (<a href="https://gadial.net/2013/05/13/modular_arithmetic/">הנה פוסט שלי</a> על חשבון מודולרי). חשבון כזה יכול להיות טריקי יותר מחשבון "רגיל": למשל, {% equation %}4\cdot6=0{% endequation %} בחשבון הזה. למספרים כאלו ששונים מאפס אבל המכפלה שלהם עדיין יוצאת אפס קוראים <strong>מחלקי אפס</strong>, והם עוד דוגמא למספרים <strong>שלא מקיימים את כלל הצמצום</strong>. למשל, אם יש לי את המשוואה

{% equation %}4x=4y{% endequation %}

כשהמשוואה הזו היא מודולו 24, אני לא יכול להסיק ש-{% equation %}x=y{% endequation %}. הנה דוגמא נגדית: {% equation %}x=4,y=10{% endequation %}. אלו שני מספרים ששניהם קטנים מ-24 (כלומר, הם לא שקולים מודולו 24 וצריכים להיחשב "אותו דבר") אבל המכפלה של שניהם ב-4 מניבה 16. שימו לב שאני פדנט ומתעקש לא לדבר על "אסור לחלק ב-4" אלא אומר משהו יותר בסיסי, שאסור <strong>לצמצם</strong> את 4 משני האגפים - הסיבה לכך היא שיש חוגים במתמטיקה שבהם אין משמעות ל"חלוקה" באיבר אבל עדיין אפשר לדבר על היכולת לצמצם אותו משני האגפים.

זה מסיים את ההתייחסות הפרטנית שלי ל"כשל" שאיתו פתחתי. עדיין נשארו לנו כמה שאלות. הראשונה, מאיפה הוא הגיע בכלל. דברים כאלו בדרך כלל מופצים באינטרנט הרחב הרבה לפני שהם מעוברתים ומגיעים אלינו. במקרה הנוכחי אין לי מושג מה המקור. כמובן, תעלולים שמערבים חלוקה באפס כדי להגיע ל"סתירה" הם עתיקי יומין ורואים אחד כזה כל כמה חודשים, אבל את האחד הספציפי הזה? עוד לא ראיתי. והסיפור עם ניוטון ו-1704? הוא חדש לי לגמרי. מאיפה הגיעה השנה 1704 דווקא? ניסיתי להתחקות על עקבות הסיפור הזה באינטרנט בעזרת מספר הקסם 1704 וחברים אבל לא מצאתי כלום. אולי אתם תצליחו יותר ממני? לפעמים סיפורים כאלו מובילים לספרים של ממש, כאלו שאפשר למצוא בחנויות וכתבו אנשים מכובדים ומהוגנים ומשלמים עבורם כסף, ואז הבידור גדול שבעתיים.

זה משאיר לנו רק את השאלה האחרונה - האם כל המתמטיקה אכן מבוססת על כשלים לוגיים? כמובן, לא הכשל הלוגי <strong>הזה</strong> עם ה-{% equation %}1=0{% endequation %} שהוסק בצורה שגויה, אבל האם יש לנו הוכחה שהמתמטיקה נמצאת על בסיס יציב וחף מכשלים?

התשובה היא שאנחנו <strong>מאמינים</strong> שהמתמטיקה כיום חפה מכשלים כאלו, אבל אין לנו <strong>הוכחה משכנעת</strong> לכך, וכרגע נראה שהוכחה כזו <strong>לעולם לא תתקיים</strong>. הייתה תקופה בתולדות המתמטיקה שבה הבעיה הזו נראתה אקוטית הרבה יותר מאשר היום - שיא התקופה הזו היה בתחילת המאה ה-20, כאשר בבסיס של המתמטיקה דאז <strong>באמת</strong> התגלו סתירות ונדרשה עבודת תיקון לא מעטה בשביל להתגבר עליהן. האופטימיות של התקופה גרמה למתמטיקאים לקוות שאפשר יהיה להתגבר עליהן "אחת ולתמיד" - למצוא ביסוס למתמטיקה שדורש הנחות יסוד <strong>מאוד פשוטות</strong>, שיהיה "ברור מאליו" שהן נכונות ואפשר יהיה להוכיח שלא יכולות להוביל לסתירות. השאיפה הזו נקראת <strong>התוכנית של הילברט</strong> והיא... נכשלה. לא במובן זה שנמצאו סתירות במתמטיקה, אלא במובן זה שנמצאה הוכחה - "<strong>משפט אי השלמות השני של גדל</strong>" - שאי אפשר יהיה לתת בסיס פשוט שכזה והוכחות של ממש ש"המתמטיקה נטולת סתירות" ייאלצו להיות מסובכות ועם הנחות לא מוכחות משל עצמן. שימו לב לנקודה העדינה פה: זה שאי אפשר להוכיח שאין סתירות במתמטיקה <strong>לא אומר</strong> שיש סתירות במתמטיקה; זה רק אומר שזו טענה שאין לנו דרך להוכיח בצורה "פשוטה". יש טענות מתמטיות רבות אחרות שאין דרך להוכיח בצורה "פשוטה"; למעשה, משפט אי השלמות <strong>הראשון</strong> של גדל נותן לנו דרך שיטתית לבנות טענות כאלו, ובהתבסס עליו אפשר להוכיח את המשפט השני. <a href="https://gadial.net/2009/05/03/godel_incompleteness_yes/">יש לי פוסט</a> על משפטי גדל, אבל אם כל נושא היסודות הרעועים-כן-או-לא של המתמטיקה מעניין אתכם, אני ממליץ על הספר "משפטי גדל ובעיית היסודות של המתמטיקה" של ארנון אברון שמכסה את הנושא בצורה בהירה ומעניינת מאוד.

ולאלו שעדיין מחפשים "סתירות" במתמטיקה - למה אתם עושים את זה בעצם? למה לשחק עם משוואות טיפשיות כשאתם יכולים לשחק עם דברים מגניבים כמו <a href="https://gadial.net/2010/05/02/congruent_numbers_and_elliptic_curves/">עקומים אליפטיים</a>? המתמטיקה מגניבה. אל תחפשו בה סתירות אלא כיף! תתעוררו, אנשים!
