---
id: 1342
title: "אז איך פותרים משוואות לינאריות?"
date: 2011-10-04 07:23:47
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - אלגברה לינארית
  - משוואה לינארית
  - ראו את זה בבית ספר
social_media_share: true
---
לטעמי נקודת הפתיחה הטובה ביותר לדיון על אלגברה לינארית היא לתאר מערכות של משוואות לינאריות ואיך פותרים אותן. ראשית, כי זו בעיה קונקרטית ובסיסית במתמטיקה; שנית, כי יש לה פתרון מושלם; שלישית, כי מבחינה טכנית הרבה מאוד מהבעיות שצצות בהקשר הרחב יותר של אלגברה לינארית (מרחבים וקטוריים) מצטמצמות לבסוף לפתרון של מערכת משוואות לינארית, ולכן זה גם הבסיס הטכני שצריך בשביל המשך הדרך (כדי <strong>לחסוך לנו עבודה</strong> בהמשך הדרך; שנוכל לומר "אה, ומכאן זה סתם לפתור משוואות לינאריות ואת זה אנחנו יודעים שאפשר לעשות), ורביעית - כי כבר בעיסוק בבעיה הקונקרטית הזו צצים ועולים אל פני השטח הרעיונות והמושגים הכלליים יותר של האלגברה הלינארית. ולבסוף, כי משוואות לינאריות הן דרך נפלאה להציג <strong>מטריצות</strong> - מהאובייקטים הבסיסיים והחשובים ביותר במתמטיקה כולה.

אבל לפני כל המהומה הזו, בואו נתחיל בקטן. מהי משוואה לינארית? משוואה היא ביטוי מהצורה "כך וכך שווה לכך וכך". {% equation %}2+3=5{% endequation %} היא דוגמה למשוואה, וגם {% equation %}e^{i\pi}+1=0{% endequation %} היא דוגמה למשוואה, וגם {% equation %}\mbox{P=NP}{% endequation %} היא "משוואה". אבל אנחנו מתעניינים במה שנקרא "פתרון משוואות". במקרה הזה לא כל האיברים שמופיעים במשוואה ידועים לנו, ואנו רוצים לגלות מה הם. למשל, {% equation %}2+x=5{% endequation %} היא משוואה שבה הפתרון פירושו לגלות את הערך של {% equation %}x{% endequation %}. אז מהצצה חטופה ב-{% equation %}2+3=5{% endequation %} ברור לנו שכנראה {% equation %}x=3{% endequation %} (ליתר דיוק: ש-{% equation %}x=3{% endequation %} הוא פתרון של המשוואה אבל אולי יש אחרים - במקרה הספציפי הזה אין), אבל מה הדרך השיטתית לפתור משוואות?

התשובה הקצרה היא - <strong>אין דרך כללית</strong>. אבל, אם המשוואות הן פשוטות יחסית, כן יש דרכים כלליות. ה"פשטות" מתבטאת בכמה שאנחנו מתעללים ב-{% equation %}x{% endequation %}: ברור לנו שמשוואה כמו {% equation %}2^{x}+\frac{\log^{3}x}{x^{x+\sin x}}=\int_{0}^{x}e^{t^{2}}dt{% endequation %} היא כנראה מסובכת מהותית יותר מ-{% equation %}2+x=5{% endequation %}, שבה אין שום התעללות ב-{% equation %}x{% endequation %} והוא פשוט מופיע כמו שהוא. <strong>משוואות לינאריות</strong> הן משוואות שבהן זה בערך מה שקורה - אם משתנה מופיע, הוא מופיע כמות שהוא, כשלכל היותר כופלים אותו במספר (לעת עתה נניח שזה מספר ממשי) כלשהו. אני רוצה להדגיש כבר עכשיו שבמשוואה יכולים להופיע כמה משתנים: אז {% equation %}2+x=5{% endequation %} היא משוואה לינארית, וגם {% equation %}5x+7=22{% endequation %} היא משוואה לינארית, וגם {% equation %}x+y+z=3{% endequation %} היא משוואה לינארית, אבל {% equation %}x^{2}=1{% endequation %} איננה משוואה לינארית כי {% equation %}x{% endequation %} כבר מופיע בחזקה גבוהה מ-1; וגם {% equation %}\sqrt{x}=4{% endequation %} אינה משוואה לינארית, ובוודאי שלא משהו כמו {% equation %}e^{x}=\cos x{% endequation %}. אז אם המשוואות המוזרות הללו (שאין לי מושג איך לפתור או אם בכלל אפשר לפתור) מפחידות אתכם, זה לא חשוב - אנחנו הולכים לדבר רק על משוואות פשוטות.

משוואה לינארית תמיד אפשר לפשט חיש קל כדי להביא אותה לצורה מאוד פשוטה. למשל, אם {% equation %}2+x+3=8{% endequation %} היא משוואה, אפשר קודם כל לשים לב לכך שאפשר להחליף את הסדר בין {% equation %}x{% endequation %} ושאר המחוברים, כלומר לקבל {% equation %}x+2+3=8{% endequation %} (זה שימוש של <strong>כלל החילוף</strong> החיבורי; אני משתמש כאן במובלע גם ב<strong>כלל הקיבוץ</strong> שפירושו ש-{% equation %}\left(2+x\right)+3{% endequation %} ו-{% equation %}2+\left(x+3\right){% endequation %} הם אותו דבר ולכן בכלל לא צריך סוגריים). כעת, {% equation %}2+3=5{% endequation %} ולכן אפשר לכתוב {% equation %}x+5=8{% endequation %}. הדרך לפשט הלאה משוואה שכזו היא לשים לב לכך שהשוויון נשמר גם אם מחסרים משני האגפים את אותו המספר: {% equation %}x+5-5=8-5{% endequation %}, ולכן {% equation %}x=3{% endequation %}. זו המחשה לעקרון הכללי: בכל משוואה, ניתן לחבר לשני האגפים את אותו מספר ולכפול את שני האגפים באותו מספר והשוויון עדיין יישמר.

לכן ברור שלא משנה איזו משוואה לינארית עם משתנה בודד {% equation %}x{% endequation %} תביאו לי, אני אוכל על ידי חיסור מתאים של מספר משני האגפים לקבל משוואה מהצורה {% equation %}ax=b{% endequation %}. אם {% equation %}a=0{% endequation %} אז זה אומר ש-{% equation %}x{% endequation %} לא הופיע במשוואה מלכתחילה ולכן זו לא משוואה שיש לנו מה לפתור בה בכלל; אחרת, אפשר לכפול את שני אגפי המשוואה ב-{% equation %}\frac{1}{a}{% endequation %} (שימו לב! אני מעדיף לא לומר "אפשר לחלק ב-{% equation %}a{% endequation %}"; לטעמי עדיף לחשוב על חילוק כעל "כפל בהופכי") ולקבל {% equation %}x=\frac{b}{a}{% endequation %}. זה הכל - ראינו כעת איך פותרים משוואה ממעלה ראשונה ולא משנה מה.

תיאוריה זה נחמד, אבל מה קורה בפועל? בואו נראה דוגמה שמצאתי אי שם - המשוואה {% equation %}1+\frac{1-2x}{3}-\frac{3x-1}{7}=6-2x{% endequation %}. ממבט ראשון היא נראית נורא מפחידה, אבל בעצם אין כאן כלום. יש שתי דרכים לתקוף משוואה כזו - אחת מסודרת ושיטתית והשניה מהירה יותר. בדרך המסודרת והשיטתית קודם כל נפריד את המשוואה למחוברים:

{% equation %}1+\frac{1}{3}-\frac{2}{3}x-\frac{3}{7}x+\frac{1}{7}=6-2x{% endequation %}

עכשיו נעביר אגפים:

{% equation %}2x-\frac{2}{3}x-\frac{3}{7}x=6-1-\frac{1}{3}-\frac{1}{7}{% endequation %}

ולסיום נוציא {% equation %}x{% endequation %} כגורם משותף באגף שמאל:

{% equation %}\left(2-\frac{2}{3}-\frac{3}{7}\right)x=6-1-\frac{1}{3}-\frac{1}{7}{% endequation %}

והנה אנחנו במשוואה מהצורה {% equation %}ax=b{% endequation %}, רק שצריך עוד להשתמש בכללי החשבון כדי להבין מהו בדיוק {% equation %}a{% endequation %} ומהו בדיוק {% equation %}b{% endequation %}. מקבלים ש-{% equation %}a=\frac{42-14-9}{21}=\frac{19}{21}{% endequation %} ו-{% equation %}b=\frac{126-21-7-3}{21}=\frac{103}{21}{% endequation %} ולכן {% equation %}x=\frac{\frac{103}{21}}{\frac{19}{21}}=\frac{95}{19}={% endequation %}

בדרך השניה פשוט עוברים בצעד אחד מהיר מהמשוואה {% equation %}1+\frac{1-2x}{3}-\frac{3x-1}{7}=6-2x{% endequation %} אל המשוואה

{% equation %}2x+\frac{7-14x-9x+3}{21}=5{% endequation %}

ומשם אל

{% equation %}2x+\frac{10-23x}{21}=5{% endequation %}

וכופלים ב-21 ומקבלים

{% equation %}42x-23x=105-10{% endequation %}

כלומר {% equation %}19x=95{% endequation %}

כלומר {% equation %}x=\frac{95}{19}{% endequation %}

זו דוגמה למשוואה מגעילה, מגעילה. זה תרגיל טכני מתיש וחסר טעם וזה לא משהו שאנחנו רוצים לעשות ביום יום. לגלות לכם סוד? כשפתרתי את המשוואה קיבלתי בשיטה הראשונה דווקא {% equation %}x=\frac{103}{19}{% endequation %}. איך? סתם טעות מפגרת אי שם במכנה המשותף של {% equation %}b{% endequation %}. מה לעשות - כשעושים עבודה של מחשב, קורות טעויות וצריך לבדוק את עצמך בשבע עיניים. זה <strong>לא</strong> מה שאנחנו רוצים להתעסק בו כאן. לכן מכאן ואילך אני אניח שאם יש לנו משוואה לינארית, היא כבר נתונה בצורה המפושטת שלה (במילים אחרות, המתמטיקה מתחילה כשהחישוב הטכני <strong>נגמר</strong>).

בואו נעבור עכשיו למשהו קצת יותר מסובך - משוואה עם שני נעלמים. למשל, {% equation %}x+y=0{% endequation %}. מה הפתרון למשוואה הזו? ובכן, {% equation %}x=0,y=0{% endequation %} הוא בוודאי פתרון. אבל גם {% equation %}x=1,y=-1{% endequation %} הוא פתרון, וגם {% equation %}x=17,y=-17{% endequation %} הוא פתרון; בעצם, לכל מספר שנציב ב-{% equation %}x{% endequation %}, אם נציב את אותו המספר עם סימן הפוך ב-{% equation %}y{% endequation %} נקבל פתרון; את זה אפשר לכתוב גם כ-{% equation %}y=-x{% endequation %} (זו עדיין משוואה, אבל כאן יותר מובהק האופן שבו ערכו של {% equation %}y{% endequation %} נקבע אחרי שקבענו את ערכו של {% equation %}x{% endequation %}). בקיצור, מה שאנחנו רואים כאן, וזה לא מובן מאליו כלל, הוא שלמשוואה לינארית עם שני משתנים יכולים להיות אינסוף פתרונות. למעשה, <strong>תמיד</strong> יש לה אינסוף פתרונות, כל עוד אני יכול להציב מספרים ממשיים כלשהם במשתנים והמשוואה לא "מנוונת", כלומר שני המשתנים באמת מופיעים בה עם מקדם שונה מאפס.

אינסוף פתרונות זה כבר מעניין. מצד אחד, זו קבוצה אינסופית; מצד שני, די בבירור היא לא כוללת את <strong>הכל</strong>: למשל, {% equation %}x=1,y=1{% endequation %} הוא לא פתרון של המשוואה {% equation %}x+y=0{% endequation %}. אם כן, לאוסף הפתרונות הזה יש אולי <strong>מבנה</strong> מעניין שמושרה עליו מעצם העובדה שכל האיברים בו מתוארים על ידי אותה משוואה. אחת ההבחנות המרתקות ביותר במתמטיקה לטעמי היא שיש לאוסף הפתרונות הזה מבנה <strong>גאומטרי</strong> (ובהכללה, שלאוספי פתרונות של משוואות, גם מסדרים גבוהים יותר, יש מבנה גאומטרי באופן כללי; זה הבסיס של הגאומטריה האלגברית שהיא תחום מתקדם מאוד במתמטיקה). עבור משוואות לינאריות בשני נעלמים המבנה הגאומטרי הוא מהפשוטים שניתן להעלות על הדעת - קו ישר; ועם זאת, כדאי לדבר עליו כמה שיותר מהר גם כי זה פשוט יפה, וגם כי זה יהיה מועיל לאינטואיציה בהמשך, למשל כשנדבר על מערכות של כמה משוואות לינאריות.

לא אוכיח כרגע שאוסף הפתרונות הוא אכן קו ישר, אבל בואו ננסה להבין קצת את האופן שבו המשוואה משפיעה על התכונות של הקו. משוואה לינארית כללית בשני משתנים היא מהצורה {% equation %}ax+by=c{% endequation %} כאשר {% equation %}a,b,c{% endequation %} הם מספרים ממשיים כלשהם, והקו הישר הוא אוסף הנקודות {% equation %}\left(x,y\right){% endequation %} שהן פתרון של המשוואה. אם {% equation %}b\ne0{% endequation %} לרוב נוהגים "לנרמל" את המשוואה על ידי חלוקה במקדם של {% equation %}y{% endequation %} והעברת אגפים ואז מקבלים את המשוואה {% equation %}y=mx+n{% endequation %}, שבה יש למספרים {% equation %}m,n{% endequation %} משמעות מובהקת למדי: {% equation %}m{% endequation %} הוא ה<strong>שיפוע</strong> של הישר (פורמלית, זהו טנגנס הזווית שהישר יוצר עם ציר ה-{% equation %}x{% endequation %}) ו-{% equation %}n{% endequation %} היא נקודת החיתוך של הישר עם ציר {% equation %}y{% endequation %}. אם במשוואה המקורית {% equation %}b=0{% endequation %}, כלומר המשוואה היא בעצם מהצורה {% equation %}ax=c{% endequation %}, אז עדיין קיבלנו תיאור של ישר: כל זוג {% equation %}\left(x,y\right){% endequation %} שבו {% equation %}x=\frac{c}{a}{% endequation %} ו-{% equation %}y{% endequation %} הוא בעל ערך כלשהו פותר את המשוואה, ולכן יש לנו כאן ישר אנכי (עם "שיפוע אינסופי" כפי שאוהבים לומר לפעמים). זו הסיבה שלכתוב {% equation %}ax+by=c{% endequation %} זה יותר נוח כשרוצים לעשות טיפול כללי במשוואה, כולל במקרים "מנוונים" שבהם המקדם של {% equation %}y{% endequation %} הוא 0 (זה הופך להיות חשוב יותר כשעוברים לדבר על מערכות של משוואות שבהן לא כל משתנה חייב להופיע בכל המשוואות).

עוד נקודה מעניינת היא ש-{% equation %}\left(0,0\right){% endequation %} ("ראשית הצירים") היא פתרון של המשוואה {% equation %}ax+by=c{% endequation %} אם ורק אם {% equation %}c=0{% endequation %} למשוואה מהצורה {% equation %}ax+by=0{% endequation %} - כזו שאין בה מספר שונה מאפס שמתרוצץ חופשי ואינו צמוד לאף משתנה - קוראים <strong>משוואה הומוגנית</strong>. המשוואות הללו יהיו חשובות לנו במיוחד בקרוב.

עכשיו, מצויידים באינטואיציה הגאומטרית הזו, בואו נעבור לנושא שגם הוא עדיין נלמד בבית הספר - מערכת של שתי משוואות בשני נעלמים. כאן נתונות שתי משוואות, והמטרה היא למצוא האם קיים פתרון שנכון עבור שתי המשוואות <strong>בו זמנית</strong>. דרך החשיבה הגרפית שלנו מקלה מאוד על ההבנה של "מה הולך כאן" - אמרתי כבר שכל משוואה מגדירה קו ישר כלשהו; אז מה שבעצם מבקשים מאיתנו הוא זה - בהינתן שני קווים ישרים, למצוא את נקודות החיתוך שלהם.

אם נלך עם האינטואיציה הגאומטרית, תכף ומייד מתברר שיש רק שלושה מקרים אפשריים: או שהקווים כלל לא נחתכים (הם <strong>מקבילים</strong>), או שהם בעצם אותו הקו, אולי בתיאור קצת שונה; או שיש בדיוק נקודת חיתוך אחת ויחידה (לא קשה להוכיח פורמלית ששני ישרים שאינם זהים נחתכים לכל היותר בנקודה אחת, כי די בשתי נקודות שדרכן עובר קו כדי לקבוע אותו בצורה יחידה).

דוגמה לשתי משוואות שמגדירות את אותו הקו בתחפושת היא זו:

{% equation %}x+y=1{% endequation %}

{% equation %}2x+2y=2{% endequation %}

המשוואה השניה היא בסך הכל הכפלה של המשוואה הראשונה ב-2, וברור שכל מה שפותר את אחת מהמשוואות יפתור גם את השניה (אם אינם מאמינים, הציבו ותראו מה קורה). למעשה, אם נעביר אגפים ונחלק במקדם של {% equation %}y{% endequation %} נקבל לבסוף עבור שתי המשוואות בדיוק את אותה משוואת ישר: {% equation %}y=-x+1{% endequation %}. כלומר, שתי המשוואות מגדירות ישר שהשיפוע שלו הוא {% equation %}-1{% endequation %} ונקודת החיתוך שלו עם ציר {% equation %}y{% endequation %} היא 1.

בואו נעבור לדבר על ישרים מקבילים. מה מאפיין ישרים שכאלו? העובדה שה<strong>שיפוע</strong> שלהם זהה, אך נקודת החיתוך שלהם עם ציר {% equation %}y{% endequation %} (או עם ציר {% equation %}x{% endequation %}, אם מדובר על ישרים בעלי שיפוע "אינסופי") אינה זהה. דוגמה היא במערכת המשוואות הבאה:

{% equation %}x+y=0{% endequation %}

{% equation %}x+y=1{% endequation %}

שתי המשוואות מגדירות ישר עם שיפוע {% equation %}-1{% endequation %}, אבל הראשון עובר דרך ראשית הצירים והשני לא. מבט חטוף במשוואה הזו מסייע לנו להבין בקלות שאין לה פתרון - איך ייתכן שהסכום של {% equation %}x,y{% endequation %} יהיה בו זמנית גם 0 וגם 1? אבל לפעמים המצב הוא יותר טריקי מכך.

לסיום, הנה מערכת שבה כל משוואה מגדירה ישר אחר:

{% equation %}2x+y=4{% endequation %}

{% equation %}x+2y=6{% endequation %}

ועכשיו נשאלת השאלה - איך פותרים את זה?

דרך אחת היא ממש לשרטט את הישרים שמתאימים לשתי המשוואות, למצוא את נקודת החיתוך שלהם, ולבדוק מה הקוארדינטות שלה. זו דרך פעולה לגיטימית, אבל קצת מסורבלת. לכן האופן שבו פותרים משוואות כאלו הוא לרוב <strong>אלגברי</strong> - מבצעים מניפולציה של סמלים, שמתבטאת בפעולות כמו "מעבירים אגף", "מציבים" וכו'. בואו נתחיל מהצבה, שהיא שיטה שפותרת גם משוואות כלליות יותר (למשל, משוואות ממעלה שניה) ולא ממש נשתמש בה בהמשך: הרעיון בהצבה הוא "לבודד" את אחד המשתנים, כפי שבודדנו את {% equation %}y{% endequation %} עד כה כשרצינו לקבל משוואות של ישרים, ואז להציב את הערך שמצאנו בתוך המשוואה השניה ולפתור אותה כשם שפותרים משוואה במשתנה יחיד. כך למשל, על ידי העברת אגפים מקבלים מהמשוואה הראשונה ש-{% equation %}y=4-2x{% endequation %}, ואחרי הצבה במשוואה השניה מקבלים {% equation %}x+2\left(4-2x\right)=6{% endequation %}, שהופך ל-{% equation %}x+8-4x=6{% endequation %}, שהופך ל-{% equation %}-3x=-2{% endequation %}, שהופך ל-{% equation %}x=\frac{2}{3}{% endequation %}. עכשיו אפשר להציב את {% equation %}x{% endequation %} חזרה בנוסחה {% equation %}y=4-2x{% endequation %} ולקבל {% equation %}y=4-\frac{4}{3}=\frac{8}{3}{% endequation %}. זו שיטה לגיטימית ויעילה מאוד.

השיטה השניה, שאציג עכשיו, היא הרבה יותר "מובנית". האבחנה שבבסיסה היא זו: אם יש לנו משוואה לינארית כלשהי (לא משנה עם כמה נעלמים), אז אוסף הפתרונות שלה נותר <strong>זהה </strong>גם אם כופלים את המשוואה במספר קבוע; ואם יש לנו שתי משוואות לינאריות כלשהן, אז כל פתרון עבור שתי המשוואות בו זמנית הוא גם פתרון עבור <strong>הסכום</strong> של שתי המשוואות. אני לא אומר זאת כרגע במפורש (טוב, בעצם כן) אבל שתי הפעולות הללו - כפל בקבוע, וחיבור שני איברים - הן הפעולות שמגדירות <strong>מרחב וקטורי</strong>, שהוא האובייקט המרכזי באלגברה לינארית.

בואו נראה איך האבחנה הזו עוזרת לנו. ניקח את המערכת שהצגתי לפני רגע, נכפול את המשוואה הראשונה בה ב-{% equation %}-\frac{1}{2}{% endequation %}, ונקבל את המערכת החדשה:

{% equation %}-x-\frac{1}{2}y=-2{% endequation %}

{% equation %}x+2y=6{% endequation %}

מובטח לי שהפתרונות של המערכת הזו זהים לפתרונות של המערכת הקודמת. כעת <strong>אחבר</strong> את שתי המשוואות הללו ואקבל משוואה חדשה:

{% equation %}\frac{3}{2}y=4{% endequation %}

שממנה נובע מייד ש-{% equation %}y=\frac{8}{3}{% endequation %} והנה כבר פתרתי.

כדי לעשות את החיים קלים יותר, לרוב משלבים את שני השלבים שתיארתי כרגע לשלב אחד: לוקחים את אחת מהמשוואות, ופשוט מחברים לה את המשוואה השניה כשאותה משוואה כבר מוכפלת בקבוע כלשהו. כך למשל אני יכול לפתור את המערכת של קודם על ידי כך שאכפול את המשוואה התחתונה דווקא במינוס 2 ואחבר אותה למשוואה העליונה. אקבל:

{% equation %}0x-3y=-8{% endequation %}

{% equation %}x+2y=6{% endequation %}

עכשיו אפשר לכפול את המשוואה הראשונה בקבוע מתאים ולקבל:

{% equation %}0x+y=\frac{8}{3}{% endequation %}

{% equation %}x+2y=6{% endequation %}

ועכשיו אפשר להוסיף למשוואה <strong>השניה</strong> את המשוואה הראשונה כשהיא מוכפלת במינוס 2, ולקבל:

{% equation %}0x+y=\frac{8}{3}{% endequation %}

{% equation %}x+0y=\frac{2}{3}{% endequation %}

מה שמעניין כאן (וניסיתי להדגיש עם ה-{% equation %}0x{% endequation %} וה-{% equation %}0y{% endequation %} שמופיעים שם) הוא שמבחינה רעיונית, עדיין יש לי כאן מערכת משוואות ולא "פתרון" - על ידי הפעולה החדשה שהמצאתי, של "להוסיף לשורה אחת כפולה של השורה השניה" אני מקבל סדרה של מערכות של משוואות, שכולן בעלות התכונה שיש להן בדיוק את אותו הפתרון. פשוט למרבה המזל, המערכת האחרונה היא ממש, ממש פשוטה ואפשר לקרוא את הפתרון ישר מתוכה.

דרך אחרת לתאר את מה שעשיתי כאן היא זו: הצגתי <strong>תהליך</strong> שמאפשר להמיר מערכת של משוואות במערכת <strong>שקולה</strong>, ובסוף התהליך תמיד מגיעים למערכת <strong>קנונית</strong> פשוטה שבה הפתרון מובן מאליו. השיטה הזו (בכפוף לתיאור קצת יותר פורמלי ומדויק שיבוא בפוסט הבא) נקראת <strong>אלימינציה גאוסית</strong> וקשה להמעיט בחשיבותה; העובדה שניתן לבצע אותה בפועל מאוד ביעילות היא הבסיס לקלות החישובית של בעיות רבות באלגברה לינארית. לסיום אני רק רוצה להעיר שטרם אמרתי זאת במפורש, אבל באופן שהצגתי לעיל אפשר לפתור מערכת של מספר כלשהו של משוואות לינאריות במספר כלשהו של משתנים; אבל הפירוט יחכה להמשך.
