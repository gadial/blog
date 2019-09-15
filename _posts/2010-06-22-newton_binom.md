---
id: 543
title: "הבינום של ניוטון"
date: 2010-06-22 20:47:22
layout: post
categories: 
  - קומבינטוריקה
tags: 
  - הבינום של ניוטון
  - מתמטיקה תיכונית
  - קומבינטוריקה
---
<a href="http://www.gadial.net/?p=534">הפוסט הקודם</a> שלי עסק במבוא לקומבינטוריקה, ברמה שבתקווה גם תלמידי תיכון יוכלו להבין. אני רוצה להמשיך כעת באותה הרוח ולהציג תוצאה קומבינטורית פשוטה אך יפה, שכבר בשלב זה ניתן להבין, באמצעות הכלים שהצגתי בפוסט הקודם - הבינום של ניוטון.

בשלב כלשהו בתיכון נלמדת הנוסחה הפשוטה הבאה: {% equation %}\left(a+b\right)^{2}=a^{2}+2ab+b^{2}{% endequation %}. למה? ככה. לפעמים גם נלמדת נוסחה יותר מסובכת: {% equation %}\left(a+b\right)^{3}=a^{3}+3a^{2}b+3ab^{2}+b^{3}{% endequation %}. כשהייתי בתיכון תיעבתי את הנוסחה הזו, עם החזקה השלישית - אף פעם לא זכרתי בדיוק איך היא הולכת ונאלצתי לבדוק בדף הנוסחאות. כעת, כשאני כותב את הפוסט, לא נזקקתי כלל לדף נוסחאות כלשהו - וזה לא שהזכרון שלי השתפר במיוחד או שאני משתמש בנוסחה הזו על בסיס יומיומי. אני מקווה שעד סיום הפוסט גם כל הקוראים יוכלו לכתוב את הנוסחה הזו "מהראש" וללא צורך בשום דף נוסחאות או אפילו חישובים ידניים.

הבינום של ניוטון הוא נוסחה כללית עבור ביטויים כאלו - ביטויים שנראים כמו {% equation %}\left(a+b\right)^{n}{% endequation %}, כאשר {% equation %}n{% endequation %} הוא מספר טבעי כלשהו. כמובן שעולה מאליה השאלה בשביל מה זה טוב; קשה לתת לה תשובה, פשוט כי הבינום אינו מטרה בפני עצמה אלא כלי שצץ לעתים קרובות כחלק מחישובים מסובכים יותר - זה אחד מהדברים שפשוט "טוב לדעת". רק אציין שלרוב השימושים הם דווקא לא טכניים-חישוביים, אלא כחלק מהוכחה תיאורטית כללית (למשל, מציאת הנגזרת של פונקציה מהצורה {% equation %}f\left(x\right)=x^{n}{% endequation %} כוללת שימוש בבינום). לא אציג את הנוסחה עדיין פשוט כי היא מפחידה במבט ראשון; קודם כל נבין מה הולך כאן ונגיע אליה באופן טבעי.

במתמטיקה באופן כללי הדרך הטובה להבין מקרה כללי היא לעתים קרובות דרך בחינת מקרים פרטיים פשוטים, אפילו פשוטים ברמה מגוחכת. {% equation %}\left(a+b\right)^{1}{% endequation %} הוא פשוט {% equation %}a+b{% endequation %}, וזה לא מלמד אותנו הרבה; אבל {% equation %}\left(a+b\right)^{2}{% endequation %} זה כבר סיפור שונה. איך באמת מגיעים לאותה נוסחה מפורסמת של {% equation %}a^{2}+2ab+b^{2}{% endequation %}?

לצורך כך בואו ונחזור רגע ליסודות. תשכחו מהבינום - איך מבצעים את פעולת הכפל הבאה - {% equation %}\left(a+b\right)\cdot c{% endequation %}? כאן בא לעזרתנו אחד מחוקי החשבון הבסיסיים ביותר - חוק הפילוג, שקובע פשוט ש-{% equation %}\left(a+b\right)c=ac+bc{% endequation %}.

השלב הבא הוא המכפלה {% equation %}\left(a+b\right)\left(c+d\right){% endequation %}. גם כאן אפשר להשתמש בחוק הפילוג בדיוק באותו האופן כמו קודם, ולקבל {% equation %}\left(a+b\right)\left(c+d\right)=a\left(c+d\right)+b\left(c+d\right){% endequation %}. כעת אפשר להשתמש בחוק הפילוג שוב (הפעם בגרסה שלו שאומרת ש-{% equation %}c\left(a+b\right)=ca+cb{% endequation %}) ולקבל {% equation %}a\left(c+d\right)+b\left(c+d\right)=ac+ad+bc+bd{% endequation %}. עד כאן חשבון פשוט - מה הקשר לקומבינטוריקה?

ובכן, אני רוצה שנחשוב על המכפלה {% equation %}\left(a+b\right)\left(c+d\right){% endequation %} באופן שונה - בתור תהליך של בחירה. בפתיחת הסוגריים, כל מחובר שנקבל בסכום הסופי מתקבל מבחירה של איבר אחד בסוגר השמאלי, בחירה של איבר אחד בסוגר הימני, והכפלתם. כך {% equation %}ac{% endequation %} מתקבל כשנבחר האיבר הראשון בכל זוג סוגריים, {% equation %}bd{% endequation %} מתקבל כשנבחר האיבר השני, וכן הלאה. שימו לב לסדר שבו כתבתי את האיברים: כתבתי {% equation %}ac{% endequation %} ולא {% equation %}ca{% endequation %} (למרות ששני ערכים אלו שווים אלו לאלו) כדי להבליט את העובדה ש-{% equation %}a{% endequation %} נבחר מהסוגריים השמאליים ואילו {% equation %}c{% endequation %} מהסוגריים הימניים.

עכשיו בואו נעבור לטפל ב-{% equation %}\left(a+b\right)^{2}{% endequation %}, שהוא מקרה פשוט יותר מהמקרה הכללי: {% equation %}\left(a+b\right)^{2}=\left(a+b\right)\left(a+b\right){% endequation %} ואחרי פתיחת הסוגריים נקבל את הסכום {% equation %}aa+ab+ba+bb{% endequation %}. כעת אפשר לשפר את מראה הסכום הזה: את {% equation %}aa{% endequation %} אפשר להחליף ב-{% equation %}a^{2}{% endequation %}, ובמקום להסתבך עם {% equation %}ab{% endequation %} ו-{% equation %}ba{% endequation %} אפשר להשתמש בחוק החילוף ולקבל {% equation %}ab+ba=ab+ab=2ab{% endequation %}. הנה כי כן הגענו ל-{% equation %}a^{2}+2ab+b^{2}{% endequation %}, אבל לדעתי יותר חשוב לזכור דווקא את התוצאה ה"גולמית": {% equation %}aa+ab+ba+bb{% endequation %}.

בואו נעבור לטפל במקרה קשה הרבה יותר: {% equation %}\left(a+b\right)^{3}=\left(a+b\right)\left(a+b\right)\left(a+b\right){% endequation %}. כאן אפשר לחשוב על תהליך פתיחת הסוגריים כעל תהליך של בחירת <strong>שלושה</strong> איברים והכפלתם - איבר אחד מכל סוגר. התוצאה הסופית תהיה סכום שבו כל מחובר מתקבל מבחירת איבר מכל אחד מזוגות הסוגריים. אם נכתוב במפורש את כל התוצאות (קצת טרחני, אני יודע) נקבל: {% equation %}aaa+aab+aba+abb+baa+bab+bba+bbb{% endequation %}. האם תוכלו להגיד לי, בלי לספור, כמה מחוברים יש? זו כבר שאלה קומבינטורית לגמרי: יש שלושה זוגות סוגריים, ומכל זוג אנו בוחרים אחד משני איברים - על כן, לפי עיקרון הכפל, יש לנו {% equation %}2\cdot2\cdot2=8{% endequation %} אפשרויות בחירה (כי הבחירה שלנו מורכבת משלושה שלבים שבכל אחד מהם יש שתי אפשרויות בחירה) ולכן יש שמונה מחוברים בסכום - עכשיו אפשר לבדוק זאת ידנית.

כעת, כיצד ניתן לפשט את הזוועה של שמונת המחוברים? את {% equation %}aaa{% endequation %} אפשר להחליף ב-{% equation %}a^{3}{% endequation %}. את {% equation %}aab{% endequation %} אפשר להחליף ב-{% equation %}a^{2}b{% endequation %}. גם את {% equation %}aba{% endequation %} אפשר להחליף ב-{% equation %}a^{2}b{% endequation %} וגם את {% equation %}baa{% endequation %} אפשר להחליף ב-{% equation %}a^{2}b{% endequation %}. אם כן, כמה פעמים יופיע {% equation %}a^{2}b{% endequation %} בסכום הסופי? כמספר הפעמים שבהן אפשר לבחור מבין שלושת הסוגריים פעמיים את {% equation %}a{% endequation %}, ופעם אחת את {% equation %}b{% endequation %}. אלו בדיוק שלוש פעמים - אפשר לחשוב על כך בשתי דרכים שונות: או שאנו בוחרים את שני זוגות הסוגריים שמהם ניקח {% equation %}a{% endequation %} ואז ממה שנשאר לוקחים {% equation %}b{% endequation %}, או שבוחרים את הסוגר שממנו ניקח את {% equation %}b{% endequation %} ואומרים שמשני הנותרים ניקח {% equation %}a{% endequation %}. בדרך השנייה ברור לגמרי שיש רק שלוש אפשרויות (יש שלושה זוגות סוגריים). בדרך הראשונה זה קצת פחות ברור ולכן הגיע הזמן לקרוא לעזרת הכלי שלמדנו בפעם הקודמת: מספר האפשרויות לבחור {% equation %}k{% endequation %} איברים מתוך {% equation %}n{% endequation %} הוא {% equation %}\frac{n!}{k!\left(n-k\right)!}{% endequation %} - ביטוי שלצורך פשטות סימנו בסימון {% equation %}{n \choose k}{% endequation %}, ואצלנו {% equation %}n=3{% endequation %} ו-{% equation %}k=2{% endequation %} כך שנקבל {% equation %}\frac{3!}{2!1!}=\frac{6}{2}=3{% endequation %}.

בואו נחזור לרגע אל {% equation %}a^{3}{% endequation %} ידידנו - כמה פעמים הוא יופיע בסכום? כמספר הפעמים שבהן ניתן לבחור {% equation %}a{% endequation %} בכל שלושת זוגות הסוגריים - אבל יש בדיוק רק בחירה אחת שכזו. פורמלית זה שווה למספר האפשרויות לבחור שלושה איברים מתוך שלושה: {% equation %}{3 \choose 3}=1{% endequation %}.

כעת הגיע הזמן לבצע קפיצת מדרגה כלשהי ולהתחיל להכליל את כל מה שעשינו פה ולתאר אותו באופן אחיד יותר. כשאנו פותחים את {% equation %}\left(a+b\right)^{3}{% endequation %}, מה אנחנו מקבלים? איברים שצורתם הכללית היא {% equation %}a^{i}b^{j}{% endequation %}, כך ש-{% equation %}i+j=3{% endequation %} (כי כל איבר מתקבל מבחירת שלושה איברים בדיוק - השאלה היא רק כמה מתוכם הם {% equation %}a{% endequation %} וכמה מתוכם הם {% equation %}b{% endequation %}). אם כן, אפשר לכתוב זאת בצורה יותר פשוטה: {% equation %}a^{i}b^{3-i}{% endequation %}. כעת נשאלת השאלה - כמה פעמים האיבר {% equation %}a^{i}b^{3-i}{% endequation %} מופיע? זהו בדיוק מספר האפשרויות לבחור את {% equation %}a{% endequation %} בדיוק {% equation %}i{% endequation %} פעמים מתוך 3 זוגות הסוגריים האפשריות, כלומר {% equation %}{3 \choose i}{% endequation %}. זה מוביל אותנו לניסוח האחיד הבא: {% equation %}\left(a+b\right)^{3}={3 \choose 0}a^{0}b^{3}+{3 \choose 1}a^{1}b^{2}+{3 \choose 2}a^{2}b+{3 \choose 3}a^{3}{% endequation %}.

אוקיי, עכשיו אתם ככל הנראה שואלים את עצמכם מה לעזאזל עשיתי כאן. במקום לקבל, כמו שהבטחתי, משהו פשוט ויפה קיבלתי ביטוי שנראה כמו זוועת עולם. אלא שאני טוען שהביטוי כלל אינו מזוויע, אחרי שעובר ההלם הראשוני, ויש בו יתרון גדול - קל לזכור אותו. שימו לב לכך שהוא מאוד תבניתי: סכום של איברים מהצורה {% equation %}{3 \choose i}a^{i}b^{3-i}{% endequation %} כשהדבר היחיד שמשתנה הוא ערכו של ה-{% equation %}i{% endequation %}. זה דבר ש<strong>קל לזכור</strong>. לא באמת צריך לזכור מה ערכו המדוייק של כל מקדם, אלא רק שכל מקדם הוא מהצורה {% equation %}{3 \choose i}{% endequation %} עבור ה-{% equation %}i{% endequation %} המתאים. כשכתבתי את הנוסחה שבתחילת הפוסט "מהראש", זה מה שהשתמשתי בו.

כעת אני רוצה לקפוץ קצת קדימה ולהציג סימון שבתיכון לא נהוג להשתמש בו (וחבל). כבר אמרתי שהנוסחה שלי ל-{% equation %}\left(a+b\right)^{3}{% endequation %} היא סכום של איברים שכולם נראים כמעט אותו דבר: {% equation %}{3 \choose i}a^{i}b^{3-i}{% endequation %}, כשהדבר היחיד שמשתנה הוא ה-{% equation %}i{% endequation %}. הדרך המתמטית לכתוב זאת היא באמצעות האות היוונית {% equation %}\Sigma{% endequation %} (סיגמה גדולה) שבאה לציין את המילה "סכום" (בשפה המתאימה, כמובן...). הנה הסימון: {% equation %}\left(a+b\right)^{3}=\sum_{i=0}^{3}{3 \choose i}a^{i}b^{3-i}{% endequation %}.

מה יש לנו פה? ובכן, אחרי הסיגמה יש לנו את {% equation %}{3 \choose i}a^{i}b^{3-i}{% endequation %} שכבר הזכרתי מספיק - זהו <strong>האיבר הכללי</strong> של הסכום. איבר כללי במובן זה שכל מחובר בסכום נראה כמוהו, לאחר הצבה של ערך מתאים ב-{% equation %}i{% endequation %}. האות {% equation %}i{% endequation %} נקראת <strong>האינדקס</strong> של הסכימה, והמספרים שכתובים מתחת ומעל לסיגמה באים לציין את הערכים שאותם {% equation %}i{% endequation %} מקבל; {% equation %}i=0{% endequation %} אומר שהערך הראשון ש-{% equation %}i{% endequation %} מקבל הוא 0, וה-3 למעלה אומר שזהו הערך האחרון שהוא מקבל. המוסכמה היא שאלא אם נאמר במפורש אחרת, {% equation %}i{% endequation %} מקבל רק ערכים שלמים, ולכן הסכום מתאר את מה שמקבלים כאשר מציבים באיבר הכללי את הערכים {% equation %}i=0,1,2,3{% endequation %}.

אני מקווה שסימן הסכימה ברור כעת ולא מפחיד; שאלה אחת שאולי התעוררה בכם היא למה לא לכתוב {% equation %}\sum_{0}^{3}{3 \choose i}a^{i}b^{3-i}{% endequation %} וחסל - למה צריך את ה-{% equation %}i={% endequation %} למטה? התשובה היא שלא תמיד ברור מהו האינדקס - לפעמים (ונראה דוגמה ממש בקרוב) יש יותר ממשתנה אחד שמופיע באיבר הכללי, וצריך להבהיר מי משמש כאינדקס הסכימה. עם זאת אעיר שכשההקשר ברור, לעתים קרובות נהוג להשמיט פרטים מסימן הסכימה, עד כדי כך שלפעמים אפשר למצוא נוסחאות כמו {% equation %}\sum a_{i}{% endequation %} וחסל - כאן השאלה אילו ערכים האינדקס מקבל תלויה לחלוטין בהקשר, וכותבי הטקסט מצפים שהקורא יוכל להסיק את המידע הזה בעצמו. באופן לא מפתיע, בטקסטי מבוא לרוב אין זוועות שכאלה.

אוקיי, אז טיפלנו בבינום עבור החזקות {% equation %}1,2,3{% endequation %}; המתמטיקאים נוהגים בשלב הזה לעבור לטפל ב-{% equation %}n{% endequation %} כללי וזה גם בדיוק מה שאני אעשה, ובלי הרבה שהיות אכתוב את הנוסחה, שזהה לגמרי למה שקיבלנו עבור המקרה של חזקה שלישית: {% equation %}\left(a+b\right)^{n}=\sum_{i=0}^{n}{n \choose i}a^{i}b^{n-i}{% endequation %}. עצרו רגע ונסו להבהיר לעצמכם למה היא נכונה.

ובכן, למה הנוסחה נכונה? בדיוק אותם שיקולים כמו קודם. {% equation %}\left(a+b\right)^{n}{% endequation %} ניתן לכתיבה כמכפלה של {% equation %}n{% endequation %} זוגות סוגריים, ולכן התוצאה הסופית תהיה סכום של איברים שהתקבלו מבחירת {% equation %}a{% endequation %}-ים ו-{% equation %}b{% endequation %}-ים - סה"כ {% equation %}n{% endequation %} פעמים עבור שניהם. אם {% equation %}i{% endequation %} הוא מספר ה-{% equation %}a{% endequation %}-ים שנבחרו, אז נקבל איבר מהצורה {% equation %}a^{i}b^{n-i}{% endequation %}, ויש לנו בדיוק {% equation %}{n \choose i}{% endequation %} דרכים שונות לבחור {% equation %}i{% endequation %} {% equation %}a{% endequation %}-ים, וזהו. מה שכתבתי כאן הוא כמעט הוכחה מתמטית, והוא בוודאי מבהיר היטב <strong>למה</strong> הנוסחה נראית כמו שהיא נראית ואיך זה קשור לקומבינטוריקה (ואם זה עדיין לא ברור - זו אשמתי, לא אשמת ההוכחה). לטעמי הוכחה זו (הגם שאינה פורמלית במאה אחוזים) טובה בהרבה מההוכחה ה"יבשה" לנכונות הבינום, שמשתמשת באינדוקציה מתמטית מזוויעה.

אם כן, זהו זה. נפתרה הבעיה הכללית של {% equation %}\left(a+b\right)^{2}{% endequation %} ו-{% equation %}\left(a+b\right)^{3}{% endequation %} וכל חזקה טבעית אחרת, והנוסחה הסופית היא קצרה ויפה להצגה (אבל חשבו כמה מזוויע יהיה לכתוב באופן מפורש את {% equation %}\left(a+b\right)^{13}{% endequation %}!). כעת אני מקווה כי גם ברור מדוע {% equation %}{n \choose i}{% endequation %} נקראים "מקדמי הבינום" - מכיוון שהם המקדמים של הגורמים מהצורה {% equation %}a^{i}b^{n-i}{% endequation %} בפיתוח נוסחת הבינום. אני גם מקווה שכעת ברור קצת יותר איך הקומבינטוריקה מתקשרת לתחומים אחרים במתמטיקה (כאן - אלגברה בסיסית) ומסייעת לנו להבין גם אותם.