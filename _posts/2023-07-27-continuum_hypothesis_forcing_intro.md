---
title: "בעקבות השערת הרצף, חלק ה': מבוא לשיטת הכפייה"
layout: post
categories:
  - תורת הקבוצות
tags:
  - השערת הרצף
image: "/assets/img/main/forcing.png"
---


<h2>מבוא</h2>

הגענו סוף סוף לתיאור שיטת הכפייה של פול כהן, אבל כדאי שנתקדם לאט ובזהירות. שום דבר בשיטה אינו קשה או מסובך במיוחד, אבל היא מאוד <strong>אבסטרקטית</strong> במבט ראשון ולכן כדאי שכל הזמן תהיה לנו דוגמא מול העיניים, לכל הפחות דוגמת צעצוע. אחת מהסיבות שאני אוהב את הספר של Weaver על כפייה הוא שיטת ההצגה שלו של הנושא הזה, ולכן אעקוב אחרי מה שהוא עושה בצורה די צמודה.

אז לפני שמתחילים, נחזור אל נקודת המוצא שאליה הגענו בעקבות הפוסטים האחרונים. אנחנו עובדים במסגרת מערכת פורמלית שנקראת {% equation %}\text{ZFC}^{+}{% endequation %} שכוללת את אקסיומות ZFC הרגילות ועוד יצור {% equation %}\mathcal{M}{% endequation %} שהוא קבוצה <strong>טרנזיטיבית בת מניה</strong> שאפשר להניח עליה שמקיימת את כל האקסיומות של ZFC (הסיפור קצת יותר מסובך מזה אבל כבר הבהרתי את הדקויות בפוסטים הקודמים).

השערת הרצף, כזכור, היא הטענה ש-{% equation %}2^{\aleph_{0}}=\aleph_{1}{% endequation %}, כאשר {% equation %}\aleph_{1}{% endequation %} היא העוצמה האינסופית הקטנה ביותר שגדולה מ-{% equation %}\aleph_{0}{% endequation %}, ואילו {% equation %}\aleph_{0}{% endequation %} היא פשוט עוצמת הטבעיים, {% equation %}\aleph_{0}=\left|\mathbb{N}\right|{% endequation %}. אנחנו יודעים ש-{% equation %}2^{\aleph_{0}}=\left|\mathcal{P}\left(\mathbb{N}\right)\right|{% endequation %}, ולכן כדי להראות שהשערת הרצף נכונה אנחנו צריכים להראות התאמה חח"ע ועל בין הקבוצה {% equation %}\mathcal{P}\left(\mathbb{N}\right){% endequation %} (קבוצת כל הקבוצות של הטבעיים) ו-{% equation %}\aleph_{1}{% endequation %} (הסודר הקטן ביותר שאינו שקול עוצמה לאף סודר קטן ממנו <strong>וגם</strong> גדול מ-{% equation %}\aleph_{0}{% endequation %} שהוא הסודר האינסופי הראשון). 

עכשיו, את כל המושגים הללו - הטבעיים {% equation %}\mathbb{N}{% endequation %}, קבוצת תתי-הקבוצות של הטבעיים {% equation %}\mathcal{P}\left(\mathbb{N}\right){% endequation %} והעוצמה {% equation %}\aleph_{1}{% endequation %} - אפשר לקחת גם אל הקבוצה {% equation %}\mathcal{M}{% endequation %}. הבניה של האובייקטים הללו מתבססת על ZFC, ולכן אפשר להפעיל את אותה בניה גם במסגרת {% equation %}\mathcal{M}{% endequation %} ולקבל קבוצות כלשהן, <strong>שהן לאו דווקא הקבוצות המקוריות</strong>. הן ה"פרשנויות" של הקבוצות הללו במסגרת היקום הזעיר של {% equation %}\mathcal{M}{% endequation %}. את הפרשנויות הללו אני אסמן ב-{% equation %}\mathbb{N}^{\mathcal{M}},\mathcal{P}\left(\mathbb{N}\right)^{\mathcal{M}},\aleph_{1}^{\mathcal{M}}{% endequation %}.

לפעמים הפרשנות של היקום הזעיר <strong>חייבת</strong> להתלכד עם המושג הכללי. זה מה שקורה עם הטבעיים. מהם הטבעיים? כזכור, {% equation %}0{% endequation %} הוא בסך הכל הקבוצה הריקה {% equation %}\emptyset{% endequation %}. הקיום של הקבוצה הריקה נובע מ-ZFC (בעזרת אקסיומת ההפרדה), ולכן יש "קבוצה ריקה" {% equation %}A{% endequation %} ששייכת ל-{% equation %}\mathcal{M}{% endequation %}. מה זה אומר ש-{% equation %}A{% endequation %} היא קבוצה ריקה? שהיא מקיימת את הנוסחה

{% equation %}\forall a\neg\left(a\in A\right){% endequation %}

אז כשאנחנו מצטמצמים אל {% equation %}\mathcal{M}{% endequation %}, זה אומר שמתקיים

{% equation %}\forall a\in\mathcal{M}\neg\left(a\in A\right){% endequation %}

האם זה אומר ש-{% equation %}A{% endequation %} היא קבוצה ריקה גם במובן ה"כללי", הרגיל? ש-{% equation %}A=\emptyset{% endequation %}? לכאורה ב-{% equation %}A{% endequation %} יכולים להיות איברים, פשוט לא איברים ששייכים ל-{% equation %}\mathcal{M}{% endequation %}. אלא שכאן נחלצת לעזרתנו העובדה ש-{% equation %}\mathcal{M}{% endequation %} היא לא סתם קבוצה אקראית ששלפנו מהרחוב - עבדנו מאוד קשה כדי לקבל {% equation %}\mathcal{M}{% endequation %} בצורה כזו שהיא תהיה <strong>טרנזיטיבית ובת מניה</strong>. בפרט, טרנזיטיביות פירושה שאם {% equation %}A\in\mathcal{M}{% endequation %} אז {% equation %}A\subseteq\mathcal{M}{% endequation %} - ב-{% equation %}A{% endequation %} אין "איברים מיותרים". לכן אם {% equation %}A{% endequation %} מקיימת את הדרישה מקבוצה ריקה ב-{% equation %}\mathcal{M}{% endequation %}, היא חייבת להיות הקבוצה הריקה באופן כללי, {% equation %}A=\emptyset{% endequation %}. קיבלנו שמה שנקרא 0 ביקום הזעיר של {% equation %}\mathcal{M}{% endequation %} הוא גם מה שנקרא 0 בעולם הרחב. מכיוון ש-{% equation %}1=0\cup\left\{ 0\right\} {% endequation %} נקבל שגם 1 זהה בשני היקומים הללו וכן הלאה: אנחנו מקבלים ש-{% equation %}\mathbb{N}{% endequation %} היא אותה קבוצה גם בעולם הרחב וגם ביקום הספציפי של {% equation %}\mathcal{M}{% endequation %}, כלומר {% equation %}\mathbb{N}^{\mathcal{M}}=\mathbb{N}{% endequation %}. על דבר כזה אומרים שהמושג "קבוצת המספרים הטבעיים" הוא <strong>אבסולוטי</strong> - אותו דבר בכל המודלים הטרנזיטיביים של ZFC.

לעומת זאת ברור שהקבוצה {% equation %}\mathcal{P}\left(\mathbb{N}\right){% endequation %} <strong>לא יכולה</strong> להיות אותו דבר גם בעולם הרחב וגם ב-{% equation %}\mathcal{M}{% endequation %}, מהטעם הפשוט שבעולם הרחב זו קבוצה לא בת מניה, אבל ב-{% equation %}\mathcal{M}{% endequation %} כל הקבוצות הן בנות מניה. איך זה עובד? כי על פי ההגדרה, {% equation %}\mathcal{P}\left(\mathbb{N}\right){% endequation %} היא לא "קבוצת כל תתי-הקבוצות האפשריות של הטבעיים"; היא "הקבוצה שלכל קבוצה של טבעיים בעולם שלנו, היא שייכת לה". לא נראה שיש הבדל בין שני אלו? אוקיי, בואו נעבור לפורמליסטיקה: {% equation %}\mathcal{P}\left(\mathbb{N}\right){% endequation %} היא הקבוצה {% equation %}A{% endequation %} שמקיימת את הנוסחה

{% equation %}\forall a\in\mathcal{M}\left(a\subseteq\mathbb{N}\to a\in A\right){% endequation %}

אם מלכתחילה ב-{% equation %}\mathcal{M}{% endequation %} לא מופיעות כל תתי-הקבוצות האפשריות של טבעיים, גם ב-{% equation %}\mathcal{P}\left(\mathbb{N}\right)^{\mathcal{M}}{% endequation %} הן לא חייבות כולן להופיע, רק אלו שב-{% equation %}\mathcal{M}{% endequation %}: אנחנו פשוט מקבלים {% equation %}\mathcal{P}\left(\mathbb{N}\right)^{\mathcal{M}}=\mathcal{P}\left(\mathbb{N}\right)\cap\mathcal{M}{% endequation %}. כמובן, זו שאלה טובה - אילו תת-קבוצות של טבעיים לא נמצאות ב-{% equation %}\mathcal{M}{% endequation %}? האם למשל {% equation %}\left\{ 2,6,7\right\} {% endequation %} לא תהיה ב-{% equation %}\mathcal{M}{% endequation %}? ובכן, לא, כי את הקיום של הקבוצה הספציפית הזו, כמו גם של כל קבוצה סופית אחרת, אני יכול להוכיח מפורשות במסגרת ZFC. אבל צריך לזכור שתת-קבוצות של טבעיים יש <strong>המון</strong>. יש מספר לא בן מניה כאלו. זה אומר שיש קבוצות שאף תיאור מילולי בעברית לא יוכל לתאר (יש מספר בן מניה של תיאורים מילוליים בעברית, כי כל תיאור כזה הוא מחרוזת סופית מעל אלפבית סופי) ושיש קבוצות שאין ב-ZFC הוכחה לקיומן (יש מספר בן מניה של הוכחות ב-ZFC כי כל הוכחה כזו היא סדרה סופית של מחרוזות סופיות מעל אלפבית בן מניה). זהו אותו איזור הדמדומים של קבוצות טבעיים מסתוריות שאין לנו איך לדבר עליהן, שבו הפשטות של {% equation %}\mathcal{M}{% endequation %} באה לידי ביטוי.

נעבור אל {% equation %}\aleph_{1}^{\mathcal{M}}{% endequation %}. מה ידוע לנו עליו? הרבה פחות, אבל משהו אחד אנחנו כן יודעים בודאות: הוא <strong>סודר</strong>. למה? כי גם "להיות סודר" זו תכונה אבסולוטית. בואו נראה את זה פורמלית אפילו אם זה קצת טרחני וחוזר על מה שכבר אמרתי. נניח ש-{% equation %}A{% endequation %} היא סודר ב-{% equation %}\mathcal{M}{% endequation %} ונוכיח שהיא סודר באופן כללי. ראשית צריך להראות ש-{% equation %}A{% endequation %} טרנזיטיבית. ניקח {% equation %}a\in A{% endequation %} כלשהו. עכשיו, בגלל ש-{% equation %}\mathcal{M}{% endequation %} טרנזיטיבית אז {% equation %}a\in\mathcal{M}{% endequation %} ולכן הטענה "{% equation %}A{% endequation %} טרנזיטיבית ב-{% equation %}\mathcal{M}{% endequation %}" תקפה ספציפית עבור {% equation %}a{% endequation %} ואומרת ש-{% equation %}a\subseteq A{% endequation %}. זה מראה ש-{% equation %}A{% endequation %} טרנזיטיבית באופן אבסולוטי. בצורה דומה, צריך להראות ש-{% equation %}A{% endequation %} סדורה לינארית על ידי {% equation %}\in{% endequation %}, כלומר שאם {% equation %}a_{1},a_{2}\in A{% endequation %} אז {% equation %}a_{1}\in a_{2}{% endequation %} או ההפך. ושוב - אנחנו מקבלים ש-{% equation %}a_{1},a_{2}\in\mathcal{M}{% endequation %} ולכן העובדה ש-{% equation %}A{% endequation %} סודר ב-{% equation %}\mathcal{M}{% endequation %} אומרת שכל זוג איברים של {% equation %}A{% endequation %} ששייכים ל-{% equation %}\mathcal{M}{% endequation %} ניתנים להשוואה ולכן גם {% equation %}a_{1},a_{2}{% endequation %} ניתנים להשוואה.

יופי, אז {% equation %}\aleph_{1}^{\mathcal{M}}{% endequation %} הוא סודר גם במובן האבסולוטי. מה שכן, הוא גם תת-קבוצה של {% equation %}\mathcal{M}{% endequation %} שהיא בת מניה ולכן הוא עצמו קבוצה בת מניה; אז אנחנו יודעים ש-{% equation %}\aleph_{1}^{\mathcal{M}}{% endequation %} הוא סודר בן מניה (תחשבו על {% equation %}\omega^{\omega}{% endequation %} וחברים דומים - אלו דוגמאות לסודרים בני מניה שהם עדיין "לא כאלו קטנים"). עכשיו, אם {% equation %}\aleph_{1}^{\mathcal{M}}{% endequation %} היא קבוצה בת מניה וגם {% equation %}\mathcal{P}\left(\mathbb{N}\right)^{\mathcal{M}}{% endequation %} היא קבוצה בת מניה אז <strong>אנחנו יודעים</strong> שקיימת התאמה חח"ע ועל {% equation %}f:\mathcal{P}\left(\mathbb{N}\right)^{\mathcal{M}}\to\aleph_{1}^{\mathcal{M}}{% endequation %}. למה זה לא מסיים את הסיפור מבחינתנו? זה <strong>לב העניין</strong>: אמנם, ההתאמה {% equation %}f{% endequation %} קיימת, אבל זה לא אומר שהיא שייכת ל-{% equation %}\mathcal{M}{% endequation %}: בסופו של דבר, {% equation %}f{% endequation %} היא פונקציה, כלומר פורמלית היא <strong>קבוצה של זוגות סדורים</strong>. האם הקבוצה הזו חייבת להשתייך אל {% equation %}\mathcal{M}{% endequation %}? לא. אם אנחנו רוצים שהיא תשתייך ל-{% equation %}\mathcal{M}{% endequation %}, נצטרך "להכריח" את {% equation %}\mathcal{M}{% endequation %} לכלול אותה. <strong>לכפות עליו</strong> לכלול אותה; מכאן השם של הטכניקה מגיע.

כמובן, אפשר לשאול למה לא לעשות משהו ממש פשוט: להגדיר {% equation %}\mathcal{M^{\prime}}=\mathcal{M}\cup\left\{ f\right\} {% endequation %} וחסל. אפשר לעשות את זה, אבל שום דבר לא מבטיח לנו שבמקרה הזה, {% equation %}\mathcal{M^{\prime}}{% endequation %} עדיין תקיים את אקסיומות ZFC; הרי ברגע שהוספנו איבר אנחנו צריכים גם לוודא שיתקיימו אקסיומות כמו זיווג (כלומר, צריך להוסיף פנימה כל קבוצה שהיא זוג של האיבר החדש + איבר קיים) וקבוצת החזקה וכו' - אי אפשר סתם להוסיף איבר וזהו! ואפילו אם הרחבנו איכשהו את {% equation %}\mathcal{M}{% endequation %} וקיבלנו {% equation %}\mathcal{M^{\prime}}{% endequation %} קסומה שכוללת את {% equation %}f{% endequation %} ואת כל מה שעוד צריך כדי ש-ZFC יתקיים, עדיין לא סיימנו, כי מה שאנחנו <strong>באמת</strong> צריכים בשלב הזה, אחרי שכבר הרחבנו את {% equation %}\mathcal{M^{\prime}}{% endequation %}, הוא שהשערת הרצף תתקיים <strong>במבנה החדש</strong> {% equation %}\mathcal{M^{\prime}}{% endequation %} הזה; אנחנו רוצים שתהיה פונקציה חח"ע ועל {% equation %}f^{\prime}:\mathcal{P}\left(\mathbb{N}\right)^{\mathcal{M}^{\prime}}\to\aleph_{1}^{\mathcal{M^{\prime}}}{% endequation %}, ואולי נצטרך <strong>שוב</strong> להרחיב את {% equation %}\mathcal{M^{\prime}}{% endequation %} כדי ש-{% equation %}f^{\prime}{% endequation %} תהיה חלק ממנו? הרי לנו תסבוכת לתפארת.

זו סיטואציה מוכרת ונפוצה במתמטיקה; אולי המקרה הכי נפוץ שבו נתקלים הוא זה של <strong>הרחבת שדות</strong>. אני יכול לקחת את השדה {% equation %}\mathbb{Q}{% endequation %} ולהוסיף לו את המספר האי-רציונלי {% equation %}\sqrt{2}{% endequation %}, אבל הקבוצה שנקבל לא תהיה שדה יותר; אנחנו חייבים להוסיף ל-{% equation %}\mathbb{Q}{% endequation %} את כל הביטויים מהצורה {% equation %}a+b\sqrt{2}{% endequation %} כדי לקבל שוב שדה (שמסומן {% equation %}\mathbb{Q}\left(\sqrt{2}\right){% endequation %}). הטכניקה הכללית של הרחבת שדות מתוארת לא בלשון הברוטלית של "בואו ניקח המון דברים ונוסיף אותם פנימה!!!!!" אלא בלשון אלגנטית ואבסטרקטית יותר: אנחנו מסתכלים <strong>חוג הפולינומים</strong> מעל השדה, לוקחים <strong>פולינום אי פריק</strong> ובונים את <strong>חוג המנה</strong> שמתקבל מחלוקה ב<strong>אידאל שנוצר</strong> על ידי הפולינום הזה. דבר דומה הולך לקרות כאן - כדי לתאר את בניית ההרחבה שלנו נשתמש בלשון חדשה וסט מושגים חדש, ואחרי קשיי העיכול הראשוניים היתרון של הגישה הזו צף על פני השטח.

<h2>תנאי כפייה</h2>

בואו נשכח בינתיים מהשערת הרצף ונציג את כל הטרמינולוגיה בהקשר של דוגמא פשוטה יחסית. נניח שאנחנו רוצים להוסיף ל-{% equation %}\mathcal{M}{% endequation %} פונקציה <strong>כלשהי</strong>. אנחנו עוד לא יודעים איזו, אבל אנחנו כן רוצים שהיא תהיה כזו שכשנוסיף אותה ל-{% equation %}\mathcal{M}{% endequation %} יתלווה אליה מבנה כלשהו שיהפוך את העבודה של "סגירת" {% equation %}\mathcal{M}{% endequation %} מסביב לה לקלה יותר. בשביל זה אנחנו רוצים לדבר על קבוצה של <strong>אילוצים</strong> שהפונקציה הזו מקיימת: האילוצים הללו ייקראו <strong>תנאי כפייה</strong> בגלל השימוש שלנו בהם לביצוע כפייה.

סוג פשוט במיוחד של אילוץ על פונקציה הוא פשוט "על הקלט {% equation %}x{% endequation %} הפונקציה מחזירה את הפלט {% equation %}y{% endequation %}", או בלשון תורת-קבוצתית, {% equation %}\left(x,y\right)\in f{% endequation %}. הכללה פשוטה של האילוץ הזה היא הרחבה שלו לאוסף כלשהו של קלטים/פלטים, ובמילים אחרות: אילוץ על {% equation %}f{% endequation %} יכול להיות פשוט <strong>פונקציה חלקית</strong>, כזו שלא מוגדרת על כל התחום שלנו עדיין.

בסדרת הפוסטים הזו ראינו דוגמה לסיטואציה כזו, למרות שגם אני כבר הספקתי לשכוח ממנה - היה משפט שעוסק באיך שאפשר למצוא למבנים מסויימים מבנים איזומורפיים שהם טרנזיטיביים, והבניה של פונקציית האיזומורפיזם נעשתה באמת על ידי התבוננות באוסף של איזומורפיזמים "חלקיים", הוכחה שהם מסתדרים טוב זה עם זה, כלומר מזדהים על התחום המשותף שלהם, ואז לקיחת איחוד של הכל. גם אצלנו אפשר לעשות משהו דומה. לדבר, נניח, על פונקציות ב-{% equation %}\left\{ 0,1\right\} ^{\mathbb{N}}{% endequation %} (פונקציות מהטבעיים לקבוצה {% equation %}\left\{ 0,1\right\} {% endequation %}; "סדרות בינאריות") ואז להסתכל על בניות חלקיות שלהן - כלומר על <strong>קבוצות</strong> של איברים מהצורה {% equation %}\left(n,b\right){% endequation %} כש-{% equation %}n\in\mathbb{N}{% endequation %} ו-{% equation %}b\in\left\{ 0,1\right\} {% endequation %}. בואו נסמן ב-{% equation %}P{% endequation %} את קבוצת כל הבניות החלקיות הללו ואת האיברים של {% equation %}P{% endequation %} (שהם בדוגמא שלנו פונקציות חלקיות) נסמן ב-{% equation %}p,q{% endequation %} וכדומה.

עכשיו אפשר לתת קצת טרמינולוגיה פשוטה (שנשתמש בה עשרות פעמים בהמשך): 

<ul> <li>נאמר ש-{% equation %}q{% endequation %} <strong>מרחיבה</strong> את {% equation %}p{% endequation %} אם {% equation %}p\subseteq q{% endequation %}, כלומר אם {% equation %}q{% endequation %} לוקחת את הפונקציה {% equation %}p{% endequation %} ואולי מוסיפה לה עוד דברים.</li>


<li>נאמר ש-{% equation %}p_{1},p_{2}{% endequation %} <strong>מתואמות</strong> אם קיימת להם הרחבה משותפת {% equation %}p_{1},p_{2}\subseteq q{% endequation %}. זה אומר שאולי {% equation %}p_{1},p_{2}{% endequation %} מוגדרות על תחומים שונים, אבל בתחום המשותף להן הערכים שלהן זהים.</li>


<li>תת-קבוצה {% equation %}D\subseteq P{% endequation %} היא <strong>צפופה</strong> אם לכל {% equation %}p\in P{% endequation %} קיימת הרחבה ב-{% equation %}D{% endequation %}.</li>

</ul>

את כל אלו אני מציג בהקשר של פונקציות חלקיות, אבל ההגדרות הללו עובדות גם אם {% equation %}P{% endequation %} היא "סתם" קבוצה, בלי הנחה מיוחדת על המבנה של האיברים שלה מעבר לכך שהם בעצמם קבוצות (כמו כל דבר שאנחנו עוסקים בו). זה יהיה השימוש שלנו ב-{% equation %}P{% endequation %} בהמשך (יש טקסטים אחרים שלוקחים את {% equation %}P{% endequation %} להיות קבוצה סדורה כלשהי; אצלנו הסדר הוא פשוט יחס ההכלה הרגיל של קבוצות). יש לנו בדיוק דרישה אחת מ-{% equation %}P{% endequation %}, אבל דרישה קריטית: ש-{% equation %}P\in\mathcal{M}{% endequation %}. כלומר, שהתנאים ה"חלקיים" שאנחנו כופים יהיו כולם שייכים ליקום הזעיר {% equation %}\mathcal{M}{% endequation %}. אנחנו הולכים לבנות את התוספת ל-{% equation %}\mathcal{M}{% endequation %} מתוך התנאים שאנחנו יודעים לנסח ב-{% equation %}\mathcal{M}{% endequation %} עצמה. אז הנה ההגדרה הפורמלית: קבוצת <strong>תנאי כפיה</strong> עבור {% equation %}\mathcal{M}{% endequation %} היא פשוט קבוצה {% equation %}P\in\mathcal{M}{% endequation %} (לפעמים קבוצה כזו מכונה <strong>מושג כפיה</strong>; תנאי הכפיה הם איבריה). ההגדרה ה"כמעט ריקה" הזו היא הסיבה שבגללה צריך לעבוד עם דוגמא מול העיניים.

עכשיו, אנחנו רוצים מושג שיתפוס את הרעיון שבו השתמשנו בפוסט הקודם ההוא, של "קבוצה של פונקציות חלקיות שמתואמות אחת עם השניה והאיחוד של כולן יתן לנו משהו טוב". לדבר הזה יש כמה שמות. שם מאוד נפוץ בספרות הוא <strong>מסנן</strong> (פילטר; <a href="https://gadial.net/2013/06/21/ultrafilters_and_ultraproducts/">הזכרתי את המושג פה</a> בעבר בהקשר אחר), אבל מה ש-Weaver הולך על פיו הוא השם <strong>אידאל</strong> (לא לערבב עם האידאלים מאלגברה מופשטת שהם משהו אחר) שמתלווה להגדרה שהיא במובן מסוים ב"היפוך כיוונים" ביחס להגדרה של מסנן. אני אשתמש כאן בהגדרה של אידאל: אידאל של {% equation %}P{% endequation %} הוא תת-קבוצה {% equation %}G\subseteq P{% endequation %} שהיא

<ul> <li>סגורה כלפי מטה: אם {% equation %}q\in G{% endequation %} ועבור {% equation %}p\in P{% endequation %} כלשהו מתקיים {% equation %}p\subseteq q{% endequation %} אז {% equation %}p\in G{% endequation %}.</li>


<li>מכוונת: אם {% equation %}p_{1},p_{2}\in G{% endequation %} אז קיים {% equation %}q\in G{% endequation %} כך ש-{% equation %}p_{1},p_{2}\subseteq q{% endequation %}.</li>

</ul>


<h2>אידאלים גנריים</h2>

אם נחזור לדוגמת בניית הפונקציה שלנו, אידאל הוא אוסף של בניות חלקיות שמסתדרות יפה זו עם זו ואם נאחד אותן נקבל משהו שהוא בעצמו פונקציה. אבל זה לא מספיק טוב לנו - אנחנו עלולים לקבל פונקציה שהיא קטנה למדי ולא באמת מגיעה אל כל מה שתנאי הכפייה {% equation %}P{% endequation %} מתארים. אז אנחנו זקוקים למושג שיתאר לנו אידאל "מספיק טוב" - המושג הזה הוא <strong>אידאל גנרי</strong>: אידאל {% equation %}G{% endequation %} הוא גנרי ביחס ל-{% equation %}\mathcal{M}{% endequation %} אם לכל קבוצה צפופה {% equation %}D\subseteq P{% endequation %} כך ש-{% equation %}D\in\mathcal{M}{% endequation %}, החיתוך של {% equation %}G{% endequation %} ו-{% equation %}D{% endequation %} אינו ריק, {% equation %}G\cap D\ne\emptyset{% endequation %}.

כדי לראות את השימושיות של ה"גנריות" הזו, בואו נחזור לדוגמא שלנו של בניית פונקציה, אבל עם מגבלה על {% equation %}P{% endequation %}: היא לא מתארת סתם בניות חלקיות של פונקציה ב-{% equation %}\left\{ 0,1\right\} ^{\mathbb{N}}{% endequation %} אלא בניות חלקיות <strong>סופיות</strong> של פונקציה כזו, כלומר ב-{% equation %}P{% endequation %} יש רק תת-קבוצות סופיות. זה טוב לנו, כי יותר קל להתעסק עם אובייקט פשוט כמו קבוצה סופית; אבל בסוף התהליך אנחנו רוצים לקבל פונקציה שהתחום שלה הוא כל {% equation %}\mathbb{N}{% endequation %}, כלומר קבוצה אינסופית.

אם אני לוקח אידאל {% equation %}G\subseteq P{% endequation %} ואז מסתכל על האיחוד של כל אבריו, {% equation %}\bigcup G{% endequation %}, אני אקבל פונקציה חלקית מ-{% equation %}\mathbb{N}{% endequation %} אל {% equation %}\left\{ 0,1\right\} {% endequation %}, שזה נחמד, אבל לא מובטח לי שהתחום של הפונקציה יהיה כל {% equation %}\mathbb{N}{% endequation %}. אם לעומת זאת {% equation %}G{% endequation %} יהיה <strong>אידאל גנרי</strong>, התחום כן הולך להיות כל {% equation %}\mathbb{N}{% endequation %}. למה? הנה תעלול פשוט: יהא {% equation %}k\in\mathbb{N}{% endequation %} כלשהו; נסתכל על הקבוצה {% equation %}D_{k}\subseteq P{% endequation %} שכוללת את כל הפונקציות החלקיות מ-{% equation %}\mathbb{N}{% endequation %} אל {% equation %}\left\{ 0,1\right\} {% endequation %} שהן <strong>מוגדרות</strong> עבור {% equation %}k{% endequation %}. זו מן הסתם קבוצה צפופה ב-{% equation %}P{% endequation %}, כי לכל פונקציה חלקית ב-{% equation %}P{% endequation %} ניתן להרחיב אותה לקבלת משהו ב-{% equation %}D_{k}{% endequation %} על ידי זה שמוסיפים לה את {% equation %}\left(k,0\right){% endequation %} או את {% equation %}\left(k,1\right){% endequation %}; התוצאה בכל מקרה תישאר קבוצה סופית ולכן תהיה שייכת ל-{% equation %}P{% endequation %}.

עכשיו, אם {% equation %}G{% endequation %} הוא אידאל גנרי, אז {% equation %}G\cap D_{k}\ne\emptyset{% endequation %}. במילים אחרות: ב-{% equation %}G{% endequation %} קיימת פונקציה חלקית שמוגדרת עבור {% equation %}k{% endequation %}. אנחנו לא יודעים שום דבר אחר על הפונקציה הזו, או מה הערך שהיא נותנת ל-{% equation %}k{% endequation %}; אנחנו רק יודעים שהיא מוגדרת על {% equation %}k{% endequation %}, ולכן כשניקח איחוד של {% equation %}G{% endequation %} התוצאה תהיה פונקציה שמוגדרת עבור {% equation %}k{% endequation %}, וזאת לכל {% equation %}k\in\mathbb{N}{% endequation %}, כך שהתחום של הפונקציה הזו יהיה {% equation %}\mathbb{N}{% endequation %}. אלגנטי למדי, וסוג של מסביר את ה"גנריות" בשם של {% equation %}G{% endequation %}: הרעיון פה הוא ש-{% equation %}G{% endequation %} איכשהו מקיף את "כל" האיזורים ש-{% equation %}P{% endequation %} מתעסק בהם, בלי להתמקד באיזור מסוים ולאבד את ה"גנריות" שלו.

אוקיי, השתכענו שאידאל גנרי זה מגניב, אבל למה בכלל קיים משהו כזה? או, טוב ששאלתם, בואו נוכיח שלכל קבוצת תנאי כפייה {% equation %}P{% endequation %} קיים אידאל גנרי. אפילו נוכיח טיפה יותר מזה: שאם {% equation %}p_{0}\in P{% endequation %} הוא תנאי כפיה ספציפי כלשהו, אז קיים אידאל גנרי {% equation %}G\subseteq P{% endequation %} ביחס ל-{% equation %}\mathcal{M}{% endequation %} שמכיל אותו, {% equation %}p_{0}\in G{% endequation %}.

ההוכחה די פשוטה אבל יש בתחילתה נקודה אחת שצריך להיזהר איתה: ל-{% equation %}P{% endequation %} יכולות להיות <strong>המון</strong> תת-קבוצות צפופות, מספר לא בן מניה של כאלו. אבל כדי לבנות אידאל שגנרי ביחס ל-{% equation %}\mathcal{M}{% endequation %} הוא <strong>לא</strong> צריך להיחתך עם כל קבוצה צפופה כזו, רק עם כאלו ששייכות ל-{% equation %}\mathcal{M}{% endequation %}, ומכיוון ש-{% equation %}\mathcal{M}{% endequation %} היא בת מניה, יש רק <strong>מספר בן מניה</strong> של קבוצות צפופות כאלו, ואפשר למספר אותן: {% equation %}D_{0},D_{1},D_{2},\ldots{% endequation %}. זהו, מעכשיו הכל פשוט.

עכשיו אפשר לבנות את {% equation %}G{% endequation %} "סדרתית". נבנה סדרה {% equation %}p_{0},p_{1},\ldots{% endequation %} של תנאי כפיה: את {% equation %}p_{0}{% endequation %} כבר יש לנו, ו-{% equation %}p_{n+1}{% endequation %} ייבחר בתור הרחבה של {% equation %}p_{n}{% endequation %} ששייכת אל {% equation %}D_{n}{% endequation %}. קיימת הרחבה כזו כי {% equation %}D_{n}{% endequation %} צפופה ב-{% equation %}P{% endequation %}. עכשיו כל מה שנשאר הוא לבנות את האידאל {% equation %}G{% endequation %} "סביב" האיברים הללו; מכיוון שאידאל דורש סגירות כלפי מטה, זה מה שניתן לו:

{% equation %}G=\left\{ p\in P\ |\ \exists n:p\subseteq p_{n}\right\} {% endequation %}

אז סגירות כלפי מטה מתקיימת על פי ההגדרה (והטרנזיטיביות של היחס {% equation %}\subseteq{% endequation %}). מה עם הדרישה שהאידאל יהיה מכוון? כלומר, שאם {% equation %}p,p^{\prime}\in G{% endequation %} אז יש להם הרחבה משותפת? זה קל: על פי הבניה של {% equation %}G{% endequation %}, קיימים {% equation %}p_{n},p_{n^{\prime}}{% endequation %} כך ש-{% equation %}p\subseteq p_{n}{% endequation %} ו-{% equation %}p^{\prime}\subseteq p_{n^{\prime}}{% endequation %}; פשוט ניקח את {% equation %}q{% endequation %} להיות או {% equation %}p_{n}{% endequation %} או {% equation %}p_{n^{\prime}}{% endequation %} - את בעל האינדקס הגדול יותר מבין שניהם.

לסיום, זה אידאל גנרי כי ככה בנינו אותו: לכל {% equation %}D_{n}{% endequation %} הוא מכיל איבר {% equation %}p_{n+1}\in D_{n}{% endequation %}. סיימנו! לבנות אידאל גנרי היה עניין די פשוט, בזכות העובדה ש-{% equation %}\mathcal{M}{% endequation %} בת מניה (עובדה שהושגה בדם יזע ודמעות מתמטיים).

אני רוצה לסיים את הפוסט הזה בחלק מהפאנץ' של אידאלים גנריים: הדבר שאנחנו בונים באמצעותם הולך להיות משהו חדש, שיוצא <strong>מחוץ</strong> לגבולות {% equation %}\mathcal{M}{% endequation %}. נראה את זה עם דוגמת הפונקציה החלקית שלנו. מה שכמובן נכון הוא שב-{% equation %}\mathcal{M}{% endequation %} יש הרבה פונקציות מלאות מ-{% equation %}\mathbb{N}{% endequation %} אל {% equation %}\left\{ 0,1\right\} {% endequation %} (בעזרת ZFC קל לבנות למשל את הפונקציה שנותנת 0 לכל קלט), אבל אנחנו נוכל להשתמש בטיעון דמוי לכסון כדי להראות שלכל {% equation %}g:\mathbb{N}\to\left\{ 0,1\right\} {% endequation %} כך ש-{% equation %}g\in\mathcal{M}{% endequation %}, נקבל {% equation %}f\ne g{% endequation %} כאשר {% equation %}f=\bigcup G{% endequation %}.

הרעיון פשוט: לכל פונקציה {% equation %}g\in\mathcal{M}{% endequation %} שכזו, נסתכל על הקבוצה הצפופה {% equation %}D_{g}{% endequation %} שכוללת את כל הפונקציות החלקיות הסופיות ב-{% equation %}P{% endequation %} ש<strong>לא מסכימות</strong> עם {% equation %}g{% endequation %} לפחות על קלט אחד. זו קבוצה צפופה כי לכל פונקציה חלקית, קיים קלט אחד לפחות שלה שטרם הגדרנו (למעשה, קיימים אינסוף כאלו; הפונקציה החלקית מוגדרת רק על מספר סופי של קלטים). נניח שהיא לא מוגדרת על {% equation %}k{% endequation %}, אז נרחיב אותה על ידי הוספת {% equation %}\left(k,1-g\left(k\right)\right){% endequation %}, ונקבל פונקציה שלא מסכימה עם {% equation %}g{% endequation %} על הערך {% equation %}k{% endequation %}. יפה.

עכשיו, בנינו את {% equation %}G{% endequation %} כך שיהיה לו חיתוך לא ריק עם כל הקבוצות הצפופות <strong>ששייכות</strong> אל {% equation %}\mathcal{M}{% endequation %}. אותה {% equation %}D_{g}{% endequation %} בהחלט שייכת אל {% equation %}\mathcal{M}{% endequation %}, כי אפשר לבנות אותה מתוך {% equation %}g{% endequation %} באמצעות אקסיומות {% equation %}\text{ZFC}{% endequation %}: {% equation %}D_{g}=\left\{ f\in P\ |\ \exists n\in\mathbb{N}:f\left(n\right)\ne g\left(n\right)\right\} {% endequation %}, כך שיש לנו הפעלה של אקסיומת ההפרדה על {% equation %}P\in\mathcal{M}{% endequation %}. לכן האידאל הגנרי {% equation %}G{% endequation %} שלנו פוגש את {% equation %}D_{g}{% endequation %}: {% equation %}G\cap D_{g}\ne\emptyset{% endequation %}. כלומר קיימת ב-{% equation %}G{% endequation %} פונקציה שלא מסכימה עם {% equation %}g{% endequation %}, ולכן כשנבנה את {% equation %}f{% endequation %} כאיחוד כל הפונקציות ב-{% equation %}G{% endequation %} היא לא תסכים עם {% equation %}g{% endequation %}, מה שמסיים את ההוכחה הזו.

בזאת סיימנו את הצגת מושגי הבסיס שלנו: תנאי כפייה, ואידאלים גנריים. השלב הבא הוא לראות איך אנחנו מרחיבים את {% equation %}\mathcal{M}{% endequation %} באמצעות {% equation %}G{% endequation %}. זה הולך להיות החלק הקשה ביותר להבנה, מבחינה קונספטואלית; ברגע שנתגבר עליו אמנם עדיין תהיה לנו עבודה טכנית לא מועטה עד השערת הרצף, אבל כבר יהיה יותר ברור מה אנחנו בעצם עושים. 