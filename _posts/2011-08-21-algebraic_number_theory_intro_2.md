---
id: 1289
title: "תורת המספרים האלגברית על קצה המזלג, חלק ב' - מתקפת האידאלים"
date: 2011-08-21 12:26:33
layout: post
categories: 
  - אלגברה מופשטת
  - תורת המספרים
tags: 
  - אידאלים
  - תורת המספרים האלגברית
---
<a href="http://www.gadial.net/?p=1281">בפוסט הקודם</a> על תורת המספרים האלגברית תיארתי את "שדה המשחק" שלנו - שדה מספרים {% equation %}K{% endequation %} (הרחבה אלגברית סופית של {% equation %}\mathbb{Q}{% endequation %}) וחוג השלמים שלו {% equation %}\mathcal{O}_{K}{% endequation %} (אוסף השלמים האלגבריים ב-{% equation %}K{% endequation %} - מספרים שמאפסים פולינום מתוקן במקדמים שלמים). חוגי שלמים צצים באופן טבעי בתורת המספרים - אמרתי שפתרון משוואת פל {% equation %}x^{2}-dy^{2}=1{% endequation %} שקול למציאת ההפיכים בחוג השלמים של {% equation %}K=\mathbb{Q}\left(\sqrt{d}\right){% endequation %}; כמו כן, הפתרון של קומר ל(מקרים רבים של) משפט האחרון של פרמה מתבסס על חוג השלמים של <a href="http://www.gadial.net/?p=183">ההרחבה הציקלוטומית</a> {% equation %}\mathbb{Q}\left(\omega_{p}\right){% endequation %}, כש-{% equation %}\omega_{p}{% endequation %} הוא שורש יחידה מסדר {% equation %}p{% endequation %}. בקיצור, עולמות מעניינים, אבל לרוע המזל - לא בכולם יש פירוק יחיד (עד כדי סדר, וכפל בהפיכים) לגורמים. האתגר שעמד בפני קומר וממשיכיו הוא למצוא דרך לשמר לפחות מקצת מהיתרונות של פירוק לגורמים גם בעולם הזה, והרעיון של קומר היה מוצלח למדי - גם אם אין פירוק יחיד לגורמים שהם אברי {% equation %}\mathcal{O}_{K}{% endequation %}, אולי אם נחפור קצת "עמוק יותר" כן יצוץ פירוק לגורמים?

כדי להבין את זה כדאי לחזור לדוגמה מהפוסט הקודם: {% equation %}60=12\cdot5=3\cdot20{% endequation %}. יש לנו כאן שני פירוקים שונים מהותית של 60, אבל אנחנו יודעים שאין כאן בעיה כי הפירוקים הללו "לא מפורקים עד הסוף". את {% equation %}12{% endequation %} אפשר לפרק שוב ולקבל {% equation %}12=2\cdot2\cdot3{% endequation %}; ואת {% equation %}20{% endequation %} אפשר לפרק שוב ולקבל {% equation %}20=2\cdot2\cdot5{% endequation %}, ובסוף נקבל את הפירוק היחיד {% equation %}60=2\cdot2\cdot3\cdot5{% endequation %}. אם כן, מה שגרם לנו ל"אשליה" שאין פירוק יחיד הוא ש<strong>לא פירקנו מספיק</strong> את המספר.

מה שקומר עושה הוא להרחיב במובן מסויים את המספרים המרוכבים על ידי המצאה של מה שהוא כינה "מספרים מרוכבים אידאליים" שהם מה שמאפשר לו להמשיך את הפירוק. רק שהשיטה הזו, גאונית ככל שתהיה, כנראה תגרום להרמת גבה מסויימת אם אציג אותה כאן, ובטח שלביקורת על השימוש במילים "מספרים מרוכבים אידאליים". ראשית, לא ברור מאיפה המספרים הללו צצו ואיך בונים אותם בכלל (למיטב הבנתי קומר לא השקיע מאמץ בנקודה הזו). שנית, לפעמים מספר מרוכב אידאלי הוא מספר מרוכב "אמיתי" ולפעמים לא - לא ברורה כל כך הההבדלה בין שני הסוגים. שלישית, למרות שיש למספרים האידאליים מושג של כפל שמתאים באופיו לזה של מספרים "רגילים", ולכן אפשר לדבר על פירוק לגורמים, אין להם מושג של חיבור שהוא בעל משמעות סבירה שמכלילה חיבור במספרים מרוכבים "רגילים", ולכן די קשה לחשוב עליהם בתור מספרים (הדיון בשאלה חסרת התשובה "מה זה בכלל מספר" יצטרך לחכות לפעם אחרת). כנראה שבעיות מסוג זה היו בראש של דדקינד, המתמטיקאי שהכליל בצורה משמעותית את הרעיונות של קומר, כשהוא בא והגדיר באופן קצת שונה את המספרים האידאליים של קומר. הרעיון של דדקינד הוא לטעמי לא פחות מנפלא, ואני מקווה שאצליח לתאר אותו היטב.

ובכן, דדקינד אומר את הדבר הבא. הבה ונתבונן ב"מספר אידאלי" {% equation %}\mathfrak{a}{% endequation %} (הפונט המוזר הוא סטנדרטי בתחום הזה). אנחנו לא יודעים הרבה על היצור הזה, פרט לכך שהוא יודע לחלק מספרים. מה זה אומר לחלק? לכאורה, לא הרבה - אמרנו ש-{% equation %}\mathfrak{a}|x{% endequation %} אם קיים {% equation %}c{% endequation %} כך ש-{% equation %}\mathfrak{a}c=x{% endequation %}, והשוויון הזה תלוי בשאלה איך אנחנו מגדירים כפל עם {% equation %}\mathfrak{a}{% endequation %} ובינתיים זה לא ממש מוסיף לנו אינטואיציה לגבי ההתנהגות של {% equation %}\mathfrak{a}{% endequation %}. מצד שני, דדקינד זיהה שתי תכונות שמאפיינות בצורה חזקה את יחס החלוקה הזה: ראשית, אם {% equation %}\mathfrak{a}|x{% endequation %} וגם {% equation %}\mathfrak{a}|y{% endequation %} אז {% equation %}\mathfrak{a}|x+y{% endequation %} (כי אם {% equation %}\mathfrak{a}b=x{% endequation %} ו-{% equation %}\mathfrak{a}c=y{% endequation %} אז {% equation %}\mathfrak{a}\left(b+c\right)=x+y{% endequation %}). שנית, אם {% equation %}\lambda{% endequation %} הוא מספר כלשהו (בחוג השלמים שאנחנו עובדים בו) ו-{% equation %}\mathfrak{a}|x{% endequation %}, אז {% equation %}\mathfrak{a}|\lambda x{% endequation %} (כי אם {% equation %}\mathfrak{a}c=x{% endequation %} אז {% equation %}\mathfrak{a}\lambda c=\lambda x{% endequation %}).

במילים: אם מספר (אידאלי או לא) מחלק שני מספרים הוא מחלק גם את סכומם; ואם הוא מחלק מספר הוא מחלק גם את המכפלה של המספר הזה בכל מספר שלא יהיה. דדקינד הבין שאלו בדיוק שתי התכונות שהוא נזקק להן כדי לאפיין "מחלק".

בשביל להבין את הצעד הבא הבה ונתבונן לרגע רק במספרים השלמים, {% equation %}\mathbb{Z}{% endequation %}. אחת מהקבוצות הפופולריות ביותר ב-{% equation %}\mathbb{Z}{% endequation %} היא קבוצת המספרים הזוגיים - {% equation %}\left\{ 0,2,-2,4,-4,\dots\right\} {% endequation %}. אם תשאלו את האיש ברחוב מהי קבוצת הזוגיים, הוא כנראה (אני מקווה) יענה לכם שאלו <strong>מספרים שמתחלקים ב</strong>-2. זו התכונה שמאפיינת את הקבוצה הזו. שתי תכונות החלוקה שהצגתי למעלה פירושן שהזוגיים סגורים לחיבור - סכום של שני זוגיים הוא זוגי - ושהם סגורים לכפל בכל מספר שהוא - זוגי כפול מספר שלם כלשהו זה תמיד זוגי. זוכרים כשהיינו ילדים והתרעמנו על כך שטבלת הכפל של זוגי/אי זוגי מפלה לטובת הזוגיים (רק אי זוגי כפול אי זוגי זה אי זוגי)? לא זוכרים? טוב, אז זה הייתי רק אני.

אותו הדבר קורה כמובן גם בקבוצת "המספרים שמתחלקים ב-3", {% equation %}\left\{ 0,3,-3,6,-6,\dots\right\} {% endequation %} שלצערה אין לה שם מפוצץ כמו "מספרים זוגיים". גם בה סכום של שני מספרים מהקבוצה גם הוא בקבוצה, וכפל במספר שלם כלשהו משאיר אותנו בקבוצה.

ועכשיו דדקינד עשה את הקפיצה הגדולה קדימה. הוא הגדיר <strong>אידאל</strong> בתור קבוצת מספרים שמקיימת את שתי התכונות הללו: סגורה לחיבור, ו"בולעת" בכפל (לצורך הפוסט הזה ופוסטים בעתיד הבה ונעמיד פנים שאין קונוטציות גסות ל"בליעה", אוקיי? כולנו עברנו את השלב של לצחקק על זה מתישהו). לאלו מכם שמכירים קצת את תורת החוגים המושג הזה ודאי מוכר מאוד שכן זה אחד המושגים הבסיסיים ביותר בה - ובכן, זה המקום שבו הוא צץ לראשונה וזו הסיבה שהוא נקרא אידאל (בתורת החוגים ההגדרה של אידאל צריכה להיות קצת יותר נוקשה - צריך לדרוש שהוא יהיה תת-חבורה חיבורית באופן מפורש כי זה לא בהכרח נובע מתכונת הבליעה).

השאלה שעולה מייד מההגדרה של דדקינד היא מהם האידאלים של {% equation %}\mathbb{Z}{% endequation %}. ובכן, יהא {% equation %}I{% endequation %} אידאל כלשהו ב-{% equation %}\mathbb{Z}{% endequation %} שאיננו קבוצה ריקה או הקבוצה {% equation %}\left\{ 0\right\} {% endequation %} (אלו במובן מסויים מקרים טריוויאליים ולא מעניינים כל כך - על פי ההגדרה הפורמליסטית יותר הקבוצה הריקה כלל אינה אידאל). אז {% equation %}I{% endequation %} מכיל מספר שלם כלשהו ששונה מאפס, {% equation %}n{% endequation %}, ומכיוון שהוא בולע כפל בכל מספר שלם, אז גם {% equation %}\left(-1\right)\cdot n=-n{% endequation %} נמצא ב-{% equation %}I{% endequation %} וגם {% equation %}0\cdot n=0{% endequation %} נמצא ב-{% equation %}I{% endequation %}. במילים אחרות, האידאל חייב להיות "סימטרי" סביב האפס.

כעת, הגענו למסקנה שבאידאל חייבים להיות מספרים טבעיים חיוביים, אז בואו ניקח את {% equation %}n{% endequation %} להיות הקטן ביותר שבהם, ובוא ניקח את {% equation %}t{% endequation %} להיות מספר טבעי <strong>כלשהו</strong> של האידאל. אנחנו יודעים שבשלמים יש חילוק עם שארית, כלומר {% equation %}t=n\cdot q+r{% endequation %}, כשהשארית מקיימת {% equation %}0\le r&lt;n{% endequation %}. כמו כן {% equation %}n{% endequation %} שייך לאידאל ולכן {% equation %}-q\cdot n{% endequation %} שייך לאידאל, ובגלל סגירות לחיבור {% equation %}t-qn=r{% endequation %} שייך לאידאל. מכיוון ש-{% equation %}r{% endequation %} הוא מספר טבעי שקטן מ-{% equation %}n{% endequation %} ו-{% equation %}n{% endequation %} נבחר להיות המספר הטבעי החיובי הקטן ביותר ששייך לאידאל, {% equation %}r=0{% endequation %} - כלומר, {% equation %}n{% endequation %} <strong>מחלק</strong> את {% equation %}t{% endequation %} לכל {% equation %}t{% endequation %} חיובי ששייך לאידאל. ולכן הוא מחלק גם כל {% equation %}t{% endequation %} שלילי ששייך לאידאל, והוא כמובן מחלק גם את אפס ({% equation %}0\cdot n=0{% endequation %}) ולכן הוא מחלק <strong>את כל המספרים באידאל</strong>.

אפשר לעשות גם את ההפך - לקחת את המספר {% equation %}n{% endequation %}, להסתכל על "קבוצת כל המספרים ש-{% equation %}n{% endequation %} מחלק" ולראות שהיא אידאל - עשינו זאת קודם עם {% equation %}n=2,3{% endequation %}. המסקנה היא כזו: במספרים השלמים, יש לנו זהות בין אידאלים ובין מספרים, והאידאלים נתפסים בתור "קבוצת כל המספרים שמתחלקים על ידי מישהו". זה לב לבו של הרעיון של דדקינד - במקום להסתבך עם המצאה של מספרים אידאליים כדי שיחלקו לנו את המספרים הסוררים שמסרבים להתפרק, הוא <strong>מגדיר</strong> אידאלים בתור קבוצות של מספרים שמקיימות תכונות מסויימות, והתכונות הללו מבטיחות שאפשר יהיה לחשוב על הקבוצות הללו בתור "קבוצת כל המספרים שמתחלקים על ידי המספר האידאלי". זה מייתר לגמרי את הצורך לדבר על המספר האידאלי עצמו - אפשר להסתפק בדיבור על קבוצת המספרים ש<strong>אמורים</strong> להתחלק על ידו, וחסל. אין כפית.

ב"הרצאות פיינמן לפיזיקה" פיינמן מספר סיפור נפלא שבא להסביר מהי אנרגיה. הסיפור כולל ילד עם מספר כלשהו של אבני לגו, ואמא שכל יום מנסה להבין לאן האבנים נעלמו. יום אחד היא רואה את כל 20 אבני הלגו על הרצפה והכל בסדר. למחרת היא רואה רק 18, אבל יש שתי בליטות מתחת לשטיח שחייבות להיות אבני לגו, אז הסכום עדיין יוצא 20. יום אחרי זה יש רק 15 אבני לגו אבל פני המים באמבטיה עלו בכך-וכך בצורה שמתאימה ל-5 אבני לגו ששקועות במים; וכו' וכו' הסיפור ממשיך ובכל פעם מתוארת תופעה אחרת שבה לא רואים את האבנים במפורש אבל ההשפעה שלהם על העולם ברורה. פיינמן מסיים את הסיפור בפאנץ' היסטרי - הוא אומר שאנרגיה זה אותו הדבר כמו בסיפור, רק ש<strong>אין אבני לגו</strong> (יש רק את התכונה "סכום הבליטות בשטיח ועליית גובה פני המים הוא קבוע"). העניין עם האידאלים מזכיר לי את זה.

האידאל "כל המספרים שמתחלקים על ידי 2" נקרא לרוב בפשטות "האידאל שנוצר על ידי 2" ומסומן {% equation %}2\mathbb{Z}{% endequation %} או {% equation %}\left(2\right){% endequation %}, כשבסימון השני משתמשים רק כשברור מה ההקשר (כלומר, בתוך איזה חוג חי האידאל הזה). מה שראינו הוא שכל אידאל ב-{% equation %}\mathbb{Z}{% endequation %} הוא מהצורה {% equation %}n\mathbb{Z}{% endequation %}. הסימון הזה די טבעי כשחושבים על זה - על פי ההגדרה, {% equation %}n\mathbb{Z}=\left\{ n\cdot z|z\in\mathbb{Z}\right\} {% endequation %}. אידאל כזה, מהצורה "איבר כפול כל החוג", נקרא <strong>אידאל ראשי</strong>, וחוג שבו כל האידאליים הם ראשיים נקרא <strong>תחום ראשי</strong> (Principal Ideal Domain). ההוכחה שהראיתי למעלה הייתה, אם כן, הוכחה ש-{% equation %}\mathbb{Z}{% endequation %} הוא תחום ראשי, אבל אפשר לשפר אותה קצת כדי להוכיח שכל חוג שבו יש חלוקה-עם-שארית דומה לזו של {% equation %}\mathbb{Z}{% endequation %} (חוג כזה נקרא "חוג אוקלידי" כי אפשר להפעיל בו את האלגוריתם האוקלידי) הוא תחום ראשי (רק צריך להיזהר טיפה עם עניין ה"מינימלי" - מה שעושים בהוכחה הכללית הוא לבחור איבר מ<strong>נורמה</strong> מינימלית, כשקיום נורמה היא חלק ממה שנדרש מחוג אוקלידי ולא אכנס להגדרה המדוייקת שלה כעת). תחומים ראשיים הם יצורים ממושמעים למדי - אפשר להוכיח שבכל תחום ראשי יש פריקות יחידה. אם כן, נובע מכך ש-{% equation %}\mathbb{Z}\left[\sqrt{-5}\right]{% endequation %} שהובא בפעם הקודמת כדוגמה לחוג שלמים בלי פריקות יחידה הוא גם בפרט לא תחום ראשי - יש בו אידאלים שאי אפשר לתאר בתור "כל החוג כפול איבר בודד". דוגמה לאידאל שכזה הוא הקבוצה {% equation %}\left\{ 3\cdot x+\left(1+\sqrt{-5}\right)y|x,y\in\mathbb{Z}\left[\sqrt{-5}\right]\right\} {% endequation %} - האידאל שנוצר על ידי שני האיברים {% equation %}3,1+\sqrt{-5}{% endequation %} (אבל לא ממש הגדרתי מה זה אומר אידאל שנוצר על ידי שני איברים...). כאן צץ הכוח של הרעיון של דדקינד במלוא עוזו - אי אפשר לחשוב על האידאל הזה בתור "כל המספרים שמתחלקים על ידי {% equation %}\mathfrak{a}{% endequation %}" עבור אף {% equation %}\mathfrak{a}{% endequation %} שנמצא ב-{% equation %}\mathbb{Z}\left[\sqrt{-5}\right]{% endequation %}; אבל אפשר <strong>להגדיר</strong> את {% equation %}\mathfrak{a}{% endequation %} בתור "המספר האידאלי שמחלק בדיוק את קבוצת המספרים הזו".

עם זאת, בינתיים לא ממש ברור מה הרווחנו - הגדרנו אידאלים, אבל לא ברור לנו לא מתי נכון לומר שאידאל מחלק מישהו, ולא מה הפעולות החשבוניות שאפשר לעשות על אידאלים. לצורך כך שוב כדאי מאוד לחזור לדוגמה של {% equation %}\mathbb{Z}{% endequation %} שבו יש זהות מוחלטת בין מספרים ובין אידאלים, ולראות איך הכל מתנהג שם.

בתור התחלה, אם {% equation %}a\in\left(n\right){% endequation %} אז זה אומר ש-{% equation %}n|a{% endequation %}, את זה כבר הבנו מזמן. אז אפשר לרמות קצת בסימון ולכתוב משהו בסגנון {% equation %}\left(n\right)|a{% endequation %} - האידאל {% equation %}\left(n\right){% endequation %} מחלק את המספר {% equation %}a{% endequation %} אם {% equation %}a\in\left(n\right){% endequation %}. בנוסף, {% equation %}a{% endequation %} בעצמו יוצר אידאל - {% equation %}\left(a\right){% endequation %}. מה היחס בין {% equation %}\left(a\right){% endequation %} ו-{% equation %}\left(n\right){% endequation %}? ובכן, אם {% equation %}n{% endequation %} מחלק את {% equation %}a{% endequation %}, אז הוא מחלק גם את כל מי שמתחלק ב-{% equation %}a{% endequation %}, כלומר את כל מי שב-{% equation %}\left(a\right){% endequation %}, כלומר {% equation %}\left(a\right)\subseteq\left(n\right){% endequation %}. לכן אפשר להגדיר סימון של חלוקה בין אידאלים: {% equation %}\left(n\right)|\left(a\right){% endequation %} פירושו ש-{% equation %}\left(a\right)\subseteq\left(n\right){% endequation %}. זה עשוי להיות טיפה מבלבל במבט ראשון - ככל שאידאל הוא <strong>גדול יותר</strong> כך הוא מחלק <strong>יותר</strong> מספרים, בניגוד לתפיסה האינטואיטיבית שלנו שכדי לחלק הרבה מספרים אתה צריך להיות קטן יחסית (לב העניין נעוץ בכך שככל שהיוצר של האידאל קטן יותר, האידאל עצמו גדול יותר). מכיוון שיחס ההכלה קיים באופן כללי לכל שתי קבוצות, קיבלנו הגדרה כללית של "חלוקה" עבור אידאלים.

השלב הבא הוא לדבר על כפל. האופן הטבעי להגדרת האידאל {% equation %}\left(a\right)\times\left(b\right){% endequation %} הוא פשוט בתור האידאל {% equation %}\left(ab\right){% endequation %}. זו אחלה הגדרה כשכל אידאל הוא ראשי, אבל מה יקרה באופן כללי יותר? ובכן, אם {% equation %}\mathfrak{a},\mathfrak{b}{% endequation %} הם שני מחלקים אידאליים, מה אנחנו יכולים להגיד על קבוצת המספרים שמתחלקת על ידי מכפלתם, {% equation %}\mathfrak{a}\mathfrak{b}{% endequation %}? די בבירור היא מכילה את כל המכפלות האפשריות של מספר שמתחלק ב-{% equation %}\mathfrak{a}{% endequation %} עם מספר שמתחלק ב-{% equation %}\mathfrak{b}{% endequation %}, כלומר אפשר להגדיר {% equation %}AB=\left\{ ab|a\in A,b\in B\right\} {% endequation %}. לרוע המזל, זה לא מספיק; לא קשה לראות שהקבוצה הזו אינה אידאל כי היא לא בהכרח סגורה לחיבור. לכן {% equation %}AB{% endequation %} צריכה להכיל גם סכומים (סופיים) של מכפלות, וזה מוביל אותנו להגדרה הבאה: אם {% equation %}A,B{% endequation %} הם אידאלים אז מכפלתם מוגדרת להיות {% equation %}AB=\left\{ \sum_{i=1}^{n}a_{i}b_{i}|a_{i}\in A,b_{i}\in B\right\} {% endequation %} (במקרה של אידאלים ראשיים אכן מתקיים {% equation %}\left(a\right)\cdot\left(b\right)=\left(ab\right){% endequation %} על פי הגדרה זו). אם יש לנו כפל, כבר אפשר לדבר על פירוק לגורמים.

לפני שנעבור לדבר על זה, קרוב לודאי שחלקכם תוהים כרגע למה לא להגדיר חיבור אידאלים באופן הכי טבעי שאפשר - {% equation %}A+B=\left\{ a+b|a\in A,b\in B\right\} {% endequation %} (קל לבדוק שזה אכן אידאל). התשובה היא שאפשר להגדיר זאת כך ואף עושים זאת וזו הגדרה נהדרת ושימושית מאוד - אבל <strong>היא לא מתאימה למה שאנחנו מבינים בתור חיבור מספרים</strong>. בואו ניקח למשל את {% equation %}\left(2\right),\left(3\right){% endequation %}. מה סכומם? נניח ש-{% equation %}n{% endequation %} הוא מספר טבעי כלשהו; שימו לב לכך ש-{% equation %}n=2\cdot n-3\cdot n=2\cdot n+3\cdot\left(-n\right){% endequation %}, כלומר {% equation %}n\in\left(2\right)+\left(3\right){% endequation %}, כלומר האידאל {% equation %}\left(2\right)+\left(3\right){% endequation %} כולל את <strong>כל</strong> השלמים - {% equation %}\left(2\right)+\left(3\right)=\mathbb{Z}=\left(1\right){% endequation %}. מי שציפה לקבל {% equation %}\left(2\right)+\left(3\right)=\left(5\right){% endequation %} ודאי מאוכזב כעת כהוגן.

באופן כללי {% equation %}A+B{% endequation %} הוא האידאל הקטן ביותר שמכיל גם את {% equation %}A{% endequation %} וגם את {% equation %}B{% endequation %} (הוא מכיל את {% equation %}A{% endequation %} כי כל סכום מהצורה {% equation %}a+0=a{% endequation %} שייך אליו; הרי {% equation %}0{% endequation %} הוא תמיד איבר של {% equation %}B{% endequation %}; באופן דומה הוא גם מכיל את {% equation %}B{% endequation %}). אפשר להגדיר אותו גם בתור "חיתוך כל האידאלים שמכילים גם את {% equation %}A{% endequation %} וגם את {% equation %}B{% endequation %}". זה תרגיל נחמד להראות שכל ההגדרות הללו שקולות, אבל ההגדרה שהכי מועילה לנו להבין מה קורה פה היא זו עם "האידאל הקטן ביותר שמכיל גם את {% equation %}A{% endequation %} וגם את {% equation %}B{% endequation %}". אמרנו ש"הכלה" היא פשוט שם אחר ל"מחלק את". אז אם נעבור לרגע לדיבור בלשון מספרים אידאליים, מה שאמרנו הוא שהמספר האידאלי {% equation %}A+B{% endequation %} הוא המספר<strong> הגדול ביותר</strong> שמחלק גם את {% equation %}A{% endequation %} וגם את {% equation %}B{% endequation %} (זוכרים? אידאל קטן יותר פירושו מספר "גדול יותר" ביחס לחלוקה). אפשר גם להגדיר זאת כך: {% equation %}A+B{% endequation %} הוא מספר אידאלי בעל התכונה שהוא מחלק את {% equation %}A{% endequation %} ואת {% equation %}B{% endequation %}, וכל מספר אידאלי אחר שמחלק את שניהם, מחלק אותו. מי שבקיא קצת באלגברה ודאי כבר הבין על מה אני מדבר פה - {% equation %}A+B{% endequation %} הוא מה שנקרא <strong>המחלק המשותף המקסימלי</strong> (GCD) של {% equation %}A,B{% endequation %}.

אם כן, מה שראינו הוא ש-{% equation %}\left(a\right)+\left(b\right)=\left(\gcd\left(a,b\right)\right){% endequation %}. זה אומר שלחיבור אידאלים יש משמעות מאוד טבעית ויפה ושימושית, אבל היא איננה מתאימה למשמעות הרגילה של חיבור מספרים. כדי להבין עד כמה כל העניין הזה נפיץ שימו לב לכך שאם יש לנו פעולה כלשהי על אידאלים, נקרא לה {% equation %}\oplus{% endequation %}, כך ש-{% equation %}\left(a\right)\oplus\left(b\right)=\left(a+b\right){% endequation %} יתרחש האסון הבא: {% equation %}\left(2\right)=\left(-2\right){% endequation %} (למה?) ולכן {% equation %}\left(2\right)\oplus\left(2\right)=\left(4\right){% endequation %} מצד אחד, ומצד שני {% equation %}\left(2\right)\oplus2=\left(2\right)\oplus\left(-2\right)=\left(0\right){% endequation %}. קיבלנו ש-{% equation %}\left(0\right)=\left(4\right){% endequation %} אבל זה בוודאי לא נכון. בקיצור, אי אפשר להגדיר את {% equation %}\oplus{% endequation %} אפילו על פי ההגדרה ה"טבעית" של {% equation %}\left(a\right)\oplus\left(b\right)=\left(a+b\right){% endequation %}. אם כן, מאוד לא סביר שנצליח למצוא דרך כלשהי להגדיר חיבור אידאלים בצורה שתתאים לחיבור מספרים - זו אחת מהבעיות עם הרעיון של "מספרים אידאליים" שדיברתי עליהן בהתחלה.

ומה בנוגע לעוד פעולה טבעית שאפשר לעשות על אידאלים - חיתוך? ובכן, חיתוך של שתי קבוצות היא הקבוצה הגדולה ביותר שמוכלת בשתיהן; ובתרגום ללשון אידאלים, זה המספר האידאלי הקטן ביותר שמתחלק בשני האידאלים שחתכנו. גם זה מושג מוכר מתורת המספרים - כפולה משותפת מינימלית, LCM. לסיום אפשר לדבר על הפעולה של איחוד אידאלים, אבל איחוד אידאלים הוא לא בהכרח אידאל בעצמו; והאידאל הקטן ביותר שמכיל את האיחוד הוא המכפלה שעליה כבר דיברנו.

עשינו כברת דרך רעיונית - מדיבור על מספרים עברנו לדיבור על אידאלים, והגדרנו על האידאלים פעולות שונות ומשונות. השלב הבא הוא להעביר את הרעיון של מספרים ראשוניים ומספרים אי פריקים לאידאליים. כזכור, {% equation %}p{% endequation %} הוא ראשוני אם מכך ש-{% equation %}p|ab{% endequation %} נובע ש-{% equation %}p|a{% endequation %} או {% equation %}p|b{% endequation %}. באותו האופן בדיוק אפשר להגדיר ש-{% equation %}\mathfrak{p}{% endequation %} הוא אידאל ראשוני אם מכך ש-{% equation %}\mathfrak{p}|ab{% endequation %} נובע ש-{% equation %}\mathfrak{p}|a{% endequation %} או {% equation %}\mathfrak{p}|b{% endequation %}. אם ניזכר במשמעות של "מספר מתחלק באידאל", אנחנו בעצם אומרים ש-{% equation %}\mathfrak{p}{% endequation %} הוא ראשוני אם מכך ש-{% equation %}ab\in\mathfrak{p}{% endequation %} נובע ש-{% equation %}a\in\mathfrak{p}{% endequation %} או {% equation %}b\in\mathfrak{p}{% endequation %} - אם מכפלה כלשהי נמצאת באידאל, אחד מגורמיה נמצא באידאל.

ההגדרה השניה שלנו הייתה של מספר אי פריק: {% equation %}p{% endequation %} הוא אי פריק אם מכך ש-{% equation %}p=ab{% endequation %} נובע ש-{% equation %}a{% endequation %} הפיך או {% equation %}b{% endequation %} הפיך. בניסוח שקול - אם {% equation %}a|p{% endequation %} אז {% equation %}a{% endequation %} הפיך או {% equation %}a=p{% endequation %}. כשעוברים לאידאלים, אם {% equation %}a{% endequation %} הפיך אז {% equation %}\left(a\right){% endequation %} הוא החוג כולו: מכיוון ש-{% equation %}a{% endequation %} הפיך אז {% equation %}1=aa^{-1}\in\left(a\right){% endequation %}, ולכן לכל {% equation %}b{% endequation %} גם {% equation %}1\cdot b\in\left(a\right){% endequation %} (השתמשתי כאן פעמיים בתכונת הבליעה). לכן אפשר להגדיר אידאל "אי פריק" כך: {% equation %}\mathfrak{p}{% endequation %} הוא אי פריק אם לכל {% equation %}a{% endequation %} כך ש-{% equation %}a|\mathfrak{p}{% endequation %} מתקיים ש-{% equation %}\left(a\right)=\mathfrak{p}{% endequation %} או {% equation %}\left(a\right)=\left(1\right){% endequation %}. לתופעה הזו קוראים בדרך כלל <strong>אידאל מקסימלי</strong> ואפשר לנסח אותה כך בחוג כללי {% equation %}R{% endequation %}: {% equation %}I\ne R{% endequation %} הוא מקסימלי ב-{% equation %}R{% endequation %} אם לכל אידאל {% equation %}J{% endequation %} המקיים {% equation %}I\subseteq J\subseteq R{% endequation %} מתקיים ש-{% equation %}J=I{% endequation %} או {% equation %}J=R{% endequation %}.

באופן כללי לא קשה להראות שאידאל מקסימלי הוא גם ראשוני אבל ההפך לא תמיד נכון בחוגים כלליים. גורם עיקרי לכך שהשימוש באידאלים בחוגי שלמים הוא כל כך מוצלח הוא העובדה שאם {% equation %}K{% endequation %} הוא שדה מספרים עם חוג שלמים {% equation %}\mathcal{O}_{K}{% endequation %}, אז כל אידאל ראשוני ב-{% equation %}\mathcal{O}_{K}{% endequation %} (שאיננו אידאל האפס) הוא גם מקסימלי. התכונה הזו היא שליש ממה שנדרש כדי להבטיח שב-{% equation %}\mathcal{O}_{K}{% endequation %} תתקיים פריקות יחידה לאידאלים; על שני השליש הנותרים אדבר בפוסט הבא.