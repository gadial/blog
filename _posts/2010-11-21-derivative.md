---
id: 856
title: "אז מה זו נגזרת?"
date: 2010-11-21 17:20:42
layout: post
categories: 
  - אנליזה מתמטית
tags: 
  - חשבון אינפיניטסימלי
  - מתמטיקה תיכונית
  - נגזרת
---
בעיית ה"מכונית שנוסעת מתל אביב לחיפה" נשחקה עד לזרא בבתי הספר, ולכן אני מקווה שתסלחו לי על כך שאני משתמש בה - רכב מנצח לא מחלפים. אם כן, המרחק מתל אביב לחיפה הוא 100 קילומטרים. מכונית יוצאת מתל אביב לחיפה ומגיעה לשם תוך שעתיים. מה הייתה מהירותה בדרך?

ובכן, אין לשאלה הזו שום תשובה חד משמעית. מהירות היא לא דבר קבוע - היא משתנה כל הזמן. אפשר להניח שבאיזור תל אביב המכונית נקלעה לפקקים שבהם לתקופות ארוכות היא לא זזה כלל, ובתקופות אחרות זזה לאט מאוד. אחר כך, כשהגיעה סוף סוף לכביש המהיר היא ככל הנראה נסעה במהירות גבוהה, עד שנתקלה בתאונת דרכים באמצע הדרך ועצרה לסייע. אולי היא אפילו הסיעה אנשים לבית החולים הקרוב ולשם כך חזרה על עקבותיה ונסעה במהירות "שלילית". כל מה שאנחנו יכולים להגיד הוא שהיא עברה מרחק כולל של 100 קילומטרים בשעתיים, ולכן מהירותה <strong>הממוצעת</strong> הייתה 50 קילומטרים בשעה.

מה בא הממוצע לתאר כאן? ובכן, נניח שהרכב היה נוסע במהירות <strong>קבועה</strong>. המהירות הממוצעת היא בדיוק המהירות בה הרכב היה צריך לנסוע באופן קבוע למשך כל הנסיעה כדי שיגיע בדיוק באותו הזמן שבו הגיע הרכב שלנו. היא בעצם מתארת את דרך הנסיעה ה"משעממת" ביותר, או ה"פשוטה" ביותר, תלוי איך אתם רוצים להסתכל על זה.

מושג הנגזרת - אחד משני המושגים המרכזיים בחשבון הדיפרנציאלי והאינטגרלי (יחד עם מושג האינטגרל) הוא בסך הכל הכללה לא מסובכת של הרעיון הזה - במקום לדבר על המהירות הממוצעת <strong>לאורך זמן</strong>, הוא מדבר על המהירות הממוצעת <strong>ברגע זמן נתון</strong>. לכאורה אין שום משמעות למה שאמרתי כרגע - ממוצע צריך להימדד <strong>לאורך זמן</strong>. הוא תמיד נמדד ביחס לשני פרקי זמן שונים - התחלה וסוף. איך אפשר לדבר עליו בנקודה מסויימת? מבחינה מתמטית, אם בזמן {% equation %}t_{1}{% endequation %} אני במיקום {% equation %}x_{1}{% endequation %} ובזמן {% equation %}t_{2}{% endequation %} אני במיקום {% equation %}x_{2}{% endequation %}, אז המהירות הממוצעת שלי היא {% equation %}\frac{x_{2}-x_{1}}{t_{2}-t_{1}}{% endequation %}; אבל אם {% equation %}t_{1}=t_{2}{% endequation %}, כלומר אני באותו זמן בשני המקרים, ועל כן גם {% equation %}x_{2}=x_{1}{% endequation %} (כי לא "הספקתי לזוז") הרי ש-{% equation %}\frac{x_{2}-x_{1}}{t_{2}-t_{1}}=\frac{0}{0}{% endequation %} ואפס חלקי אפס הוא מה שאוהבים לקרוא לו בח"מ - ביטוי חסר משמעות. זו אכן הבעיה; ולכן מושג הנגזרת הוא כל כך קסום - הוא מצליח לתת משמעות, ועוד משמעות הגיונית, טבעית ומתבקשת, לאותו בח"מ.

הרעיון הוא כזה: אמנם, אם נסתכל רק בתמונה קפואה אחת של הרכב בנקודת זמן מסויימת לא נוכל להגיד כלום על המהירות שלה; אבל אם ייתנו לנו סרטון קצר של הרכב בתנועה שמתחיל באותה נקודת זמן נוכל להסיק ממנו מה הייתה מהירות הרכב <strong>בערך</strong> באותה נקודת זמן. איך? פשוט נחשב באמצעות הסרטון מה היה המרחק שעבר הרכב במהלך הסרטון, וכמה זמן חלף (זהו אורכו של הסרטון), ובעזרת נתונים אלו נחשב את המהירות הממוצעת של הרכב במהלך הסרטון. אם אנו מניחים שהרכב לא ביצע שינוי דרסטי במהירות שלו בזמן הסרטון (מה שלא סביר אם הסרטון קצר), הרי שהמהירות הממוצעת של הרכב שנמדדה בסרטון קרובה למדי למהירות האמיתית של הרכב.

כאן אנחנו עדיין מדברים על קירוב; הרעיון העמוק של החשבון האינפיניטסימלי הוא שאפשר לעבור מדיבורים על קירובים לדיבורים על דברים מדוייקים לגמרי על ידי כך ש<strong>מקטינים את רזולוציית המדידה לאינסוף</strong>. זה רעיון שיחזור על עצמו שוב גם כאשר נעסוק באינטגרלים. כאן מה שאנו אומרים הוא - לא צריך את כל הסרט; בואו נקצוץ את הזמן שלו בחצי, ונבצע את החישוב של המהירות הממוצעת בזמן זה. אנחנו נקבל קירוב שהוא מדויק <strong>יותר</strong> מהקירוב הקודם, כי השלכנו את החצי השני של הסרט שהיה לא רלוונטי בכלל לשאלה מה הייתה המהירות של הרכב <strong>בתחילת</strong> הסרט.

אבל למה לעבוד עם חצי סרט? אפשר לעבוד עם הרבע הראשון; והשמינית הראשונה; והמאית הראשונה, וכן הלאה וכן הלאה. בכל פעם שאנו קוצצים חלק מיותר נוסף מהסרט אנחנו מקבלים קירוב טוב יותר למהירות ה"רגעית" של הרכב בתחילת הסרט. בשום שלב של הקיצוצים הללו אנחנו לא נפטרים <strong>מכל</strong> הסרט פרט לפריים הראשון; אבל באופן שנראה לא אינטואיטיבי, ככל שאנחנו זורקים יותר מידע לפח, כך הקירוב שלנו משתפר (זה לא כל כך מפתיע בהתחשב בכך שכל המידע שנזרק לפח הוא מיותר).

בעולם האמיתי שיטת העבודה הזו בלתי אפשרית כי יש גבול לכמה שניתן לקצץ את הסרט; בסופו של דבר יוותרו בידינו רק שני פריימים של הסרט - הראשון, וזה שבא מייד אחריו. אבל כאשר אנו עוסקים בפונקציות מתמטיות מהממשיים לממשיים, אפשר לבצע את שיפור הקירוב הזה עוד ועוד, "עד לאינסוף"; הדרך הפורמלית להגדיר זאת היא באמצעות מושג הגבול שהצגתי בעבר.

פורמלית, נניח שיש לנו פונקציה {% equation %}f\left(x\right){% endequation %}, ונקודה {% equation %}x_{0}{% endequation %}. חשבו על {% equation %}f{% endequation %} כמייצגת פונקציה של מיקום הרכב כתלות בזמן הנוכחי {% equation %}x{% endequation %}. אנו רוצים לדעת מה הייתה "המהירות הרגעית" של הרכב בזמן {% equation %}x_{0}{% endequation %}. הדרך לעשות זאת, כאמור, הייתה באמצעות מהירות ממוצעת. אם {% equation %}x\ne x_{0}{% endequation %} היא נקודה אחרת בזמן, אז המהירות הממוצעת בין הזמן שבו {% equation %}f{% endequation %} ב-{% equation %}x_{0}{% endequation %} והזמן שבו {% equation %}f{% endequation %} ב-{% equation %}x{% endequation %} היא {% equation %}\frac{f\left(x\right)-f\left(x_{0}\right)}{x-x_{0}}{% endequation %} (הנוסחה הזו עובדת גם כאשר {% equation %}x&gt;x_{0}{% endequation %} וגם כאשר {% equation %}x&lt;x_{0}{% endequation %}). ישנה דרך קצת יותר פשוטה לסמן את הדבר הזה - בואו נסמן את {% equation %}x-x_{0}{% endequation %} באות {% equation %}h{% endequation %}. אז {% equation %}x=x_{0}+h{% endequation %}, ולכן המהירות הממוצעת ניתנת לכתיבה בתור {% equation %}\frac{f\left(x_{0}+h\right)-f\left(x_{0}\right)}{h}{% endequation %}. ככל ש-{% equation %}h{% endequation %} יותר קרוב ל-0, כך הרזולוצייה של המדידה שלנו יותר מדויקת - יותר קשה להכניס פנימה סיפורי מעשיות כגון "נתקעתי עם הרכב באמצע הכביש וחזרתי אחורה לתחנת הדלק". ומכאן ההגדרה שלנו: {% equation %}f^{\prime}\left(x_{0}\right)=\lim_{h\to0}\frac{f\left(x_{0}+h\right)-f\left(x_{0}\right)}{h}{% endequation %}. במילים: הערך של הנגזרת של {% equation %}f{% endequation %} בנקודה {% equation %}x_{0}{% endequation %} הוא הגבול של המהירות הממוצעת של {% equation %}f{% endequation %} בנקודה {% equation %}x_{0}{% endequation %} ובנקודה קרובה {% equation %}x_{0}+h{% endequation %} כאשר משאיפים את המרחק בין שתי הנקודות לאפס.

מכיוון שלכל נקודה {% equation %}x{% endequation %} אפשר לדבר על "ערך הנגזרת של {% equation %}f{% endequation %} בנקודה {% equation %}x{% endequation %}", עולה שגם הנגזרת של {% equation %}f{% endequation %} היא בעצמה פונקציה, ומכאן הסימון - {% equation %}f^{\prime}{% endequation %} ("{% equation %}f{% endequation %} תג" בעברית). אותה {% equation %}f^{\prime}{% endequation %} נקראת "הפונקציה הנגזרת של {% equation %}f{% endequation %}" או פשוט <strong>הנגזרת</strong> שלה, ולפעמים קוראים ל-{% equation %}f^{\prime}\left(x_{0}\right){% endequation %} בשם "המספר הנגזר של {% equation %}f{% endequation %} בנקודה {% equation %}x_{0}{% endequation %}". כל אלו הם עניינים טרמינולוגיים לא חשובים עד כדי כך.

דבר אחד שמתמטיקאי צריך לעשות אחרי שהוא נתקל במושג חדש הוא לרחרח סביבו בחשדנות - האם המושג בכלל בעל משמעות? האם הוא מתקיים תמיד? למי הוא לא מתקיים? כשהוא כן מתקיים, עבור מי הוא מתקיים? ולכן אני רוצה לפתוח באכזבה - לא לכל פונקציה יש נגזרת, וגם אם יש - לא תמיד היא מוגדרת בכל מקום.הדוגמה הקלאסית ביותר היא פונקציית הערך המוחלט - {% equation %}f\left(x\right)=\left|x\right|{% endequation %}. עבור {% equation %}x&gt;0{% endequation %} הפונקציה מתנהגת בדיוק כמו {% equation %}f\left(x\right)=x{% endequation %}; ועבור {% equation %}x&lt;0{% endequation %} היא מתנהגת בדיוק כמו {% equation %}f\left(x\right)=-x{% endequation %}, ולשתי הפונקציות הללו יש נגזרת (נדבר על כך בעתיד. אולי). אבל בנקודה {% equation %}x=0{% endequation %} הכל מתרסק. בואו נראה את זה פורמלית: {% equation %}f\left(0\right)=0{% endequation %} במקרה הזה, ולכן עבור {% equation %}h&gt;0{% endequation %} נקבל {% equation %}\frac{f\left(x_{0}+h\right)-f\left(x_{0}\right)}{h}=\frac{f\left(h\right)-f\left(0\right)}{h}=\frac{h}{h}=1{% endequation %}, ואילו עבור {% equation %}h&lt;0{% endequation %} נקבל {% equation %}\frac{f\left(h\right)-f\left(0\right)}{h}=\frac{-h}{h}=-1{% endequation %}. במילים אחרות, אם נסתכל רק על תמונות מהצילומים של {% equation %}f\left(x\right){% endequation %} מהרגע ש<strong>לפני</strong> {% equation %}x=0{% endequation %}, נקבל את הרושם שהמהירות היא {% equation %}-1{% endequation %}; ואם נסתכל רק על הרגע שאחרי, נקבל את הרושם שהמהירות היא {% equation %}1{% endequation %}; אבל אז, מה המהירות באמצע? יש לנו שני קירובים שונים וסותרים. המסקנה היא שאי אפשר לדבר על המהירות ברגע הזה באופן משביע רצון, ואנחנו מסתפקים באמירה שהנגזרת של {% equation %}f{% endequation %} לא מוגדרת בנקודה הזו; ש-{% equation %}f{% endequation %} <strong>לא גזירה</strong> בנקודה הזו. באופן כללי אנחנו נוהגים לסווג את הפונקציות בעולם לגזירות ולא גזירות (ואם לא גזירות, היכן), ולמזלנו - רוב הפונקציות המעניינות גזירות.

בואו נעזוב את סיפור המכונית ונעבור לדוגמה אחרת לגמרי שבה יש משמעות לנגזרת - משיקים. במילה "משיק" במשמעותה המתמטית-גאומטרית נתקלים לרוב בבית הספר בהקשר של משיק למעגל בנקודה מסויימת. במקרה זה המשיק הוא קו ישר שנוגע במעגל באותה נקודה, ובנקודה זו בלבד (כלומר, הוא לא חותך את המעגל אלא רק "מלטף" אותו). אנחנו רוצים לדבר על משיק ליצורים גאומטריים אחרים - גרפים של פונקציות. אלא שכאן יש לנו בעיה - בהינתן גרף של פונקציה ונקודה כלשהי עליו ייתכן שיש הרבה ישרים שאפשר להעביר ולא חותכים את הגרף בשום נקודה אחרת; וגרוע מכך, ייתכן שהישר ש"מרגיש לנו נכון" בקשר להיותו משיק בנקודה מסויימת דווקא <strong>כן</strong> חותך את גרף הפונקציה בנקודות אחרות. אז מה עושים?
<div class="mceTemp"><dl id="attachment_857" class="wp-caption alignnone" style="width: 410px;"><dt class="wp-caption-dt"><a href="{{site.baseurl}}{{site.post_images}}/2010/11/400px-Tangent_to_a_curve.svg_.png"><img class="size-full wp-image-857" title="400px-Tangent_to_a_curve.svg" src="{{site.baseurl}}{{site.post_images}}/2010/11/400px-Tangent_to_a_curve.svg_.png" alt="תמונה של משיק לעקום" width="400" height="280" /></a></dt></dl></div>
מה שצריך לעשות הוא לזנוח את ההגדרה המקורית של משיק ולנסות להבין על מה אנחנו <strong>באמת</strong> מדברים כשאנו מדברים על משיק. משיק לנקודה מסויימת בעקום הוא קו ישר שהכיוון שלו זהה ל"כיוון של העקום" בנקודה זו. מי שמכיר טיפה מכניקה יכול לחשוב על זה כך: העקום מתאר תנועה של גוף בהשפעת כוח מטורלל כלשהו. המשיק בנקודה כלשהי מתאר את מסלול התנועה של הגוף מנקודה זו והלאה אם הכוח המטורלל היה עוזב אותו לנפשו שם והוא היה ממשיך בתנועתו ללא הפרעה, על פי החוק הראשון של ניוטון. ההגדרה הזו תופסת היטב את המשיק ה"קלאסי" למעגל, אבל היא טובה בהרבה מההגדרה האחרת - ובפרט, ניתן לתאר אותה באמצעות הנגזרת.

אם כן, נניח שיש לנו עקום שמתואר בתור הגרף של הפונקציה {% equation %}f\left(x\right){% endequation %} (כלומר, זה אוסף הנקודות במישור מהצורה {% equation %}\left(x,f\left(x\right)\right){% endequation %}). אמנם, אנחנו לא יכולים לתאר כך את כל העקומים (בפרט לא מעגל...) אבל לעת עתה זה מספיק לנו; אפשר בשיטות קצת יותר כלליות לטפל בכל סוגי העקומים. מה שאנחנו רוצים לדעת היא מה המשוואה של המשיק לגרף הפונקציה בנקודה {% equation %}x_{0}{% endequation %}. המשיק הוא קו ישר; אלו מכם שמכירים גאומטריה אנליטית יודעים שקו ישר ניתן לתאר באמצעות המשוואה {% equation %}y=mx+n{% endequation %}, כאשר המספר {% equation %}m{% endequation %} מכונה <strong>השיפוע</strong> של הישר, ובא לציין כמה הישר נוטה באלכסון ביחס לציר ה-{% equation %}x{% endequation %} (פורמלית, אם הזווית שהישר יוצר עם ציר ה-{% equation %}x{% endequation %} היא {% equation %}\theta{% endequation %}, אז {% equation %}m=\tan\theta{% endequation %}). עוד אתם אולי יודעים שאם נתון לנו השיפוע של ישר, ונקודה אחת שדרכה הישר עובר, הישר נקבע כך באופן יחיד. נקודה אחת שבה המשיק עובר אנחנו יודעים - זוהי בדיוק הנקודה {% equation %}\left(x_{0},f\left(x_{0}\right)\right){% endequation %}. כל מה שעלינו לגלות כעת הוא את השיפוע שלו.

אם אנחנו יודעים <strong>שתי</strong> נקודות שדרכן עובר ישר, ניתן לגלות את השיפוע שלו בקלות. נניח שאלו הן הנקודות {% equation %}\left(x_{1},y_{1}\right){% endequation %} ו-{% equation %}\left(x_{2},y_{2}\right){% endequation %}. אז נקבל את שני השוויונות {% equation %}y_{1}=mx_{1}+n{% endequation %} ו-{% equation %}y_{2}=mx_{2}+n{% endequation %}. נחסר את שני השוויונות זה מזה ונקבל {% equation %}y_{2}-y_{1}=m\left(x_{2}-x_{1}\right){% endequation %}, ובמילים אחרות, {% equation %}m=\frac{y_{2}-y_{2}}{x_{2}-x_{1}}{% endequation %}. נראה מוכר?

אם כן, כדי לחשב את השיפוע בנקודה {% equation %}x_{0}{% endequation %}, מה שנעשה הוא פשוט: עבור ערכים הולכים וקטנים של {% equation %}h{% endequation %} נעביר ישר בין הנקודה {% equation %}\left(x_{0},f\left(x_{0}\right)\right){% endequation %} והנקודה {% equation %}\left(x_{0}+h,f\left(x_{0}+h\right)\right){% endequation %} ונחשב את השיפוע שלו. נקבל קבוצה של "קירובים טובים לישר", שהולכת ונראית כמו הישר ככל ש-{% equation %}h{% endequation %} קטן יותר; ונקבל קבוצה של "קירובים טובים לשיפוע" שהולכת ונראית כמו שיפוע הישר ככל ש-{% equation %}h{% endequation %} קטן יותר. פורמלית, נקבל ש-{% equation %}m=\lim_{h\to0}\frac{f\left(x_{0}+h\right)-f\left(x_{0}\right)}{h}{% endequation %} - וזוהי <strong>בדיוק</strong> ההגדרה שלנו לנגזרת. במילים אחרות, הנגזרת של {% equation %}f{% endequation %} בנקודה {% equation %}x_{0}{% endequation %} היא שיפוע הישר שמשיק לגרף של {% equation %}f{% endequation %} בנקודה זו. זוהי הדרך לתת משמעות גאומטרית לנגזרת. יותר מכך - על הקו המשיק הזה אפשר לחשוב בתור "קירוב מסדר ראשון" של הפונקציה בנקודה {% equation %}x_{0}{% endequation %} - פונקציה פשוטה (קו ישר) שמהווה "קירוב טוב ל-{% equation %}f{% endequation %}" בסביבה קטנה של הנקודה {% equation %}x_{0}{% endequation %}.

מבחינה היסטורית, אלו שתי הבעיות שהולידו את מושג הנגזרת - הנסיון לתאר שינוי רגעי, והנסיון למצוא את המשיק לעקומים. מיותר אך הכרחי לציין שמאז הנגזרת התגלתה כשימושית באינספור הקשרים אחרים - זהו ללא ספק אחד מהמושגים הנפוצים ביותר במתמטיקה, וכל אדם בעל השכלה מתמטית מינימלית צריך להכיר אותו. הפוסט הזה הוא רק השלב הראשון.